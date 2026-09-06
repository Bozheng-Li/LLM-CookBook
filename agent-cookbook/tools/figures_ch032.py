# -*- coding: utf-8 -*-
"""figures_ch032.py — ch032 CrewAI 插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

f = F(960, 460)
f.text(480, 30, "CrewAI 的三层抽象:Role → Task → Crew", 17.5, C.ink, 800)

# 三层卡片
layers = [
    ("Agent(角色)", "role / goal / backstory\n+ tools + llm", 60, C.teal, C.teal_s),
    ("Task", "description / expected_output\n+ agent + context(依赖)", 360, C.blue, C.blue_s),
    ("Crew(团队)", "agents + tasks + process\n(sequential / hierarchical)", 660, C.indigo, C.indigo_s),
]
for name, desc, x, colr, colr_s in layers:
    f.box(x, 70, 240, 96, name, desc, fill=colr_s, stroke=colr, tc=colr, fs=13)
f.arrow(300, 118, 356, 118, color=C.faint)
f.arrow(600, 118, 656, 118, color=C.faint)

# 流程示意
f.text(480, 210, "Task 链:上下文传递(前序产出即后续输入)", 13, C.soft, 700)
t1 = f.box(80, 240, 220, 54, "Task1 调研", "expected_output: 要点清单",
           fill="#ffffff", stroke=C.teal, tc=C.ink, fs=12)
t2 = f.box(370, 240, 220, 54, "Task2 撰写", "context=[Task1]",
           fill="#ffffff", stroke=C.blue, tc=C.ink, fs=12)
t3 = f.box(660, 240, 220, 54, "Task3 审校", "context=[Task1,Task2]",
           fill="#ffffff", stroke=C.amber, tc=C.ink, fs=12)
f.arrow(300, 267, 366, 267, color=C.faint)
f.arrow(590, 267, 656, 267, color=C.faint)

f.pill(480, 340, "顺序模式:按列表执行    层级模式:自动产生 Manager 角色分派", fill=C.purple_s, tc=C.purple_d, fs=12)
f.note(480, 396, "声明式约定:把『谁做什么、交付什么』写成配置 —— SOP 的框架化", 12, C.soft, 600)
f.note(480, 436, "对照:AutoGen 自由对话(涌现) vs CrewAI 声明流水线(结构化)", 12, C.faint)
f.save("fig-crewai-layers")
print("done")
