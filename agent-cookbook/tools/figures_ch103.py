# -*- coding: utf-8 -*-
"""figures_ch103.py — ch103 安全、对齐与治理核心论文研读 插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# fig 103-1: 安全、对齐与防御三大奠基性论著演进
f = F(940, 420)
# 1. Constitutional AI
f.box(40, 60, 260, 150, "1. 宪法人工智能: CAI\nBai et al. (Anthropic 2022)\n• RLAIF: AI 监督 AI\n• 显式原则约束宪法 (Constitution)\n• 自我批判与无害化迭代修正", fill=C.blue_s, stroke=C.blue)

# 2. DPO
f.box(340, 60, 260, 150, "2. 直接偏好优化: DPO\nRafailov et al. (Stanford 2023)\n• 彻底绕开奖励模型 (Reward Model)\n• 解析推导 Bradley-Terry 闭式解\n• 一行隐式交叉熵损失颠覆 PPO", fill=C.indigo_s, stroke=C.indigo)

# 3. Prompt Injection Defense
f.box(640, 60, 260, 150, "3. 间接注入防御: Spotlighting\nHines et al. (Microsoft 2024)\n• 数据与指令信道物理隔离\n• 数据标记染色与带外分隔符\n• 构筑安全生产级免疫屏障", fill=C.teal_s, stroke=C.teal)

# 底部演进核心线索
f.box(100, 260, 740, 130, "安全对齐理论的三重认知飞跃 (Safety & Alignment Triad)\n• 从脆弱人工标注走向原则自律 (CAI): 确立宪法准则，将“安全价值”作为形式化公理固化进模型灵魂\n• 从复杂多阶段强化学习走向闭式解析 (DPO): 用优雅的对偶理论消除 PPO 训练中 PPO 策略塌陷与显存雪崩\n• 从无防备信任走向零信任防御 (Injection Defense): 视所有外部检索输入为不可信敌对数据，建立物理级沙箱隔离", fill=C.amber_s, stroke=C.amber)

f.save("fig-safety-alignment-papers")

# fig 103-2: DPO 对偶映射与解析解推导全景
f = F(940, 360)
f.box(60, 100, 220, 150, "传统 RLHF (PPO 范式)\n1. 训练奖励模型 r_psi(x, y)\n2. 引入 KL 散度约束项\n3. 调度复杂的 PPO 强化学习\n(需要 4 个大模型常驻显存)", fill=C.red_s, stroke=C.red)

f.box(360, 100, 220, 150, "Bradley-Terry 对偶代换\nr*(x, y) = beta * ln(pi(y|x) / pi_ref(y|x))\n将不可导的潜隐奖励 r\n完全用策略概率比率解析代换\n(理论数学破局)", fill=C.indigo_s, stroke=C.indigo)

f.box(660, 100, 220, 150, "直接偏好优化 (DPO 范式)\nL_DPO = -E [ ln sigma( \n  beta ln(pi(y_w) / pi_ref(y_w)) - \n  beta ln(pi(y_l) / pi_ref(y_l)) ) ]\n(稳定、极简、无 PPO 训练崩溃)", fill=C.green_s, stroke=C.green)

f.arrow(280, 175, 360, 175, "数学对偶代换")
f.arrow(580, 175, 660, 175, "闭式解导出")

f.save("fig-dpo-dual-derivation")
print("ch103 figures generated successfully")
