# -*- coding: utf-8 -*-
"""figures_ch105.py — ch105 开源 Agent 框架全景横评与技术选型 插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# fig 105-1: 五大主流开源 Agent 框架生态全景与设计哲学矩阵
f = F(940, 420)
# 1. LangGraph / LangChain
f.box(40, 60, 160, 110, "LangChain / Graph\n(状态图控制流)\n• 显式有向图与循环\n• 强大的持久化快照\n• 学习曲线较陡峭", fill=C.blue_s, stroke=C.blue)
# 2. AutoGen
f.box(220, 60, 160, 110, "Microsoft AutoGen\n(多代理会话协议)\n• 灵活的群聊管理者\n• 原生代码执行沙箱\n• 事件驱动去中心化", fill=C.indigo_s, stroke=C.indigo)
# 3. CrewAI
f.box(400, 60, 160, 110, "CrewAI\n(角色协同与任务)\n• 极简高阶声明式 API\n• 严格任务委派机制\n• 易上手、轻量灵活", fill=C.amber_s, stroke=C.amber)
# 4. MetaGPT
f.box(580, 60, 160, 110, "MetaGPT\n(软件工程 SOP)\n• 实体化标准化文档\n• 结构化消息发布订阅\n• 复杂巨型工程交付", fill=C.teal_s, stroke=C.teal)
# 5. Dify
f.box(760, 60, 140, 110, "Dify.AI\n(可视编排中台)\n• 低代码工作流画布\n• 生产级 BaaS/RAG\n• 业务人员友好", fill=C.purple_s, stroke=C.purple)

# 底部多维选型权衡坐标轴
f.box(80, 260, 780, 130, "企业级架构技术选型四维雷达矩阵 (Selection Decision Radar)\n• 确定性与长流程治理: 首选 LangGraph (强状态机、断点续传、人机协同审批)\n• 复杂研发工程流水线: 首选 MetaGPT (文档驱动、严密防群聊发散与接口漂移)\n• 快速业务 POC 原型验证: 首选 CrewAI / AutoGen (轻量开箱即用、角色灵活配对)\n• 跨部门无代码企业交付: 首选 Dify (可视化 DAG 画布、开箱即用 API 网关与运维大屏)", fill=C.faint, stroke=C.line)

f.save("fig-agent-frameworks-landscape")

# fig 105-2: 选型决策树流向拓扑
f = F(940, 360)
f.pill(120, 70, "企业 Agent 业务需求", fill=C.blue_s, tc=C.blue_d, stroke=C.blue)

f.box(60, 150, 180, 70, "需要低代码可视化?\n业务人员直接编排", fill=C.purple_s, stroke=C.purple)
f.box(280, 150, 180, 70, "强状态控制?\n复杂循环与断点恢复", fill=C.blue_s, stroke=C.blue)
f.box(500, 150, 180, 70, "需要团队分工?\n标准化多角色产出", fill=C.teal_s, stroke=C.teal)
f.box(720, 150, 180, 70, "极速轻量原型?\n开发体验简单优雅", fill=C.amber_s, stroke=C.amber)

f.arrow(120, 95, 150, 150)
f.arrow(120, 95, 370, 150)
f.arrow(120, 95, 590, 150)
f.arrow(120, 95, 810, 150)

f.pill(150, 280, "推荐: Dify", fill=C.purple_s, tc=C.purple_d, stroke=C.purple)
f.pill(370, 280, "推荐: LangGraph", fill=C.blue_s, tc=C.blue_d, stroke=C.blue)
f.pill(590, 280, "推荐: MetaGPT", fill=C.teal_s, tc=C.teal_d, stroke=C.teal)
f.pill(810, 280, "推荐: CrewAI", fill=C.amber_s, tc=C.amber_d, stroke=C.amber)

f.arrow(150, 220, 150, 260)
f.arrow(370, 220, 370, 260)
f.arrow(590, 220, 590, 260)
f.arrow(810, 220, 810, 260)

f.save("fig-framework-decision-tree")
print("ch105 figures generated successfully")
