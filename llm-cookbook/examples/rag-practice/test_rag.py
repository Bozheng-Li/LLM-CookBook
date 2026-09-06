"""自检：切分不丢字、检索排序可预测、评测指标算得对。

跑法：python test_rag.py（或 python -m pytest test_rag.py）
"""

from __future__ import annotations

import json
import math
import pathlib
import sys

from chunk import chunk_document, chunk_fixed, chunk_sentence, split_sentences
from eval import evaluate, mrr, ndcg_at_k, recall_at_k
from rag import answer, build_index, load_documents
from retrieve import BM25, DenseRetriever, HybridRetriever, reciprocal_rank_fusion, tokenize

DOC = (
    "KV Cache 把之前算过的 Key 和 Value 缓存下来。代价是显存。\n\n"
    "一个 7B 模型在 fp16 下可能占用 16 GB。这已经超过模型权重本身。"
)


def test_fixed_chunks_cover_all_text() -> None:
    """固定切分必须覆盖全文——重叠允许，漏字不允许。"""
    text = "abcdefghij" * 40
    pieces = chunk_fixed(text, size=100, overlap=20)
    covered = bytearray(len(text))
    for t, start in pieces:
        for i in range(start, start + len(t)):
            covered[i] = 1
    assert all(covered), f"有 {len(covered) - sum(covered)} 个字符没被任何块覆盖"


def test_fixed_rejects_non_advancing_window() -> None:
    """overlap >= size 会让窗口原地踏步，必须在参数校验就拦住而不是死循环。"""
    try:
        chunk_fixed("x" * 100, size=50, overlap=50)
    except ValueError:
        return
    raise AssertionError("overlap >= size 时应当报错")


def test_sentence_chunks_never_split_sentences() -> None:
    """按句切分的全部意义就在这里：任何一块的边界都是句边界。"""
    text = "第一句很短。第二句稍微长一点点。第三句是这里面最长的一句话用来触发换块。第四句。"
    sents = set(split_sentences(text))
    for piece, _ in chunk_sentence(text, size=20, overlap=1):
        for s in split_sentences(piece):
            assert s in sents, f"{s!r} 不是原文中的完整句子"


def test_sentence_chunking_always_advances() -> None:
    """回退 overlap 句时若不强制前进，size 很小就会无限循环。"""
    text = "。".join(f"这是第{i}句话内容" for i in range(30)) + "。"
    pieces = chunk_sentence(text, size=5, overlap=3)  # size 小于单句长度
    assert len(pieces) <= 40, f"块数 {len(pieces)} 异常，可能没有正常前进"
    assert len(pieces) > 0


def test_chunk_offsets_point_back_to_source() -> None:
    """引用要能定位回原文，start 偏移必须准确。"""
    for strategy in ("fixed", "sentence", "paragraph"):
        for c in chunk_document("d", DOC, strategy=strategy, size=40):
            assert DOC[c.start : c.start + len(c.text)] == c.text, (
                f"{strategy}: chunk_id={c.chunk_id} 的 start 偏移对不上原文"
            )


def test_tokenize_handles_mixed_scripts() -> None:
    toks = tokenize("KV Cache 占用 16GB 显存")
    assert "kv" in toks and "cache" in toks
    assert "16gb" in toks
    assert "显存" in toks          # 汉字 bigram
    assert "占用" in toks


def test_bm25_ranks_exact_match_first() -> None:
    chunks, _ = build_index()
    hits = BM25(chunks).search("PagedAttention 分页管理 碎片", top_k=3)
    assert hits, "应当至少召回一条"
    assert hits[0].chunk.doc_id == "kv-cache"


def test_bm25_idf_is_never_negative() -> None:
    """出现在几乎所有文档里的词，idf 若变成负数会让排序颠倒。"""
    chunks, _ = build_index()
    bm = BM25(chunks)
    assert all(v >= 0 for v in bm.idf.values()), "存在负 idf，平滑公式写错了"


