# -*- coding: utf-8 -*-
"""figures_ch049.py — ch049 Self-Play 与持续学习插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# ---- fig 49-1: Self-Play 的三种形态 ----
f = F(940, 400)
f.text(470, 32, "Self-Play 的三种形态:从对抗到自问自答", 18, C.ink, 800)
# 形态一: 对抗
f.group(50, 70, 260, 270, "① 对抗式")
a1 = f.box(90, 130, 80, 60, "提案者", None, fill=C.indigo_s, stroke=C.indigo, fs=12)
a2 = f.box(190, 130, 80, 60, "解题者", None, fill=C.teal_s, stroke=C.teal, fs=12)
f.arrow(170, 145, 190, 145, "出题", C.soft)
f.arrow(190, 175, 170, 175, "求解", C.soft)
f.note(80, 230, "互为环境: 提案者出「刚好能考住」")
f.note(80, 252, "的题, 解题者被迫变强")
f.note(80, 280, "代表: AlphaZero 自弈 · GAN 思想", 11, C.indigo_d)
# 形态二: 轮换
f.group(340, 70, 260, 270, "② 角色轮换式")
b1 = f.box(380, 130, 80, 60, "用户模拟", None, fill=C.amber_s, stroke=C.amber, fs=12)
b2 = f.box(480, 130, 80, 60, "客服Agent", None, fill=C.teal_s, stroke=C.teal, fs=12)
f.arrow(460, 145, 480, 145, "提问", C.soft)
f.arrow(480, 175, 460, 175, "应答", C.soft)
f.note(370, 230, "一人分饰两角: 模型同时扮演")
f.note(370, 252, "用户与助手, 对话即训练数据")
f.note(370, 280, "代表: SPIRAL · 对话自博弈", 11, C.indigo_d)
# 形态三: 自问自答
f.group(630, 70, 260, 270, "③ 自问自答式")
c1 = f.box(670, 130, 80, 60, "出题头", None, fill=C.purple_s, stroke=C.purple, fs=12)
c2 = f.box(770, 130, 80, 60, "解题头", None, fill=C.teal_s, stroke=C.teal, fs=12)
f.arrow(750, 145, 770, 145, "问题", C.soft)
f.arrow(770, 175, 750, 175, "答案", C.soft)
f.note(660, 230, "同一模型两个「人格」:")
f.note(660, 252, "提问器 + 求解器, 可验证域闭环")
f.note(660, 280, "代表: Absolute Zero · AZR", 11, C.indigo_d)
f.note(470, 375, "共同引擎: 「可验证性」让双方都无需人工裁判 — 出题的难度与解题的成长形成正反馈", 11.5, C.faint, anchor="middle")
f.save("fig-selfplay-forms")

# ---- fig 49-2: 持续学习的稳定性-可塑性天平 ----
f = F(940, 380)
f.text(470, 32, "持续学习的天平:稳定性与可塑性的再平衡", 18, C.ink, 800)
# 天平横梁
f.raw('<line x1="470" y1="90" x2="470" y2="120" stroke="%s" stroke-width="3"/>' % C.ink)
f.raw('<line x1="200" y1="120" x2="740" y2="120" stroke="%s" stroke-width="4"/>' % C.ink)
lb = f.box(130, 170, 200, 130, "稳定性 St.", None, fill=C.blue_s, stroke=C.blue)
f.text(230, 200, "保住旧能力", 13, C.blue_d, 800)
for i, ln in enumerate(["· 回放旧任务/数据", "· KL 锚定参考策略", "· 参数正则 (EWC 思想)"]):
    f.text(230, 224 + i * 18, ln, 11.5, C.ink)
rb = f.box(610, 170, 200, 130, "可塑性 Pl.", None, fill=C.red_s, stroke=C.red)
f.text(710, 200, "学会新能力", 13, C.red_d, 800)
for i, ln in enumerate(["· 新任务采样占比", "· 放宽 KL 约束", "· 模块化: 只调 LoRA 分支"]):
    f.text(710, 224 + i * 18, ln, 11.5, C.ink)
f.text(470, 250, "每轮训练配比 = 天平的砝码", 13, C.ink, 700)
f.note(470, 300, "忘旧(catastrophic forgetting) = 稳性不足 · 学不动(rididity) = 塑性不足 · 两者参数共享, 此消彼长", 11.5, C.faint, anchor="middle")
f.note(470, 325, "Agent 域的特殊性: 旧能力是「工具协议」(忘了就全线崩) — 稳性的底线权重比通用模型更高", 11.5, C.faint, anchor="middle")
f.save("fig-stability-plasticity")
