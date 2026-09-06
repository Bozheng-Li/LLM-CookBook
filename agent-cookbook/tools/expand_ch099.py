# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch099.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# Expand with comprehensive in-depth academic breakdowns:
# 1. Deep Dive into Transformer: Multi-Head Attention equations, Positional Encoding, Complexity analysis (O(N^2) vs Linear)
# 2. ReAct Formal Ablation Analysis: ALFWorld and HotpotQA experimental methodology and failure mode analysis
# 3. Reflexion Algorithm Pseudo-code & Memory Buffer Pruning Mechanics
# 4. Generative Agents Architecture: Dialogue synthesis, environmental collision resolution and topological relationship trees

expansion_1 = """
    <h2 id="transformer-deep-dive">深度解构 1：Transformer 的多头注意力数学矩阵与复杂度瓶颈</h2>
    <p>在《Attention Is All You Need》中，缩放点积注意力不仅是一个单流操作，而是被拓展为<strong>多头注意力（Multi-Head Attention, MHA）</strong>机制。多头的核心哲学在于：允许模型在不同的表示子空间（Representation Subspaces）中同时关注不同位置、不同语义层级的信息（例如某些注意力头专门追踪语法代词指代，另一些头专门捕获跨从句动宾因果）：</p>

    <p>$$\text{MultiHead}(Q, K, V) = \text{Concat}(\text{head}_1, ..., \text{head}_h) W^O$$</p>
    <p>$$\text{where } \text{head}_i = \text{Attention}(Q W_i^Q, K W_i^K, V W_i^V)$$</p>

    <p>其中投影矩阵参数为 $W_i^Q \in \mathbb{R}^{d_{\text{model}} \times d_k}$, $W_i^K \in \mathbb{R}^{d_{\text{model}} \times d_k}$, $W_i^V \in \mathbb{R}^{d_{\text{model}} \times d_v}$，以及输出汇聚矩阵 $W^O \in \mathbb{R}^{h d_v \times d_{\text{model}}}$。在标准 Transformer-Base 中，通常设定 $h=8$ 个头，每个头的特征维度 $d_k = d_v = d_{\text{model}} / h = 64$。</p>

    <div class="tbl-wrap">
      <table>
        <thead><tr><th>序列运算架构</th><th>时间复杂度 (每层)</th><th>最小顺序操作数 (并行度)</th><th>最大路径长度 (信息传递步长)</th></tr></thead>
        <tbody>
          <tr><td><strong>循环网络 (RNN / LSTM)</strong></td><td>$O(N \cdot d^2)$</td><td>$O(N)$ (必须按时序串行推进)</td><td>$O(N)$ (长程信息衰减极快)</td></tr>
          <tr><td><strong>卷积网络 (CNN / ByteNet)</strong></td><td>$O(k \cdot N \cdot d^2)$</td><td>$O(1)$ (高度并行)</td><td>$O(\log_k(N))$ (需通过膨胀卷积跨步)</td></tr>
          <tr><td><strong>自注意力 (Self-Attention)</strong></td><td>$O(N^2 \cdot d)$</td><td>$O(1)$ (完全由 GPU 矩阵乘法并行)</td><td>$O(1)$ (全序列任意两 Token 间直连)</td></tr>
        </tbody>
      </table>
      <caption>表 99-2 · 序列架构计算复杂度与路径长度对比矩阵（取自经典论文 Table 1）。确立了 Transformer 在长程表征上的绝对碾压优势。</caption>
    </div>

    <p>请特别注意其中的最大路径长度（Maximum Path Length）：在 RNN 中，第 1 个 Token 的信息要传递给第 $N$ 个 Token，必须穿透 $N$ 个中间循环层，信息丢失严重；而在 Transformer 中，由于每一个 Token 都能与全序列的所有 Token 直接计算点积，其<strong>逻辑信息传递距离恒定为 $O(1)$</strong>！正是这一卓越的拓扑特性，赋予了现代 Agent 系统瞬间从长达数万字的上下文历史中准确回溯关键前置条件的神奇能力。</p>
"""

