# -*- coding: utf-8 -*-
"""figures_ch071.py — ch071 科学发现 Agent 插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# ---- fig 71-1: Coscientist / ChemCrow 工具链 ----
f = F(940, 420)
f.text(470, 32, "科学 Agent 的工具链:文献-规划-执行-分析", 18, C.ink, 800)
lit = f.box(50, 100, 180, 110, "文献检索", "PubChem / Reaxys\n论文搜索", fill=C.teal_s, stroke=C.teal)
plan = f.box(280, 100, 180, 110, "规划核心", "合成路线设计\n实验方案生成", fill=C.indigo_s, stroke=C.indigo)
exec_ = f.box(510, 100, 180, 110, "执行接口", "云实验室 API\n机器人平台", fill=C.amber_s, stroke=C.amber)
ana = f.box(740, 100, 160, 110, "分析闭环", "谱图解读\n结果→下一轮", fill=C.purple_s, stroke=C.purple)
f.arrow(230, 155, 280, 155, "", C.soft)
f.arrow(460, 155, 510, 155, "", C.soft)
f.arrow(690, 155, 740, 155, "", C.soft)
f.elbow([(820, 210), (820, 310), (140, 310), (140, 210)], "结果回流 → 假设迭代", C.red, label_pos=1)
f.note(60, 250, "ChemCrow 的 18 个专业工具: 每个都是「确定性的领域知识封装」 — 安全清单工具与合成工具同级并存")
f.note(60, 280, "Coscientist 的 GPT-4 规划 + 云实验室执行: 2023 Nature 论文 — 首次端到端自主完成钯催化偶联等真实合成")
f.note(60, 320, "安全设计: 危险化合物清单双重核对 (规划时+执行前) — 科学域的「闸门」长在工具层(第60章 L3 的实验室版)", 11.5, C.indigo_d)
f.save("fig-science-tools")

# ---- fig 71-2: 自主科研的边界金字塔 ----
f = F(940, 380)
f.text(470, 32, "自主科研的能力边界:能自动化什么", 18, C.ink, 800)
tiers = [
    (60,  250, 820, 80, "已自动化 (现在): 文献综述 · 方案初稿 · 数据分析 · 图表生成 · 论文润色", C.teal),
    (60,  155, 820, 80, "人机协作 (临界): 假设生成(需人筛) · 实验执行(需人监) · 结论解读(需人判)", C.amber),
    (60,  60, 820, 80, "仍是人类领地: 科学品味(什么问题值得问) · 范式判断 · 结果的意义赋予 · 责任归属", C.red),
]
for x, y, w, h, t, colr in tiers:
    f.box(x, y, w, h, "", None, fill=C.white, stroke=colr)
    f.text(x + w/2, y + 45, t, 12, C.ink, 700)
f.note(470, 355, "判据: 「可形式化且错误可检出」的环节自动化 — 科学品味与意义赋予不可形式化, 是科研的最后人类堡垒", 11.5, C.indigo_d, anchor="middle")
f.save("fig-science-boundary")
