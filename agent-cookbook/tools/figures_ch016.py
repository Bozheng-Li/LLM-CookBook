# -*- coding: utf-8 -*-
"""figures_ch016.py — ch016 ReAct 章新插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# ---- ReAct vs CoT vs Act-only：三种范式的结构差异 ------------------------
f = F(960, 520)
f.text(480, 30, "三种范式：CoT 只有脑，Act-only 只有手，ReAct 脑手交织", 17.5, C.ink, 800)

def mini_flow(x, title, sub, items, colr, colr_s):
    """画一列小型步骤框, items: (文本, 是否高亮)"""
    f.group(x, 58, 280, 400, "", fill="#ffffff", stroke=C.line)
    f.text(x + 140, 86, title, 14.5, colr, 800)
    f.text(x + 140, 106, sub, 11, C.faint, 400)
    y = 124
    for txt, hi in items:
        h = 30 if len(txt) < 16 else 44
        f.box(x + 18, y, 244, h, "", fill=(colr_s if hi else C.gray_s),
              stroke=(colr if hi else C.line), rx=7)
        for i, ln in enumerate(wrap(txt, 210, 11)):
            f.text(x + 140, y + (h / 2) + 4 + (i - (len(wrap(txt, 210, 11)) - 1) / 2) * 13,
                   ln, 11, C.ink if hi else C.soft, 600 if hi else 400)
        y += h + 9
    f.text(x + 140, y + 26, "", 11, C.faint)

# 列 1：CoT
mini_flow(40, "Chain-of-Thought", "只有内部推理，没有外部世界", [
    ("输入问题", False),
    ("思考：先算 A…", True),
    ("思考：再算 B…", True),
    ("思考：所以 C…", True),
    ("输出答案", False),
    ("❌ 错了也不知道，无外部反馈", False),
], C.blue, C.blue_s)

# 列 2：Act-only
mini_flow(340, "Act-only", "只有行动，没有显式推理", [
    ("输入问题", False),
    ("行动：search[A]", True),
    ("观察：结果一", False),
    ("行动：search[B]", True),
    ("观察：结果二", False),
    ("❌ 盲走，错一步难回头", False),
], C.teal, C.teal_s)

# 列 3：ReAct
mini_flow(640, "ReAct", "思考与行动在同一条轨迹中交替", [
    ("Thought：先查 A 的年份", True),
    ("Action：search[A]", True),
    ("Observation：返回结果", False),
    ("Thought：A 是 1844，再查 B", True),
    ("Action：search[B] → 观察", True),
    ("✅ 有反馈的推理，可纠正", False),
], C.indigo, C.indigo_s)

f.pill(480, 490, "交织 = 每次行动前先声明理由，每次行动后用真实观察校准推理 —— Yao et al., ICLR 2023", fill=C.amber_s, tc=C.amber_d, fs=12.5)
f.save("fig-react-paradigms")

print("figures_ch016 done")
