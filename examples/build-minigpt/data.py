"""字符级数据集：不依赖外部 tokenizer，把文本压成 0..255 的字节 id。

为什么用字符而不是 BPE：本示例的语料只有 100KB，BPE 词表还没学会
高频合并规则就被用光了，多出的复杂度不换来任何教学价值。等 model.py
里的结构跑通了，再替换成 examples/build-tokenizer 里训练的 BPE
只改两个接口：data 用 tokenizer.encode(text)，vocab_size 换成词表大小。
"""

from __future__ import annotations

from pathlib import Path

import torch


class CharDataset:
    def __init__(self, path: Path, train_frac: float = 0.9) -> None:
        text = path.read_text(encoding="utf-8")
        self.text = text
        self.path = path

        # 字节 id：中文、emoji 天然是多字节，一个汉字是 2-3 个 id。
        raw = list(text.encode("utf-8"))
        self.ids = torch.tensor(raw, dtype=torch.long)
        self.vocab_size = 256

        split = int(len(self.ids) * train_frac)
        self.train_ids, self.val_ids = self.ids[:split], self.ids[split:]
        self.n_train = len(self.train_ids) // 32   # batch 数
        self.n_val = len(self.val_ids) // 32

    def get_batch(self, split: str, batch_size: int, block_size: int, device) -> tuple[torch.Tensor, torch.Tensor]:
        """取一个 batch：batch_size 个随机起点，各截 block_size+1 个字节。

        x 是前 block_size 个，y 是整体右移一位——每个位置预测下一个字节。
        随机取起点而不是顺序扫描：每步的梯度来自语料不同位置，
        等价于给优化器加噪声，通常收敛更快也更稳。
        """
        src = self.train_ids if split == "train" else self.val_ids
        n = len(src) - block_size - 1
        starts = torch.randint(0, n, (batch_size,))
        x = torch.stack([src[s : s + block_size] for s in starts])
        y = torch.stack([src[s + 1 : s + 1 + block_size] for s in starts])
        return x.to(device), y.to(device)

    def decode(self, ids: list[int]) -> str:
        return bytes(ids).decode("utf-8", errors="replace")


DATA_DIR = Path(__file__).parent / "data"
TINY_SHAKESPEARE = (
    "https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt"
)


def resolve_corpus() -> Path:
    """优先用下载的大语料，否则用仓库自带的小语料。

    自带语料保证首次运行不需要网络——这是本目录所有示例的共同约定。
    但 10KB 语料训不出通顺文本，只够看 loss 下降；想看到像样的生成结果
    请先跑 `python train.py --download`。
    """
    big = DATA_DIR / "input.txt"
    return big if big.exists() else DATA_DIR / "corpus.txt"


def download_corpus() -> Path:
    """下载 tinyshakespeare（约 1.1MB）。失败不致命，回落到自带语料。"""
    dst = DATA_DIR / "input.txt"
    if dst.exists():
        print(f"语料已存在（{dst.stat().st_size // 1024} KB），跳过下载")
        return dst

    import urllib.request

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    try:
        urllib.request.urlretrieve(TINY_SHAKESPEARE, dst)  # noqa: S310
        print(f"已下载语料（{dst.stat().st_size // 1024} KB）")
        return dst
    except Exception as e:  # noqa: BLE001
        dst.unlink(missing_ok=True)
        print(f"下载失败（{e}），回落到自带小语料。")
        print(f"也可以手动把任意 UTF-8 文本放到 {dst}，脚本会自动使用。")
        return resolve_corpus()
