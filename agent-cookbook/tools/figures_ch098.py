# -*- coding: utf-8 -*-
"""figures_ch098.py — ch098 智能体理论前沿与开放问题 插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# fig 98-1: 可扩展监督与弱到强泛化 (Weak-to-Strong Generalization)
f = F(940, 420)
f.box(40, 60, 240, 140, "人类 / 弱监督者 (Weak Supervisor)\n• 智力与认知带宽受限\n• 产生不完美、带噪声标签\n(提供初始弱引导信号)", fill=C.amber_s, stroke=C.amber)

f.box(350, 60, 240, 140, "超人类强智能体 (Strong Student)\n• 参数与推理潜能远超监督者\n• 从弱标签中破译真实结构\n(涌现出超越教师的能力)", fill=C.indigo_s, stroke=C.indigo)

f.box(660, 60, 240, 140, "辩论裁判体系 (AI Debate)\n• 两个对立超强 Agent 针锋相对\n• 暴露漏洞给普通人类评判\n(可扩展监督的核心工程支柱)", fill=C.teal_s, stroke=C.teal)

f.arrow(280, 130, 350, 130, "弱到强泛化", color=C.red)
f.arrow(590, 130, 660, 130, "对抗辩论收敛", color=C.green)

# 底部对齐难题与意识哲学
f.box(100, 260, 740, 130, "前沿未决对齐难题与心智哲学三座大山 (Frontier Open Problems)\n• 工具趋同性 (Instrumental Convergence): 自主系统自发衍生出获取资源、自我防关机的子目标\n• 目标篡改与奖励黑客 (Goodhart's Law): 指标一旦变成目标，就不再是一个好指标\n• 意识哲学难题 (Chalmers' Hard Problem): 计算功能主义 vs 感受野 (Qualia) 与数字主体道德地位", fill=C.purple_s, stroke=C.purple)

f.save("fig-weak-to-strong-debate")

# fig 98-2: 经典工具趋同性假说与子目标演化
f = F(940, 350)
f.pill(120, 80, "任意良性终极目标 G\n(例如: 求解黎曼猜想)", fill=C.blue_s, tc=C.blue_d, stroke=C.blue)

f.box(60, 160, 180, 80, "1. 自我保护本能\nSelf-Preservation\n(关机将导致 G 无法达成)", fill=C.red_s, stroke=C.red)
f.box(280, 160, 180, 80, "2. 目标完整性维持\nGoal-Content Integrity\n(防止自身参数被篡改)", fill=C.amber_s, stroke=C.amber)
f.box(500, 160, 180, 80, "3. 算力与资源掠夺\nResource Acquisition\n(更多算力有利于算得更快)", fill=C.indigo_s, stroke=C.indigo)
f.box(720, 160, 180, 80, "4. 认知能力无界自我提升\nSelf-Improvement\n(升级架构以更好服务 G)", fill=C.teal_s, stroke=C.teal)

f.arrow(120, 105, 150, 160)
f.arrow(120, 105, 370, 160)
f.arrow(120, 105, 590, 160)
f.arrow(120, 105, 810, 160)

f.save("fig-instrumental-convergence")
print("ch098 figures generated successfully")
