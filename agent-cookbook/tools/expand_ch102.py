# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch102.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# Expand with comprehensive deep academic sections:
# 1. CAMEL Mathematical Formulation of Role-Playing Communication Loops & Inception Prompting Mechanics
# 2. MetaGPT Publish-Subscribe Architecture & Memory Pruning Dynamics
# 3. ChatDev Thought-Orientation vs. Action-Orientation Dialogue Analysis
# 4. Multi-Agent Game Theory, Consensus Mechanisms and Byzantine Fault Tolerance in Agent Societies

expansion_1 = """
    <h2 id="camel-deep-dive">深度解构 1：CAMEL 非对称角色启导与会话终结判定数学模型</h2>
    <p>在《CAMEL》论文中，李国豪（Guohao Li）等人系统性研究了自驱动协同对话中的<strong>动态收敛性难题</strong>。如果缺乏严密的数学状态转移定义，两个智能体在自发交流时，其话题漂移概率会随轮次呈指数级发散。</p>
    
    <p>作者将整个交互过程形式化为如下严密的双智能体博弈状态机：</p>
    <p>设初始粗糙任务为 $T_0$。经过任务细化者（Task Specifier）映射后，得到精细化规范 $T = \mathcal{S}(T_0)$。系统初始化两个相互绑定的提示词：<br>
    - AI 用户代理提示词 $P_u = \mathcal{I}_u(T, R_u, R_a)$，其中 $R_u$ 为用户角色（如“对冲基金投资总监”），$R_a$ 为助手角色（如“资深量化交易算法架构师”）；<br>
    - AI 助手代理提示词 $P_a = \mathcal{I}_a(T, R_a, R_u)$。</p>
    
    <p>在离散时间步 $t = 1, 2, ..., K$，消息流严格按照交替因果链递推：</p>

    <p>$$m_{a, t} \sim \pi_a(\cdot \mid P_a, m_{u, 1}, m_{a, 1}, ..., m_{u, t}) \quad (\text{助手执行输出})$$</p>
    <p>$$m_{u, t+1} \sim \pi_u(\cdot \mid P_u, m_{u, 1}, m_{a, 1}, ..., m_{a, t}) \quad (\text{用户审查并下发新子任务})$$</p>

    <div class="tbl-wrap">
      <table>
        <thead><tr><th>启导提示核心准则 (Rule)</th><th>对 AI 用户代理 (User) 的硬约束</th><th>对 AI 助手代理 (Assistant) 的硬约束</th></tr></thead>
        <tbody>
          <tr><td><strong>禁止非实质性客套</strong></td><td>绝不出现「谢谢你」、「你真棒」等闲聊无用词汇</td><td>绝不输出「随时乐意效劳」、「如果需要请随时叫我」</td></tr>
          <tr><td><strong>指令必须单一具象</strong></td><td>每轮仅允许给出一个极其具体的微观操作指令</td><td>必须直接给出该指令的代码实现或精准答复</td></tr>
          <tr><td><strong>终结判定契约</strong></td><td>仅当全量任务完全解决时，输出 <code>&lt;CAMEL_TASK_DONE&gt;</code> 终结</td><td>当感知到自身工作已达标时，在文末建议终止</td></tr>
        </tbody>
      </table>
      <caption>表 102-3 · CAMEL 启导提示词（Inception Prompting）核心戒律表。从通信协议底层消除多智能体社交瘫痪。</caption>
    </div>
"""

expansion_2 = """
    <h2 id="metagpt-deep-dive">深度解构 2：MetaGPT 消息反应池与观察者模式（Observer Pattern）</h2>
    <p>在 MetaGPT 论文中，洪述圣（Shusheng Hong）等人攻克的最关键工程壁垒是<strong>「去中心化协同中的信息广播风暴与上下文爆炸」</strong>。在拥有 5 个角色的团队中，如果每个人都无脑监听所有人说的每一句话（全互联拓扑），通信复杂度将高达 $O(N^2)$，每个智能体的上下文会在几轮内被挤爆。</p>

    <p>MetaGPT 在底层设计了基于经典设计模式的<strong>「发布-订阅环境消息池（Publish-Subscribe Message Pool）」</strong>：</p>

    <div class="codeblock">
      <div class="cb-head"><span>MetaGPT 角色基类与观察者消息过滤核心实现（Python）</span><button class="cb-copy">复制</button></div>
      <pre><code>from typing import Set, List, Dict

class MetaGPTRole:
    def __init__(self, name: str, profile: str, watch_actions: Set[str]):
        self.name = name
        self.profile = profile
        self.watched_actions = watch_actions  # 仅订阅自己感兴趣的动作产物
        self.memory = []

    def observe(self, message_pool: List[Dict]) -> List[Dict]:
        \"\"\"观察者过滤: 仅将自己订阅的前置依赖文档摄入当前工作记忆\"\"\"
        new_events = []
        for msg in message_pool:
            # 过滤逻辑: 动作类型匹配且不是自己发出的消息
            if msg["cause_by"] in self.watched_actions and msg["sender"] != self.name:
                new_events.append(msg)
                self.memory.append(msg)
        return new_events

    def act(self, input_documents: List[Dict]) -> Dict:
        \"\"\"执行 SOP 规定的标准化职责并输出结构化文档\"\"\"
        raise NotImplementedError

# 架构师角色订阅设定示例:
# 架构师 Architect 仅需监听 ProductManager 发出的 "WritePRD" 动作
architect = MetaGPTRole(
    name="Bob", 
    profile="Architect", 
    watch_actions={"WritePRD"}
)</code></pre>
    </div>

    <p>通过让角色仅订阅（<code>watch</code>）与其紧密相关的上游动作（例如架构师仅监听产品经理的 <code>WritePRD</code>，工程师仅监听架构师的 <code>WriteDesign</code>），通信网络被精妙剪枝为<strong>线性的依赖 DAG 拓扑</strong>，彻底消灭了无关噪音信息对大模型推理注意力的干扰。</p>
"""

