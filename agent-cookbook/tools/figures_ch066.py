# -*- coding: utf-8 -*-
"""figures_ch066.py — ch066 VLM 插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# ---- fig 66-1: VLM 双塔架构 ----
f = F(940, 420)
f.text(470, 32, "VLM 双塔架构:视觉编码器 × 语言解码器 × 对齐层", 18, C.ink, 800)
img = f.box(60, 100, 180, 130, "图像输入", "截图 / 照片 / 文档", fill=C.gray_s, stroke=C.line)
enc = f.box(60, 270, 180, 100, "视觉编码器", "ViT / CLIP 系", fill=C.teal_s, stroke=C.teal)
prj = f.box(330, 270, 160, 100, "投影层", "视觉→语言\ntoken 空间", fill=C.amber_s, stroke=C.amber)
llm = f.box(560, 270, 170, 100, "语言解码器", "LLM 主干", fill=C.indigo_s, stroke=C.indigo)
out = f.box(800, 270, 100, 100, "输出", "文本/动作", fill=C.purple_s, stroke=C.purple)
f.arrow(150, 230, 150, 270, "", C.soft)
f.arrow(240, 320, 330, 320, "", C.soft)
f.arrow(490, 320, 560, 320, "", C.soft)
f.arrow(730, 320, 800, 320, "", C.soft)
# 对齐训练
f.raw('<rect x="330" y="120" width="400" height="70" rx="10" fill="%s" stroke="%s" stroke-dasharray="6 4"/>' % ("#fafaf7", C.line))
f.text(530, 148, "对齐训练三阶段", 12.5, C.indigo_d, 800)
f.text(530, 172, "① 图文对比预训练 ② 指令微调 ③ 偏好/RLHF", 11, C.ink)
f.note(60, 60, "关键工程量在「投影层」: 视觉特征压缩成多少个视觉 token, 直接决定上下文成本与细节保留的平衡", 11.5, C.ink)
f.note(60, 405, "Agent 视角: VLM 的「眼睛」质量(定位/OCR/空间关系)决定 GUI Agent 的上限 — 第67章的前置", 11.5, C.faint)
f.save("fig-vlm-architecture")

# ---- fig 66-2: 视觉 token 的成本谱系 ----
f = F(940, 380)
f.text(470, 32, "视觉 token 成本谱系:分辨率 × 压缩策略", 18, C.ink, 800)
rows = [
    ("低分辨率 (512px, 全图)", 90,  C.teal,   "~256 tok", "粗布局理解 · 快"),
    ("中分辨率 (1024px, 全图)", 155, C.blue,  "~1k tok",  "常规截图 · 主流默认"),
    ("高分辨率 + 切块 (2k)",   220, C.amber,  "~3-4k tok", "OCR/小按钮 · 贵"),
    ("动态分辨率 (原生比例)",   285, C.purple, "自适应",     "新趋势: 按内容分配预算"),
]
for label, y, colr, tok, note_ in rows:
    f.pill(230, y, label, colr + "_s" if hasattr(C, colr[2:] + "_s") else C.indigo_s, colr, fs=12)
    f.text(560, y + 4, tok, 12, C.ink, 800)
    f.text(780, y + 4, note_, 11, C.faint)
f.note(470, 345, "GUI Agent 的隐性大头: 每步交互都重新截图 = 表征成本 × 交互轮数 — 第52章token账本的视觉面", 11.5, C.ink, anchor="middle")
f.save("fig-vision-tokens")
