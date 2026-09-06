# -*- coding: utf-8 -*-
"""figures_ch051.py — ch051 SWE-bench 插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# ---- fig 51-1: SWE-bench 评测流水线 ----
f = F(940, 420)
f.text(470, 32, "SWE-bench 的评测流水线:从 issue 到绿测", 18, C.ink, 800)
b1 = f.box(50, 100, 170, 110, "① 真实 Issue", "GitHub issue +\n关联 PR", fill=C.indigo_s, stroke=C.indigo)
b2 = f.box(260, 100, 170, 110, "② 检出仓库", "parent commit\n+ 环境配置", fill=C.teal_s, stroke=C.teal)
b3 = f.box(470, 100, 170, 110, "③ 模型改码", "生成 patch\n(diff 格式)", fill=C.amber_s, stroke=C.amber)
b4 = f.box(680, 100, 210, 110, "④ 沙箱执行测试", "fail→pass 验证\n+ PASS_TO_PASS", fill=C.purple_s, stroke=C.purple)
f.arrow(220, 155, 260, 155, "", C.soft)
f.arrow(430, 155, 470, 155, "", C.soft)
f.arrow(640, 155, 680, 155, "", C.soft)
f.note(70, 250, "判定双闸: ① FAIL_TO_PASS — issue 相关测试必须从红变绿")
f.note(70, 274, "        ② PASS_TO_PASS — 周边测试必须保持绿 (防「修一个坏三个」)")
f.note(70, 298, "评分: resolved = 双闸全过。没有裁判模型 — 测试就是唯一的上帝")
f.note(70, 330, "这也是它难以作弊、被广泛信任的原因: 一切判定可执行、可复现、可审计", 11.5, C.indigo_d)
f.save("fig-swebench-pipeline")

# ---- fig 51-2: 家族谱系 ----
f = F(940, 380)
f.text(470, 32, "SWE-bench 家族谱系与 LiveCodeBench 的互补", 17, C.ink, 800)
root = f.pill(150, 100, "SWE-bench (2023.10)", C.indigo_s, C.indigo_d, fs=13)
kids = [
    (330, 90,  C.blue,   "Lite (300 题)", "轻量子集 · 快速回归"),
    (330, 170, C.teal,   "Verified (500 题)", "OpenAI 人工校验 · 去歧义 · 行业主标"),
    (330, 250, C.amber,  "Multimodal", "含 UI 截图 · 前端任务"),
    (330, 330, C.purple, "SWE-bench-Live / MM", "持续更新 · 防老化分支"),
]
for x, y, colr, t, d in kids:
    f.box(x, y, 220, 56, t, None, fill=C.white, stroke=colr, fs=12.5)
    f.text(x + 110, y - 8, d, 10.5, C.faint)
    f.arrow(248, 100, x, y + 28, "", C.soft)
lcb = f.box(640, 60, 250, 130, "LiveCodeBench", "竞赛题持续滚动更新\n(月度新增+时效切片)\n专治「见过的题」", fill=C.teal_s, stroke=C.teal)
f.arrow(560, 118, 640, 125, "代码域互为补充", C.soft)
f.note(765, 220, "一个考「修真实仓库」(工程能力)", 11.5, C.ink, anchor="middle")
f.note(765, 242, "一个考「写新代码」(算法能力)", 11.5, C.ink, anchor="middle")
f.note(765, 264, "两者都高才是完整的代码 Agent", 11.5, C.indigo_d, anchor="middle")
f.save("fig-swebench-family")
