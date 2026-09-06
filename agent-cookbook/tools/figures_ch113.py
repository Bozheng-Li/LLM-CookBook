# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# 图 113-1: 智能体 300 条核心术语体系知识分类拓扑 (Agent Glossary Taxonomy)
f = F(940, 420)
f.box(40, 50, 240, 150, "1. 理论形式化与认知基础\n• MDP / POMDP / Dec-POMDP\n• 贝尔曼最优性算子 & 压缩映射\n• 双系统认知 (System 1/2)\n• 维纳负反馈 & 艾什比多样性定律", fill=C.blue_s, stroke=C.blue)
f.box(340, 50, 260, 150, "2. 规划、推理与对齐算法\n• ReAct / Plan-and-Solve / ToT\n• 蒙特卡洛树搜索 (MCTS) & UCT\n• PPO / DPO / GRPO / PRM\n• 弱到强泛化 & 宪政 AI", fill=C.indigo_s, stroke=C.indigo)
f.box(640, 50, 260, 150, "3. 架构组件与工程中间件\n• GBNF 语法掩码 & Pydantic\n• 稠密/稀疏混合检索 & RRF 融合\n• PagedAttention & Radix Tree\n• Saga 事务补偿 & Redis 幂等锁", fill=C.teal_s, stroke=C.teal)

f.arrow(280, 125, 340, 125, color=C.blue)
f.arrow(600, 125, 640, 125, color=C.indigo)

f.box(80, 250, 780, 140, "4. 评测基准、沙箱隔离与安全治理 (Evaluation, Security & Governance)\n• SWE-bench / WebArena / GAIA / AgentBench 四大权威基准靶场\n• 间接提示词注入 (Indirect Injection) & CaMeL 双大模型物理隔离\n• Linux gVisor Sentry 用户态内核 & Firecracker 轻量化 MicroVM\n• 确定性自动化判题 Harness & 端到端状态断言回归防线", fill=C.purple_s, stroke=C.purple)

f.arrow(160, 200, 160, 250, color=C.blue)
f.arrow(470, 200, 470, 250, color=C.indigo)
f.arrow(770, 200, 770, 250, color=C.teal)

f.save("fig-agent-glossary-taxonomy")
print("Saved fig-agent-glossary-taxonomy.svg")

# 图 113-2: 术语交叉索引网络与智能检索查找状态机 (Glossary Query & Indexing Graph)
f2 = F(940, 360)
f2.box(40, 50, 190, 260, "中英文标准术语\n\n• 中英文双语对照\n• 权威学术首倡论文出处\n• 工业界标准缩写 (Acronym)\n• 跨学科交叉源语映射", fill=C.gray_s, stroke=C.line)
f2.box(260, 50, 200, 260, "形式化数学与理论本质\n\n• 严谨数学公式形式化表述\n• 核心状态空间定义与转移\n• 认知心理学对应机理\n• 控制论系统边界与收敛性", fill=C.blue_s, stroke=C.blue)
f2.box(490, 50, 200, 260, "工业系统架构映射\n\n• 典型开源开源框架接口\n• 生产级关键避坑场景\n• 性能开销与显存复杂度\n• 降级熔断与幂等性保障", fill=C.amber_s, stroke=C.amber)
f2.box(720, 50, 180, 260, "全书章节无缝穿梭\n\n• 基础篇/机制篇精准定位\n• 实战项目对应代码锚点\n• 顶会论文精读深层链接\n• 形成自洽立体知识图谱", fill=C.green_s, stroke=C.green)

f2.arrow(230, 180, 260, 180, color=C.indigo)
f2.arrow(460, 180, 490, 180, color=C.amber)
f2.arrow(690, 180, 720, 180, color=C.green)

f2.save("fig-glossary-indexing-graph")
print("Saved fig-glossary-indexing-graph.svg")
