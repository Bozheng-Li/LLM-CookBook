"""自检：分块实现必须与朴素实现数值等价，且不产生 nan。

跑法：python test_attention.py（或 python -m pytest test_attention.py）
"""

from __future__ import annotations

import math
import sys

import torch

from attention import (
    flash_attention,
    naive_attention,
    peak_score_matrix_elements,
)

torch.manual_seed(0)


def _qkv(B=2, H=3, T=128, D=32, dtype=torch.float32):
    g = torch.Generator().manual_seed(1234)
    shape = (B, H, T, D)
    return (
        torch.randn(shape, generator=g, dtype=dtype),
        torch.randn(shape, generator=g, dtype=dtype),
        torch.randn(shape, generator=g, dtype=dtype),
    )


def test_matches_naive_causal():
    q, k, v = _qkv()
    got = flash_attention(q, k, v, causal=True, block_q=32, block_k=32)
    want = naive_attention(q, k, v, causal=True)
    assert torch.allclose(got, want, atol=1e-5), (got - want).abs().max().item()


def test_matches_naive_non_causal():
    q, k, v = _qkv()
    got = flash_attention(q, k, v, causal=False, block_q=32, block_k=32)
    want = naive_attention(q, k, v, causal=False)
    assert torch.allclose(got, want, atol=1e-5), (got - want).abs().max().item()


def test_block_size_does_not_change_result():
    """块大小是性能旋钮，不该影响数值。不整除的尺寸也要对。"""
    q, k, v = _qkv(T=100)
    ref = naive_attention(q, k, v, causal=True)
    for bq, bk in [(1, 1), (7, 13), (32, 64), (128, 128), (100, 100)]:
        got = flash_attention(q, k, v, causal=True, block_q=bq, block_k=bk)
        assert torch.allclose(got, ref, atol=1e-5), f"block_q={bq} block_k={bk}"


def test_no_nan_when_query_block_precedes_key_block():
    """因果掩码下整块 -inf 是最容易出 nan 的路径，单独钉住。"""
    q, k, v = _qkv(T=64)
    out = flash_attention(q, k, v, causal=True, block_q=16, block_k=16)
    assert torch.isfinite(out).all()


def test_first_row_attends_only_to_itself():
    """因果时第 0 行只能看到位置 0，输出必须精确等于 v[0]。"""
    q, k, v = _qkv(T=32)
    out = flash_attention(q, k, v, causal=True, block_q=8, block_k=8)
    assert torch.allclose(out[:, :, 0, :], v[:, :, 0, :], atol=1e-6)


def test_matches_torch_sdpa():
    """与 PyTorch 官方实现对齐——它内部本身就用 FlashAttention。"""
    q, k, v = _qkv()
    want = torch.nn.functional.scaled_dot_product_attention(q, k, v, is_causal=True)
    got = flash_attention(q, k, v, causal=True, block_q=64, block_k=64)
    assert torch.allclose(got, want, atol=1e-5), (got - want).abs().max().item()


def test_gradients_match_naive():
    """反向也要对。在线 softmax 全靠 autograd 反传，缩放因子写错会在这里暴露。"""
    q, k, v = _qkv(T=64)
    grads = []
    for fn in (naive_attention, flash_attention):
        qq, kk, vv = (t.clone().requires_grad_(True) for t in (q, k, v))
        fn(qq, kk, vv, causal=True).sum().backward()
        grads.append((qq.grad, kk.grad, vv.grad))
    for a, b in zip(*grads):
        assert torch.allclose(a, b, atol=1e-5), (a - b).abs().max().item()


def test_memory_claim_is_real():
    """省显存不是口号：分块的峰值分数矩阵与 T 无关。"""
    naive_1k, blocked = peak_score_matrix_elements(1024, 64, 64)
    naive_8k, blocked_8k = peak_score_matrix_elements(8192, 64, 64)
    assert naive_8k == 64 * naive_1k          # T 翻 8 倍，朴素涨 64 倍
    assert blocked == blocked_8k == 4096      # 分块不变
    assert naive_8k / blocked_8k > 16000


def test_softmax_is_numerically_stable_on_large_scores():
    """减去行最大值的意义：不减的话 exp 会溢出成 inf。"""
    q, k, v = _qkv(T=64, D=16)
    q, k = q * 50, k * 50                     # 分数量级推到 exp 溢出区
    out = flash_attention(q, k, v, causal=True, block_q=16, block_k=16)
    ref = naive_attention(q, k, v, causal=True)
    assert torch.isfinite(out).all()
    assert torch.allclose(out, ref, atol=1e-4)


def test_scale_matches_one_over_sqrt_d():
    """缩放因子写错很难从输出看出来，用单位向量构造一个可手算的例子。"""
    B = H = 1
    T, D = 2, 4
    q = torch.zeros(B, H, T, D)
    k = torch.zeros(B, H, T, D)
    v = torch.tensor([[[[1.0, 0, 0, 0], [0.0, 1, 0, 0]]]])
    q[..., 0] = 1.0
    k[0, 0, 0, 0] = 1.0                       # 只有 k[0] 与 q 对齐
    out = flash_attention(q, k, v, causal=True, block_q=1, block_k=1)
    # 第 1 行看到 k[0]（分数 1/√D）和 k[1]（分数 0），权重 softmax([1/√D, 0])
    w = math.exp(1 / math.sqrt(D))
    assert abs(out[0, 0, 0, 0].item() - 1.0) < 1e-6            # 第 0 行只看到 k[0] -> v[0]
    assert abs(out[0, 0, 1, 0].item() - w / (w + 1)) < 1e-6    # 缩放因子错则此值必偏
    assert abs(out[0, 0, 1, 1].item() - 1 / (w + 1)) < 1e-6


if __name__ == "__main__":
    tests = sorted(
        (n, f) for n, f in globals().items() if n.startswith("test_") and callable(f)
    )
    failed = 0
    for name, fn in tests:
        try:
            fn()
            print(f"  PASS {name}")
        except AssertionError as e:
            failed += 1
            print(f"  FAIL {name}: {e}")
    print(f"\n{len(tests) - failed}/{len(tests)} passed")
    sys.exit(1 if failed else 0)
