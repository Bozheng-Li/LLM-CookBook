# -*- coding: utf-8 -*-
"""figures_ch057.py — ch057 LLM-as-Judge 插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# ---- fig 57-1: 三种偏差 ----
f = F(940, 400)
f.text(470, 32, "Judge 的三种系统性偏差与校正", 18, C.ink, 800)
cells = [
    (60,  80, 260, 200, C.red,    "位置偏差", "偏好 A/B 中的特定位置\n(通常偏爱先出现的)", "校正: 双向评两次\n取一致或均值"),
    (340, 80, 260, 200, C.amber,  "长度偏差", "偏好更长的回答\n(把啰嗦当详实)", "校正: 长度分层比较\n+ 长度惩罚项"),
    (620, 80, 260, 200, C.purple, "自我偏好", "偏好自己的风格/输出\n(同源模型的偏爱)", "校正: 异源裁判\n(不同家族的模型)"),
]
for x, y, w, h, colr, t, d, fix in cells:
    f.box(x, y, w, h, t, None, fill=C.white, stroke=colr, fs=14)
    f.text(x + w/2, y + 40, d.split("\n")[0], 11, C.ink)
    f.text(x + w/2, y + 58, d.split("\n")[1], 11, C.ink)
    f.text(x + w/2, y + 100, "校正:", 11, colr, 800)
    f.text(x + w/2, y + 122, fix.split("\n")[0], 11, C.indigo_d)
    f.text(x + w/2, y + 140, fix.split("\n")[1], 11, C.indigo_d)
f.note(470, 320, "偏差检测的通用方法: 换位/换序/换裁判后重评 — 前后一致性低于 80% 即偏差存在, 需启用对应校正", 11.5, C.ink, anchor="middle")
f.note(470, 348, "底线认知: Judge 是「有偏差的测量仪器」— 校正能让它可用, 但永远别把它当真值", 11.5, C.indigo_d, anchor="middle")
f.save("fig-judge-bias")

# ---- fig 57-2: 多裁判裁决流程 ----
f = F(940, 380)
f.text(470, 32, "多裁判裁决:一致性与仲裁", 18, C.ink, 800)
j1 = f.box(70, 100, 160, 80, "裁判 A", "强模型", fill=C.indigo_s, stroke=C.indigo)
j2 = f.box(70, 220, 160, 80, "裁判 B", "异源模型", fill=C.teal_s, stroke=C.teal)
j3 = f.box(70, 150, 160, 80, "裁判 C", "规则判分", fill=C.amber_s, stroke=C.amber)
ag = f.box(400, 160, 160, 90, "一致性检查", None, fill=C.white, stroke=C.ink)
ar = f.box(680, 100, 200, 70, "一致 (≥2/3)", "采纳多数", fill=C.teal_s, stroke=C.teal)
hu = f.box(680, 240, 200, 70, "分歧", "人工仲裁 + 入校准集", fill=C.red_s, stroke=C.red)
f.arrow(230, 140, 400, 185, "", C.soft)
f.arrow(230, 260, 400, 225, "", C.soft)
f.arrow(230, 190, 400, 205, "", C.soft)
f.arrow(560, 185, 680, 140, "", C.soft)
f.arrow(560, 225, 680, 270, "", C.soft)
f.note(470, 350, "校准集闭环: 人工仲裁的结论回流为「裁判的训练/少样本示例」— 裁判随业务共同进化 (第46章判别器纪律的评测版)", 11.5, C.faint, anchor="middle")
f.save("fig-judge-ensemble")
