# -*- coding: utf-8 -*-
"""figures_ch069.py — ch069 具身智能插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# ---- fig 69-1: VLA 模型架构 ----
f = F(940, 420)
f.text(470, 32, "VLA 模型:视觉-语言-动作的统一序列建模", 18, C.ink, 800)
cam = f.box(60, 100, 170, 110, "视觉输入", "相机帧 / 深度图", fill=C.gray_s, stroke=C.line)
enc = f.box(60, 250, 170, 100, "视觉编码器", "ViT / 专用主干", fill=C.teal_s, stroke=C.teal)
core = f.box(370, 100, 220, 130, "多模态主干", "LLM (语言+视觉 token)\n指令理解 · 任务推理", fill=C.indigo_s, stroke=C.indigo)
dec = f.box(370, 270, 220, 100, "动作解码器", "离散 token / 扩散头", fill=C.amber_s, stroke=C.amber)
act = f.box(740, 150, 150, 130, "机器人", "关节控制\n末端执行器", fill=C.purple_s, stroke=C.purple)
f.arrow(230, 300, 370, 190, "", C.soft)
f.arrow(480, 230, 480, 270, "动作 token", C.soft)
f.arrow(590, 200, 740, 200, "控制指令", C.soft)
lang = f.box(740, 20, 150, 70, "语言指令", "「把杯子放到盘子上」", fill=C.teal_s, stroke=C.teal, fs=12)
f.arrow(815, 90, 815, 150, "", C.soft)
f.note(470, 395, "与 GUI Agent 的同构: 都是「感知→(语言条件化)→动作」— 差别在动作空间(连续/低频/物理不可逆)与数据获取成本", 11.5, C.faint, anchor="middle")
f.save("fig-vla-architecture")

# ---- fig 69-2: 具身的四道鸿沟 ----
f = F(940, 400)
f.text(470, 32, "从数字到物理:具身智能的四道鸿沟", 18, C.ink, 800)
gaps = [
    (60,  100, 400, 120, C.red,   "① 数据鸿沟", "互联网数据≠机器人数据\n真机数据采集极贵(遥操作小时计)"),
    (500, 100, 400, 120, C.amber, "② 实时鸿沟", "LLM 推理秒级 vs 控制毫秒级\n高频闭环需要分层架构"),
    (60,  250, 400, 120, C.purple,"③ 安全鸿沟", "物理动作不可逆(可能伤人)\n安全冗余必须是硬件级"),
    (500, 250, 400, 120, C.teal,  "④ 迁移鸿沟", "仿真到现实(sim2real)\n实验室到千家万户"),
]
for x, y, w, h, colr, t, d in gaps:
    f.box(x, y, w, h, t, None, fill=C.white, stroke=colr, fs=13.5)
    for i, ln in enumerate(d.split("\n")):
        f.text(x + w/2, y + 56 + i * 17, ln, 10.5, C.ink)
f.note(470, 385, "四道鸿沟 = 具身创业公司的「死亡四问」— 每一问的答案决定技术路线与商业模式", 11.5, C.indigo_d, anchor="middle")
f.save("fig-embodied-gaps")
