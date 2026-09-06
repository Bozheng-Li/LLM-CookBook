# -*- coding: utf-8 -*-
"""figures_ch091.py — ch091 智能体形式化：MDP、POMDP 与博弈论基础 插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# fig 91-1: 从 MDP 到 POMDP 形式化映射
f = F(940, 420)
# 左侧: 完全可观测 MDP
f.box(60, 60, 360, 200, "完全可观测 MDP (Markov Decision Process)", fill=C.blue_s, stroke=C.blue)
f.pill(120, 120, "状态 State: S_t", fill=C.white, stroke=C.blue)
f.pill(320, 120, "动作 Action: A_t", fill=C.white, stroke=C.indigo)
f.pill(220, 200, "奖励 Reward: R_t", fill=C.white, stroke=C.amber)
f.arrow(170, 120, 270, 120, "策略 π(a|s)")
f.arrow(320, 140, 260, 185, "环境转移 P(s'|s,a)")
f.arrow(180, 185, 120, 140)

# 右侧: 部分可观测 POMDP (带有信念状态与观察函数)
f.box(520, 60, 360, 200, "部分可观测 POMDP (Partially Observable)", fill=C.purple_s, stroke=C.purple)
f.pill(580, 110, "隐藏状态: S_t (隐变量)", fill=C.faint, stroke=C.line)
f.pill(780, 110, "观察 Observation: O_t", fill=C.white, stroke=C.teal)
f.pill(680, 170, "信念状态: b(s) (Belief)", fill=C.white, stroke=C.purple)
f.pill(780, 225, "动作: A_t", fill=C.white, stroke=C.indigo)

f.arrow(640, 110, 720, 110, "发射概率 O(o|s)")
f.arrow(780, 130, 700, 160, "贝叶斯滤波更新")
f.arrow(710, 190, 750, 215, "策略 π(a|b)")

# 底部多智能体博弈论延伸
f.box(100, 290, 740, 100, "从单智能体到多智能体博弈论 (Stochastic Game & Nash Equilibrium)\n• 随机博弈: S_t 下多智能体联合动作 a = (a_1, ..., a_N)，转移概率 P(s' | s, a_1, ..., a_N)\n• 纳什均衡 (Nash): 任意智能体在其他对手策略固定时，单方面偏离无法获得更高期望回报\n• 不完全信息扩展式博弈 (Extensive-form Game): 完美贝叶斯均衡与信念一致性更新", fill=C.amber_s, stroke=C.amber)

f.save("fig-mdp-pomdp-formal")

# fig 91-2: 贝尔曼最优方程与状态价值递归展开
f = F(940, 350)
f.pill(120, 175, "当前状态 V(s)", fill=C.blue_s, tc=C.blue_d, stroke=C.blue)

f.box(280, 80, 180, 80, "动作候选 a_1\nQ*(s, a_1)\n即时奖励 R(s, a_1)", fill=C.indigo_s, stroke=C.indigo)
f.box(280, 190, 180, 80, "动作候选 a_2\nQ*(s, a_2)\n即时奖励 R(s, a_2)", fill=C.amber_s, stroke=C.amber)

f.arrow(170, 165, 280, 120, "max_a")
f.arrow(170, 185, 280, 230, "max_a")

f.box(560, 60, 220, 60, "后续状态 s'_1 (概率 P(s'_1|s,a))\n折现期望 γ V*(s'_1)", fill=C.teal_s, stroke=C.teal)
f.box(560, 130, 220, 60, "后续状态 s'_2 (概率 P(s'_2|s,a))\n折现期望 γ V*(s'_2)", fill=C.teal_s, stroke=C.teal)
f.box(560, 230, 220, 60, "后续状态 s'_3 (概率 P(s'_3|s,a))\n折现期望 γ V*(s'_3)", fill=C.purple_s, stroke=C.purple)

f.arrow(460, 110, 560, 90)
f.arrow(460, 130, 560, 160)
f.arrow(460, 230, 560, 260)

f.pill(850, 175, "递归收敛\nBanach不动点", fill=C.green_s, tc=C.ink, stroke=C.green)
f.arrow(780, 90, 850, 150)
f.arrow(780, 160, 850, 175)
f.arrow(780, 260, 850, 200)

f.save("fig-bellman-optimality-tree")
print("ch091 figures generated successfully")
