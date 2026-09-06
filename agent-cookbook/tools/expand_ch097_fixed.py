# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch097.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

expansion_1 = """
    <h2 id="synaptic-intelligence-math">突触智能（Synaptic Intelligence）：参数轨迹路径积分的在线重要性度量</h2>
    <p>虽然弹性权重整合（EWC）在理论上极为优美，但它存在一个致命的计算痛点：每当完成一个新任务时，必须在全量训练集上重新跑一遍完整的前向反向传播，以计算高昂的费希尔信息矩阵（FIM）。在面对数据流连续涌入的流式场景（Online Continual Learning）中，这种批量回算的方式在工程上是无法承受的。</p>
    
    <p>弗里德曼·岑克（Friedemann Zenke）等人在 2017 年提出了<strong>突触智能算法（Synaptic Intelligence, SI）</strong>。SI 巧妙地将参数重要性的评估无缝融入到了正常的训练梯度优化过程中，利用<strong>参数空间中的路径积分（Path Integral）</strong>在线度量每个参数对损失下降的实际贡献：</p>

    <p>设在任务训练过程中，参数随优化器从初始点 $\\theta(0)$ 演化至最优解 $\\theta(T)$。参数 $\\theta_i$ 在整个训练轨迹中对总任务损失下降的累计物理贡献标量 $\\omega_i$ 可严格表示为线积分：</p>

    <p>$$\\omega_i(t) = \\int_{\\theta_i(0)}^{\\theta_i(T)} \\frac{\\partial \\mathcal{L}}{\\partial \\theta_i} d\\theta_i \\approx \\sum_{k=1}^K g_{i, k} \\cdot \\Delta \\theta_{i, k}$$</p>

    <p>其中 $g_{i, k} = \\frac{\\partial \\mathcal{L}_k}{\\partial \\theta_i}$ 为第 $k$ 步的即时梯度，$\\Delta \\theta_{i, k} = \\theta_{i, k} - \\theta_{i, k-1}$ 为该步的参数位移。最终分配给参数 $\\theta_i$ 的突触重要性权重 $\\Omega_i$ 为：</p>

    <p>$$\\Omega_i = \\sum_{\\tau < \\text{current}} \\frac{\\omega_i^\\tau}{(\\Delta_i^\\tau)^2 + \\xi}$$</p>

    <p>其中 $\\Delta_i^\\tau = \\theta_i^\\tau(T) - \\theta_i^\\tau(0)$ 为整个任务中参数的总位移，$\\xi$ 为防除零阻尼项。与 EWC 相比，<strong>突触智能（SI）完全不需要额外的多余计算 Pass</strong>：优化器每推进一步，系统在内存中顺便将梯度与位移相乘累加，以极小的常数级计算开销实现了对神经突触重要性的毫秒级精准追踪！</p>
"""

expansion_2 = """
    <h2 id="dark-experience-replay">暗经验回放（Dark Experience Replay, DER++）：软逻辑与暗知识的连续保鲜</h2>
    <p>在传统的经验回放（Experience Replay）中，算法仅仅将旧任务的输入样本与硬真实标签（Hard Labels）缓存在 Buffer 中。然而，马泰奥·布扎加（Matteo Buzzega）等人在 NeurIPS 2020 上指出了一个惊人的理论真相：<strong>网络在过去任务上产生的未归一化输出 Logits 向量，蕴含着比单一类别标签多数百倍的几何暗知识（Dark Knowledge）！</strong></p>

    <p>如果仅仅用硬标签强行微调，模型的决策边界依然会在未观察的边缘流形上剧烈扭曲。<strong>DER++ 算法</strong>通过在回放缓冲区中同时保留样本在当时的原始 Logits 快照 $\\mathbf{z}$，在训练新任务的同时，施加双重蒸馏约束：</p>

    <p>$$\\mathcal{L}_{\\text{DER++}}(\\theta) = \\mathcal{L}_{\\text{New}}(\\mathbf{x}_{\\text{new}}, \\mathbf{y}_{\\text{new}}) + \\alpha \\cdot \\|\\mathbf{z}_{\\text{past}} - h_\\theta(\\mathbf{x}_{\\text{buf}})\\|_2^2 + \\beta \\cdot \\mathcal{L}_{\\text{CE}}(h_\\theta(\\mathbf{x}_{\\text{buf}}), \\mathbf{y}_{\\text{buf}})$$</p>

    <div class="codeblock">
      <div class="cb-head"><span>暗经验回放 (DER++) 连续流损失计算核心（der_replay.py）</span><button class="cb-copy">复制</button></div>
      <pre><code>import torch
import torch.nn as nn
import torch.nn.functional as F

class DarkExperienceReplayLoss(nn.Module):
    def __init__(self, alpha: float = 0.5, beta: float = 0.5):
        super().__init__()
        self.alpha = alpha  # 暗知识 Logits MSE 约束强度
        self.beta = beta    # 真实标签交叉熵约束强度

    def forward(self, model_outputs_new: torch.Tensor, targets_new: torch.Tensor,
                buffer_samples: torch.Tensor, buffer_logits: torch.Tensor, 
                buffer_labels: torch.Tensor, model: nn.Module) -> torch.Tensor:
        # 1. 当前批次新任务损失
        loss_new = F.cross_entropy(model_outputs_new, targets_new)

        # 2. 对缓冲区旧样本进行前向推理
        outputs_buf = model(buffer_samples)

        # 3. 欧氏距离约束: 强制模型在旧样本上的 Logits 输出分布与当年完全一致 (暗知识保鲜)
        loss_dark = F.mse_loss(outputs_buf, buffer_logits)

        # 4. 硬标签分类损失
        loss_label = F.cross_entropy(outputs_buf, buffer_labels)

        total_loss = loss_new + self.alpha * loss_dark + self.beta * loss_label
        return total_loss</code></pre>
    </div>

    <p>通过保留未激活类别的微弱相对概率，模型在学习新任务时，其高维分类超平面（Hyperplanes）被多维度弹性网格牢牢固定，彻底阻止了参数在正交空空间中的无规律自由漂移，成为当前学术界在流式持续学习基准上最强悍的黄金 SOTA 之一。</p>
"""

