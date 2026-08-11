"""切分：把长文档变成可检索的片段。

这一步的质量上限决定了整个 RAG 的上限——检索器再好，也找不回被切坏的信息。
本模块只用标准库，中英文都能处理。

三种策略，可以直接对比效果：
  fixed      固定长度 + 重叠，最简单，会切断句子
  sentence   按句边界聚合到目标长度，不切断句子
  paragraph  按空行切段，再对超长段落降级为 sentence
"""

from __future__ import annotations

import re
from dataclasses import dataclass

# 中英文句末标记。中文标点后面通常没有空格，所以不能只靠 r'[.!?]\s'。
SENT_END = re.compile(r"(?<=[。！？；!?;])|(?<=[.])(?=\s)")


@dataclass(frozen=True)
class Chunk:
    doc_id: str
    chunk_id: str
    text: str
    start: int  # 在原文中的起始字符偏移，用于把引用定位回原文

    def __len__(self) -> int:
        return len(self.text)


def split_sentences(text: str) -> list[str]:
    parts = [s.strip() for s in SENT_END.split(text) if s and s.strip()]
    return parts


def chunk_fixed(text: str, size: int = 300, overlap: int = 60) -> list[tuple[str, int]]:
    if overlap >= size:
        raise ValueError(f"overlap({overlap}) 必须小于 size({size})，否则窗口不前进")
    out: list[tuple[str, int]] = []
    step = size - overlap
    for start in range(0, max(len(text), 1), step):
        piece = text[start : start + size]
        if not piece.strip():
            continue
        out.append((piece, start))
        if start + size >= len(text):
            break
    return out


def chunk_sentence(text: str, size: int = 300, overlap: int = 1) -> list[tuple[str, int]]:
    """按句聚合。overlap 的单位是「句」，不是字符——这样重叠部分永远是完整句子。"""
    sents = split_sentences(text)
    if not sents:
        return []

    # 先记住每句在原文的偏移，切完还能定位回去
    offsets: list[int] = []
    cursor = 0
    for s in sents:
        idx = text.find(s, cursor)
        offsets.append(idx if idx >= 0 else cursor)
        cursor = offsets[-1] + len(s)

    out: list[tuple[str, int]] = []
    i = 0
    while i < len(sents):
        buf: list[str] = []
        start_i = i
        while i < len(sents) and sum(len(x) for x in buf) + len(sents[i]) <= size:
            buf.append(sents[i])
            i += 1
        if not buf:  # 单句超长，只能整句放进去
            buf = [sents[i]]
            i += 1
        # 从原文切片而不是 "".join(buf)：split_sentences 会 strip 掉句间空白，
        # 拼回去的字符串和原文对不上，start 偏移就失去了定位能力。
        end = offsets[i - 1] + len(sents[i - 1])
        out.append((text[offsets[start_i] : end], offsets[start_i]))
        if i >= len(sents):
            break
        i = max(start_i + 1, i - overlap)  # 回退 overlap 句，但必须前进至少一句
    return out


def chunk_paragraph(text: str, size: int = 300, overlap: int = 1) -> list[tuple[str, int]]:
    out: list[tuple[str, int]] = []
    cursor = 0
    for para in re.split(r"\n\s*\n", text):
        stripped = para.strip()
        if not stripped:
            cursor += len(para) + 2
            continue
        base = text.find(stripped, cursor)
        base = base if base >= 0 else cursor
        if len(stripped) <= size:
            out.append((stripped, base))
        else:
            for piece, off in chunk_sentence(stripped, size=size, overlap=overlap):
                out.append((piece, base + off))
        cursor = base + len(stripped)
    return out


STRATEGIES = {
    "fixed": chunk_fixed,
    "sentence": chunk_sentence,
    "paragraph": chunk_paragraph,
}


def chunk_document(
    doc_id: str, text: str, strategy: str = "paragraph", size: int = 300, overlap: int = 1
) -> list[Chunk]:
    if strategy not in STRATEGIES:
        raise ValueError(f"未知策略 {strategy!r}，可选：{sorted(STRATEGIES)}")
    fn = STRATEGIES[strategy]
    # fixed 的 overlap 单位是字符，其余是句。默认取 size 的 20%，
    # 这样调小 size 时不会撞上 overlap >= size 的参数错误。
    kw = {"size": size, "overlap": max(1, size // 5) if strategy == "fixed" else overlap}
    return [
        Chunk(doc_id=doc_id, chunk_id=f"{doc_id}#{i}", text=t, start=s)
        for i, (t, s) in enumerate(fn(text, **kw))
    ]