def test_dense_vectors_are_unit_length() -> None:
    chunks, _ = build_index()
    d = DenseRetriever(chunks)
    for v in d.vecs:
        norm = sum(x * x for x in v.values()) ** 0.5
        assert abs(norm - 1.0) < 1e-9, f"向量未归一化，模长 {norm}"


def test_rrf_needs_no_score_normalization() -> None:
    """RRF 只看名次。把一路的分数整体放大一千倍，结果必须完全不变。"""
    chunks, _ = build_index()
    bm, dn = BM25(chunks), DenseRetriever(chunks)
    q = "LoRA 秩怎么选"
    a = bm.search(q, 10)
    b = dn.search(q, 10)
    scaled = [type(h)(h.chunk, h.score * 1000, h.source) for h in a]
    r1 = [h.chunk.chunk_id for h in reciprocal_rank_fusion([a, b])]
    r2 = [h.chunk.chunk_id for h in reciprocal_rank_fusion([scaled, b])]
    assert r1 == r2, "分数缩放改变了 RRF 结果，说明实现里混进了原始分数"


def test_hybrid_recovers_what_one_route_misses() -> None:
    """融合的价值：任一路排进前列的文档，融合结果里都不该整个掉出候选集。"""
    chunks, hybrid = build_index()
    bm, dn = BM25(chunks), DenseRetriever(chunks)
    q = "连续批处理 吞吐"
    top_ids = {h.chunk.doc_id for h in hybrid.search(q, top_k=5)}
    for route in (bm, dn):
        best = route.search(q, top_k=1)
        if best:
            assert best[0].chunk.doc_id in top_ids, f"{route.__class__.__name__} 的首选被融合丢掉了"


def test_answer_is_fully_grounded() -> None:
    """抽取式回答的每一句都必须逐字出现在某个被引用的片段里。"""
    docs = load_documents()
    _, retr = build_index()
    a = answer("QLoRA 用了哪几个技巧", retr)
    assert a.citations, "回答必须带引用"
    corpus = "".join(docs.values())
    for sent in split_sentences(a.text):
        assert sent in corpus, f"回答里出现了原文中不存在的句子：{sent!r}"


def test_answer_admits_when_retrieval_is_empty() -> None:
    """一条 token 都对不上时必须说不知道，而不是拼一句似是而非的话。"""
    _, retr = build_index()
    a = answer("zzz qqq xxx yyy", retr)
    assert "没有找到" in a.text
    assert a.citations == []


def test_abstain_threshold_gates_on_dense_score() -> None:
    """拒答开关本身要可用：阈值拉到 1.0 时任何问题都必须拒答。"""
    _, retr = build_index()
    a = answer("QLoRA 用了哪几个技巧", retr, min_score=1.0)
    assert "没有找到" in a.text and a.citations == []
    b = answer("QLoRA 用了哪几个技巧", retr, min_score=0.0)
    assert b.citations, "关闭阈值后应当正常回答"


def test_lexical_retriever_cannot_calibrate_abstention() -> None:
    """钉住一个负面结论：字符 bigram 词袋的分数分布无法区分「无关」。

    无关问题的最高分 >= 真实问题的最低分，说明不存在一个既不误杀
    又不漏放的阈值。这不是 bug，是词面检索的固有局限——真要拒答，
    得换语义编码器。哪天换了，这条测试会失败，那时应当更新它。
    """
    cases = json.loads(
        (pathlib.Path(__file__).parent / "data" / "qa.json").read_text(encoding="utf-8")
    )
    chunks, _ = build_index()
    dn = DenseRetriever(chunks)
    top = lambda q: (dn.search(q, 1)[0].score if dn.search(q, 1) else 0.0)  # noqa: E731
    real_min = min(top(c["q"]) for c in cases)
    noise_max = max(
        top(q)
        for q in ("紫色的大象在星期四会做什么梦", "窗外的树叶正在慢慢变黄", "他昨天买了一双新鞋子")
    )
    assert noise_max >= real_min, (
        f"无关问题上限 {noise_max:.3f} 已低于真实问题下限 {real_min:.3f}，"
        "两个分布分开了——检索器变强了，请更新这条断言和 rag.py 里的说明"
    )


