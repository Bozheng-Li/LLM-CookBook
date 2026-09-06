# -*- coding: utf-8 -*-
"""figures_ch014.py — 第 14 章插图：Workflow 还是 Agent 决策树"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# ---- 图 14-3 决策树：这个任务该用几级自主性（新画） ------------------------
f = F(960, 520)
f.text(480, 30, "Workflow 还是 Agent：一条自上而下的决策链", 17, C.ink, 800)
f.text(480, 52, "Anthropic 的原则：从最简单的方案开始，只有评测证明必要时才增加自主性", 12, C.faint)

start = f.box(390, 76, 180, 52, "一个新任务", "先问下面三个问题", fill=C.gray_s, stroke=C.line, fs=13.5, sub_fs=10.5)
d1 = f.diamond(480, 190, 300, 84, "Q1 · 任务的执行路径\n能否预先写成固定流程？")
f.arrow(start["cx"], 128, start["cx"], 148, color=C.faint)

yes1 = f.box(60, 150, 220, 72, "用 Workflow 就够", "链 / 路由 / 并行（第 6-8 章）\n大多数业务流程的答案", fill=C.blue_s, stroke=C.blue, tc=C.blue_d, fs=13, sub_fs=10.5)
f.arrow(330, 190, 280, 190, label="能", color=C.blue, sw=1.6)

d2 = f.diamond(480, 320, 300, 84, "Q2 · 失败动作能否低成本\n验证或回滚？")
f.arrow(480, 232, 480, 278, label="不能枚举", color=C.amber, sw=1.6, label_dy=-8)
no2 = f.box(60, 286, 220, 72, "先加人工审批或缩小任务", "HITL 检查点（第 25 章）\n把任务切成可验证的小块", fill=C.red_s, stroke=C.red, tc=C.red_d, fs=13, sub_fs=10.5)
f.arrow(330, 320, 280, 320, label="否", color=C.red, sw=1.6)

d3 = f.diamond(480, 450, 300, 84, "Q3 · 需要跨多步动态选工具\n并利用中间结果吗？")
f.arrow(480, 362, 480, 408, label="可验证/可回滚", color=C.amber, sw=1.6, label_dy=-8)
single = f.box(760, 286, 176, 72, "单次工具调用即可", "结构化输出（第 8 章）\n不必引入循环", fill=C.teal_s, stroke=C.teal, tc=C.teal_d, fs=13, sub_fs=10.5)
f.arrow(630, 320, 760, 320, label="只差一步", color=C.teal, sw=1.6, label_dy=-8)
agent = f.box(760, 416, 176, 72, "上 Agent Loop", "模型驱动决策 + 环境闭环\n三种刹车必配（第 15 章）", fill=C.indigo_s, stroke=C.indigo, tc=C.indigo_d, fs=13, sub_fs=10.5)
f.arrow(630, 450, 760, 452, label="是", color=C.indigo, sw=1.6, label_dy=-8)

f.note(60, 486, "回看你的位置：绝大多数生产系统落在 Workflow 与「单次工具调用」两档；真正需要完整 Agent Loop 的，是路径无法枚举且可验证的任务。", 12, C.ink, anchor="start")
f.note(60, 506, "自主性每升一级，评测与护栏的投入至少翻一倍——这是成本，不是勋章。", 12, C.soft, anchor="start")
f.save("fig-workflow-agent-decision")
