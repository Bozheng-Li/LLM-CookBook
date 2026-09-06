# -*- coding: utf-8 -*-
"""figures_ch064.py — ch064 对齐与价值观插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# ---- fig 64-1: 对齐的分层架构 ----
f = F(940, 420)
f.text(470, 32, "对齐的分层架构:厂商底色 × 应用层重塑", 18, C.ink, 800)
b1 = f.box(70, 90, 240, 130, "第①层 厂商对齐", "RLHF/RLVR/宪政AI\n价值观的「底色」\n(不可控, 随版本漂移)", fill=C.indigo_s, stroke=C.indigo)
b2 = f.box(350, 90, 240, 130, "第②层 应用层重塑", "系统提示角色定义\n行为准则 · 拒答策略定制\n(可控的补丁层)", fill=C.teal_s, stroke=C.teal)
b3 = f.box(630, 90, 240, 130, "第③层 评测与反馈", "边缘样本门禁\n过度拒绝监控\n投诉归因回流", fill=C.amber_s, stroke=C.amber)
f.arrow(310, 155, 350, 155, "塑造", C.soft)
f.arrow(590, 155, 630, 155, "验证", C.soft)
f.elbow([(750, 220), (750, 300), (190, 300), (190, 220)], "评测结论回流: 准则修订/样本扩充", C.red, label_pos=1)
f.note(470, 350, "三条张力: 有用性↔安全性 · 一致性↔灵活性 · 通用底色↔领域价值 — 应用层的价值在「为你的业务重新排序」", 11.5, C.ink, anchor="middle")
f.note(470, 385, "第②层是本章主战场: 底色改不了, 但「在你的场景里, 什么算好」可以显式定义并被评测", 11.5, C.faint, anchor="middle")
f.save("fig-alignment-layers")

# ---- fig 64-2: 行为准则工程 ----
f = F(940, 400)
f.text(470, 32, "行为准则工程:从价值观到可评测条款", 18, C.ink, 800)
vals = [
    (110, 100, "价值观层", "诚实 · 安全 · 公正\n尊重用户自主权", C.indigo),
    (400, 100, "原则层", "「不确定时说明不确定」\n「高危操作必须确认」", C.teal),
    (690, 100, "条款层", "「金额错误率>0.5%时\n必须提示用户复核」", C.amber),
    (400, 260, "评测层", "每条条款配 5~10 个\n可判分测试样本", C.purple),
]
for x, y, t, d, colr in vals:
    f.box(x, y, 150, 100, t, None, fill=C.white, stroke=colr, fs=13)
    for i, ln in enumerate(d.split("\n")):
        f.text(x + 75, y + 50 + i * 17, ln, 10, C.faint if i > 0 else C.ink)
f.arrow(260, 150, 400, 150, "", C.soft)
f.arrow(550, 150, 690, 150, "", C.soft)
f.arrow(475, 200, 475, 260, "落到可测", C.soft)
f.elbow([(475, 360), (110, 360), (110, 200)], "评测失败 → 条款或样本修订", C.red, label_pos=1)
f.note(470, 395-5, "「不可评测的价值观是装饰」— 条款层是价值观的工程化终点, 评测层是条款的生命线", 11.5, C.indigo_d, anchor="middle")
f.save("fig-values-engineering")
