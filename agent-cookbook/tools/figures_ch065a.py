# -*- coding: utf-8 -*-
"""figures_ch065a.py — ch065 风险分级插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

f = F(940, 420)
f.text(470, 32, "风险分级与义务阶梯: AI Act 的 Agent 映射", 18, C.ink, 800)
tiers = [
    (60,  100, 200, 200, "不可接受风险", C.red, "禁止类", "隐性操纵的\n目标函数", "直接禁用"),
    (290, 100, 200, 200, "高风险", C.amber, "严格义务类", "影响用户权益的\n自主决策(招聘/信贷)", "审计+人管+文档"),
    (520, 100, 200, 200, "有限风险", C.blue, "透明义务类", "大多数面向\n用户的 Agent", "告知「AI 在对话」"),
    (750, 100, 140, 200, "最小风险", C.teal, "自由类", "内部辅助工具", "鼓励自愿守则"),
]
for x, y, w, h, t, colr, kind, ex, duty in tiers:
    f.box(x, y, w, h, t, None, fill=C.white, stroke=colr, fs=13)
    f.text(x + w/2, y + 46, kind, 10.5, colr, 800)
    for i, ln in enumerate(ex.split("\n")):
        f.text(x + w/2, y + 80 + i * 17, ln, 10, C.ink)
    f.text(x + w/2, y + h - 14, duty, 9.5, C.indigo_d, 700)
f.note(470, 340, "分级决定义务, 义务决定工程清单 — 「你的 Agent 是哪一级」是治理的第一问 (按用途而非技术定级)", 11.5, C.ink, anchor="middle")
f.note(470, 372, "同一系统不同用途可跨级 (内部筛选=最小, 对外招聘=高风险) — 按部署实例定级, 不按产品名", 11.5, C.faint, anchor="middle")
f.save("fig-risk-tiers")
