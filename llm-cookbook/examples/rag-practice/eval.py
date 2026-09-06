"""评测：把「检索好不好」变成三个可比较的数字，而不是靠翻结果找感觉。

三个指标各管一件事：
  Recall@k  正确文档进没进候选集。检索的天花板——它是 0，后面再好也没用。
  MRR       正确文档排第几。同样都召回了，排第 1 和排第 10 对生成的影响完全不同。
  nDCG@k    带位置折损的综合分，对多个正确文档的场景更合适。

跑法：
  python eval.py                       # 全部检索器 × 全部切分策略
  python eval.py --strategy sentence   # 只看一种切分
  python eval.py --show-failures       # 打印失败用例，这是最有用的一屏
"""

from __future__ import annotations

import argparse
import json
import math
import pathlib
import sys

from chunk import chunk_document
from rag import load_documents
from retrieve import BM25, DenseRetriever, HybridRetriever

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

QA_PATH = pathlib.Path(__file__).parent / "data" / "qa.json"


def recall_at_k(retrieved_docs: list[str], gold: list[str], k: int) -> float:
    top = set(retrieved_docs[:k])
    return len(top & set(gold)) / len(gold)


def mrr(retrieved_docs: list[str], gold: list[str]) -> float:
    for i, d in enumerate(retrieved_docs, start=1):
        if d in gold:
            return 1.0 / i
    return 0.0


def ndcg_at_k(retrieved_docs: list[str], gold: list[str], k: int) -> float:
    dcg = sum(1.0 / math.log2(i + 1) for i, d in enumerate(retrieved_docs[:k], 1) if d in gold)
    ideal = sum(1.0 / math.log2(i + 1) for i in range(1, min(len(gold), k) + 1))
    return dcg / ideal if ideal else 0.0


def evaluate(retriever, cases: list[dict], k: int = 5) -> dict:
    r, m, n = [], [], []
    failures = []
    for c in cases:
        hits = retriever.search(c["q"], top_k=k)
        # 同一文档的多个 chunk 只算一次，按最好名次保留
        docs: list[str] = []
        for h in hits:
            if h.chunk.doc_id not in docs:
                docs.append(h.chunk.doc_id)
        r.append(recall_at_k(docs, c["gold"], k))
        m.append(mrr(docs, c["gold"]))
        n.append(ndcg_at_k(docs, c["gold"], k))
        if docs[:1] != c["gold"][:1]:
            failures.append({"q": c["q"], "kind": c["kind"], "gold": c["gold"], "got": docs[:3]})
    avg = lambda xs: sum(xs) / len(xs) if xs else 0.0  # noqa: E731
    return {
        f"recall@{k}": avg(r),
        "mrr": avg(m),
        f"ndcg@{k}": avg(n),
        "failures": failures,
    }


def main() -> None:
    p = argparse.ArgumentParser(description="RAG 检索质量评测")
    p.add_argument("--k", type=int, default=5)
    p.add_argument("--strategy", choices=["fixed", "sentence", "paragraph", "all"], default="all")
    p.add_argument("--size", type=int, default=300)
    p.add_argument("--show-failures", action="store_true")
    a = p.parse_args()

    cases = json.loads(QA_PATH.read_text(encoding="utf-8"))
    docs = load_documents()
    strategies = ["fixed", "sentence", "paragraph"] if a.strategy == "all" else [a.strategy]

    print(f"知识库 {len(docs)} 篇 · 评测问题 {len(cases)} 条 · k={a.k}\n")
    header = f"{'切分':>10}  {'块数':>4}  {'检索器':>8}  {'Recall@k':>9}  {'MRR':>7}  {'nDCG@k':>7}"
    print(header)
    print("-" * len(header))

    all_failures: dict[str, list] = {}
    for strat in strategies:
        chunks = []
        for doc_id, text in docs.items():
            chunks.extend(chunk_document(doc_id, text, strategy=strat, size=a.size))
        for name, retr in [
            ("BM25", BM25(chunks)),
            ("向量", DenseRetriever(chunks)),
            ("混合RRF", HybridRetriever(chunks)),
        ]:
            res = evaluate(retr, cases, k=a.k)
            print(
                f"{strat:>10}  {len(chunks):>4}  {name:>8}  "
                f"{res[f'recall@{a.k}']:>9.3f}  {res['mrr']:>7.3f}  {res[f'ndcg@{a.k}']:>7.3f}"
            )
            all_failures[f"{strat}/{name}"] = res["failures"]

    # 分开看两类问题：字面重叠的和同义改写的。差距就是稀疏检索的短板。
    print("\n按问题类型拆开（paragraph 切分）：")
    chunks = []
    for doc_id, text in docs.items():
        chunks.extend(chunk_document(doc_id, text, strategy="paragraph", size=a.size))
    for kind in ("lexical", "paraphrase"):
        subset = [c for c in cases if c["kind"] == kind]
        label = "字面重叠" if kind == "lexical" else "同义改写"
        row = [f"  {label}（{len(subset)} 条）"]
        for name, retr in [("BM25", BM25(chunks)), ("向量", DenseRetriever(chunks)), ("混合RRF", HybridRetriever(chunks))]:
            res = evaluate(retr, subset, k=a.k)
            row.append(f"{name} Recall@{a.k}={res[f'recall@{a.k}']:.3f}")
        print("  ".join(row))

    if a.show_failures:
        print("\n失败用例（Top-1 文档不对）：")
        key = "paragraph/混合RRF"
        for f in all_failures.get(key, []):
            print(f"  [{f['kind']}] {f['q']}")
            print(f"      期望 {f['gold']} · 实际 {f['got']}")
        if not all_failures.get(key):
            print("  （无）")


if __name__ == "__main__":
    main()
