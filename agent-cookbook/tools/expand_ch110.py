# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch109.html" # target is ch110
path = r"D:/agent-cookbook/chapters/ch110.html"

with open(path, "r", encoding="utf-8") as f:
    text = f.read()

rich_qa_addition = """
    <h3>Q13: 面对高并发大流量场景，智能体系统的流式输出（Streaming）与工具调用如何优雅兼顾？</h3>
    <p><strong>【核心考点】</strong>SSE（Server-Sent Events）长连接、Token 级增量解析、双轨缓冲区设计。</p>
    <p><strong>【参考回答】</strong>在大模型生成工具调用指令时，如果等待全部 JSON 字符串生成完毕再解析，首字延迟（TTFT）与端到端等待时间（Latency）将严重恶化用户体验。工业界解决方案采用<strong>双轨流式状态机（Dual-track Streaming Buffer）</strong>：客户端通过 SSE 接收增量 Delta Token。状态机维护内部缓冲区，实时监测是否出现 <code>tool_calls</code> 的特殊标识。若为纯文本思考，则零延迟直接流式透传给前端 UI；一旦监测到工具调用标记，流式输出立即无缝切换至静默缓冲模式，在后台持续拼接 JSON 片段并进行轻量级预解析。一旦 JSON 闭合，立刻分派本地轻量级 Worker 异步拉起外部 API，完成执行后再将控制权平滑交还给生成引擎。这种方案兼顾了极低的首字延迟与严谨的工具调用契约。</p>

    <h3>Q14: 如何防范智能体在多轮迭代中陷入“工具调用死循环”？请给出三级熔断机制。</h3>
    <p><strong>【核心考点】</strong>状态机环路检测、哈希签名去重、滑动窗口重复率计算与强制降级。</p>
    <p><strong>【参考回答】</strong>智能体死循环通常源于模型对报错信息产生理解偏差，持续以相同或微小变动的参数重复请求同一工具。三级熔断体系设计如下：① <strong>一级硬限：全局步数上限（Max Steps Hard Limit）</strong>：针对单次任务设定严格的交互步数上限（如 10 步），一旦超出立即中断并触发人工接管；② <strong>二级检测：动作指纹哈希检测（Action Fingerprint Cycle Detector）</strong>：对每次调用的 <code>(tool_name, hash(parameters))</code> 进行指纹计算并压入有界双端队列。若发现连续出现 2 次完全相同的调用，或在最近 5 步内出现特定状态闭环，系统强行向 Prompt 注入高优先级警告；③ <strong>三级软控：重复语义发散熔断</strong>：当连续 3 步的环境返回内容相似度（Cosine Similarity）超过 0.95 时，判定为无进展振荡（Oscillation），强制将系统控制权路由至通用答复或降级兜底网关。</p>

    <h2 id="advanced-troubleshooting-playbook">模块六：生产级高频踩坑现场与应急排错实战（Q45 - Q50）</h2>

    <h3>Q45: 生产环境中偶尔发生“模型丢失前置指令，擅自编造虚假参数”的事故，根因与治理方案是什么？</h3>
    <p><strong>【核心考点】</strong>长上下文“迷失在中间（Lost in the Middle）”、注意力稀释、系统提示词锚定加固。</p>
    <p><strong>【参考回答】</strong>大语言模型的自注意力矩阵在长序列下呈现典型的“首尾偏置（U-shaped Attention）”，位于上下文居中位置的信息极易被稀释和遗忘。当多轮工具调用返回的大量杂乱原始数据填充了上下文时，开头的 System Prompt 会逐渐失去对生成的控制力。<strong>系统级治理方案</strong>：① <strong>提示词双重锚定（System Prompt Sandwiching）</strong>：在上下文开头声明全局规则，并在上下文的最末尾（紧邻当前模型生成的触发点前）动态追加轻量级的<strong>即时约束强化锚点（Episodic Anchor）</strong>；② <strong>工具输出强制摘要压缩（Tool Observation Pruning）</strong>：严禁将原始数千行的数据库查询全集或网页 HTML 直接抛入上下文，必须先经由本地启发式规则或轻量级小模型清洗提取核心键值，将每个 Observation 的 Token 消耗严格控制在安全预算内。</p>

    <h3>Q46: 什么是智能体系统的状态漂移（State Drift）？如何利用有向图状态机（State Graph）予以纠偏？</h3>
    <p><strong>【核心考点】</strong>隐式状态 vs 显式状态机、Pregel 图计算、条件边校验。</p>
    <p><strong>【参考回答】</strong>如果仅依赖大模型的会话上下文隐式推断当前业务所处的流程节点（如：是处于“信息收集阶段”还是“支付确认阶段”），随着多轮交互的推进，模型极易产生认知漂移，在尚未收集齐全参数时跳步触发终态。利用 LangGraph 等<strong>显式有向状态图（Explicit State Graph）</strong>对业务进行形式化解耦：将全局状态显式固化为带强类型的 <code>AgentState</code> 结构体，所有流转依赖强约束的<strong>条件边（Conditional Edges）</strong>。大模型仅在具体的节点（Node）内负责局部计算，而“能否进入下一阶段”由确定性的 Python 代码断言（Assertion）判定。这种“模型负责单点推理、代码掌控全局拓扑”的架构，从根本上杜绝了跳步与状态失控。</p>

    <h3>Q47: 智能体在调用敏感数据库时，如何构建绝对可靠的只读安全防御墙？</h3>
    <p><strong>【核心考点】</strong>数据库账号最小权限（RBAC）、AST 抽象语法树词法分析、事务级只读回滚。</p>
    <p><strong>【参考回答】</strong>绝对不能仅依靠 Prompt 嘱咐“请只生成 SELECT 语句”。工业级防御必须构筑三道物理级防线：① <strong>网络与凭据物理只读（Physical Read-Only Replica）</strong>：Agent 连接的数据库连接池必须是只读从库（Read-Replica），且该数据库账号在 PostgreSQL / MySQL 级别被彻底剥离了所有 INSERT / UPDATE / DELETE / DROP 等写权限；② <strong>SQLGlot / AST 抽象语法树语法静态分析</strong>：在 SQL 文本发送至数据库执行前，经过本地 AST 解析引擎。递归遍历语法树的每个节点，凡包含数据修改语义或潜在注入函数的语句，直接在网关层抛出异常拦截；③ <strong>事务强制回滚（Transaction Level Rollback）</strong>：所有会话默认开启只读事务 <code>SET TRANSACTION READ ONLY</code>，执行完毕后一律执行 <code>ROLLBACK</code>，形成多层物理闭环。</p>
"""

target = '<section class="refs">'
if target in text:
    new_text = text.replace(target, rich_qa_addition + "\n" + target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added rich QA additions to ch110")
else:
    print("Target not found")
