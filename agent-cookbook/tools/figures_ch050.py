# -*- coding: utf-8 -*-
"""figures_ch050.py — ch050 评测方法论插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# ---- fig 50-1: 评测分类学 ----
f = F(940, 440)
f.text(470, 32, "Agent 评测的分类学:四个正交维度", 18, C.ink, 800)
# 维度1: 静态-动态
f.arrow(80, 120, 420, 120, "", C.soft, both=True)
f.text(95, 105, "静态(固定题集)", 12.5, C.indigo, 800, anchor="start")
f.text(405, 105, "动态(生成/进化)", 12.5, C.red, 800, anchor="end")
# 维度2: 结果-过程
f.arrow(520, 120, 860, 120, "", C.soft, both=True)
f.text(535, 105, "结果导向", 12.5, C.indigo, 800, anchor="start")
f.text(845, 105, "过程导向", 12.5, C.red, 800, anchor="end")
# 四象限
quads = [
    (120, 170, C.teal,  "静态 × 结果", "SWE-bench · BFCL\nGAIA · BrowseComp", "最主流: 可复现可排行"),
    (120, 300, C.blue,  "静态 × 过程", "AgentBench 部分子集\nτ-bench 轨迹约束", "诊断用: 定位哪类失败"),
    (450, 170, C.amber, "动态 × 结果", "WebArena 随机化\n自建影子回归", "防背题: 与时俱进"),
    (450, 300, C.purple,"动态 × 过程", "课程式评测(第45章)\nPRM 检查点评估", "研究前沿: 难维护"),
]
for x, y, colr, t, ex, note_ in quads:
    b = f.box(x, y, 290, 110, t, None, fill=C.white, stroke=colr)
    f.text(x + 145, y - 10, t, 13, colr, 800)
    for i, ln in enumerate(ex.split("\n")):
        f.text(x + 145, y + 42 + i * 16, ln, 11, C.ink)
    f.text(x + 145, y + 132, note_, 10.5, C.faint)
f.note(80, 430, "选型建议: 主榜用「静态×结果」保证可比性; 自建回归用「动态×结果」防泄漏; 过程维度做诊断不做排名", 11.5, C.faint)
f.save("fig-eval-taxonomy")

# ---- fig 50-2: 泄漏与饱和 ----
f = F(940, 380)
f.text(470, 32, "榜单的两大老年病:泄漏与饱和", 18, C.ink, 800)
# 左: 饱和曲线
f.box(60, 90, 380, 240, "", None, fill=C.white, stroke=C.line_soft)
f.text(250, 80, "饱和: 分数挤在顶部", 13, C.amber, 800)
f.raw('<polyline points="90,290 140,180 190,140 240,125 290,118 340,115 400,113" fill="none" stroke="%s" stroke-width="2.5"/>' % C.amber)
f.raw('<polyline points="90,300 140,240 190,205 240,185 290,175 340,168 400,164" fill="none" stroke="%s" stroke-width="2.5"/>' % C.indigo)
f.raw('<polyline points="90,308 140,280 190,255 240,240 290,232 340,226 400,222" fill="none" stroke="%s" stroke-width="2.5"/>' % C.teal)
f.text(415, 113, "头部模型", 10.5, C.amber, 700, anchor="end")
f.text(415, 167, "次级模型", 10.5, C.indigo, 700, anchor="end")
f.text(415, 225, "上一代", 10.5, C.teal, 700, anchor="end")
f.note(80, 310, "症状: 前三名差距 <2%, 噪声级别 — 排名失去信息量")
f.note(80, 332, "解法: 更难版本 (V2) · 难题子集 · 动态出题")
# 右: 泄漏
f.box(500, 90, 380, 240, "", None, fill=C.white, stroke=C.line_soft)
f.text(690, 80, "泄漏: 题目进了训练数据", 13, C.red, 800)
f.raw('<rect x="540" y="120" width="300" height="60" rx="8" fill="%s" stroke="%s"/>' % (C.red_s, C.red))
f.text(690, 145, "评测题集 (公开)", 12, C.red_d, 800)
f.text(690, 165, "↓ 爬虫/合成管线无意摄入", 10.5, C.ink)
f.raw('<rect x="540" y="200" width="300" height="60" rx="8" fill="%s" stroke="%s"/>' % (C.indigo_s, C.indigo))
f.text(690, 225, "下一代训练语料", 12, C.indigo_d, 800)
f.text(690, 245, "→ 分数虚高, 真实能力未变", 10.5, C.ink)
f.note(520, 310, "症状: 新模型分数跳升, 但同类任务实测不涨")
f.note(520, 332, "解法: 私有保留集 · 去污染扫描 · 动态评测")
f.save("fig-leak-saturation")
