import os

path = r"D:/agent-cookbook/chapters/ch092.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# Expand with comprehensive deep sections:
# 1. State-Space Representation & Kalman Filtering (Continuous State Estimation for Embodied Agents)
# 2. Synergetics & Order Parameters (Hermann Haken's Slaving Principle in Multi-Agent Swarms)
# 3. Step-by-Step Chaos Theory & Sensitivity to Initial Conditions in Long-horizon LLM Agent Loops

expansion_1 = """
    <h2 id="kalman-state-space">状态空间理论与卡尔曼滤波：连续具身感知的最优估计</h2>
    <p>在第七部分（具身智能）与第九部分（项目 9 具身桌面操控）中，智能体面对的物理传感器与视觉输入往往充斥着高斯测量噪声（Measurement Noise）。单纯依赖单帧截屏瞬时数值，系统很容易因为一两帧画面模糊或光影突变而产生剧烈的控制超调。</p>
    
    <p>现代控制论的另一大基石是<strong>状态空间表征（State-Space Representation）</strong>与鲁道夫·卡尔曼（Rudolf E. Kálmán）在 1960 年提出的<strong>卡尔曼滤波方程（Kalman Filter）</strong>。系统将智能体与外部世界的动态交互建模为一阶线性随机微分/差分方程：</p>

    <p>$$\mathbf{x}_{k} = \mathbf{A} \mathbf{x}_{k-1} + \mathbf{B} \mathbf{u}_{k} + \mathbf{w}_{k} \quad (\text{系统物理状态演进})$$</p>
    <p>$$\mathbf{z}_{k} = \mathbf{H} \mathbf{x}_{k} + \mathbf{v}_{k} \quad (\text{传感器多模态观测观测值})$$</p>

    <p>其中 $\mathbf{w}_k \sim \mathcal{N}(0, \mathbf{Q})$ 为环境过程噪声，$\mathbf{v}_k \sim \mathcal{N}(0, \mathbf{R})$ 为传感器测量噪声。卡尔曼滤波通过精妙的两步交替递归——<strong>「时间更新（Time Update: 预测先验 $\hat{\mathbf{x}}_k^-$）」</strong>与<strong>「测量更新（Measurement Update: 利用卡尔曼增益 $\mathbf{K}_k$ 校正后验 $\hat{\mathbf{x}}_k$）」</strong>，在最小均方误差（MMSE）意义下实现了对真实隐藏物理状态的数学最优无偏估计：</p>

    <p>$$\mathbf{K}_k = \mathbf{P}_k^- \mathbf{H}^T (\mathbf{H} \mathbf{P}_k^- \mathbf{H}^T + \mathbf{R})^{-1}$$</p>
    <p>$$\hat{\mathbf{x}}_k = \hat{\mathbf{x}}_k^- + \mathbf{K}_k (\mathbf{z}_k - \mathbf{H} \hat{\mathbf{x}}_k^-)$$</p>

    <div class="codeblock">
      <div class="cb-head"><span>连续视觉具身卡尔曼滤波状态融合器（kalman_filter.py）</span><button class="cb-copy">复制</button></div>
      <pre><code>import numpy as np

class EmbodiedKalmanTracker:
    def __init__(self, dt: float = 0.05):
        # 状态向量: [x, y, vx, vy]^T (位置与速度)
        self.x = np.zeros((4, 1))
        # 状态转移矩阵 A
        self.A = np.array([
            [1, 0, dt, 0],
            [0, 1, 0, dt],
            [0, 0, 1,  0],
            [0, 0, 0,  1]
        ])
        # 观测矩阵 H (传感器仅能测量位置 [x, y])
        self.H = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0]
        ])
        # 协方差矩阵 P, Q, R
        self.P = np.eye(4) * 1.0
        self.Q = np.eye(4) * 0.01  # 过程噪声
        self.R = np.eye(2) * 0.5   # 视觉截屏定位测量噪声 (像素抖动)

    def filter_step(self, measured_pos: Tuple[float, float]) -> Tuple[float, float]:
        \"\"\"输入带噪声的 VLM 坐标读数，输出最优物理平滑坐标\"\"\"
        z = np.array([[measured_pos[0]], [measured_pos[1]]])

        # 1. 预测步 (Predict)
        x_pred = self.A @ self.x
        P_pred = self.A @ self.P @ self.A.T + self.Q

        # 2. 更新步 (Update)
        S = self.H @ P_pred @ self.H.T + self.R
        K = P_pred @ self.H.T @ np.linalg.inv(S) # 计算卡尔曼最优增益

        # 创新残差校正
        y = z - self.H @ x_pred
        self.x = x_pred + K @ y
        self.P = (np.eye(4) - K @ self.H) @ P_pred

        return float(self.x[0, 0]), float(self.x[1, 0])</code></pre>
    </div>
"""

