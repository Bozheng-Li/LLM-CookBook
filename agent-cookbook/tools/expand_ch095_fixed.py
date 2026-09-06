# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch095.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

expansion_1 = """
    <h2 id="symlog-twohot-math">DreamerV3 数值稳定性革命：Symlog 仿射缩放与双热编码（Two-Hot Encoding）</h2>
    <p>在强化学习历史上，算法超参数往往极其脆弱：在一个任务（如 Atari 乒乓球）上调好的学习率和损失权重，换到另一个任务（如机械臂 3D 抓取）上就会瞬间发生数值梯度爆炸（Gradient Explosion）或消失。这是因为不同物理环境的奖励与观察值在尺度上存在<strong>高达数个数量级的巨大鸿沟</strong>（有些任务的即时奖励是 0.01，而有些任务的分数高达 500,000）。</p>
    
    <p>DreamerV3 之所以能够用<strong>完全固定的一套超参数统治跨域数十个基准</strong>，其核心数学秘密就在于两项开创性的数值稳定性技术：<strong>对称对数变换（Symlog Transformation）</strong>与<strong>连续目标离散双热表示（Two-Hot Categorical Representation）</strong>。</p>

    <h3 id="symlog-formulation">对称对数变换（Symlog）数学公式</h3>
    <p>传统的 $\\log(x)$ 变换无法处理负数且在 $x \\to 0$ 时发生无穷大发散。Symlog 创造性地通过符号函数（Sign）对称保留了正负区间的对称动态压缩特性：</p>

    <p>$$\\text{symlog}(x) = \\text{sign}(x) \\cdot \\ln(|x| + 1)$$</p>
    <p>其完全可逆的逆变换公式（Symexp）为：</p>
    <p>$$\\text{symexp}(y) = \\text{sign}(y) \\cdot \\left( \\exp(|y|) - 1 \\right)$$</p>

    <p>通过在神经网络的输入端与输出端前置包裹 Symlog 算子，跨度从 $10^{-4}$ 到 $10^6$ 的极端物理动态范围，被近乎完美地非线性压缩至 $[-15, 15]$ 的平缓数值区间内，彻底消除了梯度范数剧烈震荡的隐患。</p>

    <h3 id="two-hot-encoding-formulation">双热离散分类表征（Two-Hot Encoding）</h3>
    <p>传统的均方误差回归（MSE Loss）在遇到极端离群点时，会产生高达误差平方倍数的巨额梯度，瞬间冲垮神经网络。DreamerV3 彻底抛弃了标量回归，将价值函数 $V$ 与奖励预测 $r$ 离散化为 255 个等间距的 Symlog 桶（Buckets）。对于任意连续目标值 $y$，其被编码为与其相邻的两个离散桶上的凸组合（Convex Combination）：</p>

    <p>设 $y$ 落在区间 $[b_k, b_{k+1}]$ 之间，分配给两个相邻桶的概率分别为：</p>
    <p>$$p_k = \\frac{b_{k+1} - y}{b_{k+1} - b_k}, \\quad p_{k+1} = \\frac{y - b_k}{b_{k+1} - b_k}$$</p>
    <p>神经网络通过 Softmax 输出对所有桶的概率分布，并使用标准的交叉熵损失（Cross-Entropy Loss）进行训练。这使得损失函数的梯度永远被截断在 $[-1, 1]$ 之间，无论真实世界的奖励发生怎样暴力的突变，世界模型都能如同坚固的岩石一般岿然不动。</p>
"""

