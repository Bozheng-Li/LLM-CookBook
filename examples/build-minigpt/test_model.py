"""miniGPT 的结构自检：因果性、RoPE 相对性、初始 loss、权重绑定。

这些不是"跑通就行"的冒烟测试，而是每一条都对应一个真实会犯且难以察觉的错误。
比如因果掩码写反了模型照样收敛（甚至 loss 更低），只有专门测才发现。

运行：python test_model.py     或    python -m pytest test_model.py -v
"""

from __future__ import annotations

import math

import torch
import torch.nn.functional as F

from model import (
    GPTConfig,
    MiniGPT,
    RMSNorm,
    apply_rope,
    attention_reference,
    build_rope_cache,
)

torch.manual_seed(0)


def _tiny() -> GPTConfig:
    return GPTConfig(vocab_size=64, block_size=16, n_layer=2, n_head=2, n_embd=32)


def test_attention_reference_matches_sdpa() -> None:
    """手写朴素实现必须和 PyTorch 的融合算子数值一致。

    这条测试保证了"教学版"和"生产版"讲的是同一件事——
    否则正文里的公式推导就和实际跑的代码脱节了。
    """
    q, k, v = (torch.randn(2, 2, 8, 16, dtype=torch.float64) for _ in range(3))
    ours = attention_reference(q, k, v)
    theirs = F.scaled_dot_product_attention(q, k, v, is_causal=True)
    assert torch.allclose(ours, theirs, atol=1e-10), (ours - theirs).abs().max()


def test_attention_is_causal() -> None:
    """位置 t 的输出不能被 t 之后的 token 影响。

    做法：改动最后一个位置的输入，检查前面所有位置的输出完全不变。
    掩码写成上三角、或忘记 is_causal，这条立刻失败。
    """
    cfg = _tiny()
    model = MiniGPT(cfg).eval()
    idx = torch.randint(0, cfg.vocab_size, (1, 8))

    with torch.no_grad():
        base, _ = model(idx)
        tampered = idx.clone()
        tampered[0, -1] = (tampered[0, -1] + 1) % cfg.vocab_size
        after, _ = model(tampered)

    assert torch.allclose(base[:, :-1], after[:, :-1], atol=1e-6), "未来 token 泄漏到了过去"
    assert not torch.allclose(base[:, -1], after[:, -1]), "最后一个位置本应改变"


def test_rope_encodes_relative_position() -> None:
    """RoPE 的核心性质：旋转后的点积只依赖相对位置。

    取同一对向量，分别放在 (2,5) 和 (7,10)，间隔都是 3，
    点积必须相同。这是它能外推到训练长度之外的数学基础。
    """
    head_dim = 16
    cos, sin = build_rope_cache(32, head_dim, torch.device("cpu"))
    a = torch.randn(1, 1, 1, head_dim, dtype=torch.float32)
    b = torch.randn(1, 1, 1, head_dim, dtype=torch.float32)

    def dot_at(i: int, j: int) -> float:
        qi = apply_rope(a, cos[i : i + 1], sin[i : i + 1])
        kj = apply_rope(b, cos[j : j + 1], sin[j : j + 1])
        return float((qi * kj).sum())

    assert math.isclose(dot_at(2, 5), dot_at(7, 10), abs_tol=1e-4)
    assert math.isclose(dot_at(0, 1), dot_at(20, 21), abs_tol=1e-4)
    # 间隔不同则点积不同，否则说明位置信息根本没进去
    assert not math.isclose(dot_at(0, 1), dot_at(0, 9), abs_tol=1e-3)


def test_rmsnorm_normalizes_scale() -> None:
    norm = RMSNorm(64)
    x = torch.randn(4, 64) * 100      # 故意放大 100 倍
    y = norm(x)
    rms = y.pow(2).mean(-1).sqrt()
    assert torch.allclose(rms, torch.ones(4), atol=1e-3), rms
    # 与 LayerNorm 的差别：不减均值，所以输出均值不为 0
    assert y.mean(-1).abs().max() > 1e-3


