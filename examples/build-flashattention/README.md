# 手写 FlashAttention

对应正文：[第 15 章 · 手写 FlashAttention](../../pages/15-practice/build-flashattention.html)

只依赖 PyTorch，**CPU 也能跑通全部测试**。这里实现的是算法本身——在线 softmax——
而不是 CUDA kernel。算法看懂了，kernel 只是把同一个循环搬进 SRAM。

## 跑起来

```bash
cd examples/build-flashattention
pip install -r requirements.txt

python test_attention.py     # 10 项等价性自检，CPU 约 10 秒
python bench.py              # 显存与耗时对比表
python bench.py --seq 4096 8192 --block 128
```

## 核心就是这七行

`attention.py` 里 `flash_attention()` 的内层循环：

```python
m_new = torch.maximum(m, _safe_softmax_max(s))
correction = torch.exp(m - m_new)        # 把旧累加值换算到新基准
p = torch.exp(s - m_new.unsqueeze(-1))
l = correction * l + p.sum(dim=-1)       # 分母
acc = correction.unsqueeze(-1) * acc + p @ vj   # 未归一化的加权 V
m = m_new
# 循环结束后才除一次：out = acc / l
```

朴素实现必须先算完整个 `T×T` 分数矩阵才能做 softmax，因为要先知道全局最大值和
全局分母。在线 softmax 的破解办法是：**先按当前已知的最大值累加，等看到更大的值
时再用 `exp(m_old - m_new)` 把旧账重算一遍**。归一化推迟到最后统一做一次。

## 实测数据

`python bench.py --seq 512 1024 2048 4096`（RTX，B=1 H=8 D=64，块 128×128）：

```
     T      朴素 ms      分块 ms        朴素峰值        分块峰值       最大误差
   512        1.3        5.2     29.4 MB     16.4 MB    6.6e-07
  1024        1.6       23.3     84.1 MB     23.4 MB    1.1e-06
  2048        6.2       60.0    290.1 MB     36.4 MB    6.0e-07
  4096       21.9      261.2   1100.1 MB     62.4 MB    6.0e-07
```

三个可以直接读出来的结论：

**1. 显存曲线的形状完全不同。** T 从 512 涨到 4096（8 倍），朴素峰值涨了 37 倍
（接近 T² 的 64 倍，差在 q/k/v 本身是线性的），分块只涨了不到 4 倍。分块那一列
剩下的增长全部来自 q/k/v/out 张量本身——分数矩阵那部分**恒定为
`block_q × block_k`，与 T 无关**。这就是 128K 上下文能跑起来的全部原因。

**2. 纯 PyTorch 分块版更慢，而且慢得越来越多。** 这不是 bug。Python 层的
循环开销远大于省下的显存带宽。FlashAttention 论文的加速来自 kernel 融合：
分块常驻 SRAM，避免 HBM 往返。用 Python 写循环等于把这个优势原地放弃，
只保留显存收益。想要速度就用 `F.scaled_dot_product_attention`——它内部
就是这个算法的 CUDA 实现（`test_matches_torch_sdpa` 验证了两者等价）。

**3. 误差在 1e-6 量级，是浮点累加顺序不同导致的，不是实现错误。**
`test_block_size_does_not_change_result` 用 5 组块大小（含不整除的 7/13）
钉死了这一点：块大小是性能旋钮，不该影响数值。

## 最容易踩的坑：整块 -inf 产生 nan

因果掩码下，某个 Q 块可能完全排在某个 K 块之前，那一块的分数**整行都是 -inf**。
此时：

```python
m = -inf                    # 行最大值也是 -inf
exp(m - m) = exp(-inf + inf) = exp(nan) = nan   # 一个 nan 污染整个输出
```

`attention.py` 里两道防线：`_safe_softmax_max()` 在整行 -inf 时返回 0 而不是
-inf；以及两处 `torch.nan_to_num(..., nan=0.0)` 兜住首块（`m` 初值为 -inf）
和全掩码块。`test_no_nan_when_query_block_precedes_key_block` 专门盯着这条路径。

顺带一提，因果时内层循环只扫到 `k_limit = q_end` 就停——后面的 K 块整块会被
掩掉，算了也是 -inf。这一行直接省掉约一半计算量。

## 十项自检在验什么

| 测试 | 抓的是什么 |
| --- | --- |
| `test_matches_naive_causal` / `_non_causal` | 数值等价，两种掩码模式各一遍 |
| `test_block_size_does_not_change_result` | 块大小不影响结果，含不整除尺寸 7/13 |
| `test_no_nan_when_query_block_precedes_key_block` | 整块 -inf 路径 |
| `test_first_row_attends_only_to_itself` | 因果第 0 行输出必须精确等于 `v[0]` |
| `test_matches_torch_sdpa` | 与官方 FlashAttention 实现对齐 |
| `test_gradients_match_naive` | 反向也对——缩放因子写错会在梯度上暴露 |
| `test_memory_claim_is_real` | 把「省显存」写成可断言的数值关系 |
| `test_softmax_is_numerically_stable_on_large_scores` | 分数放大 50 倍仍不溢出 |
| `test_scale_matches_one_over_sqrt_d` | 用单位向量构造可手算的期望值 |

其中 `test_scale_matches_one_over_sqrt_d` 值得单独说：缩放因子写成 `1/D` 或
漏掉，输出看起来依然"正常"，loss 也能降，只是收敛更慢——从结果上根本发现不了。
这条测试把 q/k 设成单位向量，让期望输出可以手算成 `exp(1/√D)/(exp(1/√D)+1)`，
缩放因子一错这个值必偏。

## 想继续深入

| 方向 | 怎么做 |
| --- | --- |
| 看真正的加速 | 用 Triton 重写内层循环（需要 GPU + `pip install triton`），对比 `bench.py` 的耗时列 |
| 理解反向为什么也能省显存 | 反向需要 P 矩阵，FlashAttention 的做法是重算而非存储——用 `l` 和 `m` 就能恢复 |
| 连到推理章节 | KV cache 场景下 Q 只有一行，这个循环退化成单次扫描，是 decode 阶段的形态 |

原论文：[FlashAttention](https://arxiv.org/abs/2205.14135) ·
[FlashAttention-2](https://arxiv.org/abs/2307.08691)（改了循环顺序和工作划分）
