# -*- coding: utf-8 -*-
"""figures_ch077.py — ch077 World Models 插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# ---- fig 77-1: Ha & Schmidhuber 经典三要素 ----
f = F(940, 420)
f.text(470, 32, "World Models 经典三要素架构 (Ha & Schmidhuber, 2018)", 18, C.ink, 800)

v = f.box(60, 110, 200, 120, "视觉模型 V (Vision / VAE)", "观测数据 x_t → 隐空间 z_t\n无监督感知表征压缩", fill=C.teal_s, stroke=C.teal)
m = f.box(370, 110, 200, 120, "记忆模型 M (Memory / MDN-RNN)", "z_t + 动作 a_t → 预测 z_{t+1}\n学习世界时空物理流转动力学", fill=C.indigo_s, stroke=C.indigo)
c = f.box(680, 110, 200, 120, "控制器 C (Controller)", "z_t + 隐状态 h_t → 输出动作 a_t\n极简小参数策略网络 (易进化)", fill=C.amber_s, stroke=C.amber)

f.arrow(260, 170, 370, 170, "隐向量 z_t", C.soft)
f.arrow(570, 170, 680, 170, "预测分布 P(z)", C.soft)
f.elbow([(780, 230), (780, 290), (470, 290), (470, 230)], "动作 a_t 反馈", C.red, label_pos=1)

f.raw('<rect x="110" y="330" width="720" height="60" rx="8" fill="#fafaf7" stroke="%s" stroke-dasharray="6 4"/>' % C.line)
f.text(470, 355, "「在梦中训练」(Training in Dreams): 控制器 C 完全脱离真实环境，纯粹在记忆模型 M 虚拟的想象梦境中演化", 11.5, C.indigo_d, 700)
f.text(470, 375, "核心哲学: 感知(V)负责压缩现实，记忆(M)负责推演未来，决策(C)负责驾驭想象", 10.5, C.faint)
f.save("fig-world-model-classic")

# ---- fig 77-2: 隐式 vs 显式世界模型对比 ----
f = F(940, 380)
f.text(470, 32, "显式生成式世界模型 vs 隐式潜在空间模型 (Latent Dynamics)", 18, C.ink, 800)

b1 = f.box(60, 100, 380, 220, "显式生成式 (如 Sora / Genie / Video-WM)", None, fill=C.white, stroke=C.teal)
f.text(250, 130, "显式生成式 (如 Sora / Genie)", 14, C.teal, 800)
for i, ln in enumerate([
    "· 形式: 像素级视频预测 (Pixel-level Diffusion)",
    "· 优点: 人类直观可解释，保真度极高，通用泛化强",
    "· 缺点: 推理算力极其昂贵，像素渲染充满视觉冗余",
    "· 适用: 仿真数据自合成、交互式虚拟环境生成"
]):
    f.text(250, 165 + i * 22, ln, 11, C.ink)

b2 = f.box(500, 100, 380, 220, "隐式潜在模型 (如 DreamerV3 / MuZero / JEPA)", None, fill=C.white, stroke=C.indigo)
f.text(690, 130, "隐式潜在模型 (如 DreamerV3 / JEPA)", 14, C.indigo, 800)
for i, ln in enumerate([
    "· 形式: 任务相关的隐空间状态转移 (Latent Transitions)",
    "· 优点: 零像素生成开销，直击任务因果核心，极速秒级前瞻",
    "· 缺点: 内部向量不可直视，极易发生隐空间坍塌与漂移",
    "· 适用: 复杂物理控制、前瞻式深度搜索规划 (MCTS)"
]):
    f.text(690, 165 + i * 22, ln, 11, C.ink)

f.note(470, 350, "趋同共识: 规划需要隐式极速推演(Dreamer范式)，数据与可解释性需要显式逼真生成(Genie范式)，两者正走向分工融合", 11.5, C.indigo_d, anchor="middle")
f.save("fig-world-model-comparison")
