# 手写 miniGPT

对应正文：[第 15 章 · 从零实现 miniGPT](../../pages/15-practice/build-minigpt.html)

只依赖 PyTorch。自带 40 KB 语料，**首次运行不需要网络**。

## 跑起来

```bash
cd examples/build-minigpt
pip install -r requirements.txt

python test_model.py               # 11 项结构自检，约 5 秒
python train.py                    # 300 步，CPU 约 2 分钟 / GPU 约 6 秒
python train.py --steps 500 --download   # 用完整 1.1MB 语料，效果明显更好
```

实测输出（RTX，500 步，40 KB 自带语料）：

```
设备 cuda · 语料 corpus.txt（39907 字符）· 词表 256
参数量 836,736（非 embedding 803,968）

  step    train      val        lr  ms/step
     0   5.5435   5.5455  1.00e-05    427.5
   100   2.6940   2.7440  2.84e-04     21.7
   300   1.8786   2.0731  1.15e-04     18.9
   499   1.7412   1.9794  3.35e-09     18.4

随机基线 loss = ln(256) = 5.5452
```

生成结果已经有对白结构和类词形态：

```
That First: alf; Thus Citay, the ha's with to the poscess and thaalge, kno,
rether sherefore, be my bed is in you march: bells: gode, breage ae rest
```

## 代码地图

| 文件 | 行数 | 作用 |
| --- | --- | --- |
| `model.py` | ~200 | RMSNorm、RoPE、因果注意力、SwiGLU、Block、生成 |
| `data.py` | ~80 | 字节级数据集与批采样 |
| `train.py` | ~150 | warmup+余弦退火、梯度裁剪、分组 weight decay |
| `test_model.py` | ~180 | 11 项结构自检 |

结构上是现代配置（Pre-LN + RMSNorm + RoPE + SwiGLU + 权重绑定），
不是 GPT-2 原版。每个选择在 `model.py` 的注释里都写了理由。

## 四个可以自己动手验证的现象

**1. 初始 loss 必须等于 ln(vocab_size)。** 训练第 0 步打印 5.5435，
而 ln(256) = 5.5452。差距在 0.002 以内说明随机初始化确实给出了近似均匀
分布。这是最便宜也最有效的初始化检查——偏高说明 logits 尺度失控，
偏低往往意味着标签泄漏。

**2. 权重绑定会制造一种真实的标签泄漏。** `test_weight_tying_creates_measurable_leak`
把这件事固定成了测试。如果让每个位置预测它自己（`model(idx, idx)`），
vocab=64 时 loss 会从基线 4.16 掉到 3.54——因为 `head.weight` 与
`tok_emb.weight` 是同一个张量，残差路径上输入 embedding 的分量直接和输出
投影点积回自身。写自定义评测循环时这个坑很容易踩到，而且 loss 变低不会
触发任何告警。

**3. 因果掩码写反了模型照样收敛。** `test_attention_is_causal` 的做法是改动
最后一个 token，然后断言前面所有位置的输出**逐位不变**。掩码方向错误时
loss 曲线甚至更漂亮（模型能看到答案），只有这条测试能抓住。

**4. 40 KB 语料一定会过拟合。** 500 步后 train 1.74 / val 1.98，差距在持续
拉大。加 `--download` 换成 1.1 MB 语料再跑，会看到两条曲线贴得更紧。
这比任何关于正则化的文字说明都直观。

## 常见改动

| 想验证什么 | 怎么改 |
| --- | --- |
| RoPE 到底有没有用 | 在 `CausalSelfAttention.forward` 里注释掉 `apply_rope` 那行 |
| Pre-LN vs Post-LN | 把 `Block.forward` 改成 `x = self.norm1(x + self.attn(x, ...))`，然后把 `n_layer` 提到 12 看是否还能训 |
| SwiGLU vs 普通 MLP | 把 `SwiGLU` 换成 `Linear-GELU-Linear`，隐藏维用 `4 * n_embd` 保持参数量可比 |
| 换成 BPE 词表 | 用 `examples/build-tokenizer` 训一个 tokenizer，`data.py` 里把字节 id 换成 `tok.encode(text)` |

## 与生产实现的距离

本例刻意省略了：KV cache（推理章节单独讲）、混合精度、梯度累积、
分布式、checkpoint 恢复、dropout。补齐这些之后基本就是
[nanoGPT](https://github.com/karpathy/nanoGPT) 的形态，可以直接对照阅读。
