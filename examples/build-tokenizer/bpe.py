"""字节级 BPE：训练、编码、解码，只用标准库。

为什么在字节上做而不是在字符上做：字符级词表要么漏字（生僻字、emoji 变成 UNK），
要么大到离谱（Unicode 有十几万码位）。字节只有 256 个，任何文本都能表示，
代价是一个汉字要占 3 个初始 token，靠合并规则再压回去。GPT-2 起的主流做法都是这个。

预分词（pre-tokenization）是另一个容易被跳过的步骤：如果不先按词/空白切开，
BPE 会把 "the" 和后面的标点合成一个 token，也会跨越空格合并出 "of the" 这种
既不通用又浪费词表的单元。所以先用正则切成"词片"，合并只在词片内部进行。
"""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

# GPT-2 预分词正则的标准库版本。原版用 regex 模块的 \p{L}/\p{N}，
# 这里用 [^\W\d_] 表示"字母"、\d 表示"数字"，效果等价且不引入第三方依赖。
# 分支顺序有意义：先切出英文缩写，再切"可带前导空格的字母串/数字串/符号串"，
# 最后兜底空白。前导空格留在 token 里，解码时才能无损还原。
PRE_TOKEN_RE = re.compile(
    r"'(?:s|t|re|ve|m|ll|d)"
    r"| ?[^\W\d_]+"
    r"| ?\d+"
    r"| ?[^\s\w]+"
    r"|\s+(?!\S)"
    r"|\s+",
    re.UNICODE,
)

Pair = tuple[int, int]


def pre_tokenize(text: str) -> list[str]:
    """把文本切成词片。合并只在词片内部发生。"""
    return PRE_TOKEN_RE.findall(text)


def _word_counts(text: str) -> Counter[tuple[int, ...]]:
    """统计每个词片（转成字节元组后）的出现次数。

    按词片去重是训练能跑快的关键：语料里 "the" 出现十万次，
    我们只需要为它统计一次内部 pair，再乘以词频。
    """
    counts: Counter[tuple[int, ...]] = Counter()
    for word in pre_tokenize(text):
        counts[tuple(word.encode("utf-8"))] += 1
    return counts


def _pair_stats(words: dict[tuple[int, ...], int]) -> Counter[Pair]:
    stats: Counter[Pair] = Counter()
    for symbols, freq in words.items():
        for pair in zip(symbols, symbols[1:]):
            stats[pair] += freq
    return stats


def _merge_word(symbols: tuple[int, ...], pair: Pair, new_id: int) -> tuple[int, ...]:
    """把一个词片里所有出现的 pair 替换成新 id。

    从左到右扫描且命中后跳两格：这保证 "aaa" 在合并 (a,a) 时得到 [aa, a]
    而不是重叠匹配。训练和推理必须用同一套规则，否则编码结果对不上。
    """
    out: list[int] = []
    i = 0
    while i < len(symbols):
        if i < len(symbols) - 1 and symbols[i] == pair[0] and symbols[i + 1] == pair[1]:
            out.append(new_id)
            i += 2
        else:
            out.append(symbols[i])
            i += 1
    return tuple(out)


class BPETokenizer:
    """merges 是有序的合并规则表，顺序即优先级，编码时必须按训练顺序重放。"""

    def __init__(self, merges: list[Pair] | None = None) -> None:
        self.merges: list[Pair] = list(merges or [])
        self._rank: dict[Pair, int] = {p: i for i, p in enumerate(self.merges)}
        self._vocab: dict[int, bytes] = self._build_vocab()

    # ---- 训练 ----------------------------------------------------------

    @classmethod
    def train(cls, text: str, vocab_size: int, verbose: bool = False) -> "BPETokenizer":
        if vocab_size < 256:
            raise ValueError("vocab_size 至少要 256，字节表本身就占满了前 256 个 id")

        words = dict(_word_counts(text))
        merges: list[Pair] = []

        for step in range(vocab_size - 256):
            stats = _pair_stats(words)
            if not stats:
                break  # 语料已经被压成单 token，提前停比凑满词表更诚实
            # max 的 key 里带上 pair 本身：频次相同时按 id 排序，
            # 保证同一份语料每次训练出完全一样的词表（可复现）。
            best = max(stats.items(), key=lambda kv: (kv[1], kv[0]))[0]
            new_id = 256 + step
            words = {_merge_word(w, best, new_id): f for w, f in words.items()}
            merges.append(best)
            if verbose and (step + 1) % 50 == 0:
                print(f"  merge {step + 1:4d}: {best} -> {new_id} (freq={stats[best]})")

        return cls(merges)

    # ---- 词表 ----------------------------------------------------------

    def _build_vocab(self) -> dict[int, bytes]:
        vocab: dict[int, bytes] = {i: bytes([i]) for i in range(256)}
        for i, (a, b) in enumerate(self.merges):
            vocab[256 + i] = vocab[a] + vocab[b]
        return vocab

    @property
    def vocab_size(self) -> int:
        return 256 + len(self.merges)

    def token_bytes(self, token_id: int) -> bytes:
        return self._vocab[token_id]

    # ---- 编解码 --------------------------------------------------------

    def _encode_word(self, word: str) -> list[int]:
        ids = list(word.encode("utf-8"))
        while len(ids) >= 2:
            # 每轮找当前序列里 rank 最小（最早学到）的 pair。
            # 不能简单按 merges 顺序遍历全表——那是 O(vocab) 每轮，
            # 而且合并会产生新的相邻关系，必须重新找。
            pairs = set(zip(ids, ids[1:]))
            candidate = min(pairs, key=lambda p: self._rank.get(p, float("inf")))
            if candidate not in self._rank:
                break
            ids = list(_merge_word(tuple(ids), candidate, 256 + self._rank[candidate]))
        return ids

    def encode(self, text: str) -> list[int]:
        out: list[int] = []
        for word in pre_tokenize(text):
            out.extend(self._encode_word(word))
        return out

    def decode(self, ids: list[int]) -> str:
        raw = b"".join(self._vocab[i] for i in ids)
        # errors="replace"：一个 token 可能只是某个汉字的半截字节，
        # 单独解码本来就不合法。这是字节级 BPE 的正常现象，不是 bug。
        return raw.decode("utf-8", errors="replace")

    # ---- 持久化 --------------------------------------------------------

    def save(self, path: str | Path) -> None:
        Path(path).write_text(
            json.dumps({"merges": [list(p) for p in self.merges]}, ensure_ascii=False),
            encoding="utf-8",
        )

    @classmethod
    def load(cls, path: str | Path) -> "BPETokenizer":
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        return cls([tuple(p) for p in data["merges"]])
