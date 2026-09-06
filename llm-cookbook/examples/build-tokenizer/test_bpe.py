"""BPE 实现的自检：训练、编码、解码、持久化，全部可复现。

运行：python -m pytest test_bpe.py -v   （或用 python test_bpe.py 直接跑）
"""

from __future__ import annotations

import tempfile
from collections import Counter
from pathlib import Path

from bpe import BPETokenizer, pre_tokenize

CORPUS = Path(__file__).parent / "data" / "corpus.txt"


def test_pre_tokenize_keeps_spaces() -> None:
    # 前导空格属于词片，否则解码时无法还原空格（编码器无法区分
    # "the model" 和 "themodel"）。
    words = pre_tokenize("the model")
    assert words[0].endswith("the")
    assert words[1].startswith(" ") and "model" in words[1]


def test_train_is_deterministic() -> None:
    text = CORPUS.read_text(encoding="utf-8")
    t1 = BPETokenizer.train(text, 512)
    t2 = BPETokenizer.train(text, 512)
    assert t1.merges == t2.merges, "同一语料必须训出完全相同的合并序列"


def test_roundtrip_is_lossless() -> None:
    text = CORPUS.read_text(encoding="utf-8")
    tok = BPETokenizer.train(text, 1024)
    assert tok.decode(tok.encode(text)) == text


def test_roundtrip_across_scripts_and_emoji() -> None:
    tok = BPETokenizer.train("héllo 你好 🚀 中文与英文混排的测试文本。", 512)
    for s in ["héllo", "你好世界", "🚀", "the model runs."]:
        assert tok.decode(tok.encode(s)) == s


def test_merge_is_left_to_right_non_overlapping() -> None:
    # 合并 (a,a) 时 "aaa" 必须得到 [aa, a]，而不是重叠地把中间字符用两次。
    tok = BPETokenizer.train("aaa aa aaa", 257)
    assert tok.encode("aaa") == [tok.vocab_size - 1, ord("a")]


def test_unknown_bytes_are_invocab() -> None:
    tok = BPETokenizer.train("abc", 256)  # 不训练任何合并
    assert tok.vocab_size == 256
    # 字节表覆盖任何 UTF-8 输入，绝无 UNK。
    assert tok.decode(tok.encode("😀")) == "😀"


def test_frequency_ordering() -> None:
    # "ab" 出现 10 次、"cd" 出现 2 次：第一个学到的必须是 (a, b)。
    text = "ab" * 10 + "cd" * 2
    tok = BPETokenizer.train(text, 257)
    assert tok.merges[0] == (ord("a"), ord("b"))


def test_save_load_roundtrip() -> None:
    text = CORPUS.read_text(encoding="utf-8")
    tok = BPETokenizer.train(text, 512)
    with tempfile.TemporaryDirectory() as d:
        path = Path(d) / "tok.json"
        tok.save(path)
        loaded = BPETokenizer.load(path)
    assert loaded.merges == tok.merges
    assert loaded.encode("the model") == tok.encode("the model")


def test_vocab_builds_correct_bytes() -> None:
    tok = BPETokenizer.train("ab ab ab", 258)
    # 第一个合并 (a, b) -> id 256，其字节必须是 b"ab"。
    assert tok.token_bytes(256) == b"ab"


if __name__ == "__main__":
    import sys

    from pathlib import Path as P

    # 简易 runner：不依赖 pytest 也能验证
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    failed = 0
    for fn in fns:
        try:
            fn()
            print(f"  PASS {fn.__name__}")
        except Exception as e:  # noqa: BLE001
            failed += 1
            print(f"  FAIL {fn.__name__}: {e!r}")
    sys.exit(1 if failed else 0)
