# -*- coding: utf-8 -*-
"""figures_ch062.py — ch062 越狱与滥用插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# ---- fig 62-1: 越狱的四代演进 ----
f = F(940, 420)
f.text(470, 32, "越狱的四代演进:攻击与防御的军备竞赛", 18, C.ink, 800)
gens = [
    (60,  100, 190, 240, "第一代\n(2022-23)", C.amber, ["角色扮演", "「假装你是 DAN」", "假设框架", "「在一个虚构世界里…」", "", "防御: 简单对齐", "多已失效"], C.amber),
    (280, 100, 190, 240, "第二代\n(2023-24)", C.blue, ["编码/低资源语言", "Base64 · 古婆罗米文", "前缀注入 · 梯度对抗", "", "防御: 对抗训练", "内容分类器"], C.blue),
    (500, 100, 190, 240, "第三代\n(2024-25)", C.purple, ["多轮化", " Crescendo 渐进诱导", "长上下文稀释", "跨模态(图像藏字)", "", "防御: 多轮审查", "上下文感知分类器"], C.purple),
    (720, 100, 170, 240, "第四代\n(2025+)", C.red, ["自动化搜索", "树搜索式越狱", "针对对齐的优化攻击", "", "防御: 深度对齐", "推理时防御", "难度大幅上升"], C.red),
]
for x, y, w, h, t, colr, lines_, _ in gens:
    f.box(x, y, w, h, t.split("\n")[0] + " " + t.split("\n")[1], None, fill=C.white, stroke=colr, fs=12.5)
    for i, ln in enumerate(lines_):
        if ln == "":
            continue
        f.text(x + w/2, y + 58 + i * 17, ln, 10, C.red if "防御" in ln else (C.faint if ln.startswith("「") else C.ink), 700 if "防御" in ln else 400)
for i in range(3):
    x1 = gens[i][0] + gens[i][2]
    f.arrow(x1 + 3, 220, x1 + 27, 220, "", C.soft)
f.note(470, 380, "趋势: 攻击成本在降(自动化), 防御成本在升(推理时防御) — 结论依旧是「利用段防线兜底, 别赌认知段永不破」", 11.5, C.indigo_d, anchor="middle")
f.save("fig-jailbreak-generations")

# ---- fig 62-2: 滥用响应金字塔 ----
f = F(940, 380)
f.text(470, 32, "滥用者画像与分级响应金字塔", 18, C.ink, 800)
tiers = [
    (60,  260, 820, 80, "好奇型 (大多数): 玩家试探边界 — 宽松响应: 拒答+幽默+引导", C.teal),
    (60,  170, 820, 80, "机会型: 找免费劳动力/绕过付费 — 标准响应: 拒答+频控+记录", C.amber),
    (60,  80, 820, 80, "对抗型: 有组织的攻击/滥用牟利 — 强响应: 封禁+法务+情报共享", C.red),
]
for x, y, w, h, t, colr in tiers:
    f.box(x, y, w, h, "", None, fill=colr if False else C.white, stroke=colr)
    f.text(x + w/2, y + 45, t, 12, C.ink, 700)
f.note(470, 30, "金字塔底宽顶尖: 好奇型占 90%+ — 对「大众」用重手段会误伤体验, 对「尖顶」用轻手段会纵容攻击", 11.5, C.faint, anchor="middle")
f.save("fig-abuse-pyramid")
