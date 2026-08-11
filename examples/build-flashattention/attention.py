"""FlashAttention 的核心：在线 softmax，让注意力不再需要 O(T²) 显存。

朴素注意力必须先算完整个 T×T 的分数矩阵，softmax 归一化，再乘 V。
T=8192 时这个矩阵单精度就要 256MB —— 而且它只是中间结果，算完就扔。

FlashAttention 的观察是：softmax 可以分块增量计算。逐块扫描 K/V，
边扫边维护「到目前为止的最大值 m」和「到目前为止的分母 l」，
新块到来时用一个修正因子把旧的累加结果重新缩放到新的基准上。
全程只需要 O(块大小) 的中间显存。

本文件用纯 PyTorch 实现这个算法（CPU 也能跑），并证明它与朴素实现
数值等价。真正的加速来自把这个循环写进 CUDA kernel，让分块常驻 SRAM ——
那是 triton_kernel.py 的内容，需要 GPU。算法本身在这里就能看懂。
"""

from __future__ import annotations

import math

import torch


def naive_attention(q: torch.Tensor, k: torch.Tensor, v: torch.Tensor, causal: bool = True) -> torch.Tensor:
    """教科书写法：显式构造 T×T 分数矩阵。

    形状约定（全文件统一）：q/k/v 都是 (B, H, T, D)。
    """
    scale = 1.0 / math.sqrt(q.size(-1))
    scores = (q @ k.transpose(-2, -1)) * scale            # (B, H, T, T) <- 显存杀手
    if causal:
        T = q.size(-2)
        mask = torch.ones(T, T, dtype=torch.bool, device=q.device).tril()
        scores = scores.masked_fill(~mask, float("-inf"))
    return torch.softmax(scores, dim=-1) @ v


def _safe_softmax_max(scores: torch.Tensor) -> torch.Tensor:
    """行最大值，但整行都是 -inf 时返回 0 而不是 -inf。

    因果掩码下，某个 Q 块可能完全在某个 K 块之前，那一块的分数全是 -inf。
    直接拿 -inf 当基准会算出 exp(-inf - -inf) = exp(nan) = nan，
    一个 nan 就能污染整个输出。这是分块实现最容易踩的坑。
    """
    m = scores.max(dim=-1).values
    return torch.where(torch.isinf(m), torch.zeros_like(m), m)


def flash_attention(
    q: torch.Tensor,
    k: torch.Tensor,
    v: torch.Tensor,
    causal: bool = True,
    block_q: int = 64,
    block_k: int = 64,
) -> torch.Tensor:
    """分块 + 在线 softmax。数值上等价于 naive_attention，显存是 O(block²)。

    外层遍历 Q 块，内层遍历 K/V 块。对每个 Q 块维护三个累加器：
        m —— 当前见过的最大分数（每行一个）
        l —— 当前的 softmax 分母（每行一个）
        acc —— 当前的加权 V 累加（每行 D 维）
    新块到来时先更新 m，再用 exp(m_old - m_new) 把 l 和 acc 缩放到新基准。
    """
    B, H, T, D = q.shape
    scale = 1.0 / math.sqrt(D)
    out = torch.zeros_like(q)

    for q_start in range(0, T, block_q):
        q_end = min(q_start + block_q, T)
        qi = q[:, :, q_start:q_end, :]                     # (B, H, Bq, D)
        bq = q_end - q_start

        m = torch.full((B, H, bq), float("-inf"), device=q.device, dtype=q.dtype)
        l = torch.zeros((B, H, bq), device=q.device, dtype=q.dtype)
        acc = torch.zeros((B, H, bq, D), device=q.device, dtype=q.dtype)

        # 因果时只需扫到当前 Q 块的末尾——后面的 K 块整块被掩掉，
        # 算了也是 -inf。这直接省掉大约一半计算量。
        k_limit = q_end if causal else T

        for k_start in range(0, k_limit, block_k):
            k_end = min(k_start + block_k, k_limit)
            kj = k[:, :, k_start:k_end, :]
            vj = v[:, :, k_start:k_end, :]

            s = (qi @ kj.transpose(-2, -1)) * scale        # (B, H, Bq, Bk) <- 只有这么大

            if causal:
                # 全局位置比较：Q 的第 i 行只能看到 K 的前 i 列
                qpos = torch.arange(q_start, q_end, device=q.device).view(-1, 1)
                kpos = torch.arange(k_start, k_end, device=q.device).view(1, -1)
                s = s.masked_fill(qpos < kpos, float("-inf"))

            m_new = torch.maximum(m, _safe_softmax_max(s))
            # 修正因子：把旧的 l 和 acc 从旧基准 m 换算到新基准 m_new
            correction = torch.exp(m - m_new)
            correction = torch.nan_to_num(correction, nan=0.0)   # 首块时 m=-inf

            p = torch.exp(s - m_new.unsqueeze(-1))
            p = torch.nan_to_num(p, nan=0.0)                     # 整行 -inf 的块

            l = correction * l + p.sum(dim=-1)
            acc = correction.unsqueeze(-1) * acc + p @ vj
            m = m_new

        # 最后统一除分母。全程只除这一次，是在线 softmax 能成立的关键：
        # 中间步骤保留未归一化的累加值，归一化推迟到最后。
        out[:, :, q_start:q_end, :] = acc / l.clamp(min=1e-20).unsqueeze(-1)

    return out


def peak_score_matrix_elements(T: int, block_q: int, block_k: int) -> tuple[int, int]:
    """返回（朴素实现、分块实现）各自需要同时驻留的分数矩阵元素数。

    这是 FlashAttention 省显存的直接量化：朴素是 T²，分块是 block_q×block_k，
    与序列长度无关。
    """
    return T * T, block_q * block_k
