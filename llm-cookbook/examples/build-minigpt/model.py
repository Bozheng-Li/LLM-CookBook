"""一个能训练的最小 GPT：约 200 行覆盖 Transformer 解码器的全部结构。

刻意保留的现代做法（与 GPT-2 原版不同，与 LLaMA 系一致）：
  - Pre-LN：残差前做归一化，深层才训得稳
  - RMSNorm：去掉均值项，比 LayerNorm 少一半统计量
  - SwiGLU：门控前馈，同参数量下比 ReLU MLP 效果好
  - RoPE：旋转位置编码，位置信息进注意力分数而非输入
  - 权重绑定：embedding 与输出头共享，小模型上省下可观参数

刻意省略的：dropout（小数据上我们要看的是过拟合本身）、
KV cache（推理章节单独讲）、混合精度（会掩盖数值问题）。
"""

from __future__ import annotations

import math
from dataclasses import dataclass

import torch
import torch.nn as nn
import torch.nn.functional as F


@dataclass
class GPTConfig:
    vocab_size: int = 256
    block_size: int = 128       # 上下文长度
    n_layer: int = 4
    n_head: int = 4
    n_embd: int = 128
    tie_weights: bool = True

    @property
    def head_dim(self) -> int:
        assert self.n_embd % self.n_head == 0, "n_embd 必须能被 n_head 整除"
        return self.n_embd // self.n_head


class RMSNorm(nn.Module):
    """x / rms(x) * g。没有减均值，也没有 bias。

    LayerNorm 减均值是为了让分布居中，但残差网络里这一项的收益很小，
    去掉后少一次归约、少一组参数，效果基本不变。这是 LLaMA 的选择。
    """

    def __init__(self, dim: int, eps: float = 1e-6) -> None:
        super().__init__()
        self.eps = eps
        self.weight = nn.Parameter(torch.ones(dim))

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        rms = torch.rsqrt(x.pow(2).mean(-1, keepdim=True) + self.eps)
        return x * rms * self.weight


def build_rope_cache(seq_len: int, head_dim: int, device, base: float = 10000.0):
    """预计算 RoPE 的 cos/sin 表。

    RoPE 把位置编码成一个二维旋转：把 head_dim 拆成 head_dim/2 对，
    第 i 对以角速度 base^(-2i/d) 随位置旋转。查询和键各自旋转后做点积，
    结果只依赖两者的相对位置——这就是它能外推的原因。
    """
    assert head_dim % 2 == 0, "RoPE 需要偶数维，每两维配成一对做旋转"
    inv_freq = 1.0 / (base ** (torch.arange(0, head_dim, 2, device=device).float() / head_dim))
    pos = torch.arange(seq_len, device=device).float()
    freqs = torch.outer(pos, inv_freq)          # (T, head_dim/2)
    return freqs.cos(), freqs.sin()


def apply_rope(x: torch.Tensor, cos: torch.Tensor, sin: torch.Tensor) -> torch.Tensor:
    """x: (B, n_head, T, head_dim)。对每对相邻维度做二维旋转。"""
    T = x.size(-2)
    cos, sin = cos[:T], sin[:T]                  # 支持比缓存短的序列
    x1, x2 = x[..., 0::2], x[..., 1::2]          # 偶数维、奇数维配成一对
    rot1 = x1 * cos - x2 * sin
    rot2 = x1 * sin + x2 * cos
    return torch.stack((rot1, rot2), dim=-1).flatten(-2)


class CausalSelfAttention(nn.Module):
    def __init__(self, cfg: GPTConfig) -> None:
        super().__init__()
        self.n_head = cfg.n_head
        self.head_dim = cfg.head_dim
        # 一次算出 q/k/v：三个矩阵乘合成一个，GPU 上更划算。
        self.qkv = nn.Linear(cfg.n_embd, 3 * cfg.n_embd, bias=False)
        self.proj = nn.Linear(cfg.n_embd, cfg.n_embd, bias=False)

    def forward(self, x: torch.Tensor, cos: torch.Tensor, sin: torch.Tensor) -> torch.Tensor:
        B, T, C = x.shape
        q, k, v = self.qkv(x).split(C, dim=2)
        # (B, T, C) -> (B, n_head, T, head_dim)
        q = q.view(B, T, self.n_head, self.head_dim).transpose(1, 2)
        k = k.view(B, T, self.n_head, self.head_dim).transpose(1, 2)
        v = v.view(B, T, self.n_head, self.head_dim).transpose(1, 2)

        # 位置信息只加在 q 和 k 上，不加在 v 上——v 携带内容，不携带位置。
        q, k = apply_rope(q, cos, sin), apply_rope(k, cos, sin)

        # is_causal=True 让 PyTorch 内部用 FlashAttention 路径，
        # 不materialize T×T 的注意力矩阵。手写版见 attention_reference()。
        y = F.scaled_dot_product_attention(q, k, v, is_causal=True)
        y = y.transpose(1, 2).contiguous().view(B, T, C)
        return self.proj(y)


def attention_reference(q, k, v) -> torch.Tensor:
    """朴素实现，仅用于对拍。生产路径请用 F.scaled_dot_product_attention。

    除以 sqrt(head_dim)：点积的方差随维度线性增长，不缩放的话 softmax
    会饱和成 one-hot，梯度直接消失。
    """
    att = (q @ k.transpose(-2, -1)) / math.sqrt(q.size(-1))
    T = q.size(-2)
    mask = torch.ones(T, T, dtype=torch.bool, device=q.device).tril()
    att = att.masked_fill(~mask, float("-inf"))
    return F.softmax(att, dim=-1) @ v