expansion_3 = """
    <h2 id="task-arithmetic-merging">任务算术与模型合并（Task Arithmetic & Model Merging）：大模型时代的无痛缝合</h2>
    <p>在大语言模型（LLM）参数量突破 700 亿的时代，任何在数万亿 Token 上重新跑持续学习训练的想法在经济上都是自杀式的。加布里埃尔·伊尔哈（Gabriel Ilharco）等人在 2023 年提出的<strong>任务算术（Task Arithmetic）</strong>，开创了一套令人叹为观止的代数模型操作流派：</p>
    
    <p>设基础预训练模型权重为 $\\Theta_{\\text{Base}}$。若模型在编程任务 A 上微调得到 $\\Theta_A$，在数学任务 B 上微调得到 $\\Theta_B$。我们可以提取各自的<strong>任务增量向量（Task Vectors）</strong>：</p>

    <p>$$\\tau_A = \\Theta_A - \\Theta_{\\text{Base}}, \\quad \\tau_B = \\Theta_B - \\Theta_{\\text{Base}}$$</p>

    <p>惊人的是，在参数空间内，这些任务向量直接满足线性的代数相加与正交组合性质！我们可以直接像做加减法一样，将两个独立的专业技能缝合进一个单一模型中，而<strong>完全不需要进行任何重新训练或接触原始训练数据</strong>：</p>

    <p>$$\\Theta_{\\text{Merged}} = \\Theta_{\\text{Base}} + \\lambda_A \\cdot \\tau_A + \\lambda_B \\cdot \\tau_B$$</p>

    <div class="tbl-wrap">
      <table>
        <thead><tr><th>模型合并算法</th><th>底层代数操作</th><th>解决的核心参数冲突</th><th>终身学习适应性</th></tr></thead>
        <tbody>
          <tr><td><strong>线性平均加权 (Linear Merging)</strong></td><td>权重直接代数线性平均叠加</td><td>简单暴力，若两任务在同一参数上更新方向相反，产生破坏性干涉（Destructive Interference）</td><td>仅适用于差异极小的同源微调模型</td></tr>
          <tr><td><strong>Ties-Merging (Yadav et al., 2023)</strong></td><td>修剪极小冗余梯度（Trim）+ 符号投票一致性消除（Elect Sign）+ 均值融合（Merge）</td><td>彻底消除跨任务向量符号相反导致的抵消相消问题，保留高信度主导参数</td><td>跨领域长程多任务融合的首选生产级方案</td></tr>
          <tr><td><strong>DARE (Yu et al., 2024)</strong></td><td>随机将 90%~99% 的微调参数丢弃（Drop），并通过动态缩放剩余参数保持期望恒定</td><td>参数极度稀疏化，不同任务向量在几何空间中几乎天然正交，互不干扰</td><td>支持将上百个独立专业 LoRA 插件无损拼合进单一巨型主干</td></tr>
        </tbody>
      </table>
      <caption>表 97-4 · 大模型时代主流模型合并（Model Merging）技术方案对比表。开启了零数据、纯参数空间终身知识缝合的新纪元。</caption>
    </div>
"""

insert_target = '<h2 id="faq">'
if insert_target in text:
    new_text = text.replace(insert_target, expansion_1 + "\n" + expansion_2 + "\n" + expansion_3 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Successfully expanded ch097.html")
else:
    print("Target not found")
