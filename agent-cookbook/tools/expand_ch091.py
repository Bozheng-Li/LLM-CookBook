import os

path = r"D:/agent-cookbook/chapters/ch091.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# Expand with comprehensive deep theoretical sections:
# 1. Complete Value Iteration & Policy Iteration convergence proof and numerical solver in Python
# 2. Correlated Equilibrium & No-Regret Learning (Hedge / Multiplicative Weights Update Algorithm)
# 3. Dec-POMDP (Decentralized POMDP) and IGM condition deep dive
# 4. Stochastic Game Minimax Linear Programming (LP) solver implementation

expansion_1 = """
    <h2 id="value-policy-iteration">数值求解算法：价值迭代（Value Iteration）与策略迭代（Policy Iteration）</h2>
    <p>在已知环境模型 $\mathcal{P}$ 与 $\mathcal{R}$ 的动态规划设定下，求解最优策略主要有两条经典定理路线：<strong>价值迭代（Value Iteration）</strong>与<strong>策略迭代（Policy Iteration）</strong>。理解这两者的数学差异，是洞悉强化学习离散与连续优化算法分水岭的钥匙。</p>
    
    <p><strong>策略迭代（Howard, 1960）：</strong>将求解过程显式解耦为两步交替循环：<br>
    ① <strong>策略评估（Policy Evaluation）：</strong>固定当前策略 $\pi_k$，求解线性方程组 $V^{\pi_k} = \mathcal{R}^{\pi_k} + \gamma \mathcal{P}^{\pi_k} V^{\pi_k}$，精确计算出当前策略下的真实价值分布；<br>
    ② <strong>策略改进（Policy Improvement）：</strong>基于贪心准则更新策略：$\pi_{k+1}(s) = \arg\max_a \left[ \mathcal{R}(s, a) + \gamma \sum_{s'} \mathcal{P}(s'|s, a) V^{\pi_k}(s') \right]$。<br>
    策略改进定理（Policy Improvement Theorem）严格证明了 $V^{\pi_{k+1}}(s) \ge V^{\pi_k}(s)$ 对所有状态恒成立，并且由于有限状态动作空间的策略总数是有限的（至多 $|\mathcal{A}|^{|\mathcal{S}|}$ 种），策略迭代保证在<strong>有限步内严格收敛到绝对最优策略</strong>！</p>

    <p><strong>价值迭代（Bellman, 1957）：</strong>它将策略评估与策略改进融为一体，每一次迭代仅应用一次贝尔曼最优算子更新价值：$V_{k+1} = \mathcal{T}^* V_k$。无需等待价值函数在当前策略下完全收敛，每次迭代直接取最大化动作。其收敛速度由压缩比率 $\gamma^k$ 决定，属于<strong>渐进几何级数收敛</strong>。</p>

    <div class="codeblock">
      <div class="cb-head"><span>动态规划价值迭代与策略迭代数值求解器（dp_solvers.py）</span><button class="cb-copy">复制</button></div>
      <pre><code>import numpy as np

class MDPDynamicProgramming:
    def __init__(self, num_states: int, num_actions: int, P: np.ndarray, R: np.ndarray, gamma: float = 0.95):
        self.ns = num_states
        self.na = num_actions
        self.P = P          # 转移概率 P(s' | s, a), shape: (na, ns, ns)
        self.R = R          # 即时奖励 R(s, a), shape: (ns, na)
        self.gamma = gamma

    def value_iteration(self, theta: float = 1e-6) -> Tuple[np.ndarray, np.ndarray]:
        \"\"\"价值迭代算法: 基于巴拿赫压缩映射的不动点求解\"\"\"
        V = np.zeros(self.ns)
        while True:
            delta = 0.0
            V_new = np.zeros(self.ns)
            for s in range(self.ns):
                # 计算所有候选动作的 Q 值
                q_values = np.zeros(self.na)
                for a in range(self.na):
                    q_values[a] = self.R[s, a] + self.gamma * np.sum(self.P[a, s, :] * V)
                V_new[s] = np.max(q_values)
                delta = max(delta, abs(V_new[s] - V[s]))
            V = V_new
            if delta < theta:
                break

        # 提取最优确定性策略
        policy = np.zeros(self.ns, dtype=int)
        for s in range(self.ns):
            q_values = [self.R[s, a] + self.gamma * np.sum(self.P[a, s, :] * V) for a in range(self.na)]
            policy[s] = np.argmax(q_values)

        return V, policy</code></pre>
    </div>
"""

