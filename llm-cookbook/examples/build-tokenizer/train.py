"""训练一个 BPE 并打印压缩率——把"学会了什么"变成可以看的数字。

用法:
    python train.py                      # 默认语料，词表 1024
    python train.py --vocab-size 2048
    python train.py --input mytext.txt --save tokenizer.json
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from bpe import BPETokenizer, pre_tokenize

# Windows 控制台默认 GBK，打不出 ✓ 这类字符；把 stdout 切到 UTF-8。
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

HERE = Path(__file__).parent
DEFAULT_CORPUS = HERE / "data" / "corpus.txt"


def report(tok: BPETokenizer, text: str) -> None:
    ids = tok.encode(text)
    n_bytes = len(text.encode("utf-8"))
    n_chars = len(text)

    print(f"\n词表大小      {tok.vocab_size}")
    print(f"原文字符      {n_chars}")
    print(f"原文字节      {n_bytes}")
    print(f"token 数      {len(ids)}")
    print(f"压缩率        {n_bytes / len(ids):.2f} 字节/token")
    print(f"字符/token    {n_chars / len(ids):.2f}")

    # 无损性是 tokenizer 的底线：解不回原文，后面训练再好也没意义。
    assert tok.decode(ids) == text, "解码结果与原文不一致"
    print("往返一致      ✓")

    print("\n学到的最长 10 个 token：")
    long_tokens = sorted(
        (tok.token_bytes(i) for i in range(256, tok.vocab_size)),
        key=len,
        reverse=True,
    )[:10]
    for b in long_tokens:
        print(f"  {len(b):3d} 字节  {b.decode('utf-8', errors='replace')!r}")


def main() -> None:
    ap = argparse.ArgumentParser(description="训练字节级 BPE")
    ap.add_argument("--input", type=Path, default=DEFAULT_CORPUS)
    ap.add_argument("--vocab-size", type=int, default=1024)
    ap.add_argument("--save", type=Path, default=None)
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    text = args.input.read_text(encoding="utf-8")
    print(f"语料 {args.input.name}：{len(text)} 字符，{len(pre_tokenize(text))} 个词片")

    print(f"训练中（目标词表 {args.vocab_size}）...")
    tok = BPETokenizer.train(text, args.vocab_size, verbose=not args.quiet)

    report(tok, text)

    if args.save:
        tok.save(args.save)
        print(f"\n已保存到 {args.save}")

    print("\n编码示例：")
    for s in ["hello world", "大模型", " the model"]:
        ids = tok.encode(s)
        pieces = [tok.token_bytes(i).decode("utf-8", errors="replace") for i in ids]
        print(f"  {s!r:16} -> {len(ids)} tokens {pieces}")


if __name__ == "__main__":
    main()
