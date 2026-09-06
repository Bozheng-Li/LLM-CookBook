# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch105.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

expansion_more = """
    <h2 id="enterprise-migration-roadmap">从原型到高可用生产：四阶段企业级平滑迁移实战路径</h2>
    <p>很多企业技术团队在立项初期往往使用 CrewAI 或纯 LangChain 快速搭建了一个演示 Demo，当业务部门提出「需要支持每天几十万单业务流转、需要支持人工审批驳回、需要支持审计合规与灰度发布」时，原有的原型架构立刻暴露出严重的不可维护性。成熟的架构团队应当遵循<strong>「四阶段渐进式演化法则（4-Phase Progressive Evolution）」</strong>完成系统的平滑重构与生产落地：</p>
    
    <p><strong>第一阶段：概念验证期（PoC 探索，1~2 周）。</strong>首选 CrewAI 或原生 AutoGen。这一阶段的核心目标是<strong>「快速验证大模型能否真正理解该业务领域的复杂逻辑」</strong>。用最少的人力和代码行数把流程串通，向业务部门高管直观展示 AI 的自动化潜力，避免在基础设施上过早进行无意义的过度设计；</p>
    
    <p><strong>第二阶段：状态机固化与流程解耦（架构重构，2~4 周）。</strong>当业务逻辑得到验证后，技术团队必须果断剥离易失性的群聊封装，将核心业务流程<strong>全量重构至 LangGraph 的强类型状态图中</strong>。显式定义每一个 Node 的输入输出 TypedDict，用确定性代码编写条件边（Conditional Edges），为每一个涉及外部系统调用的动作挂载分布式持久化 Checkpointer（如 Redis 或 PostgreSQL 适配器），为未来的长时程断点自愈打下坚固基础；</p>
    
    <p><strong>第三阶段：平台化中台演进（低代码赋能，4~8 周）。</strong>引入 Dify 或基于 FastAPI 封装的企业专属 Agent 开放平台。将第二阶段沉淀下来的成熟核心图工作流，封装为标准化的微服务 API 与插件，暴露给全公司其他业务系统；同时利用 Dify 的可视化界面，允许运营与业务专家自主对下游提示词、检索召回阈值进行动态微调与 A/B 测试；</p>
    
    <p><strong>第四阶段：全链路可观测性与合规治理（生产护航，持续运行）。</strong>接入 OpenTelemetry、Langfuse 或 Arize Phoenix 等分布式追踪中台（第 79 章）。对每一次用户会话进行全局 Trace ID 染色，实时监控 P95 响应延迟、Token 消耗预算、敏感数据脱敏情况与工具调用失败率；设置自动熔断告警与降级策略，确保整个智能体系统在承受突发高并发流量冲击时坚如磐石。</p>
"""

insert_target = '<div class="callout note">'
if insert_target in text:
    new_text = text.replace(insert_target, expansion_more + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added enterprise migration roadmap to ch105.html")
else:
    print("Target not found")