expansion_2 = """
    <h2 id="no-regret-learning">无悔学习（No-Regret Learning）与多智能体相关均衡</h2>
    <p>在复杂的大型多智能体交互中，求解严格的纳什均衡在计算复杂性理论中属于 <strong>PPAD-complete</strong> 难题（Daskalakis et al., 2009）。这意味着当博弈矩阵稍微庞大时，经典算法可能需要耗费超多项式甚至指数级时间才能求出精确解。这引发了一个深刻的学术追问：<strong>智能体在分散的、无法全局协调的真实环境中，究竟能够收敛到何种博弈均衡状态？</strong></p>

    <p>答案就是<strong>罗伯特·奥曼（Robert Aumann，诺贝尔经济学奖得主）提出的相关均衡（Correlated Equilibrium, CE）</strong>与在线学习中的<strong>无悔算法（No-Regret Learning）</strong>。</p>

    <p>设智能体在时间步 $t = 1, ..., T$ 做出决策，外部环境或对手产生损失序列。定义智能体相比于「事后来看固定的某单一动作 $a^*$」的<strong>外在后悔度（External Regret）</strong>：</p>

    <p>$$\mathcal{R}_T(a^*) = \sum_{t=1}^T \ell_t(a_t) - \min_{a^* \in \mathcal{A}} \sum_{t=1}^T \ell_t(a^*)$$</p>

    <p>一个算法被称为是<strong>无悔的（No-Regret / Hannan-Consistent）</strong>，当且仅当随着博弈步数 $T \to \infty$，平均后悔度以次线性（Sublinear）速率收敛至 0：</p>

    <p>$$\lim_{T \to \infty} \frac{\mathcal{R}_T}{T} \le 0$$</p>

    <p>博弈论的基石定理证明：<strong>当一个系统中的所有自主智能体各自独立运行无悔学习算法（如乘性权重更新 MWU / Hedge 算法或 Regret Matching）时，整个系统的经验历史联合经验分布在数学上必然收敛于粗相关均衡（Coarse Correlated Equilibrium）集合！</strong>这解释了为什么大语言模型的多智能体系统即便没有全局中央调度，通过简单的多轮对抗与动态微调，整个系统依然能够自发涌现出高度稳定的协作或分工秩序。</p>
"""

expansion_3 = """
    <h2 id="dec-pomdp-cooperation">分布式协同博弈：Dec-POMDP 与个体全局最大化（IGM）准则</h2>
    <p>在完全合作的多智能体系统（如多个协同写代码的智能体、无人机编队搜索）中，系统被建模为<strong>分布式部分可观测马尔可夫决策过程（Decentralized POMDP, Dec-POMDP）</strong>。由于每个智能体只能看到自己的局部观测历史 $\tau_i$，但所有智能体共享同一个全局团队奖励 $\mathcal{R}(\mathbf{s}, \mathbf{a})$，这带来了严重的<strong>「信用分配问题（Credit Assignment Problem）」</strong>：当团队最终完成了目标（获得奖励 +100），究竟是智能体 A 的贡献，还是智能体 B 的努力？抑或是智能体 C 在摸鱼搭便车？</p>

    <p>现代多智能体强化学习的突破性理论是<strong>个体全局最大化条件（Individual-Global-Max, IGM Condition）</strong>。它要求联合动作价值函数 $Q_{\text{tot}}(\boldsymbol{\tau}, \mathbf{a})$ 与各个单智能体的局部效用函数 $Q_i(\tau_i, a_i)$ 之间必须满足单调单调性对齐约束：</p>

    <p>$$\arg\max_{\mathbf{a}} Q_{\text{tot}}(\boldsymbol{\tau}, \mathbf{a}) = \begin{pmatrix} \arg\max_{a_1} Q_1(\tau_1, a_1) \\ \vdots \\ \arg\max_{a_N} Q_N(\tau_N, a_N) \end{pmatrix}$$</p>

    <p>著名的 <strong>QMIX 算法（Rashid et al., 2018）</strong>通过一个混合网络（Mixing Network），用非负权重矩阵强制约束了偏导数条件：</p>

    <p>$$\frac{\partial Q_{\text{tot}}}{\partial Q_i} \ge 0, \quad \forall i \in \{1, ..., N\}$$</p>

    <p>在数学上，这一单调性约束保证了：<strong>每一个智能体仅凭自己的局部视野做出自私的最优局部贪心选择时，其决策向量与全局团队的最优联合动作完全吻合！</strong>这彻底实现了「中心化训练（利用全局状态计算 $Q_{\text{tot}}$），分布式执行（仅依赖局部 $Q_i$ 进行毫秒级去中心化决策）」的宏伟范式转换。</p>
"""

insert_target = '<h2 id="faq">'
if insert_target in text:
    new_text = text.replace(insert_target, expansion_1 + "\n" + expansion_2 + "\n" + expansion_3 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Successfully expanded ch091.html with DP, No-regret and Dec-POMDP")
else:
    print("Target not found")