expansion_2 = """
    <h2 id="react-ablation-analysis">深度解构 2：ReAct 消融实验方法论与 ALFWorld 具身测试</h2>
    <p>在 ReAct 论文中，姚顺宇（Shunyu Yao）等人为了证明「思考与行动交织」的必要性，在两大极具挑战性的基准——多跳知识问答（HotpotQA）与文本具身交互环境（ALFWorld）上，进行了极其详尽严格的消融对比实验：</p>

    <div class="tbl-wrap">
      <table>
        <thead><tr><th>对比范式</th><th>HotpotQA 准确率</th><th>ALFWorld 任务成功率</th><th>典型的致命翻车模式</th></tr></thead>
        <tbody>
          <tr><td><strong>仅行动 (Act-only)</strong></td><td>27.4%</td><td>45%</td><td><strong>目标迷失：</strong>在环境中机械地执行拿取、放下物品，却忘记了终极目标，陷入盲目试错</td></tr>
          <tr><td><strong>仅推理 (Reason-only / CoT)</strong></td><td>33.6%</td><td>无法完成交互</td><td><strong>事实幻觉：</strong>凭空捏造不存在的事实（如编造虚假人名与历史），无法与外部环境闭环</td></tr>
          <tr><td><strong>ReAct 协同模式 (完备版)</strong></td><td><strong>35.1% (自愈微调达 43%)</strong></td><td><strong>71% (相对提升 57%!)</strong></td><td><strong>动静相宜：</strong>思考负责规划子步骤与诊断错误，行动负责精准执行与注入真实观测</td></tr>
        </tbody>
      </table>
      <caption>表 99-3 · ReAct 经典论文消融实验成绩对照表。揭示思考与行动融合带来的非线性协同红利。</caption>
    </div>

    <p>在具身交互游戏 ALFWorld 中，智能体必须在虚拟房间中完成复杂的家庭杂务（例如「把一个热过的苹果放到冰箱里」）。仅行动（Act-only）基线模型在拿到苹果后，由于缺乏中间思考状态的动态维持，往往直接把生苹果放进了冰箱；而 ReAct 模型在动作前会显式插入一条 Thought：<code>"Thought: I need to heat the apple before placing it in the fridge. I should find a microwave first."</code>，成功引导自身先走向微波炉完成加热，再走向冰箱，展现出了清晰、具备因果链条的理性行为。</p>
"""

expansion_3 = """
    <h2 id="reflexion-algorithm-mechanics">深度解构 3：Reflexion 的反思记忆缓冲区与剪枝动力学</h2>
    <p>诺亚·欣恩（Noah Shinn）等人在设计 Reflexion 架构时，面临的最大技术挑战是：<strong>如何防止多轮自我反思（Self-Reflection）产生的批评文本挤爆大模型的有限上下文窗口？</strong></p>
    
    <p>如果系统在连续失败 5 次后，把每次反思的长篇大论全部塞入当前 Prompt，会导致注意力被过去的多次失败严重污染。Reflexion 创造性地引入了<strong>滑窗滑动淘汰与经验正交剪枝机制（Memory Buffer Sliding & Pruning）</strong>：</p>

    <p>记忆缓冲区容量被硬性限制为固定大小 $\Omega_{\text{mem}} \le 3$。系统仅保留最近 3 次在不同方向上尝试失败的教训，且强制要求每次反思的篇幅压缩在 1~3 句话以内。其伪代码与数据流控制算法如下：</p>

    <div class="codeblock">
      <div class="cb-head"><span>Reflexion 语言强化学习核心算法伪代码（Python 实现骨架）</span><button class="cb-copy">复制</button></div>
      <pre><code>class ReflexionFramework:
    def __init__(self, actor_llm, evaluator_tool, self_reflect_llm, max_trials: int = 4):
        self.actor = actor_llm
        self.evaluator = evaluator_tool
        self.reflector = self_reflect_llm
        self.max_trials = max_trials
        self.memory_buffer: List[str] = [] # 语言经验记忆池，容量最多3条

    def solve_task(self, task_description: str) -> Tuple[bool, str]:
        for trial_idx in range(self.max_trials):
            print(f"=== 开始第 {trial_idx + 1} 次尝试 ===")
            
            # 1. 组装输入: 任务描述 + 过去失败的精炼反思教训
            reflections_context = "\n".join([f"- 历史教训: {r}" for r in self.memory_buffer])
            actor_prompt = f"任务: {task_description}\n\n历史反思教训:\n{reflections_context}"
            
            # 2. 演员模型执行生成轨迹
            trajectory = self.actor.generate_solution(actor_prompt)
            
            # 3. 评估者客观判定 (如运行自动化单元测试)
            is_success, eval_logs = self.evaluator.evaluate(trajectory)
            if is_success:
                print("🎉 任务圆满解决！成功通过所有断言。")
                return True, trajectory

            # 4. 任务失败: 触发自我反思 (Self-Reflection)
            print("❌ 尝试失败，正在进行因果归因反思...")
            reflect_prompt = f\"\"\"分析本次执行失败的根本诱因:
任务目标: {task_description}
执行轨迹: {trajectory}
报错回显: {eval_logs}

请用 2 句话指出你的核心错误，并给出下一次必须采取的规避策略。\"\"\"
            new_reflection = self.reflector.generate(reflect_prompt).strip()
            
            # 5. 记忆流滑动更新: 保持最多 3 条最精炼的教训
            self.memory_buffer.append(new_reflection)
            if len(self.memory_buffer) > 3:
                self.memory_buffer.pop(0)

        print(f"在 {self.max_trials} 次尝试后仍未达成目标。")
        return False, trajectory</code></pre>
    </div>

    <p>这种纯粹在文本层运行的自进化循环，使得智能体在完全不触碰底层反向传播与浮点梯度的情况下，展现出了近乎生物级的自主演进与适应韧性，成为现代长时程自主编码智能体不可或缺的核心模块。</p>
"""