expansion_2 = """
    <h2 id="dreamer-policy-optimization">梦境中的演员-评论家：基于 GAE 的潜空间策略优化循环</h2>
    <p>当 RSSM 世界模型在潜空间中以超过每秒 100,000 步的惊人速度推演出长度为 $H$ 的虚拟轨迹时，策略网络（Actor $\\pi_\\psi(a \\mid s)$）与价值网络（Critic $v_\\xi(s)$）是如何在纯梦境中直接收敛的？</p>

    <p>系统采用基于广义优势估计（Generalized Advantage Estimation, GAE / $\\lambda$-return）的潜空间价值回溯：</p>

    <p>$$V_t^\\lambda = \\hat{r}_t + \\hat{\\gamma}_t \\left( (1 - \\lambda) v_\\xi(\\hat{s}_{t+1}) + \\lambda V_{t+1}^\\lambda \\right), \\quad V_H^\\lambda = v_\\xi(\\hat{s}_H)$$</p>

    <p>策略网络 Actor 的优化目标极为优雅：<strong>直接利用潜空间可微动态模型（Differentiable Dynamics）的梯度链，通过反向传播将未来长期价值的梯度一穿到底地回传给当前动作！</strong></p>

    <div class="codeblock">
      <div class="cb-head"><span>潜空间梦境轨迹生成与策略梯度更新实现（dreamer_trainer.py）</span><button class="cb-copy">复制</button></div>
      <pre><code>import torch
import torch.nn as nn
from typing import Dict

class LatentDreamerTrainer:
    def __init__(self, rssm_core, actor_net, critic_net, horizon: int = 15, gamma: float = 0.99, lambda_: float = 0.95):
        self.rssm = rssm_core
        self.actor = actor_net
        self.critic = critic_net
        self.horizon = horizon
        self.gamma = gamma
        self.lambda_ = lambda_

    def imagine_ahead(self, initial_h: torch.Tensor, initial_z: torch.Tensor) -> Dict[str, torch.Tensor]:
        h_seq = [initial_h]
        z_seq = [initial_z]
        action_seq = []

        curr_h, curr_z = initial_h, initial_z

        for step in range(self.horizon):
            state_feat = torch.cat([curr_h, curr_z], dim=-1)
            action = self.actor(state_feat)
            action_seq.append(action)

            next_h, next_z = self.rssm.imagine_step_prior(curr_h, curr_z, action)
            h_seq.append(next_h)
            z_seq.append(next_z)

            curr_h, curr_z = next_h, next_z

        return {
            "h": torch.stack(h_seq, dim=0),
            "z": torch.stack(z_seq, dim=0),
            "actions": torch.stack(action_seq, dim=0)
        }

    def compute_lambda_returns(self, rewards: torch.Tensor, values: torch.Tensor) -> torch.Tensor:
        H = rewards.shape[0]
        returns = torch.zeros_like(values)
        returns[-1] = values[-1]

        for t in reversed(range(H)):
            returns[t] = rewards[t] + self.gamma * (
                (1.0 - self.lambda_) * values[t+1] + self.lambda_ * returns[t+1]
            )
        return returns[:-1]</code></pre>
    </div>
"""

expansion_3 = """
    <h2 id="world-model-agent-frontiers">前沿演进：具身大模型中的端到端世界模拟器</h2>
    <p>随着具身机器人与通用电脑控制（Computer Use，第 89 章）的爆发，世界模型正在从过去单纯的几层小 GRU，全面升级为<strong>千亿参数规模的自回归视觉世界生成器（如 Sora, Genie, UniSim）</strong>。智能体在下发点击或操控机械臂之前，内部模拟器可以在 1 秒内生成出未来 5 秒内屏幕界面的动态渲染视频流，直接在视觉视频预测的特征空间中进行反事实风险推演。</p>

    <div class="tbl-wrap">
      <table>
        <thead><tr><th>世界模型代际</th><th>代表性系统</th><th>核心架构与基元</th><th>与动作控制的协同范式</th></tr></thead>
        <tbody>
          <tr><td><strong>第一代: 状态空间与小网络</strong></td><td>World Models (2018), DreamerV1</td><td>VAE + MDN-RNN / GRU 连续隐变量</td><td>通过重参数化梯度回传至 Actor 网络</td></tr>
          <tr><td><strong>第二代: 离散变分与鲁棒缩放</strong></td><td>DreamerV3, IRIS, DayDreamer</td><td>离散分类潜变量 + Symlog 仿射鲁棒缩放</td><td>实现从像素到连续动作的通用零超参收敛</td></tr>
          <tr><td><strong>第三代: 大规模生成式世界模拟器</strong></td><td>Sora, Genie, UniSim, GAIA-1</td><td>自回归多模态 Transformer + Diffusion 潜扩散</td><td>作为通用因果仿真引擎，为上层 Agent 提供闭环环境评估</td></tr>
        </tbody>
      </table>
      <caption>表 95-3 · 世界模型跨越三代技术周期的演进图谱。从隐空间动力学演化至具身全真物理世界模拟器。</caption>
    </div>
"""

insert_target = '<h2 id="faq">'
if insert_target in text:
    new_text = text.replace(insert_target, expansion_1 + "\n" + expansion_2 + "\n" + expansion_3 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Successfully expanded ch095.html")
else:
    print("Target not found")
