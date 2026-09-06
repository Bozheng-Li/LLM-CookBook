# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch099.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

expansion_more = """
    <h2 id="cross-paper-comparative-synthesis">四大奠基之作的横向交织与当代生产级架构映射</h2>
    <p>将这四篇改变历史走向的经典论文放在同一个全景坐标系中审视，我们会惊讶地发现：一个现代顶尖的商用智能体系统（如 Claude 3.5 驱动的 Computer Use、OpenAI 的 Operator 或开源的 SWE-agent），在底层实际上正是这四种思想的<strong>高度集大成者</strong>：</p>

    <div class="tbl-wrap">
      <table>
        <thead><tr><th>生产级 Agent 核心模块</th><th>继承的经典论文核心遗产</th><th>在现代工业级系统中的落地形态</th><th>消除的核心工程隐患</th></tr></thead>
        <tbody>
          <tr><td><strong>多模态执行中枢</strong></td><td>Transformer (Vaswani 2017)</td><td>视觉 Token 与文本 Token 在统一多头注意力中全并行交互</td><td>消除异构多模态信号的信息割裂，支持端到端长上下文寻址</td></tr>
          <tr><td><strong>工具调度与环境闭环</strong></td><td>ReAct (Yao 2022)</td><td>结构化 Function Calling 契约协议与 Observation 严格拦截</td><td>消除盲目试错调用，确保每一步工具执行均在思考指导下推进</td></tr>
          <tr><td><strong>报错自愈与测试自驱动</strong></td><td>Reflexion (Shinn 2023)</td><td>利用 Pytest 单元测试断言失败堆栈，在上下文中生成因果修正建议</td><td>避免在同一语法或逻辑错误上反复打转死锁，实现无需微调的在线自愈</td></tr>
          <tr><td><strong>跨会话长期记忆中枢</strong></td><td>Generative Agents (Park 2023)</td><td>时间新鲜度、重要性打分与向量相关性三维加权动态记忆流</td><td>彻底打破单次会话长度限制，实现用户偏好与长期工程知识的终身固化</td></tr>
        </tbody>
      </table>
      <caption>表 99-4 · 四大奠基论文在当代生产级智能体中的综合映射表。从原子机制熔铸为工业级可信系统。</caption>
    </div>

    <p>没有 Transformer 的全并行注意力计算，智能体就失去了处理高维复杂上下文的大脑；没有 ReAct 的动静协同，智能体就会沦为只能闭目空想的幻觉机器；没有 Reflexion 的自省自愈，智能体就会在第一处代码报错前彻底瘫痪；而没有 Generative Agents 的长记忆与社交拟真，智能体就永远无法迈入跨越时间尺度的多主体协同社会。这四篇论文不仅是学者们书架上的珍贵典藏，更是每一位志在打造世界级智能体系统的工程师心中永恒燃烧的理论灯塔！</p>
"""

insert_target = '<div class="callout note">'
if insert_target in text:
    new_text = text.replace(insert_target, expansion_more + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added cross-paper comparative synthesis section")
else:
    print("Target not found")
