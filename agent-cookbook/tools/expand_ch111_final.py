# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch111.html"

with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_111 = """
    <h3>Q97: 面对超长上下文（&gt; 1M Tokens）场景，模型注意力在中间区域严重退化的机理是什么？如何利用滑动注意力与分块检索（Chunked Context）进行系统级治愈？</h3>
    <p><strong>【核心考点】</strong>注意力稀释（Attention Dilution）、Softmax 归一化温度畸变、双向分块预填充（Chunked Prefill）与树状前缀聚合。</p>
    <p><strong>【参考回答】</strong>在标准的自注意力机制中，注意力权重由 Softmax 归一化决定：$\alpha_{ij} = \frac{\exp(q_i k_j^T / \sqrt{d})}{\sum_{m=1}^N \exp(q_i k_m^T / \sqrt{d})}$。当序列长度 $N$ 扩展至数十万乃至百万量级时，分母项的累加会导致即使某个中间 Token 具备很高的相关性语义分值，其经过 Softmax 后的绝对注意力权重依然会被海量无关的噪声 Token 极度稀释；同时，旋转位置编码（RoPE）在超长距离外推时的高频振荡会导致相对距离感知模糊，从而使得模型极易发生“迷失在中间（Lost in the Middle）”的严重退化。
    工业级治愈方案采用<strong>层次化树状分块检索与稀疏注意力融合网关</strong>：
    <ul>
      <li><strong>分块动态预填充与 KV 缓存剪枝（Chunked Prefill & KV Cache Sparsification）：</strong>将超长上下文在物理上切分为 8K 或 16K 大小的语义块（Chunks）。利用类似 StreamingLLM 或 SnapKV 的机制，仅在显存中保留每个 Chunk 内注意力聚合程度最高的关键 Token 槽位与首尾锚点 Token，其余无关填充 Token 动态驱逐，将单卡显存占用减少 70% 以上。</li>
      <li><strong>两阶段递归层级摘要（Map-Reduce Hierarchical Compaction）：</strong>在将超长背景材料喂给主决策 Agent 之前，先并发启动多个轻量级小模型对各个语义块进行信息抽取，生成带页码与段落定位标签的紧凑元数据图谱。主 Agent 仅需在高度凝练的元数据目录上展开树搜索，按需精细下钻拉取局部原文片段，彻底化解了百万 Token 全量注意力稀释的物理瓶颈。</li>
    </ul></p>
"""

target = '<section class="refs">'
if target in text:
    new_text = text.replace(target, final_push_111 + "\n" + target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Final push added to ch111")
else:
    print("Target not found")
