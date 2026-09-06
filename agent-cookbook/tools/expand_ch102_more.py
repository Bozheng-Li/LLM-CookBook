# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch102.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

expansion_more = """
    <h2 id="cross-paradigm-synthesis-engineering">从论文到生产：构建工业级多智能体软件工厂的五大架构铁律</h2>
    <p>综合研读 CAMEL、MetaGPT 与 ChatDev 这三篇改变多智能体协同历史走向的奠基之作，我们可以将原本分散在各论文中的学术洞见，系统性升华为构建企业级多智能体软件工厂（Enterprise Multi-Agent Factory）的<strong>五大硬核架构铁律</strong>：</p>
    
    <p><strong>第一铁律：契约高于对话（Artifact Over Chat）。</strong>这是 MetaGPT 带来的最宝贵遗产。在任何严肃的工业级多 Agent 系统中，严禁允许智能体之间进行无边界的口语化私聊。智能体之间流转的一等公民实体，必须是具备确定性 JSON Schema、严格 Markdown 表格或代码文件的<strong>结构化文档契约（Structured Artifacts）</strong>。文档即契约，接口即法典，任何不符合 Schema 的输出在进入下游前必须被直接打出编译红灯；</p>
    
    <p><strong>第二铁律：职责非对称隔离（Asymmetric Role Decoupling）。</strong>CAMEL 深刻证明了角色的职责必须严格非对称。在一个任务闭环中，必须清晰界定谁是「唯一的出题与验收方（Commander / Verifier）」，谁是「唯一的执行交付方（Worker）」。如果两个智能体都试图充当管理者，系统就会发生死锁撕扯；如果两个都试图充当打工人，任务就会停滞无序；</p>
    
    <p><strong>第三铁律：微观结对对抗审查（Granular Pairwise Review）。</strong>ChatDev 揭示的结对审查机制是消灭 Bug 的黄金法则。任何关键产出（一段核心业务逻辑、一份高危 SQL 迁移脚本、一组防火墙规则）在提交合并前，必须交由一个拥有对立提示词立场的审查者 Agent 进行严格的静态代码走查与边界值审查，绝不允许代码未经交叉双向确认即直接合入生产主干；</p>
    
    <p><strong>第四铁律：全局黑板最小订阅（Least Privilege Pub-Sub）。</strong>坚决杜绝让每一个 Agent 监听全集群所有广播消息的愚蠢设计。必须基于观察者模式与最小权限原则，根据任务依赖有向无环图（DAG），为每个角色开辟专属的只读订阅通道。架构师只看需求，工程师只看架构，测试员只看代码与单测，以极致的拓扑剪枝维护每个 Agent 上下文窗口的最高信噪比；</p>
    
    <p><strong>第五铁律：离散状态机物理阻断（Deterministic FSM Boundary）。</strong>大语言模型的输出终究存在小概率的随机抖动。多智能体系统在推进阶段演化时，绝不能单纯依赖大模型在文本里说一句“我认为当前阶段已完成”。各阶段的流转与跳转，必须由底层的<strong>确定性有限状态机（Finite State Machine, FSM）与代码执行断言</strong>进行物理硬锁死（例如只有当真实沙箱中 <code>pytest</code> 返回 exit code 0 时，状态机才允许推进至交付态）。</p>
"""

insert_target = '<div class="callout note">'
if insert_target in text:
    new_text = text.replace(insert_target, expansion_more + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added engineering rules section to ch102.html")
else:
    print("Target not found")
