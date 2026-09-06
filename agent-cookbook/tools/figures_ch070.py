# -*- coding: utf-8 -*-
"""figures_ch070.py — ch070 游戏仿真 Agent 插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# ---- fig 70-1: Voyager 技能库循环 ----
f = F(940, 420)
f.text(470, 32, "Voyager 循环:自动课程 × 技能库 × 迭代提示", 18, C.ink, 800)
env = f.box(60, 120, 190, 130, "Minecraft 环境", "开放世界探索", fill=C.teal_s, stroke=C.teal)
ag = f.box(370, 120, 200, 130, "Agent (GPT-4)", "代码即动作\n(写 JS 操控行为)", fill=C.indigo_s, stroke=C.indigo)
lib = f.box(700, 120, 190, 130, "技能库", "已验证技能代码\n可检索可组合", fill=C.amber_s, stroke=C.amber)
cur = f.box(370, 300, 200, 80, "自动课程", "按当前状态出下一个目标", fill=C.purple_s, stroke=C.purple, fs=12)
f.arrow(250, 185, 370, 185, "观测", C.soft)
f.arrow(570, 185, 700, 185, "技能入库", C.soft)
f.arrow(700, 220, 570, 220, "复用/组合", C.soft)
f.arrow(570, 150, 250, 150, "动作代码", C.soft)
f.arrow(470, 300, 470, 250, "下一目标", C.soft)
f.elbow([(60, 185), (30, 185), (30, 340), (370, 340)], "环境反馈", C.red, label_pos=2)
f.note(470, 400, "三大件的协同: 课程出「该学什么」→ 环境验证「学没学会」→ 技能库让「学会的永远不丢」— 开放世界无终点学习的完整闭环", 11.5, C.indigo_d, anchor="middle")
f.save("fig-voyager-loop")

# ---- fig 70-2: 世界模型的预测-想象 ----
f = F(940, 380)
f.text(470, 32, "生成式世界模型:在「脑内」预演未来", 18, C.ink, 800)
obs = f.box(60, 150, 150, 90, "当前观测", None, fill=C.teal_s, stroke=C.teal)
wm = f.box(330, 130, 220, 130, "世界模型", "观测+动作 →\n预测下一状态\n(视频/潜变量)", fill=C.indigo_s, stroke=C.indigo)
sim1 = f.box(640, 60, 130, 70, "想象 A", None, fill=C.amber_s, stroke=C.amber, fs=12)
sim2 = f.box(640, 180, 130, 70, "想象 B", None, fill=C.amber_s, stroke=C.amber, fs=12)
sel = f.box(820, 120, 90, 70, "择优", None, fill=C.purple_s, stroke=C.purple, fs=12)
a1 = f.arrow(210, 180, 330, 180, "动作 a₁", C.soft)
a2 = f.arrow(550, 160, 640, 95, "", C.soft)
a3 = f.arrow(550, 200, 640, 215, "", C.soft)
f.arrow(770, 95, 820, 140, "", C.soft)
f.arrow(770, 215, 820, 165, "", C.soft)
f.note(470, 320, "用途: 规划时「脑内试错」(零真实代价) · 仿真数据生成(第69章数据鸿沟的解法之一) · 评估能力(想象中跑评测)")
f.note(470, 350, "关键风险: 幻觉的物理版 — 「想象错了却信了」— 世界模型的保真度验证是前置工程", 11.5, C.red)
f.save("fig-world-model")
