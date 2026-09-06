# -*- coding: utf-8 -*-
"""figures_ch097.py — ch097 终身学习与持续适应 插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# fig 97-1: 稳定性-塑性困境与持续学习三大主流流派
f = F(940, 420)
# 左端: 极端可塑性
f.box(40, 60, 240, 140, "过度塑性 (Plasticity)\n• 极速吸收新任务数据\n• 旧任务权重被剧烈改写覆盖\n• 灾难性遗忘 (Catastrophic Forgetting)", fill=C.red_s, stroke=C.red)
# 右端: 过度稳定性
f.box(660, 60, 240, 140, "过度稳定性 (Stability)\n• 旧任务能力被死锁保护\n• 无法适应环境新分布漂移\n• 学习能力僵死 (Intransigence)", fill=C.blue_s, stroke=C.blue)

# 中间: 帕累托最优平衡
f.pill(470, 130, "帕累托最优平衡\nPareto Frontier", fill=C.green_s, stroke=C.green)
f.arrow(280, 130, 410, 130)
f.arrow(660, 130, 530, 130)

# 下方三大核心流派
f.box(40, 240, 260, 150, "1. 正则化约束 (Regularization)\n• EWC (Fisher 信息矩阵加权)\n• SI (突触智能积分路径)\n保护核心参数不发生大位移", fill=C.amber_s, stroke=C.amber)

f.box(340, 240, 260, 150, "2. 经验回放 (Replay/CLS)\n• 经验池生成式回放 (Dark Exp)\n• 双重记忆系统 (海马体-皮层)\n新旧数据混合防止决策边界侵蚀", fill=C.indigo_s, stroke=C.indigo)

f.box(640, 240, 260, 150, "3. 动态参数隔离 (Architecture)\n• 动态路由 LoRA / MoE 专家\n• 任务专属子网络 (Progressive)\n新任务分配新模块，旧权重冻结", fill=C.purple_s, stroke=C.purple)

f.save("fig-continual-learning-dilemma")

# fig 97-2: EWC 弹性权重整合二次曲面约束
f = F(940, 360)
f.box(60, 100, 220, 150, "任务 A 最优权重参数\n\\theta_A^*\n在任务 A 空间达到极小值\n计算 Fisher 对角元素 F_i", fill=C.blue_s, stroke=C.blue)

f.box(360, 100, 220, 150, "新任务 B 损失梯度拉扯\n\\nabla L_B(\\theta)\n试图将权重拉向\\theta_B^*\n(极易破坏任务 A 的性能)", fill=C.red_s, stroke=C.red)

f.box(660, 100, 220, 150, "EWC 弹性二次惩罚项\n\\sum_i F_i (\\theta_i - \\theta_{A,i}^*)^2\n沿低曲率方向平滑演进\n(兼顾任务 A 与 B 的平衡点)", fill=C.green_s, stroke=C.green)

f.arrow(280, 175, 360, 175, "学习新任务")
f.arrow(580, 175, 660, 175, "弹性约束")

f.save("fig-ewc-fisher-quadratic")
print("ch097 figures generated successfully")
