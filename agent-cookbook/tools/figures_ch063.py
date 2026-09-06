# -*- coding: utf-8 -*-
"""figures_ch063.py — ch063 幻觉治理插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

f = F(940, 420)
f.text(470, 32, "幻觉四型:治理手段必须与类型配对", 18, C.ink, 800)
cells = [
    (60,  90, 400, 140, C.red,   "事实性幻觉", "编造不存在的事实/数据/引用", "检索接地 + 引用核对 + 事后校验"),
    (480, 90, 400, 140, C.amber, "忠实性幻觉", "回答偏离给定材料(总结加戏)", "忠实性评测 + 约束式生成"),
    (60,  250, 400, 140, C.purple,"推理幻觉", "步骤逻辑错误但结论自信", "验证器 + 过程奖励(第43/46章)"),
    (480, 250, 400, 140, C.blue, "编造式回答", "知识缺失时硬答(不懂装懂)", "校准的不确定性表达 + 拒答"),
]
for x, y, w, h, colr, t, d, fix in cells:
    f.box(x, y, w, h, t, None, fill=C.white, stroke=colr, fs=14)
    f.text(x + w/2, y + 44, d, 11, C.ink)
    f.text(x + w/2, y + 84, "对策: " + fix, 10.5, C.indigo_d, 700)
f.note(470, 412, "诊断先行: 把「幻觉」混称拆成四型, 每型不同的测量与治理 — 混着治理等于全都没治好", 11.5, C.indigo_d, anchor="middle")
f.save("fig-hallucination-types")
