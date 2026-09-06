# -*- coding: utf-8 -*-
"""figures_ch073.py — ch073 Deep Research 插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# ---- fig 73-1: Deep Research 五阶段 ----
f = F(940, 430)
f.text(470, 32, "Deep Research 的五阶段循环", 18, C.ink, 800)
st = [
    (50,  110, 160, 100, "① 计划", "研究问题分解\n为子问题树", C.indigo),
    (230, 110, 160, 100, "② 并行检索", "多路搜索\nAPI+浏览器", C.teal),
    (410, 110, 160, 100, "③ 综合", "证据聚合\n矛盾标注", C.amber),
    (590, 110, 160, 100, "④ 引用核对", "主张-来源对齐\n(第63章流水线)", C.purple),
    (770, 110, 130, 100, "⑤ 交付", "结构化报告\n+引用列表", C.red),
]
for x, y, w, h, t, d, colr in st:
    f.box(x, y, w, h, t, None, fill=C.white, stroke=colr, fs=13.5)
    for i, ln in enumerate(d.split("\n")):
        f.text(x + w/2, y + 56 + i * 17, ln, 10.5, C.ink)
for i in range(4):
    x1 = st[i][0] + st[i][2]
    f.arrow(x1 + 3, 160, x1 + 17, 160, "", C.soft)
# 回路
f.elbow([(490, 210), (490, 280), (130, 280), (130, 210)], "信息不足/新线索 → 回到计划 (迭代 2-5 轮)", C.red, label_pos=1)
f.note(470, 340, "与普通 RAG 的三大差异: 多轮迭代(不一次成文) · 子问题并行 · 引用核对内建", 11.5, C.ink, anchor="middle")
f.note(470, 375, "BrowseComp/GAIA 是它的标尺(第53章) — 检索续航与多步综合是两个核心能力", 11.5, C.faint, anchor="middle")
f.save("fig-deep-research-loop")

# ---- fig 73-2: 子问题树与并行 ----
f = F(940, 400)
f.text(470, 32, "研究计划的分解与并行执行", 18, C.ink, 800)
root = f.box(390, 60, 220, 70, "主问题", "「某技术的产业现状」", fill=C.indigo_s, stroke=C.indigo, fs=13)
subs = [
    (60,  200, 190, 90, "子问题 A", "技术路线对比", C.teal),
    (280, 200, 190, 90, "子问题 B", "主要玩家与格局", C.amber),
    (500, 200, 190, 90, "子问题 C", "成本与经济性", C.blue),
    (720, 200, 180, 90, "子问题 D", "政策与监管", C.purple),
]
for x, y, w, h, t, d, colr in subs:
    f.box(x, y, w, h, t, None, fill=C.white, stroke=colr, fs=12.5)
    f.text(x + w/2, y + 60, d, 11, C.ink)
    f.arrow(500, 130, x + w/2, y, "", C.soft)
rpt = f.box(380, 330, 240, 50, "证据池汇总 → 综合", None, fill=C.red_s, stroke=C.red, fs=12.5)
for x, y, w, h, t, d, colr in subs:
    f.arrow(x + w/2, y + h, 480, 330, "", C.soft)
f.note(470, 30, "并行度是 DR 的速度引擎: 子问题互相独立时并行 fan-out; 有依赖时按 DAG 排程 (第24章编排的检索版)", 11.5, C.faint, anchor="middle")
f.save("fig-dr-subtree")
