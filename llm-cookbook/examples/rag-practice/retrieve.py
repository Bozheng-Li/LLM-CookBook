"""检索：BM25、向量相似、以及把两者融合的 RRF。全部零依赖手写。

为什么不直接上 embedding 模型：这个例子要能离线跑、能在几秒内跑完、
而且每一步的分数都要能手算验证。用真实 embedding 会让"检索为什么返回这条"
变成黑盒。接口留好了——`DenseRetriever` 换成任何 encode(str)->vector
的模型即可，融合和评测代码一行都不用改。
"""

from __future__ import annotations

import math
import re
from collections import Counter
from dataclasses import dataclass

from chunk import Chunk

CJK = re.compile(r"[一-鿿]")
ASCII_WORD = re.compile(r"[a-z0-9]+")


def tokenize(text: str) -> list[str]:
    """中文切二元字组，英文按词。

    中文不切词而用 bigram，是因为无依赖分词器的准确率还不如 bigram 稳定，
    而 bigram 对检索召回其实相当够用——代价是词表变大。
    """
    text = text.lower()
    toks = ASCII_WORD.findall(text)
    cjk_runs = CJK.findall(text)
    # 连续汉字之间才组 bigram，跨标点不组
    for run in re.findall(r"[一-鿿]+", text):
        toks.extend(run[i : i + 2] for i in range(len(run) - 1))
        if len(run) == 1:
            toks.append(run)
    del cjk_runs
    return toks


@dataclass
class Hit:
    chunk: Chunk
    score: float
    source: str = ""


class BM25:
    """Okapi BM25。k1 控制词频饱和速度，b 控制文档长度归一强度。"""

    def __init__(self, chunks: list[Chunk], k1: float = 1.5, b: float = 0.75) -> None:
        self.chunks = chunks
        self.k1, self.b = k1, b
        self.docs = [tokenize(c.text) for c in chunks]
        self.lens = [len(d) for d in self.docs]
        self.avg_len = sum(self.lens) / len(self.lens) if self.lens else 0.0
        self.tf = [Counter(d) for d in self.docs]
        df: Counter[str] = Counter()
        for d in self.docs:
            df.update(set(d))
        n = len(self.docs)
        # 加 0.5 的平滑形式，保证 df 接近 N 时 idf 不会变成负数导致排序颠倒
        self.idf = {t: math.log(1 + (n - c + 0.5) / (c + 0.5)) for t, c in df.items()}

    def search(self, query: str, top_k: int = 5) -> list[Hit]:
        q = tokenize(query)
        scored: list[Hit] = []
        for i, tf in enumerate(self.tf):
            s = 0.0
            for t in q:
                f = tf.get(t, 0)
                if not f:
                    continue
                norm = 1 - self.b + self.b * (self.lens[i] / self.avg_len or 1)
                s += self.idf.get(t, 0.0) * f * (self.k1 + 1) / (f + self.k1 * norm)
            if s > 0:
                scored.append(Hit(self.chunks[i], s, "bm25"))
        scored.sort(key=lambda h: (-h.score, h.chunk.chunk_id))
        return scored[:top_k]


class DenseRetriever:
    """用 TF-IDF 加权的字符特征向量近似"语义"检索。

    这不是真正的语义模型——它抓的是词形重叠，抓不到"显存不够"和"OOM"是一回事。
    保留它是为了让 RRF 融合有两路真实分数可融，同时暴露稀疏检索的固有短板：
    见 `eval.py` 里那条同义改写的查询。
    """

    def __init__(self, chunks: list[Chunk]) -> None:
        self.chunks = chunks
        docs = [tokenize(c.text) for c in chunks]
        n = len(docs)
        df: Counter[str] = Counter()
        for d in docs:
            df.update(set(d))
        self.idf = {t: math.log((n + 1) / (c + 1)) + 1 for t, c in df.items()}
        self.vecs = [self._vec(d) for d in docs]

    def _vec(self, toks: list[str]) -> dict[str, float]:
        tf = Counter(toks)
        v = {t: (1 + math.log(f)) * self.idf.get(t, 1.0) for t, f in tf.items()}
        norm = math.sqrt(sum(x * x for x in v.values())) or 1.0
        return {t: x / norm for t, x in v.items()}

    def search(self, query: str, top_k: int = 5) -> list[Hit]:
        qv = self._vec(tokenize(query))
        out: list[Hit] = []
        for c, v in zip(self.chunks, self.vecs):
            # 只遍历较短的一边，查询通常远短于文档
            s = sum(w * v.get(t, 0.0) for t, w in qv.items())
            if s > 0:
                out.append(Hit(c, s, "dense"))
        out.sort(key=lambda h: (-h.score, h.chunk.chunk_id))
        return out[:top_k]


def reciprocal_rank_fusion(runs: list[list[Hit]], k: int = 60, top_k: int = 5) -> list[Hit]:
    """RRF：只看排名不看分数，所以不需要在两路之间做分数归一。

    这是它最实用的性质——BM25 的分数是无上界的，余弦相似度在 [0,1]，
    强行归一化再加权会引入一个需要调的超参，而 RRF 没有。
    """
    acc: dict[str, float] = {}
    keep: dict[str, Chunk] = {}
    for run in runs:
        for rank, hit in enumerate(run, start=1):
            acc[hit.chunk.chunk_id] = acc.get(hit.chunk.chunk_id, 0.0) + 1.0 / (k + rank)
            keep[hit.chunk.chunk_id] = hit.chunk
    merged = [Hit(keep[cid], s, "rrf") for cid, s in acc.items()]
    merged.sort(key=lambda h: (-h.score, h.chunk.chunk_id))
    return merged[:top_k]


class HybridRetriever:
    def __init__(self, chunks: list[Chunk]) -> None:
        self.bm25 = BM25(chunks)
        self.dense = DenseRetriever(chunks)

    def search(self, query: str, top_k: int = 5, pool: int = 20) -> list[Hit]:
        return reciprocal_rank_fusion(
            [self.bm25.search(query, pool), self.dense.search(query, pool)], top_k=top_k
        )
