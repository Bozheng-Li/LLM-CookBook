# -*- coding: utf-8 -*-
"""figures_ch007.py — 第 7 章插图: 元提示 / 自动提示优化循环"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

f = F(900, 460)
f.text(450, 32, "元提示:让 LLM 批判并改写提示词的优化循环", 17, C.ink, 800)

a = f.box(60, 90, 190, 62, "① 初始提示", "手写,或让 LLM 起草", fill=C.indigo_s, stroke=C.indigo, tc=C.indigo_d)
b = f.box(330, 90, 200, 62, "② 在评测集上运行", "N 条用例逐一打分", fill=C.teal_s, stroke=C.teal, tc=C.teal_d)
c = f.box(610, 90, 220, 62, "③ 得分 + 失败案例", "把错误模式喂回给 LLM", fill=C.amber_s, stroke=C.amber, tc=C.amber_d)
d = f.box(610, 250, 220, 62, "④ LLM 批判与改写", "诊断原因 → 产出新提示", fill=C.purple_s, stroke=C.purple, tc=C.purple_d)
diam = f.diamond(430, 281, 150, 84, "分数达标?")
done = f.box(150, 250, 190, 62, "冻结上线", "提示词进入版本管理", fill=C.green_s, stroke=C.green, tc="#166534")

f.arrow(250, 121, 326, 121, color=C.faint)
f.arrow(530, 121, 606, 121, color=C.faint)
f.arrow(720, 152, 720, 246, color=C.faint)
# 否 → 回到运行
f.elbow([(610, 281), (430, 281)], color=C.faint)
f.elbow([(355, 281), (155, 281), (155, 156)], color=C.red, sw=1.8, dash="5 4")
f.text(250, 270, "否:换上新提示,再来一轮", 11.5, C.red_d, 700, style='paint-order:stroke;stroke:#fff;stroke-width:3px;')
# 是 → 冻结
f.elbow([(430, 238), (430, 204), (245, 204), (245, 246)], color=C.green, sw=1.8)
f.text(443, 212, "是", 12, C.green, 700, style='paint-order:stroke;stroke:#fff;stroke-width:3px;')
# C -> A 直连改写后的提示? 用 D 回到 B 已表达
f.note(450, 388, "APE(Zhou et al. 2022)、OPRO(Yang et al. 2023)与 DSPy 都是这个循环的工程化实现", 12, C.faint, anchor="middle")
f.note(450, 414, "前提:评测集必须能自动判分 —— 没有可靠分数,优化的是噪声而不是提示词", 12, C.faint, anchor="middle")
f.note(450, 440, "每轮成本 = N 次评测调用 + 1 次改写调用;通常 3~5 轮内收敛,之后收益递减", 12, C.faint, anchor="middle")
f.save("fig-meta-prompt")

print("figures_ch007 done")
