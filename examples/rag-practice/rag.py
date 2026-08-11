"""构建索引 + 生成带引用的回答。

生成部分刻意不接模型：`answer()` 做的是抽取式回答——从检索到的片段里
挑最相关的句子拼起来，并标注来源。这样整个 pipeline 完全确定、可离线跑，
而且检索质量的好坏会直接反映在回答里，不会被模型的语言能力掩盖。

接真模型只需改 `answer()` 一个函数，检索、评测、引用格式都不用动。
文件末尾给了改法。
"""

from __future__ import annotations

import json
import pathlib
from dataclasses import asdict, dataclass

from chunk import Chunk, chunk_document, split_sentences
from retrieve import BM25, DenseRetriever, Hit, HybridRetriever, tokenize

KB_DIR = pathlib.Path(__file__).parent / "data" / "kb"


def load_documents(kb_dir: pathlib.Path = KB_DIR) -> dict[str, str]:
    docs = {}
    for p in sorted(kb_dir.glob("*.md")):
        docs[p.stem] = p.read_text(encoding="utf-8")
    if not docs:
        raise FileNotFoundError(f"{kb_dir} 里没有 .md 文件")
    return docs


def build_index(
    strategy: str = "paragraph", size: int = 300
) -> tuple[list[Chunk], HybridRetriever]:
    chunks: list[Chunk] = []
    for doc_id, text in load_documents().items():
        chunks.extend(chunk_document(doc_id, text, strategy=strategy, size=size))
    return chunks, HybridRetriever(chunks)


@dataclass
class Answer:
    query: str
    text: str
    citations: list[dict]

    def render(self) -> str:
        lines = [self.text, ""]
        for i, c in enumerate(self.citations, 1):
            lines.append(f"  [{i}] {c['doc_id']} (score {c['score']:.3f})")
            lines.append(f"      {c['excerpt']}")
        return "\n".join(lines)


def answer(
    query: str, retriever, top_k: int = 3, max_sentences: int = 3, min_score: float = 0.0
) -> Answer:
    """抽取式回答：从命中片段里选与查询词重叠最高的句子。

    刻意不用模型的好处是——回答里出现的每一个字都能追溯到某个原文句子，
    「忠实度」这一项恒等于 1，评测时只需要关心检索召回和答案覆盖。

    min_score 是拒答阈值，作用在稠密路的余弦分数上（有界于 [0,1]，可比）。
    默认 0 即关闭。**这里不给一个"推荐值"是有意的**：本例的检索器是字符
    bigram 词袋，实测真实问题的首位分数低到 0.103，而无关问题能高到 0.163
    ——两个分布是重叠的，任何阈值都会同时误杀和漏放。想要可用的拒答，
    前提是换成真正的语义编码器，而不是调这个数。test_rag.py 里
    test_lexical_retriever_cannot_calibrate_abstention 把这个结论钉住了。
    """
    if min_score > 0:
        dense = getattr(retriever, "dense", None)
        if dense is not None:
            best = dense.search(query, top_k=1)
            if not best or best[0].score < min_score:
                return Answer(query=query, text="知识库中没有找到相关内容。", citations=[])

    hits: list[Hit] = retriever.search(query, top_k=top_k)
    q = set(tokenize(query))

    scored: list[tuple[float, str, Hit]] = []
    for h in hits:
        for sent in split_sentences(h.chunk.text):
            st = set(tokenize(sent))
            if not st:
                continue
            # Jaccard 而非纯交集大小：否则长句永远赢
            overlap = len(q & st) / len(q | st)
            if overlap > 0:
                scored.append((overlap, sent, h))
    scored.sort(key=lambda x: (-x[0], x[1]))

    picked: list[str] = []
    seen: set[str] = set()
    for _, sent, _h in scored:
        if sent in seen:
            continue
        seen.add(sent)
        picked.append(sent)
        if len(picked) >= max_sentences:
            break

    text = "".join(picked) if picked else "知识库中没有找到相关内容。"
    citations = [
        {
            "doc_id": h.chunk.doc_id,
            "chunk_id": h.chunk.chunk_id,
            "score": h.score,
            "excerpt": h.chunk.text[:80].replace("\n", " ") + ("…" if len(h.chunk.text) > 80 else ""),
        }
        for h in hits
    ]
    return Answer(query=query, text=text, citations=citations)


def to_json(a: Answer) -> str:
    return json.dumps(asdict(a), ensure_ascii=False, indent=2)


# 换成真模型：把上面 answer() 里挑句子那段替换成一次 API 调用即可。
#
#   ctx = "\n\n".join(f"[{i}] {h.chunk.text}" for i, h in enumerate(hits, 1))
#   prompt = (
#       "只依据下列证据回答，每个论断后用 [编号] 标注来源；"
#       f"证据中没有的内容必须回答「无法从证据中确定」。\n\n{ctx}\n\n问题：{query}"
#   )
#   text = client.messages.create(model=..., messages=[{"role":"user","content":prompt}])
#
# citations 那段不用改——它已经是稳定的接口契约。
# 换真检索模型同理：把 DenseRetriever 换成任何 encode(str)->list[float] 的
# 编码器，RRF 融合和 eval.py 一行都不用动。
_ = (BM25, DenseRetriever)  # 供 REPL 直接 import 用
