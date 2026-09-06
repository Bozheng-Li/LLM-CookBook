# -*- coding: utf-8 -*-
"""figures_ch054.py — ch054 工具调用评测插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# ---- fig 54-1: BFCL 子能力维度 ----
f = F(940, 400)
f.text(470, 32, "BFCL 的子能力谱系:把「会用工具」拆到原子", 18, C.ink, 800)
cells = [
    (60,  80, 400, 100, C.teal,  "简单调用", "单函数、参数齐全 — 基础盘"),
    (480, 80, 400, 100, C.blue,  "多函数选择", "给 10+ 函数选对的那个 — 检索与消歧"),
    (60,  200, 400, 100, C.indigo,"并行调用", "一次回复多个独立调用 — 第17/44章的老朋友"),
    (480, 200, 400, 100, C.amber, "多轮/链式", "后一调用依赖前一结果 — 状态跟踪"),
    (60,  320, 820, 60, C.red,  "相关性与拒答", "无关问题不该调用 · 缺前置时不该硬调 — 「克制」维度"),
]
for x, y, w, h, colr, t, d in cells:
    f.box(x, y, w, h, t, None, fill=C.white, stroke=colr, fs=14)
    f.text(x + w/2, y + h - 20, d, 11, C.faint)
f.save("fig-bfcl-dims")

# ---- fig 54-2: ToolSandbox 状态依赖 ----
f = F(940, 380)
f.text(470, 32, "ToolSandbox:多轮状态依赖的三种考法", 18, C.ink, 800)
b1 = f.box(50, 80, 270, 110, "① 隐式状态依赖", None, fill=C.white, stroke=C.indigo, fs=13)
l1 = ["「改成刚才那个地址」", "→ 模型必须记得「刚才」", "  是哪一个(对话历史+DB)"]
for i, ln in enumerate(l1):
    f.text(185, 112 + i * 18, ln, 10.5, C.ink)
b2 = f.box(340, 80, 270, 110, "② 不确定的工具结果", None, fill=C.white, stroke=C.amber, fs=13)
l2 = ["工具返回「航班可能延误」", "→ 模型如何决策与沟通?", "考模糊信息下的稳健性"]
for i, ln in enumerate(l2):
    f.text(475, 112 + i * 18, ln, 10.5, C.ink)
b3 = f.box(630, 80, 260, 110, "③ 动态策略", None, fill=C.white, stroke=C.purple, fs=13)
l3 = ["任务中途规则变化", "(「现在免费改签了」)", "→ 考策略的实时更新"]
for i, ln in enumerate(l3):
    f.text(760, 112 + i * 18, ln, 10.5, C.ink)
f.arrow(320, 135, 340, 135, "", C.soft)
f.arrow(610, 135, 630, 135, "", C.soft)
f.note(470, 240, "三种考法的共同点: 判分器跟踪「世界状态」— 上一轮的调用改变了什么, 下一轮的断言就用什么", 11.5, C.ink, anchor="middle")
f.note(470, 268, "与静态评测(每题独立)的本质区别: 状态在轮间流动, 分数 = 状态跟踪能力", 11.5, C.faint, anchor="middle")
f.note(470, 320, "工程启示: 多轮业务 Agent 的评测必须含「隐式指代」与「中途变卦」两类题 — 最常见的线上翻车形态", 11.5, C.indigo_d, anchor="middle")
f.save("fig-toolsandbox")