expansion_4 = """
    <h2 id="generative-agents-architecture">深度解构 4：斯坦福小镇的环境碰撞拓扑与对话自发合成</h2>
    <p>在朴俊成（Joon Sung Park）等人的经典论文中，构建 25 个具有人格的虚拟角色并不仅仅是在后台跑 25 个独立的大模型 API。为了让角色在《模拟人生》的二维世界中产生真实的物理交互（如避免两个人穿墙重叠、在咖啡馆相遇时自然打招呼），系统在底层设计了一套<strong>基于空间拓扑图的环境碰撞与感知广播引擎</strong>：</p>

    <div class="codeblock">
      <div class="cb-head"><span>斯坦福小镇树状空间层级环境模型</span><button class="cb-copy">复制</button></div>
      <pre><code>Lin Family House (住宅)
└── Common Room (客厅)
    ├── Wooden Desk (木桌)
    │   └── Laptop (笔记本电脑) [状态: 正在休眠]
    └── Coffee Table (茶几)
        └── Coffee Maker (咖啡机) [状态: 正在煮咖啡]
Hobbs Cafe (霍布斯咖啡馆)
└── Dining Area (就餐区)
    └── Round Table #1 (一号圆桌) [状态: 约翰·林正坐在椅上阅读]</code></pre>
    </div>

    <p>当一个智能体在小镇中移动时，系统每秒计算一次其视野半径内（例如 5 格像素范围内）的其他角色与物品状态。如果检测到角色 A 与角色 B 处于同一子房间内，且两人的当前动作均允许社交打断（例如不是在深度睡眠状态），系统自动触发<strong>对话自发合成流水线（Dialogue Synthesis Pipeline）</strong>：</p>
    <p><strong>第一步：检索双方的关系与近期记忆：</strong>角色 A 检索关于角色 B 的最后一次交谈记录，角色 B 检索对角色 A 的初始印象标签；<br>
    <strong>第二步：自回归交替生成台词：</strong>大模型模拟真实的自然语言对话，交替输出双方台词，并在每句话后评估「对话是否应当自然结束」；<br>
    <strong>第三步：双向记忆入库：</strong>对话结束后，完整对话的精简摘要作为两条独立的情景记忆，分别写入角色 A 与角色 B 的记忆流中，成为未来深层反思的种子。</p>
    <p>这种将严密的底层树状空间数据结构与上层认知记忆模型无缝咬合的系统工程设计，正是《Generative Agents》论文历经数年依然在学术界与工业界被奉为圭臬的根本原因。</p>
"""

insert_target = '<div class="callout note">'
if insert_target in text:
    new_text = text.replace(insert_target, expansion_1 + "\n" + expansion_2 + "\n" + expansion_3 + "\n" + expansion_4 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Successfully expanded ch099.html with 4 deep dives")
else:
    print("Target not found")
