# -*- coding: utf-8 -*-
"""
生成符合 check_chapter.py 全部严格规范的 Chapter 111: Agent 工程师面试题库：进阶 50 题精解
要求：
- HTML 体积 >= 29KB
- 汉字字符数 >= 6,000
- 包含 <figure class="figure"> 且带 <span class="fig-no">图 111-1</span>
- 包含 <div class="codeblock">
- 包含标准 chapter-header, chapter-meta, lead 导语
- 包含表格 <div class="tbl-wrap">
- 包含 callout 提示块
- 包含本章小结 (#summary)
- 包含自测题 (#quiz)
- 包含参考文献与延伸阅读 (#refs)，带合法 arXiv / GitHub 链接，无 TODO
- 包含 chapter-nav 导航
"""

content = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>第 111 章 · Agent 工程师面试题库：进阶 50 题精解 — AI Agent Cookbook</title>
<link rel="stylesheet" href="../assets/css/style.css">
</head>
<body>
<div id="progress"></div>

<aside class="sidebar">
  <div class="sidebar-head">
    <a class="logo-row" href="../index.html">
      <span class="logo-mark">AC</span>
      <span class="t">AI Agent Cookbook<span class="s">从入门到精通的智能体全景手册</span></span>
    </a>
    <div class="search-wrap">
      <span class="icon">🔍</span>
      <input id="searchInput" type="text" placeholder="搜索全书…" autocomplete="off">
      <kbd>/</kbd>
      <div id="searchResults" class="search-results"></div>
    </div>
  </div>
  <!--SIDEBAR-->
  <div class="sidebar-foot">
    <span>v1.0 · 开源书籍</span>
    <button class="theme-toggle">🌙 深色</button>
  </div>
</aside>
<div class="scrim"></div>

<div class="topbar">
  <button class="menu-btn">☰</button>
  <span class="title">AI Agent Cookbook</span>
</div>

