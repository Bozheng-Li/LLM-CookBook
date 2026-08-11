"""训练 miniGPT，在 CPU 上 2 分钟内跑完并看到 loss 明显下降。

用法:
    python train.py                     # 默认：300 步，CPU 可跑
    python train.py --steps 2000 --device cuda
    python train.py --sample-only --ckpt out/ckpt.pt
"""

from __future__ import annotations

import argparse
import math
import sys
import time
from pathlib import Path

import torch

from data import CharDataset, download_corpus, resolve_corpus
from model import GPTConfig, MiniGPT

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

HERE = Path(__file__).parent


def pick_device(requested: str) -> torch.device:
    if requested != "auto":
        return torch.device(requested)
    if torch.cuda.is_available():
        return torch.device("cuda")
    return torch.device("cpu")


def lr_at(step: int, total: int, base_lr: float, warmup: int) -> float:
    """线性 warmup + 余弦退火。

    warmup 存在的原因很具体：训练最初几十步梯度方向噪声极大，
    直接用全学习率会把随机初始化的权重推到很难恢复的区域。
    """
    if step < warmup:
        return base_lr * (step + 1) / warmup
    progress = (step - warmup) / max(1, total - warmup)
    return base_lr * 0.5 * (1.0 + math.cos(math.pi * progress))


@torch.no_grad()
def evaluate(model: MiniGPT, data: CharDataset, split: str, batches: int, batch_size: int, device) -> float:
    model.eval()
    losses = []
    for _ in range(batches):
        x, y = data.get_batch(split, batch_size, model.cfg.block_size, device)
        _, loss = model(x, y)
        losses.append(loss.item())
    model.train()
    return sum(losses) / len(losses)


def main() -> None:
    ap = argparse.ArgumentParser(description="训练 miniGPT")
    ap.add_argument("--steps", type=int, default=300)
    ap.add_argument("--batch-size", type=int, default=32)
    ap.add_argument("--block-size", type=int, default=128)
    ap.add_argument("--n-layer", type=int, default=4)
    ap.add_argument("--n-head", type=int, default=4)
    ap.add_argument("--n-embd", type=int, default=128)
    ap.add_argument("--lr", type=float, default=3e-4)
    ap.add_argument("--warmup", type=int, default=30)
    ap.add_argument("--eval-every", type=int, default=50)
    ap.add_argument("--device", default="auto")
    ap.add_argument("--seed", type=int, default=1337)
    ap.add_argument("--out", type=Path, default=HERE / "out")
    ap.add_argument("--download", action="store_true", help="下载 1.1MB 完整语料（默认用自带的 40KB）")
    ap.add_argument("--sample-only", action="store_true")
    ap.add_argument("--ckpt", type=Path, default=None)
    args = ap.parse_args()

    torch.manual_seed(args.seed)
    device = pick_device(args.device)
    corpus = download_corpus() if args.download else resolve_corpus()
    data = CharDataset(corpus)
    print(f"设备 {device} · 语料 {data.path.name}（{len(data.text)} 字符）· 词表 {data.vocab_size}")

    if args.sample_only:
        ckpt = torch.load(args.ckpt or args.out / "ckpt.pt", map_location=device, weights_only=False)
        model = MiniGPT(ckpt["config"]).to(device)
        model.load_state_dict(ckpt["model"])
        print(sample(model, data, device))
        return

    cfg = GPTConfig(
        vocab_size=data.vocab_size,
        block_size=args.block_size,
        n_layer=args.n_layer,
        n_head=args.n_head,
        n_embd=args.n_embd,
    )
    model = MiniGPT(cfg).to(device)
    print(f"参数量 {model.num_params():,}（非 embedding {model.num_params(True):,}）")

    # weight decay 只加在矩阵上，不加在 norm 的增益和 bias 上——
    # 对一维参数做 L2 正则会直接把归一化的缩放能力压掉。
    decay = [p for p in model.parameters() if p.dim() >= 2]
    no_decay = [p for p in model.parameters() if p.dim() < 2]
    opt = torch.optim.AdamW(
        [{"params": decay, "weight_decay": 0.1}, {"params": no_decay, "weight_decay": 0.0}],
        lr=args.lr,
        betas=(0.9, 0.95),
    )

    print(f"\n{'step':>6} {'train':>8} {'val':>8} {'lr':>9} {'ms/step':>8}")
    t0 = time.time()
    for step in range(args.steps):
        lr = lr_at(step, args.steps, args.lr, args.warmup)
        for g in opt.param_groups:
            g["lr"] = lr

        x, y = data.get_batch("train", args.batch_size, cfg.block_size, device)
        _, loss = model(x, y)
        opt.zero_grad(set_to_none=True)
        loss.backward()
        # 梯度裁剪：语言模型偶尔会遇到一个 batch 让梯度范数暴涨，
        # 不裁的话一步就能毁掉之前所有训练。
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        opt.step()

        if step % args.eval_every == 0 or step == args.steps - 1:
            tr = evaluate(model, data, "train", 5, args.batch_size, device)
            va = evaluate(model, data, "val", 5, args.batch_size, device)
            ms = (time.time() - t0) / (step + 1) * 1000
            print(f"{step:6d} {tr:8.4f} {va:8.4f} {lr:9.2e} {ms:8.1f}")

    args.out.mkdir(parents=True, exist_ok=True)
    torch.save({"model": model.state_dict(), "config": cfg}, args.out / "ckpt.pt")
    print(f"\n已保存 {args.out / 'ckpt.pt'}")

    print(f"\n随机基线 loss = ln({data.vocab_size}) = {math.log(data.vocab_size):.4f}")
    print("训练后 loss 低于这个数，说明模型确实学到了字符分布。\n")
    print("--- 生成样例 ---")
    print(sample(model, data, device))


def sample(model: MiniGPT, data: CharDataset, device, n: int = 400) -> str:
    ctx = torch.zeros((1, 1), dtype=torch.long, device=device)
    out = model.generate(ctx, n, temperature=0.8, top_k=40)
    return data.decode(out[0].tolist())


if __name__ == "__main__":
    main()
