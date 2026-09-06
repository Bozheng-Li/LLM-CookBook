# -*- coding: utf-8 -*-
"""figures_ch005.py — 第 5 章插图: BPE 合并过程 与 上下文经济学"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# ---- 图 5-2 BPE: 从字符到子词 ----------------------------------------------
f = F(920, 310)
f.text(460, 32, "BPE:高频字符对不断合并,直到词表用尽", 17, C.ink, 800)
# panel 1
f.group(50, 66, 240, 168, "① 初始:按字符切", fill="#ffffff")
f.text(170, 122, "u n b e l i e v", 13, C.ink, 600, mono=True)
f.text(170, 142, "a b l e", 13, C.ink, 600, mono=True)
f.mtext(170, 178, ["每个字符都是", "独立 Token", "词表从 26 个字母起步"], 11.5, C.soft, 400, 1.6)
# panel 2
f.group(340, 66, 240, 168, "② 统计相邻对频率", fill="#ffffff")
f.mtext(460, 108, ["『li』出现 12000 次 → 合并", "『ab』出现 11000 次 → 合并", "『un』『able』… 依次合并", "循环:重新统计 → 再合并", "直到达到词表大小上限"], 11.5, C.soft, 400, 1.75)
# panel 3
f.group(630, 66, 240, 168, "③ 收敛:子词词表", fill="#ffffff")
f.text(750, 122, "un | believ | able", 13, C.teal_d, 700, mono=True)
f.mtext(750, 158, ["13 个字符 → 3 个 Token", "常见词整存,罕见词拆开", "词表 5 万~20 万(量级)"], 11.5, C.soft, 400, 1.75)
f.arrow(292, 150, 336, 150, color=C.faint, sw=1.6)
f.arrow(582, 150, 626, 150, color=C.faint, sw=1.6)
f.note(460, 276, "任意新词都能一路拆到字符级 —— 这是 BPE 词表『没有未知词』的原因;各厂商词表互不通用,Token 数不能跨模型比较", 12, C.faint, anchor="middle")
f.save("fig-bpe-merge")

# ---- 图 5-3 上下文的经济学 ---------------------------------------------------
f = F(920, 430)
f.text(460, 32, "上下文的经济学:多轮对话成本加速上涨", 17, C.ink, 800)
# 左: 柱状图
f.text(250, 66, "每轮输入 Token 数(API 无状态,历史全部重发)", 12.5, C.soft, 700)
rounds = [(1.2, "第 1 轮"), (2.6, "第 2 轮"), (4.2, "第 3 轮"), (6.0, "第 4 轮"), (8.0, "第 5 轮"), (10.2, "第 6 轮")]
base_y, bx = 340, 80
for i, (v, lab) in enumerate(rounds):
    h = v * 24
    x = bx + i * 76
    f.raw('<rect x="%d" y="%d" width="52" height="%d" rx="5" fill="%s" opacity="0.85"/>' % (x, base_y - h, h, C.indigo if i % 2 == 0 else C.teal))
    f.text(x + 26, base_y - h - 8, "%.1fK" % v, 11, C.ink, 700)
    f.text(x + 26, base_y + 18, lab, 11, C.faint, 600)
f.raw('<line x1="64" y1="%d" x2="540" y2="%d" stroke="%s" stroke-width="1.5"/>' % (base_y, base_y, C.line))
f.text(250, base_y + 44, "总成本 ≈ O(n²):第 n 轮要把前 n-1 轮全部重发一遍", 12, C.red_d, 600)
# 右: 省钱开关
f.group(570, 60, 310, 292, "四个省钱开关", fill="#ffffff")
f.mtext(592, 104, [
    "① Prompt Caching",
    "   命中部分五折~一折",
    "② 滚动摘要压缩历史",
    "   旧对话压成结构化便签",
    "③ 大结果落盘",
    "   上下文只放指针 + 摘要",
    "④ 级联路由",
    "   简单轮次换便宜的小模型",
], 12.5, C.ink, 400, 1.85, anchor="start")
f.note(460, 404, "计费 = 输入单价 × 输入 Token + 输出单价 × 输出 Token;输出单价通常是输入的 3~5 倍(量级)", 12, C.faint, anchor="middle")
f.save("fig-context-econ")

print("figures_ch005 done")