def test_metrics_match_hand_computed_values() -> None:
    assert recall_at_k(["a", "b", "c"], ["b"], 5) == 1.0
    assert recall_at_k(["a", "b", "c"], ["z"], 5) == 0.0
    assert recall_at_k(["a", "b"], ["a", "z"], 5) == 0.5
    assert mrr(["a", "b", "c"], ["b"]) == 0.5          # 排第 2 -> 1/2
    assert mrr(["a", "b"], ["z"]) == 0.0
    # 唯一正确文档排第 2：DCG = 1/log2(3)，IDCG = 1/log2(2) = 1
    assert abs(ndcg_at_k(["a", "b"], ["b"], 5) - 1 / math.log2(3)) < 1e-9
    assert ndcg_at_k(["b"], ["b"], 5) == 1.0


def test_recall_at_k_respects_k() -> None:
    """k 必须真的截断，否则 Recall@1 和 Recall@10 会算出同一个数。"""
    docs = ["x", "y", "z", "gold"]
    assert recall_at_k(docs, ["gold"], 3) == 0.0
    assert recall_at_k(docs, ["gold"], 4) == 1.0


def test_eval_dedupes_chunks_of_same_document() -> None:
    """同一文档的多个 chunk 都命中时只能算一次，否则 Recall 会虚高。"""
    _, retr = build_index()
    cases = [{"q": "KV Cache 显存", "gold": ["kv-cache"], "kind": "lexical"}]
    res = evaluate(retr, cases, k=5)
    assert res["recall@5"] <= 1.0


def test_eval_set_references_existing_documents() -> None:
    """评测集里的 gold 文档名必须真实存在，否则整份跑分都是 0 而没人察觉。"""
    cases = json.loads(
        (pathlib.Path(__file__).parent / "data" / "qa.json").read_text(encoding="utf-8")
    )
    known = set(load_documents())
    for c in cases:
        for g in c["gold"]:
            assert g in known, f"评测集引用了不存在的文档 {g!r}"
        assert c["kind"] in {"lexical", "paraphrase"}


def test_paraphrase_queries_are_actually_harder() -> None:
    """同义改写子集的表现必须明显差于字面重叠子集。

    这条测试固定的是本例最想说明的结论：纯词面检索抓不住语义。
    哪天它失败了，说明检索器换成了真正的语义模型——那时应当更新这条断言，
    而不是删掉它。
    """
    cases = json.loads(
        (pathlib.Path(__file__).parent / "data" / "qa.json").read_text(encoding="utf-8")
    )
    _, retr = build_index()
    lex = evaluate(retr, [c for c in cases if c["kind"] == "lexical"], k=5)
    par = evaluate(retr, [c for c in cases if c["kind"] == "paraphrase"], k=5)
    assert lex["mrr"] > par["mrr"], (
        f"字面 MRR {lex['mrr']:.3f} 未高于改写 MRR {par['mrr']:.3f}"
    )


def test_chunking_strategy_changes_chunk_count() -> None:
    """三种策略应当给出不同的切分粒度，否则说明某个分支没生效。"""
    counts = {
        s: len([c for d, t in load_documents().items() for c in chunk_document(d, t, strategy=s)])
        for s in ("fixed", "sentence", "paragraph")
    }
    assert len(set(counts.values())) > 1, f"三种策略块数完全相同：{counts}"


if __name__ == "__main__":
    tests = sorted((n, f) for n, f in globals().items() if n.startswith("test_") and callable(f))
    failed = 0
    for name, fn in tests:
        try:
            fn()
            print(f"  PASS {name}")
        except AssertionError as e:
            failed += 1
            print(f"  FAIL {name}: {e}")
    print(f"\n{len(tests) - failed}/{len(tests)} passed")
    sys.exit(1 if failed else 0)
