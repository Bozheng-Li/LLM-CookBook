# -*- coding: utf-8 -*-
"""figures_ch031.py — ch031 AutoGen 插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

f = F(960, 480)
f.text(480, 30, "AutoGen GroupChat:消息驱动的话筒轮转", 17.5, C.ink, 800)

# 中心消息总线
f.box(360, 200, 240, 64, "GroupChat 消息流", "所有发言进入共享历史",
      fill=C.indigo_s, stroke=C.indigo, tc=C.indigo_d, fs=13)
agents = [("Coder\n写代码", 90, 90, C.teal), ("Executor\n跑代码", 380, 80, C.blue),
          ("Critic\n提意见", 670, 90, C.amber), ("UserProxy\n人类", 820, 230, C.purple)]
for name, x, y, colr in agents:
    f.box(x, y, 130, 56, name, fill=C.white, stroke=colr, tc=colr, fs=12)
    if x < 400:
        f.elbow([(x + 65, y + 56), (x + 65, 232), (356, 232)], color=C.faint, sw=1.3)
    elif x < 800:
        f.elbow([(x + 65, y + 56), (x + 65, 232), (604, 232)], color=C.faint, sw=1.3)
    else:
        f.arrow(818, 258, 606, 240, color=C.faint, sw=1.3)
f.pill(480, 330, "Manager(LLM)决定下一个发言者 —— 控制流在对话中涌现", fill=C.amber_s, tc=C.amber_d, fs=12.5)
f.note(480, 300, "0.2 版: round-robin / 手动 / LLM 选人   0.4 版: 事件驱动重写", 11.5, C.faint)
f.note(480, 372, "话筒轮转 = 发言权控制(speaker selection),群聊模式的核心开关", 12, C.soft, 600)
f.note(480, 452, "优势: 零编排代码即可协作   代价: 轮次不可预测 → 生产需配 max_rounds 硬刹车", 12, C.faint)
f.save("fig-autogen-groupchat")
print("done")
