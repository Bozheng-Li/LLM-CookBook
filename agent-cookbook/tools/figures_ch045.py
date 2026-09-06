# -*- coding: utf-8 -*-
"""figures_ch045.py — ch045 Agent RL 插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *



# ---- fig 45-1: Agent RL 闭环 ----
f = F(940, 400)
f.text(470, 36, "Agent RL 闭环:在环境里学策略", 18, C.ink, 800)

b_env = f.box(60, 100, 210, 130, "环境 Environment", "模拟器 / 沙箱 / 真实站点\n状态 s · 动作空间 A", fill=C.indigo_s, stroke=C.indigo)
b_tr  = f.box(365, 100, 210, 130, "轨迹 τ=(o₁,a₁,r₁,…)", "多步交互完整记录\n成功与失败都是数据", fill=C.amber_s, stroke=C.amber)
b_ag  = f.box(670, 100, 210, 130, "Agent(策略 π)", "LLM + 提示 + 记忆\n观测 o → 动作 a", fill=C.teal_s, stroke=C.teal)

f.arrow(270, 150, 365, 150, "执行动作 aₜ", C.ink)
f.arrow(575, 150, 670, 150, "返回观测 oₜ₊₁", C.ink)
f.elbow([(775, 230), (775, 320), (470, 320)], "奖励 r / 验证信号", C.red, label_pos=1)
f.elbow([(470, 320), (165, 320), (165, 230)], "策略更新 (GRPO/PPO)", C.purple, label_pos=0)
f.note(470, 360, "与单轮 RLVR 的差别:奖励要等整条轨迹跑完才结算——多步延迟回报是 Agent RL 的全部难点来源", 11.5, C.faint, anchor="middle")
f.save("fig-agent-rl-loop")

# ---- fig 45-2: 课程学习难度阶梯 ----
f = F(940, 420)
f.text(470, 34, "课程学习:难度阶梯与升级条件", 18, C.ink, 800)
steps = [
    (60,  310, 250, 80,  "L1 单步任务", C.teal,  "单工具单轮\n查天气 / 单位换算", ">70%"),
    (330, 235, 250, 155, "L2 多步链式", C.amber, "3~8 步·有依赖\n订机票 / 填表单", "30~70%"),
    (600, 160, 280, 230, "L3 长程开放", C.red,   "10+ 步·需探索恢复\n跨页聚合 / 多系统协同", "<30%"),
]
for x, y, w, h, t, colr, sub, pr in steps:
    f.box(x, y, w, h, t, sub, fill=colr + "_s" if isinstance(colr, str) else colr, stroke=colr)
    f.text(x + w/2, y - 12, "通过率 " + pr, 12.5, colr, 800)
f.arrow(312, 330, 330, 315, "", C.soft)
f.arrow(582, 300, 600, 285, "", C.soft)
f.note(470, 405, "升级条件:上一级通过率稳定(均值达标且方差小)——任务太难只产出「全失败」轨迹,组内全同分,GRPO 无梯度", 11.5, C.faint, anchor="middle")
f.save("fig-agent-curriculum")

# ---- fig 45-3: 失败轨迹的三种用法 ----
f = F(940, 380)
f.text(470, 34, "失败轨迹不是废料:三种再利用", 18, C.ink, 800)
b = f.box(60, 90, 200, 110, "失败轨迹池", "执行日志 + 失败步\n错误类型标注", fill=C.red_s, stroke=C.red)
u1 = f.box(360, 50, 230, 90, "① 失败-修正对", "失败段 vs 修复后续跑\n→ 轨迹级 DPO", fill=C.blue_s, stroke=C.blue)
u2 = f.box(360, 165, 230, 90, "② 错误类型课程", "按失败原因聚类\n→ 定向补训与出题", fill=C.teal_s, stroke=C.teal)
u3 = f.box(360, 280, 230, 80, "③ 难例回炉", "多次失败的任务\n→ 加回训练分布加权", fill=C.purple_s, stroke=C.purple)
f.arrow(260, 110, 360, 95, "", C.soft)
f.arrow(260, 145, 360, 195, "", C.soft)
f.arrow(260, 180, 360, 315, "", C.soft)
f.box(660, 90, 220, 260, "反例:直接拿失败轨迹\n做 SFT(负示范)", "模型学会的是「如何体面地失败」\n而不是如何成功——失败数据\n必须先转为对比信号或课程信号", fill="#ffffff", stroke=C.faint, dash="5 4")
f.save("fig-agent-failure-reuse")
