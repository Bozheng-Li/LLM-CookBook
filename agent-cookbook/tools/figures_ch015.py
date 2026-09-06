# -*- coding: utf-8 -*-
"""figures_ch015.py — 第 15 章插图：循环中上下文的生长与检查点"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# ---- 图 15-3 循环中上下文的生长（新画） ------------------------------------
f = F(960, 500)
f.text(480, 30, "步进式执行的真相：上下文随每一轮单调生长", 17, C.ink, 800)
f.text(480, 52, "Agent 的全部状态就是那份 messages 列表——看清它如何变长，就看清了循环的一切", 12, C.faint)

cols = [
    ("第 0 轮", [("system", "角色 + 规则 + 工具表", C.gray_s, C.line, C.ink),
                ("user", "任务：调研 X 并写摘要", C.blue_s, C.blue, C.blue_d)]),
    ("第 1 轮", [("assistant", "tool_call: search(X)", C.indigo_s, C.indigo, C.indigo_d),
                ("tool", "搜索结果（裁剪后回填）", C.teal_s, C.teal, C.teal_d)]),
    ("第 2 轮", [("assistant", "tool_call: fetch(url)", C.indigo_s, C.indigo, C.indigo_d),
                ("tool", "网页正文（截断到预算）", C.teal_s, C.teal, C.teal_d)]),
    ("第 3 轮", [("assistant", "最终回答（不再调工具）", C.green_s, C.green, "#166534")]),
]
x = 46
for name, msgs in cols:
    f.group(x, 76, 200, 250, name, fill="#ffffff", stroke=C.faint, fs=12.5)
    yy = 112
    for role, txt, fillc, strokec, tc in msgs:
        h = 44 if len(txt) <= 14 else 58
        f.box(x + 12, yy, 176, h, "", fill=fillc, stroke=strokec, rx=8, sw=1.2)
        f.text(x + 100, yy + 17, role, 10.5, tc, 800)
        f.mtext(x + 100, yy + 34, wrap(txt, 150, 10), 10, C.ink, 500, 1.3)
        yy += h + 10
    x += 226
for ax in (262, 488, 714):
    f.arrow(ax, 200, ax + 34, 200, color=C.faint, sw=1.8)
    f.text(ax + 17, 186, "追加", 10.5, C.faint)

f.group(46, 350, 894, 116, "两个工程推论", fill=C.amber_s, stroke=C.amber, fs=12.5)
f.text(70, 386, "① 成本随步数超线性增长：第 n 轮要为前 n-1 轮的全部上下文再付一次输入 token 的钱——循环的账单是平方量级的", 12, C.ink, 600, anchor="start")
f.text(70, 410, "② 状态 = 某一时刻的 messages：把它序列化存盘即「检查点」；载入后接着跑即「恢复」——暂停、审批、断点续跑全靠它", 12, C.ink, 600, anchor="start")
f.text(70, 440, "工具结果过大时先裁剪再回填（上下文预算见第 23 章）；已被回答的旧观察可以压缩成一行摘要，为后续步骤腾地方。", 11.5, C.soft, 400, anchor="start")
f.save("fig-loop-state")
