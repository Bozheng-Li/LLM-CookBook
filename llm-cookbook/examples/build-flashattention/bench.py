"""把「省显存」从口号变成一张表：同一组输入，两种实现，实测峰值显存与耗时。

跑法：
  python bench.py                    # 默认序列长度 512/1024/2048
  python bench.py --seq 4096 8192    # 自己指定
  python bench.py --device cuda      # 有 GPU 时看真实显存峰值

CPU 上没有显存概念，脚本会退回到「理论峰值元素数」这一列——
它同样能说明问题，因为省的正是那个 T×T 中间矩阵。
"""

from __future__ import annotations

import argparse
import sys
import time

import torch

from attention import flash_attention, naive_attention, peak_score_matrix_elements

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass


def _timed(fn, *args, warmup: int = 1, iters: int = 3, **kw) -> tuple[torch.Tensor, float]:
    for _ in range(warmup):
        out = fn(*args, **kw)
    if torch.cuda.is_available():
        torch.cuda.synchronize()
    t0 = time.perf_counter()
    for _ in range(iters):
        out = fn(*args, **kw)
    if torch.cuda.is_available():
        torch.cuda.synchronize()
    return out, (time.perf_counter() - t0) / iters * 1e3


def _peak_mb(device: str) -> float:
    """已分配显存峰值。CPU 上无从测量，返回 -1 由调用方处理。"""
    if device != "cuda":
        return -1.0
    return torch.cuda.max_memory_allocated() / 1024**2


def run(seq_lens: list[int], device: str, block: int, heads: int, head_dim: int) -> None:
    print(f"设备 {device} · B=1 H={heads} D={head_dim} · 块大小 {block}×{block}\n")
    print(f"{'T':>6}  {'朴素 ms':>9}  {'分块 ms':>9}  {'朴素峰值':>10}  {'分块峰值':>10}  {'最大误差':>9}")

    for T in seq_lens:
        shape = (1, heads, T, head_dim)
        g = torch.Generator(device="cpu").manual_seed(0)
        q, k, v = (torch.randn(shape, generator=g).to(device) for _ in range(3))

        naive_ms = naive_out = None
        naive_peak = -1.0
        # 长序列上朴素实现会 OOM——这本身就是要展示的结论，不是脚本失败。
        try:
            if device == "cuda":
                torch.cuda.reset_peak_memory_stats()
            naive_out, naive_ms = _timed(naive_attention, q, k, v, causal=True)
            naive_peak = _peak_mb(device)
        except torch.cuda.OutOfMemoryError:
            torch.cuda.empty_cache()

        if device == "cuda":
            torch.cuda.reset_peak_memory_stats()
        flash_out, flash_ms = _timed(
            flash_attention, q, k, v, causal=True, block_q=block, block_k=block
        )
        flash_peak = _peak_mb(device)

        if naive_out is None:
            naive_cell, naive_mem, err_cell = "OOM", "OOM", "—"
        else:
            naive_cell = f"{naive_ms:.1f}"
            elems, _ = peak_score_matrix_elements(T, block, block)
            naive_mem = f"{naive_peak:.1f} MB" if naive_peak >= 0 else f"{elems / 1e6:.1f}M 元素"
            err_cell = f"{(flash_out - naive_out).abs().max().item():.1e}"

        if flash_peak >= 0:
            flash_mem = f"{flash_peak:.1f} MB"
        else:
            _, elems = peak_score_matrix_elements(T, block, block)
            flash_mem = f"{elems / 1e6:.3f}M 元素"

        print(
            f"{T:>6}  {naive_cell:>9}  {flash_ms:>9.1f}  {naive_mem:>10}  {flash_mem:>10}  {err_cell:>9}"
        )

    print(
        "\n注：纯 PyTorch 分块版比朴素实现更慢是正常的——Python 循环的开销远大于省下的"
        "\n带宽。真正的加速要把这个循环写成 CUDA/Triton kernel，让分块常驻 SRAM。"
        "\n本表要说明的是显存那一列：它与序列长度无关。"
    )


def main() -> None:
    p = argparse.ArgumentParser(description="朴素注意力 vs 分块注意力：显存与耗时对比")
    p.add_argument("--seq", type=int, nargs="+", default=[512, 1024, 2048])
    p.add_argument("--device", default="cuda" if torch.cuda.is_available() else "cpu")
    p.add_argument("--block", type=int, default=128)
    p.add_argument("--heads", type=int, default=8)
    p.add_argument("--head-dim", type=int, default=64)
    a = p.parse_args()
    run(a.seq, a.device, a.block, a.heads, a.head_dim)


if __name__ == "__main__":
    main()
