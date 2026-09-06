# -*- coding: utf-8 -*-
"""figures_ch053.py — ch053 通用 Agent 基准插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# ---- fig 53-1: GAIA 三级难度 ----
f = F(940, 400)
f.text(470, 32, "GAIA:人类可解、机器难解的三级阶梯", 18, C.ink, 800)
levels = [
    (70, 120, 240, 170, "Level 1", C.teal,   "1~3 步\n「这份 PDF 里的表格\n第几行是总和?」", "人: 15s"),
    (350, 90, 240, 200, "Level 2", C.amber,  "5~10 步, 多源信息\n「查这家公司最新年报,\n对比我给的预算表」", "人: 2min"),
    (630, 60, 260, 230, "Level 3", C.red,    "10+ 步, 长程探索\n「这个作者引用过的\n所有 dataset 里哪个\n下载量最高?」", "人: 5min"),
]
for x, y, w, h, t, colr, sub, hu in levels:
    f.box(x, y, w, h, t, None, fill=C.white, stroke=colr, fs=15)
    f.text(x + w/2, y + 44, sub.split("\n")[0], 11, C.ink)
    f.text(x + w/2, y + 62, sub.split("\n")[1], 11, C.ink)
    if len(sub.split("\n")) > 2:
        f.text(x + w/2, y + 80, sub.split("\n")[2], 11, C.ink)
    f.text(x + w/2, y + h - 14, hu, 11, colr, 800)
f.arrow(310, 200, 350, 190, "", C.soft)
f.arrow(590, 185, 630, 175, "", C.soft)
f.note(470, 330, "设计哲学: 每道题都让「人类轻松解答」先验证过 — 难度来自「步骤多、需要工具、需要坚持」")
f.note(470, 355, "而非「智力门槛」。2023 年发布时: 人类 92% vs GPT-4(带插件) 15% — 90 分的鸿沟震撼了行业", 11.5, C.indigo_d)
f.note(470, 380, "2025 年头部系统 ~75%: 两年抹平 — 但 Level 3 仍是分化区", 11.5, C.faint)
f.save("fig-gaia-levels")

# ---- fig 53-2: tau-bench 的规则遵循 ----
f = F(940, 400)
f.text(470, 32, "tau-bench:客服场景的「能力 × 可靠性」双维评测", 18, F(940,400) if False else C.ink, 800)
# 用户模拟器
u = f.box(70, 90, 200, 110, "用户模拟器", "LLM 扮演用户\n带性格/需求/情绪", fill=C.amber_s, stroke=C.amber)
# 策略文档
p = f.box(70, 250, 200, 100, "领域策略文档", "退款规则 · 政策约束\n(必须遵守的教条)", fill=C.indigo_s, stroke=C.indigo)
a = f.box(370, 160, 200, 120, "被测 Agent", "工具调用 +\n对话 + 规则遵循", fill=C.teal_s, stroke=C.teal)
db = f.box(660, 100, 220, 90, "数据库断言", "操作结果正确性\n(退款已执行等)", fill=C.purple_s, stroke=C.purple)
pw = f.box(660, 250, 220, 90, "pass^k 指标", "连续 k 次全对\n(可靠性 > 峰值)", fill=C.red_s, stroke=C.red)
f.arrow(270, 145, 370, 190, "对话", C.soft)
f.arrow(370, 250, 270, 300, "读策略", C.soft)
f.arrow(570, 195, 660, 150, "", C.soft)
f.arrow(570, 245, 660, 290, "", C.soft)
f.note(470, 375, "核心洞察: 客服场景「一次错」就是事故 — pass^1=85% 的模型 pass^3 可能只有 61% — 可靠性是独立于能力的产品指标", 11.5, C.faint, anchor="middle")
f.save("fig-taubench")
