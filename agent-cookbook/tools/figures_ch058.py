# -*- coding: utf-8 -*-
"""figures_ch058.py — ch058 威胁模型插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# ---- fig 58-1: Agent 攻击面全景 ----
f = F(940, 460)
f.text(470, 32, "Agent 的攻击面:每个箭头都是一道信任边界", 18, C.ink, 800)
core = f.box(370, 180, 200, 110, "Agent 核心", "LLM + 编排 + 记忆", fill=C.indigo_s, stroke=C.indigo)
sur = [
    (70,  80,  C.teal,   "用户输入", "直接注入·社会工程"),
    (330, 60,  C.amber,  "检索内容", "间接注入·网页投毒"),
    (620, 80,  C.blue,   "工具返回", "载荷·数据投毒"),
    (70,  320, C.purple, "记忆/配置", "持久化劫持"),
    (330, 340, C.red,    "多Agent通信", "同伴劫持·A2A注入"),
    (620, 320, C.indigo, "模型/依赖", "供应链投毒"),
]
for x, y, colr, t, d in sur:
    f.box(x, y, 170, 80, t, None, fill=C.white, stroke=colr, fs=12.5)
    f.text(x + 85, y + 62, d, 9.5, C.faint)
    tgt_x = min(max(x + 85, 380), 560)
    if y < 180:
        f.arrow(x + 85, y + 80, tgt_x, 180, "", C.soft)
    else:
        f.arrow(x + 85, y, tgt_x, 290, "", C.soft)
f.note(470, 445, "STRIDE 对照: 伪造(S)=身份冒充 · 篡改(T)=记忆/工具投毒 · 抵赖(R)=动作无审计 · 信息泄露(I)=外泄与越权读取", 11, C.ink, anchor="middle")
f.note(470, 448, "", 11, C.ink, anchor="middle")
f.save("fig-attack-surface")