expansion_2 = """
    <h2 id="synergetics-haken">协同学与序参数：哈肯役使原理在多智能体系统中的涌现</h2>
    <p>当一个复杂系统由成百上千个微观智能体构成时（例如庞大的智能体金融交易市场、蜂群协作搜救系统），整个系统宏观层面的秩序究竟是如何自发涌现的？德国物理学家赫尔曼·哈肯（Hermann Haken）在 20 世纪 70 年代创立了<strong>协同学（Synergetics）</strong>，提出了极具洞察力的<strong>役使原理（Slaving Principle）</strong>。</p>

    <p>在临界相变点附近，一个复杂动态系统内部存在着两类具有截然不同物理时间尺度的变量：<br>
    - <strong>快弛豫变量（Fast-decaying Stable Modes）：</strong>衰减速度极快，阻尼巨大，生命周期短暂；<br>
    - <strong>慢演化变量（Slow-decaying Unstable Modes / Order Parameters）：</strong>衰减极慢，主导着系统全局宏观结构的长期演进，被定义为<strong>「序参数（Order Parameter）」</strong>。</p>

    <p>哈肯的役使原理在数学上证明：<strong>慢演化的少数几个序参数，在宏观层面上完全支配（Slave，役使）了成千上万个微观快变量的集体行为；反过来，全体微观变量的相互协作又共同维持着序参数的稳定存在！</strong></p>

    <div class="tbl-wrap">
      <table>
        <thead><tr><th>协同学核心概念</th><th>物理世界典型案例</th><th>在多 Agent 群体系统中的对应表征</th><th>系统调控核心支点</th></tr></thead>
        <tbody>
          <tr><td><strong>微观快变量 (Fast Modes)</strong></td><td>激光介质中单个原子的离散相位跃迁</td><td>单个 Agent 的单步 Prompt 输出、单次 HTTP 工具请求、临时记忆 Token</td><td>通过局部规则设计允许高频自主随机微调</td></tr>
          <tr><td><strong>宏观序参数 (Order Parameters)</strong></td><td>激光腔内发生相位锁定的宏观单色相干光场</td><td>多 Agent 群体共识协议、分工拓扑结构、共享全局黑板变量状态</td><td>架构师仅需调控序参数，即可驭领全群体</td></tr>
          <tr><td><strong>役使机制 (Slaving)</strong></td><td>激光光场强迫所有原子步调一致协同受激辐射</td><td>顶层规划大纲强制约束各个执行 Agent 协同向总目标收敛</td><td>消除微观混乱内耗，形成群体超智能涌现</td></tr>
        </tbody>
      </table>
      <caption>表 92-2 · 协同学哈肯役使原理与多智能体系统映射表。揭示微观局部自由与宏观协同秩序的辩证统一。</caption>
    </div>

    <p>这一理论直接启发了多智能体编排的高级架构设计（如第 33 章多 Agent 拓扑模式与第 83 章 Deep Research）：架构团队绝不需要事无巨细地为每个子 Agent 编写详尽微观指令，只需精巧设计代表系统“宏观序参数”的<strong>全局状态黑板与激励规则</strong>，微观智能体便会在协同相变中自发被序参数所“役使”，涌现出高度条理化的跨学科复杂分工合作。</p>
"""

expansion_3 = """
    <h2 id="chaos-butterfly-effect">混沌理论与蝴蝶效应：长程长时程 Agent 的发散性悲剧</h2>
    <p>气象学家爱德华·洛伦兹（Edward Lorenz）在 1963 年研究大气对流微分方程时，发现了著名的混沌吸引子与「蝴蝶效应」：一个非线性确定性动力学系统，即使其演化规则完全确定且不含任何外部随机性，只要其最大李雅普诺夫指数（Lyapunov Exponent）为正（$\lambda_{\max} > 0$），两个初始状态之间极其微小的微米级差异 $\delta x_0$，都会随时间步 $t$ 呈指数级爆炸式发散：</p>

    <p>$$\|\delta x(t)\| \approx \|\delta x_0\| \cdot e^{\lambda_{\max} t}$$</p>

    <p>在基于自回归大语言模型的长程长时程 Agent（Long-Horizon Agent）中，这一混沌发散性悲剧每天都在真实发生：</p>
    <p><strong>第一步微偏：</strong>在第 1 步决策时，大模型在两个近乎等价的词汇之间进行采样（例如选择了「或许我们应该首先扫描子目录」而非「直接读取根目录」）；<br>
    <strong>误差累积放大：</strong>到了第 5 步，由于前文 Prompt 包含了该偏好，大模型开始围绕子目录展开长篇大论；<br>
    <strong>彻底失控发散：</strong>到了第 20 步，初始的微小概率抖动经过连续 20 次自回归非线性 Transformer 层的自激迭代，智能体已经完全忘记了用户最初的核心任务，在与主目标毫无关联的偏僻边缘分支上疯狂打转！</p>

    <p>控制系统论给出的根治处方是<strong>「引入李雅普诺夫渐近稳定吸引子（Lyapunov Asymptotic Stability Attractor）」</strong>：在长程任务调度器中，必须硬编码周期性状态重投影算子（State Reprojection Operator）。每推进 5 步，强制由一个冻结不变的高位监督器将当前的状态向量重新投影回初始的目标流形（Target Manifold）上，强制将发散项指数衰减因子压制为负值（$\lambda_{\text{effective}} < 0$），从动力学底层扼杀混沌发散的萌芽。</p>
"""

insert_target = '<h2 id="faq">'
if insert_target in text:
    new_text = text.replace(insert_target, expansion_1 + "\n" + expansion_2 + "\n" + expansion_3 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Successfully expanded ch092.html with Kalman, Synergetics and Chaos theory")
else:
    print("Target not found")
