# -*- coding: utf-8 -*-
"""figures_ch030.py — ch030 Claude Code 剖析插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

f = F(960, 520)
f.text(480, 30, "Claude Code 的运行时解剖:无状态核心 + 三圈护栏", 17.5, C.ink, 800)

# 核心循环
core = f.box(370, 130, 220, 100, "Agent Loop", "工具循环 + todo.md\n+ /compact 压缩",
             fill=C.indigo_s, stroke=C.indigo, tc=C.indigo_d, fs=13.5)
f.note(480, 260, "核心保持无状态:每轮从完整上下文重新出发", 11.5, C.faint)

# 内圈: 权限
f.group(250, 70, 460, 300, "", fill="#ffffff", stroke=C.teal, dash="7 4")
f.text(492, 92, "权限圈(每次工具调用)", 12.5, C.teal_d, 800)
# 外圈: 沙箱
f.group(150, 40, 660, 360, "", fill="#ffffff", stroke=C.amber, dash="7 4")
f.text(492, 62, "沙箱圈(文件系统/网络边界)", 12.5, C.amber_d, 800)

tools = [("Read 读", 300, 120), ("Edit 改", 300, 190), ("Bash 执行", 620, 120), ("WebFetch", 620, 190)]
for t, x, y in tools:
    f.box(x, y, 110, 44, t, fill=C.teal_s, stroke=C.teal, tc=C.teal_d, fs=12)
f.arrow(370, 180, 330, 142, color=C.faint)
f.arrow(370, 180, 330, 212, color=C.faint)
f.arrow(590, 180, 616, 142, color=C.faint)
f.arrow(590, 180, 616, 212, color=C.faint)
f.pill(492, 330, "CLAUDE.md 项目记忆 / 子代理 / Hooks 钩子", fill=C.purple_s, tc=C.purple_d, fs=12)
f.text(150 + 8, 386, "三圈之外: 你的真实系统 —— Agent 永远只能在圈内做事", 11.5, C.soft, 600, anchor="start")
f.save("fig-claude-code-anatomy")
print("done")
