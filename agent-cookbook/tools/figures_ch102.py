# -*- coding: utf-8 -*-
"""figures_ch102.py — ch102 多智能体协同、角色扮演与社会模拟核心论文研读 插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# fig 102-1: 多智能体协同三大经典论文演进图谱
f = F(940, 420)
# 1. CAMEL
f.box(40, 60, 260, 150, "1. 角色扮演与自驱对话: CAMEL\nLi et al. (KAUST 2023)\n• 初始启导提示 (Inception Prompting)\n• 消除对话死锁与无限客套\n• 首创双智能体自主协同范式", fill=C.blue_s, stroke=C.blue)

# 2. MetaGPT
f.box(340, 60, 260, 150, "2. 软件工程 SOP 实体化: MetaGPT\nHong et al. (DeepWisdom 2023)\n• 引入标准作业程序 (SOP)\n• 角色分工: PRD/架构/设计/代码/QA\n• 结构化输出大幅消减幻觉与噪声", fill=C.indigo_s, stroke=C.indigo)

# 3. ChatDev
f.box(640, 60, 260, 150, "3. 虚拟软件公司瀑布流: ChatDev\nQian et al. (Tsinghua 2023)\n• 聊天链 (Chat Chain) 阶段解耦\n• 结对编程与双向交叉审查 (Review)\n• 1 美元、7 分钟完成端到端软件开发", fill=C.teal_s, stroke=C.teal)

# 底部演进核心线索
f.box(100, 260, 740, 130, "多智能体社会性协同的三重理论跃迁 (Multi-Agent Paradigm Shifts)\n• 从无序群聊到角色启导 (CAMEL): 严格定义用户代理（User Agent）与助手代理（Assistant Agent），实现零人工干预自主收敛\n• 从随意自然语言到工业级 SOP 规范 (MetaGPT): 借鉴现代制造业 SOP，将信息流约束在结构化文档（PRD/API设计）而非漫无边际的群聊中\n• 从单向瀑布到细粒度结对双向审查 (ChatDev): 引入软件工程“设计-编码-测试”多阶段聊天链，通过对抗性纠错将缺陷抹杀在阶段内", fill=C.amber_s, stroke=C.amber)

f.save("fig-mas-papers-evolution")

# fig 102-2: MetaGPT 标准作业程序 (SOP) 与文档驱动协作流
f = F(940, 360)
f.pill(120, 80, "用户一行需求输入", fill=C.blue_s, tc=C.blue_d, stroke=C.blue)

f.box(40, 150, 160, 90, "产品经理 (Product)\n编写标准需求文档\n输出: PRD.md\n(用户故事 / 边界需求)", fill=C.indigo_s, stroke=C.indigo)

f.box(230, 150, 160, 90, "系统架构师 (Architect)\n设计系统架构与拓扑\n输出: System_Design\n(数据结构 / 接口声明)", fill=C.purple_s, stroke=C.purple)

f.box(420, 150, 160, 90, "项目经理 (PM)\n分配依赖与任务拆解\n输出: Task_List\n(甘特图 / 文件优先级)", fill=C.amber_s, stroke=C.amber)

f.box(610, 150, 160, 90, "工程师 (Engineer)\n编写全量源码文件\n输出: main.py / etc.\n(严格对齐 API 规范)", fill=C.teal_s, stroke=C.teal)

f.box(790, 150, 130, 90, "质检 (QA)\n编写并执行单测\n静态语法审查\n(Bug 反思修正)", fill=C.green_s, stroke=C.green)

f.arrow(120, 105, 120, 150)
f.arrow(200, 195, 230, 195, "PRD")
f.arrow(390, 195, 420, 195, "架构图")
f.arrow(580, 195, 610, 195, "任务清单")
f.arrow(770, 195, 790, 195, "代码")

f.save("fig-metagpt-sop-pipeline")
print("ch102 figures generated successfully")