def test_initial_loss_matches_uniform_baseline() -> None:
    """随机初始化时，模型应当接近均匀分布，loss ≈ ln(vocab_size)。

    这是最有价值的一条初始化检查：初始 loss 明显偏高说明 logits
    尺度失控，偏低则往往意味着标签泄漏或权重初始化把某些类别拉偏了。

    注意 targets 必须与 idx 独立。若写成 model(idx, idx)——让每个位置
    预测它自己——在权重绑定下 loss 会降到 3.5 左右（vocab=64 时基线 4.16），
    因为 head 与 tok_emb 共享权重，残差路径上输入 embedding 的分量
    直接和输出投影点积回自身。这正是本条测试要抓的泄漏形态。
    """
    cfg = _tiny()
    model = MiniGPT(cfg)
    idx = torch.randint(0, cfg.vocab_size, (8, 16))
    targets = torch.randint(0, cfg.vocab_size, (8, 16))
    _, loss = model(idx, targets)
    expected = math.log(cfg.vocab_size)
    assert abs(loss.item() - expected) < 0.25, f"初始 loss {loss.item():.3f} 偏离 {expected:.3f}"


def test_weight_tying_creates_measurable_leak() -> None:
    """把上面那个坑固定成一条正向测试：同位置自预测确实会泄漏。

    留着它有两个用处：一是说明"loss 比基线低"不总是好消息，
    二是任何人以后改动残差结构导致泄漏消失时，这条会失败并提醒复查。
    """
    cfg = _tiny()
    model = MiniGPT(cfg)
    idx = torch.randint(0, cfg.vocab_size, (8, 16))
    _, leaked = model(idx, idx)
    _, clean = model(idx, torch.randint(0, cfg.vocab_size, (8, 16)))
    assert leaked.item() < clean.item() - 0.3, (leaked.item(), clean.item())


def test_weight_tying_shares_storage() -> None:
    cfg = _tiny()
    tied = MiniGPT(cfg)
    assert tied.head.weight.data_ptr() == tied.tok_emb.weight.data_ptr()

    untied = MiniGPT(GPTConfig(**{**cfg.__dict__, "tie_weights": False}))
    assert untied.head.weight.data_ptr() != untied.tok_emb.weight.data_ptr()
    # 绑定确实省下了 vocab_size × n_embd 个参数
    assert untied.num_params() - tied.num_params() == cfg.vocab_size * cfg.n_embd


def test_gradients_reach_every_parameter() -> None:
    """没有梯度的参数 = 白占显存的死代码，通常是忘了接进计算图。"""
    cfg = _tiny()
    model = MiniGPT(cfg)
    idx = torch.randint(0, cfg.vocab_size, (2, 8))
    _, loss = model(idx, idx)
    loss.backward()
    dead = [n for n, p in model.named_parameters() if p.grad is None or p.grad.abs().sum() == 0]
    # head 与 tok_emb 绑定，梯度合并到同一个张量上，只报一次
    assert not dead, f"这些参数没有收到梯度：{dead}"


def test_generate_shape_and_determinism() -> None:
    cfg = _tiny()
    model = MiniGPT(cfg)
    ctx = torch.zeros((1, 1), dtype=torch.long)

    torch.manual_seed(42)
    a = model.generate(ctx, 10, temperature=0.8, top_k=5)
    torch.manual_seed(42)
    b = model.generate(ctx, 10, temperature=0.8, top_k=5)

    assert a.shape == (1, 11)
    assert torch.equal(a, b), "固定随机种子后采样必须可复现"


def test_generate_respects_block_size() -> None:
    """超出上下文时靠左截断，不应该越界报错。"""
    cfg = _tiny()
    model = MiniGPT(cfg)
    ctx = torch.zeros((1, 1), dtype=torch.long)
    out = model.generate(ctx, cfg.block_size + 20)
    assert out.shape == (1, cfg.block_size + 21)


def test_no_nan_in_forward() -> None:
    cfg = _tiny()
    model = MiniGPT(cfg)
    idx = torch.randint(0, cfg.vocab_size, (4, 16))
    logits, loss = model(idx, idx)
    assert torch.isfinite(logits).all() and torch.isfinite(loss)


if __name__ == "__main__":
    import sys

    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    failed = 0
    for fn in fns:
        try:
            fn()
            print(f"  PASS {fn.__name__}")
        except Exception as e:  # noqa: BLE001
            failed += 1
            print(f"  FAIL {fn.__name__}: {e!r}")
    print(f"\n{len(fns) - failed}/{len(fns)} passed")
    sys.exit(1 if failed else 0)