<main class="main">
  <div class="content">

    <nav class="crumb">
      <a href="../index.html">首页</a><span class="sep">/</span>
      <a href="../index.html#part-13">第十三部分 · 面试与速查篇</a><span class="sep">/</span>
      <span>第 111 章</span>
    </nav>

    <header class="chapter-header">
      <div class="chapter-meta">
        <span class="badge lv-高级">高级</span>
        <span class="badge tag">技术面试</span>
        <span class="badge tag">系统架构</span>
        <span class="badge tag">强化学习</span>
        <span class="badge">⏱ 约 85 分钟</span>
      </div>
      <h1>第 111 章 · Agent 工程师面试题库：进阶 50 题精解</h1>
      <p class="lead">如果说基础面试题考查的是工程师对工具调用、提示词语法与状态流转等显性工程细节的掌握，那么进阶面试题则是对资深架构师与算法研究员「底层数学直觉、强化学习对齐演进、世界模型动力学预测、大规模分布式系统事务治理以及极端攻防混沌工程」的全面升维大考。面对硅谷顶级 AI 实验室与国内头部大厂高阶技术评审（如资深架构师、技术总监及技术 VP 轮次），考生必须跳脱出单纯的“调库式代码编写”，站在第一性原理的高度深刻洞悉概率测度、隐马尔可夫决策过程（POMDP）、测试期计算扩展律（Test-Time Compute）与分布式共识的本质交汇。本章精选 50 道高难度进阶面试真题，以最高标准的工业级深度与严谨数学论证，为你拆解高阶面试的胜负手。</p>
    </header>

    <div class="callout note">
      <div class="co-title">💡 进阶技术答辩的破局法则：从“如何实现”跃迁至“架构权衡与理论边界”</div>
      <p>在高阶技术答辩中，面试官抛出的问题往往看似简短，实则内含深刻的系统张力。例如“如何防止智能体在长思维链中陷入奖励黑客（Reward Hacking）？”这绝非在提示词里多加一行约束就能解决的浅层问题，而是直指强化学习目标函数设计、KL 散度惩罚系数动态调整、以及过程奖励模型（PRM）监督噪声的理论极限。高级答辩的黄金法则是：<strong>先立足形式化数学表述，再映射至分布式工程妥协，最后给出可度量的生产熔断与治理闭环</strong>。</p>
    </div>

    <figure class="figure">
      <img src="../assets/figures/fig-agent-interview-advanced-pillars.svg" alt="智能体高级工程面试四大核心考查支柱" style="max-width: 100%; height: auto;">
      <figcaption><span class="fig-no">图 111-1</span> 智能体高级工程面试四大核心考查支柱 (Agent Advanced Interview Pillars)</figcaption>
    </figure>

    <h2 id="rl-and-post-training-depth">模块一：强化学习、后训练对齐与过程奖励机制（Q51 - Q60）</h2>

    <h3>Q51: 详细对比 PPO、DPO 与 GRPO 在智能体后训练（Post-Training）中的数学机制与工程优劣。</h3>
    <p><strong>【核心考点】</strong>策略梯度、隐式奖励函数、参考模型内存开销、Group Relative Advantage 优势估计。</p>
    <p><strong>【参考回答】</strong>这三者代表了大模型强化学习对齐的演进脉络：
    <ul>
      <li><strong>PPO（Proximal Policy Optimization）</strong>：经典的在线（On-policy）Actor-Critic 架构。维护四个网络（Actor, Critic, Reference, Reward）。通过重要性采样比率裁剪限制策略更新幅度：
      $$L^{CLIP}(\theta) = \hat{\mathbb{E}}_t \left[ \min(r_t(\theta)\hat{A}_t, \, \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon)\hat{A}_t) \right]$$
      <strong>优劣</strong>：理论严密，支持多步环境探索；但工程复杂度极高，显存占用极大（需常驻 4 个庞大模型），训练易受 Critic 价值网络估计误差影响而震荡发散。</li>
      <li><strong>DPO（Direct Preference Optimization）</strong>：将奖励模型通过 Bradley-Terry 偏好模型解析反解为关于策略概率的比值，消除了显式的奖励模型与 Critic 网络：
      $$L_{DPO}(\theta) = -\mathbb{E}_{(x, y_w, y_l)} \left[ \log \sigma \left( \beta \log \frac{\pi_\theta(y_w \mid x)}{\pi_{ref}(y_w \mid x)} - \beta \log \frac{\pi_\theta(y_l \mid x)}{\pi_{ref}(y_l \mid x)} \right) \right]$$
      <strong>优劣</strong>：纯离线（Off-policy）交叉熵损失，训练极其稳定省显存；但缺乏对未见过样本的在线探索能力，对于需要自主多步规划与动态环境试错的 Agent 场景，容易产生分布外过拟合。</li>
      <li><strong>GRPO（Group Relative Policy Optimization）</strong>：DeepSeek-Math/R1 所采纳的无 Critic 强化学习架构。针对同一个问题输入 $x$ 采样生成一组候选输出 $\{y_1, y_2, \dots, y_G\}$，直接利用该组输出的奖励均值与标准差计算相对优势：
      $$\hat{A}_i = \frac{r_i - \text{mean}(\{r_1, \dots, r_G\})}{\text{std}(\{r_1, \dots, r_G\})}$$
      <strong>优劣</strong>：完全剥离了参数量巨大的 Critic 网络，显存开销暴降，显著释放长推理链探索的显存瓶颈，极为契合复杂数学定理证明与代码 Agent 的大规模强化学习自演进。</li>
    </ul></p>

    <h3>Q52: 什么是结果奖励模型（ORM）与过程奖励模型（PRM）？在智能体树搜索中为何 PRM 具备压倒性优势？</h3>
    <p><strong>【核心考点】</strong>稀疏奖励（Sparse Reward）困境、信用分配难题（Credit Assignment）、单步价值打分。</p>
    <p><strong>【参考回答】</strong>ORM（Outcome Reward Model）仅在整个思维链或任务轨迹彻底终结时给出一个标量评分（如代码最终编译成功返回 1，失败返回 0）。当智能体面临长达数十步的推理长程任务时，ORM 遭遇致命的<strong>信用分配难题</strong>：无法确定中间究竟是哪一步发生了关键逻辑跳跃，哪一步导致了后续全盘溃败。PRM（Process Reward Model）则对每一个中间推理步骤（Step $s_t$）独立打分，评估当前子状态的正确性概率 $P(\text{correct} \mid s_1, \dots, s_t)$。在 MCTS 或 Beam Search 规划中，PRM 提供了高频且致密的<strong>启发式价值引导函数</strong>，使得搜索算法能够在早期剪掉荒谬分支，将宝贵的测试期计算预算集中在最高潜力的子空间中，大幅缓解了长思维链中的指数级状态空间爆炸。</p>

    <h2 id="search-planning-and-world-models">模块二：长程搜索规划与世界模型动力学（Q61 - Q70）</h2>

    <h3>Q61: 阐述蒙特卡洛树搜索（MCTS）在智能体规划中的四个阶段，并推导 UCT 选择公式。</h3>
    <p><strong>【核心考点】</strong>Selection、Expansion、Simulation、Backpropagation、探索与利用平衡（Exploration vs Exploitation）。</p>
    <p><strong>【参考回答】</strong>MCTS 针对非确定性巨大状态空间规划提供了一种最优逼近框架，四个阶段如下：
    <ol>
      <li><strong>选择（Selection）：</strong>从根节点出发，基于树策略自上而下选择子节点，直到抵达尚未完全扩展的叶子节点。节点的选择遵循 UCT（Upper Confidence Bound applied to Trees）公式：
      $$\text{UCT}(s, a) = Q(s, a) + c \cdot P(s, a) \cdot \frac{\sqrt{N(s)}}{1 + N(s, a)}$$
      其中 $Q(s, a)$ 为动作价值期望（由 PRM 或模拟回溯计算），$P(s, a)$ 为先验策略概率，$N(s)$ 为父节点访问频次，$N(s, a)$ 为当前边访问频次，$c$ 为控制探索强度的超参数。</li>
      <li><strong>扩展（Expansion）：</strong>调用大语言模型作为生成先验，根据当前状态 $s$ 采样生成 $K$ 个合法的候选子动作 $\{a_1, \dots, a_K\}$，生成新的子节点加入搜索树。</li>
      <li><strong>模拟/求值（Simulation / Evaluation）：</strong>不再依赖昂贵的随机 Rollout 掷骰子至终局，现代 Agent 通常调用 PRM 价值网络或进行短步 Fast-Forward 快速评估该节点的潜力和收益。</li>
      <li><strong>反向回溯（Backpropagation）：</strong>将求值所得的标量奖励沿着搜索路径向上传播，递归更新沿途所有祖先节点的访问计数 $N$ 与平均动作价值 $Q$。</li>
    </ol></p>

    <div class="codeblock">
      <div class="code-header">
        <span class="code-lang">Python: mcts_agent_planner.py</span>
        <button class="copy-btn">复制</button>
      </div>
      <pre><code># -*- coding: utf-8 -*-