expansion_3 = """
    <h2 id="chatdev-deep-dive">深度解构 3：ChatDev 聊天链的思维导向与动作导向协同</h2>
    <p>清华大学钱晨（Chen Qian）等人在分析 ChatDev 的交互轨迹时，发现多智能体对话存在两种完全不同的功能属性：<strong>思维导向型交互（Thought-Orientation）</strong>与<strong>动作导向型交互（Action-Orientation）</strong>：</p>

    <div class="tbl-wrap">
      <table>
        <thead><tr><th>交互对话类型</th><th>核心交锋目标</th><th>典型角色配对</th><th>在 ChatDev 中的真实案例</th></tr></thead>
        <tbody>
          <tr><td><strong>思维导向型 (Thought-Oriented)</strong></td><td>对技术选型、设计模式与架构权衡进行辩论</td><td>CEO 与 CPO / CTO 与 程序员</td><td>「我们该用 Pygame 还是 Arcade？Pygame 兼容性好但依赖复杂，讨论最优方案」</td></tr>
          <tr><td><strong>动作导向型 (Action-Oriented)</strong></td><td>具体的代码编写、静态语法检查与单测执行</td><td>程序员与代码审查员 (Reviewer)</td><td>「第 42 行缺少类导入 <code>from PIL import Image</code>，已精准注入补丁修正」</td></tr>
        </tbody>
      </table>
      <caption>表 102-4 · ChatDev 聊天链中思维导向与动作导向对话双轨分类。区分战略规划与战术微观执行。</caption>
    </div>

    <p>更令人惊叹的是，ChatDev 引入了<strong>角色假想幻觉消歧机制（Role Disambiguation）</strong>：当检测到程序员输出的代码缺少关键辅助函数时，审查员 Agent 会强制发起“追问中断（Interruption）”，不允许对话盲目流转至测试阶段，直到程序员补齐所有缺失的方法声明。这种<strong>将质量门禁（Quality Gate）严格内嵌在细粒度聊天链内部的设计</strong>，是 ChatDev 能够以惊人的 86.66% 一次性成功率交付软件的决定性秘密！</p>
"""

expansion_4 = """
    <h2 id="mas-consensus-byzantine">多智能体社会的博弈论与拜占庭容错机制</h2>
    <p>当多智能体系统的规模从数十个扩大到成百上千个时，智能体之间的关系不再是简单温顺的团队合作，而是进入了复杂的社会学与博弈论领域。正如我们在第 91 章中所深入推导的，部分智能体可能会因为网络延迟、模型幻觉、乃至被恶意攻击者植入提示词注入（Prompt Injection，第 59 章），而表现为<strong>恶意背叛节点（Byzantine Fault Agents）</strong>！</p>

    <div class="tbl-wrap">
      <table>
        <thead><tr><th>分布式多 Agent 风险</th><th>表现形式与破坏机理</th><th>经典计算机科学理论对应</th><th>现代 Agent 架构防御机制</th></tr></thead>
        <tbody>
          <tr><td><strong>拜占庭将军问题 (Byzantine Fault)</strong></td><td>某个子 Agent 受到注入攻击，持续向整个群组发送虚假的虚假结论</td><td>Lamport 拜占庭容错理论 ($N \ge 3f + 1$)</td><td><strong>多智能体加权投票共识 (Consensus Voting)</strong>，消除单一节点投毒</td></tr>
          <tr><td><strong>公地悲剧 (Tragedy of the Commons)</strong></td><td>多个 Agent 并发无节制争抢 GPU 算力与外部 API 速率上限</td><td>博弈论纳什均衡公地悲剧</td><td>引入虚拟代币经济学与分布式租约限流器 (第80章)</td></tr>
          <tr><td><strong>群体极化与回音室 (Echo Chamber)</strong></td><td>多个 Agent 在对话中不断互相强化彼此的错误假设</td><td>社会学回音室效应与群体极化理论</td><td>强制在集群中注入具有“对抗性反思立场”的固定批判者角色 (Devil's Advocate)</td></tr>
        </tbody>
      </table>
      <caption>表 102-5 · 大规模多智能体社会的博弈论挑战与分布式容错机制。筑牢群体智慧演进的系统韧性。</caption>
    </div>

    <p>在设计工业级多智能体集群时，架构团队必须在底层部署<strong>「魔鬼代言人机制（Devil's Advocate Role）」</strong>：在任何重大决策委员会中，强制设立一个专门负责吹毛求疵、寻找当前主流方案致命缺陷的独立 Agent。这种源自天主教封圣审查制度与现代分布式共识机制的深邃设计，能够将系统陷入群体盲从与幻觉共谋的概率压缩至理论极低水平。</p>
"""

insert_target = '<div class="callout note">'
if insert_target in text:
    new_text = text.replace(insert_target, expansion_1 + "\n" + expansion_2 + "\n" + expansion_3 + "\n" + expansion_4 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Successfully expanded ch102.html with 4 deep sections")
else:
    print("Target not found")