class SwiGLU(nn.Module):
    """门控前馈：SiLU(W1 x) * (W3 x) 再过 W2。

    隐藏维取 8/3 倍而非 4 倍：门控多了一个投影矩阵，按 8/3 缩放后
    总参数量与标准 4 倍 MLP 持平，比较才公平。
    """

    def __init__(self, cfg: GPTConfig) -> None:
        super().__init__()
        hidden = int(8 * cfg.n_embd / 3)
        hidden = 32 * ((hidden + 31) // 32)      # 对齐到 32，对 GPU 友好
        self.w1 = nn.Linear(cfg.n_embd, hidden, bias=False)
        self.w3 = nn.Linear(cfg.n_embd, hidden, bias=False)
        self.w2 = nn.Linear(hidden, cfg.n_embd, bias=False)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.w2(F.silu(self.w1(x)) * self.w3(x))


class Block(nn.Module):
    """Pre-LN 残差块：x = x + f(norm(x))。

    与 Post-LN（x = norm(x + f(x))）的关键差别是残差路径上没有归一化，
    梯度可以原样传到底层。这是能训深的直接原因。
    """

    def __init__(self, cfg: GPTConfig) -> None:
        super().__init__()
        self.norm1 = RMSNorm(cfg.n_embd)
        self.attn = CausalSelfAttention(cfg)
        self.norm2 = RMSNorm(cfg.n_embd)
        self.mlp = SwiGLU(cfg)

    def forward(self, x: torch.Tensor, cos: torch.Tensor, sin: torch.Tensor) -> torch.Tensor:
        x = x + self.attn(self.norm1(x), cos, sin)
        x = x + self.mlp(self.norm2(x))
        return x


class MiniGPT(nn.Module):
    def __init__(self, cfg: GPTConfig) -> None:
        super().__init__()
        self.cfg = cfg
        self.tok_emb = nn.Embedding(cfg.vocab_size, cfg.n_embd)
        self.blocks = nn.ModuleList(Block(cfg) for _ in range(cfg.n_layer))
        self.norm_f = RMSNorm(cfg.n_embd)
        self.head = nn.Linear(cfg.n_embd, cfg.vocab_size, bias=False)
        if cfg.tie_weights:
            # 输入 embedding 与输出投影共享权重。小模型上 vocab×n_embd
            # 可能占总参数的一半，绑定后省下的量很可观，且通常还略微提升效果。
            self.head.weight = self.tok_emb.weight

        self.apply(self._init_weights)
        # 残差投影按 1/sqrt(2*n_layer) 缩放：n_layer 个残差分支累加后
        # 方差会线性增长，不缩放的话深层激活会爆掉。GPT-2 起的标准做法。
        for name, p in self.named_parameters():
            if name.endswith("proj.weight") or name.endswith("w2.weight"):
                nn.init.normal_(p, mean=0.0, std=0.02 / math.sqrt(2 * cfg.n_layer))

        cos, sin = build_rope_cache(cfg.block_size, cfg.head_dim, torch.device("cpu"))
        # register_buffer：随 .to(device) / state_dict 移动，但不是可学参数。
        self.register_buffer("rope_cos", cos, persistent=False)
        self.register_buffer("rope_sin", sin, persistent=False)

    @staticmethod
    def _init_weights(m: nn.Module) -> None:
        if isinstance(m, (nn.Linear, nn.Embedding)):
            nn.init.normal_(m.weight, mean=0.0, std=0.02)
            if isinstance(m, nn.Linear) and m.bias is not None:
                nn.init.zeros_(m.bias)

    def num_params(self, non_embedding: bool = False) -> int:
        n = sum(p.numel() for p in self.parameters())
        if non_embedding:
            n -= self.tok_emb.weight.numel()
        return n

    def forward(self, idx: torch.Tensor, targets: torch.Tensor | None = None):
        B, T = idx.shape
        assert T <= self.cfg.block_size, f"序列长 {T} 超过 block_size {self.cfg.block_size}"
        x = self.tok_emb(idx)
        for block in self.blocks:
            x = block(x, self.rope_cos, self.rope_sin)
        x = self.norm_f(x)
        logits = self.head(x)

        loss = None
        if targets is not None:
            # 展平成 (B*T, vocab)：交叉熵按 token 平均，与批大小和序列长解耦。
            loss = F.cross_entropy(logits.view(-1, logits.size(-1)), targets.reshape(-1))
        return logits, loss

    @torch.no_grad()
    def generate(
        self,
        idx: torch.Tensor,
        max_new_tokens: int,
        temperature: float = 1.0,
        top_k: int | None = None,
    ) -> torch.Tensor:
        self.eval()
        for _ in range(max_new_tokens):
            # 超过上下文就截断左侧。没有 KV cache，所以每步重算整个前缀——
            # 教学版可以接受，生产必须缓存。
            idx_cond = idx[:, -self.cfg.block_size:]
            logits, _ = self(idx_cond)
            logits = logits[:, -1, :] / max(temperature, 1e-5)
            if top_k is not None:
                v, _ = torch.topk(logits, min(top_k, logits.size(-1)))
                logits[logits < v[:, [-1]]] = float("-inf")
            probs = F.softmax(logits, dim=-1)
            idx = torch.cat((idx, torch.multinomial(probs, num_samples=1)), dim=1)
        return idx