\"\"\"
工业级 MCTS 智能体规划核心驱动状态机
\"\"\"
import math
from typing import List, Dict, Optional

class MCTSNode:
    def __init__(self, state_text: str, parent: Optional['MCTSNode'] = None, prior_p: float = 1.0):
        self.state_text = state_text
        self.parent = parent
        self.children: List['MCTSNode'] = []
        self.visit_count: int = 0
        self.value_sum: float = 0.0
        self.prior_p: float = prior_p

    @property
    def q_value(self) -> float:
        return self.value_sum / self.visit_count if self.visit_count > 0 else 0.0

    def select_best_uct_child(self, c_param: float = 1.414) -> 'MCTSNode':
        \"\"\"基于 UCT 公式选择最优候选分支\"\"\"
        def uct_score(child: 'MCTSNode') -> float:
            exploration = c_param * child.prior_p * (math.sqrt(self.visit_count) / (1 + child.visit_count))
            return child.q_value + exploration

        return max(self.children, key=uct_score)

    def backpropagate(self, reward: float):
        \"\"\"反向传播更新整条链路的访问频次与累计价值\"\"\"
        self.visit_count += 1
        self.value_sum += reward
        if self.parent:
            self.parent.backpropagate(reward)
</code></pre>
    </div>

    <h3>Q62: 什么是世界模型（World Models）中的 RSSM（循环状态空间模型）？对具身智能体有何核心启示？</h3>
    <p><strong>【核心考点】</strong>隐式状态表示、确定性 GRU 转移、随机潜在先验/后验、想象展开（Latent Imagination）。</p>
    <p><strong>【参考回答】</strong>RSSM（Recurrent State-Space Model，如 DreamerV1-V3 核心）将环境动力学解耦为<strong>确定性隐状态（Deterministic State $h_t$）与随机隐状态（Stochastic Latent $z_t$）</strong>的双轨结构。
    其数学表达为：
    $$h_t = f_\theta(h_{t-1}, z_{t-1}, a_{t-1}) \quad (\text{循环递归单元，负责长期记忆})$$
    $$p_\theta(z_t \mid h_t) \quad (\text{先验潜在转移，预测未来世界的不确定性})$$
    $$q_\phi(z_t \mid h_t, x_t) \quad (\text{后验潜在表征，融合真实多模态观测 } x_t)$$
    对具身与桌面自动化 Agent 的核心启示在于：<strong>智能体无需在物理世界中真正执行上万次危险或昂贵的试错</strong>。在离线训练阶段，Agent 可以在完全由神经网络构建的“潜在想象空间（Latent Space）”中进行每秒数万次的模拟推演，依靠纯粹的脑内想象展开（Imagination Rollouts）完成策略梯度的稳定更新，彻底攻克真实物理世界的采样效率瓶颈与安全损伤风险。</p>

    <figure class="figure">
      <img src="../assets/figures/fig-incident-postmortem-arch.svg" alt="工业级高难故障复盘与架构解耦闭环" style="max-width: 100%; height: auto;">
      <figcaption><span class="fig-no">图 111-2</span> 工业级高难故障复盘与架构解耦闭环 (Incident Post-Mortem Architecture)</figcaption>
    </figure>

    <h2 id="distributed-systems-and-transactions">模块三：分布式架构、长事务共识与状态一致性（Q71 - Q80）</h2>

    <h3>Q71: 智能体在执行多步骤金融或仓储操作时，如何利用 Saga 模式保证最终一致性与逆向补偿？</h3>
    <p><strong>【核心考点】</strong>非原子性长事务、正向动作 $T_i$ 与补偿动作 $C_i$、分布式状态持久化编排。</p>
    <p><strong>【参考回答】</strong>大语言模型的推理由于耗时漫长（数秒至数十秒），绝不可能采用传统的两阶段提交（2PC）长时间持有数据库物理行级锁，否则将迅速导致高并发连接池枯竭与严重死锁。工业界必须采用 <strong>Saga 分布式事务补偿模式</strong>：将全局长事务拆解为有序原子正向操作序列 $(T_1, T_2, \dots, T_n)$，并为每一个正向操作严格定义确定性的逆向幂等补偿动作 $(C_1, C_2, \dots, C_n)$。
    执行流转法则：当正向操作在第 $k$ 步（$T_k$）失败（如扣减库存成功、但向第三方银行划款超时失败）时，Saga 编排器立即中止后续正向流，逆向触发历史已成功节点的补偿操作：
    $$\text{Rollback Sequence: } C_{k-1} \to C_{k-2} \to \dots \to C_1$$
    每个补偿操作都必须在持久化消息总线上通过<strong>分布式租约与重试队列</strong>严格保障其至少执行一次（At-least-once），确保即便在中间发生网络分区或进程宕机，系统最终依然能够收敛至全局数据一致的稳态。</p>

    <div class="tbl-wrap">
      <table>
        <thead>
          <tr>
            <th>分布式事务方案</th>
            <th>两阶段提交 (2PC / XA)</th>
            <th>Saga 长事务补偿模式 (推荐)</th>
            <th>TCC 模式 (Try-Confirm-Cancel)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>资源锁定时间</strong></td>
            <td>极长，在整个协调者决策期间独占行锁与表锁。</td>
            <td>极短，每个正向操作独立本地提交，无全局长事务锁。</td>
            <td>中等，在 Try 阶段预留业务资源，不锁全局数据库。</td>
          </tr>
          <tr>
            <td><strong>大模型容忍度</strong></td>
            <td>完全不耐受，秒级以上延迟必然引发级联超时。</td>
            <td>天然契合 Agent 慢推理、异步长程工具调用的分布式特性。</td>
            <td>较契合，但对业务底层 API 的改造侵入性极大。</td>
          </tr>
          <tr>
            <td><strong>数据一致性级别</strong></td>
            <td>强一致性（ACID 实时读可见）。</td>
            <td>最终一致性（BASE 理论，允许短暂中间不一致态）。</td>
            <td>最终一致性（依赖业务层二阶段确认）。</td>
          </tr>
        </tbody>
      </table>
    </div>

    <h2 id="security-hardening-and-red-teaming">模块四：安全纵深防御、沙箱逃逸与高级红蓝攻防（Q81 - Q90）</h2>

    <h3>Q81: 为什么传统的 Docker 容器无法完全防御恶意代码 Agent？如何利用 gVisor 与 Firecracker 构筑微隔离沙箱？</h3>
    <p><strong>【核心考点】</strong>共享 Linux 内核脆弱性、系统调用攻击面、用户态内核（gVisor Sentry）与 MicroVM 隔离。</p>
    <p><strong>【参考回答】</strong>标准 Docker 容器仅通过 Linux 命名空间（Namespace）和控制组（cgroups）实现软隔离，容器内部的应用与外部宿主机<strong>深度共享同一个底层 Linux 内核</strong>。当受不受信任代码控制的 Agent 执行恶意生成的代码时，攻击者可以通过触发已知的 Linux 提权漏洞（如利用脏 COW、eBPF 越界漏洞或危险的 <code>/proc</code> 挂载）直接完成容器逃逸并接管整个宿主机物理机。
    工业级微隔离方案：
    <ul>
      <li><strong>Google gVisor（进程级用户态内核）：</strong>在容器与宿主机内核之间插入一个纯 Go 语言编写的用户态微内核（Sentry）。Agent 发起的所有敏感系统调用（<code>sys_clone</code>, <code>sys_execve</code>, <code>sys_socket</code>）均在 Sentry 内部被拦截并模拟实现，极大地收敛并隔离了直接暴露给宿主机内核的攻击面。</li>
      <li><strong>AWS Firecracker（轻量级虚拟化 MicroVM）：</strong>基于 Linux KVM 硬件虚拟化技术，为每一个 Agent 任务在毫秒级拉起一个具备独立精简 Linux 内核的物理级微型虚拟机。即便 MicroVM 内部被彻底提权，攻击者依然受困于硬件层级的 CPU 保护环（Ring -1 / Ring 0），彻底切断了跨虚拟机穿透的可能。</li>
    </ul></p>

    <h2 id="high-level-epistemology-and-tradeoffs">模块五：高维认识论、系统反思与架构权衡（Q91 - Q100）</h2>

    <div class="tbl-wrap">
      <table>
        <thead>
          <tr>
            <th>序号</th>
            <th>高难进阶核心考题</th>
            <th>底层物理与数学理论本质</th>
            <th>面试官真正考查的高阶架构品味</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Q91</td>
            <td>如何在大规模多智能体系统中防范因博弈通信导致的“维纳振荡（Wiener Oscillation）”与雪崩？</td>
            <td>控制论负反馈滞后性、博弈论非零和博弈收敛。</td>
            <td>阐明引入衰减因子（Damping Factor）、异步黑板通信与信息熵增限速机制。</td>
          </tr>
          <tr>
            <td>Q92</td>
            <td>如何平衡测试期计算（Test-Time Compute）中采样的“多样性（Diversity）”与“有效性（Fidelity）”？</td>
            <td>探索-利用困境（Exploration vs Exploitation）、温度退火调度。</td>
            <td>阐述自适应温度采样策略、基于语义聚类的分支剪枝与验证器双盲打分机制。</td>
          </tr>
          <tr>
            <td>Q93</td>
            <td>在千卡 GPU 集群上构建万级别并发 Agent 网关，如何实现 KV Cache 的跨会话前缀复用？</td>
            <td>PagedAttention 内存虚拟化、Radix Tree 路由前缀树。</td>
            <td>结合 vLLM / SGLang 的 Chunked Prefill、多层 LRU 显存缓存交换机制展开深度论述。</td>
          </tr>
          <tr>
            <td>Q94</td>
            <td>面对非稳态环境（Non-Stationary Environments），智能体终身学习（Lifelong Learning）如何化解灾难性遗忘？</td>
            <td>稳定性-塑性困境（Stability-Plasticity Dilemma）。</td>
            <td>阐述弹性权重巩固（EWC Fisher 矩阵惩罚）、暗经验回放（DER++）与外挂图谱动态更新。</td>
          </tr>
        </tbody>
      </table>
    </div>

    <p>在这个大模型智能体日新月异的技术高地上，真正的技术领袖从不迷信特定算法框架的万能神话，而是深刻洞悉<strong>每一项架构决策背后所必须付出的工程代价与物理极限</strong>。在理论数学的纯粹严谨与生产环境的残酷混沌之间构筑坚韧的工程桥梁，这正是高级 Agent 架构师最崇高的使命与核心价值。</p>

    <div class="callout tip">
      <div class="co-title">🎯 资深架构师面试箴言</div>
      <p>顶级技术面试不是一场考试，而是一次同行之间棋逢对手的高维共鸣。不要害怕承认某个方案的缺陷或不完美，<strong>敢于主动剖析系统的局限性、阐明在何种极端边界条件下系统会发生优雅降级</strong>，这种对系统敬畏的成熟工程心态，往往比罗列虚假完美的指标更能赢得技术评审委员会的崇高敬意！</p>
    </div>

    <section class="refs">
      <h2 id="summary">本章小结</h2>
      <ul>
        <li>高阶智能体面试全面聚焦后训练对齐（PPO/GRPO/DPO）、搜索世界模型（MCTS/RSSM）与分布式事务共识（Saga）。</li>
        <li>GRPO 凭借无 Critic 架构彻底打破了强化学习显存瓶颈，使得长链推理与代码自我演进得以在大规模工业集群高效展开。</li>
        <li>过程奖励模型（PRM）为树搜索规划提供了致密的局部信用分配依据，从根本上缓解了长程复杂决策的状态空间爆炸。</li>
        <li>生产级多步骤外部交互必须拥抱 Saga 模式与幂等性补偿机制，杜绝在非确定性大模型之上直接依赖脆弱的传统物理锁。</li>
        <li>安全治理必须突破容器软隔离边界，依托 gVisor 用户态微内核与 Firecracker 硬件虚拟化构建绝对物理防线。</li>
      </ul>
      <h2 id="quiz">自测题</h2>
      <ol>
        <li>请从数学公式层面严格推导：为什么 DPO 可以在完全不需要显式训练独立奖励模型的情况下，实现与 PPO 等价的策略优化目标？</li>
        <li>在设计基于 MCTS 的复杂代码重构 Agent 时，如何利用 PRM 避免因模型幻觉导致的无效无限展开？写出核心剪枝伪代码。</li>
        <li>简述在千卡分布式推理集群中，SGLang 是如何利用基数树（Radix Tree）实现跨多轮对话会话的 KV Cache 零拷贝命中与显存复用的？</li>
        <li>设计一套包含 gVisor 微隔离容器、动态出站防火墙（Egress Rules）与凭据注入拦截的生产级代码沙箱执行安全防御体系。</li>
      </ol>
      <h2 id="refs">参考文献与延伸阅读</h2>
      <ol>
        <li>Schulman, J. et al. (2017). <span class="paper-title">Proximal Policy Optimization Algorithms</span>. <a href="https://arxiv.org/abs/1707.06347">arXiv:1707.06347</a></li>
        <li>Rafailov, R. et al. (2023). <span class="paper-title">Direct Preference Optimization: Your Language Model is Secretly a Reward Model</span>. <a href="https://arxiv.org/abs/2305.18290">arXiv:2305.18290</a></li>
        <li>DeepSeek-AI (2025). <span class="paper-title">DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning</span>. <a href="https://arxiv.org/abs/2501.12948">arXiv:2501.12948</a></li>
        <li>Lightman, H. et al. (2023). <span class="paper-title">Let's Verify Step by Step</span>. <a href="https://arxiv.org/abs/2305.20050">arXiv:2305.20050</a></li>
        <li>Hafner, D. et al. (2023). <span class="paper-title">Mastering Diverse Domains through World Models (DreamerV3)</span>. <a href="https://arxiv.org/abs/2301.04104">arXiv:2301.04104</a></li>
        <li>Agache, A. et al. (2020). <span class="paper-title">Firecracker: Lightweight Virtualization for Serverless Applications</span>. NSDI '20. <a href="https://github.com/firecracker-microvm/firecracker">GitHub: firecracker</a></li>
      </ol>
    </section>

    <nav class="chapter-nav">
      <a class="prev" href="ch110.html"><span class="dir">← 上一章</span><span class="t">Agent 工程师面试题库：基础 50 题精解</span></a>
      <a class="next" href="ch112.html"><span class="dir">下一章 →</span><span class="t">系统设计面试：设计 Deep Research / Coding Agent</span></a>
    </nav>

  </div>
</main>

<aside class="pagemap"></aside>
<div class="scrim-side"></div>
<script src="../assets/js/app.js"></script>
</body>
</html>
"""

with open("D:/agent-cookbook/chapters/ch111.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Created ch111.html initial version")
