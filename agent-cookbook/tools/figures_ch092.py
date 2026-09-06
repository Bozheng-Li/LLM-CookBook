# -*- coding: utf-8 -*-
"""figures_ch092.py — ch092 控制论与系统论：反馈控制、自适应与负熵 插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# fig 92-1: 诺伯特·维纳经典控制论与闭环负反馈调节
f = F(940, 420)
f.box(40, 70, 160, 100, "目标设定\nSetpoint r(t)\n期望状态 / 用户 Prompt", fill=C.blue_s, stroke=C.blue)
f.pill(260, 120, "误差比较器\ne(t) = r(t) - y(t)", fill=C.white, stroke=C.red)
f.box(360, 70, 160, 100, "控制器 (Agent 大脑)\nPID / LLM 规划器\n动作控制量 u(t)", fill=C.indigo_s, stroke=C.indigo)
f.box(580, 70, 160, 100, "被控受控对象 (Plant)\n软件系统 / 物理世界\n状态转移受环境扰动", fill=C.amber_s, stroke=C.amber)
f.pill(820, 120, "输出量 y(t)", fill=C.green_s, stroke=C.green)

f.arrow(200, 120, 260, 120)
f.arrow(260, 120, 360, 120)
f.arrow(520, 120, 580, 120)
f.arrow(740, 120, 820, 120)

# 外部不可控环境扰动 d(t)
f.pill(660, 20, "环境外部扰动 d(t)", fill=C.red_s, stroke=C.red)
f.arrow(660, 38, 660, 70)

# 负反馈回路
f.elbow([(820, 140), (820, 230), (260, 230), (260, 140)], label="负反馈传感测量回传回路: 抑制系统偏离，驱动误差 e(t) -> 0", color=C.red, label_pos=1)

# 底部系统论稳态与负熵
f.box(100, 290, 740, 100, "系统论稳态与耗散结构负熵流 (Homeostasis & Negentropy)\n• 薛定谔生命观: 智能体通过不断从环境吸收‘负熵’（有效信息）对抗内部‘熵增’（混乱与幻觉）\n• 普里戈金耗散结构: 远离平衡态的开放系统，通过与外界连续交换物质、能量与信息维持有序\n• 阿什比必要多样性定律: 控制器的内部状态多样性必须大于等于被控环境的扰动多样性", fill=C.purple_s, stroke=C.purple)

f.save("fig-cybernetics-feedback-loop")

# fig 92-2: 阿什比必要多样性定律与状态自适应匹配
f = F(940, 350)
f.box(60, 90, 220, 170, "环境扰动多样性\nVariety(D) = 2^k\n• 网络异常波动\n• 用户输入长尾歧义\n• 系统版本频繁更迭\n(高维物理世界熵增)", fill=C.red_s, stroke=C.red)

f.box(360, 90, 220, 170, "阿什比必要多样性定律\nVariety(R) >= Variety(D)\n唯有多样性才能吸收多样性\n(Law of Requisite Variety)", fill=C.amber_s, stroke=C.amber)

f.box(660, 90, 220, 170, "智能体响应多样性\nVariety(R)\n• 多模态工具调用库\n• 层次化自愈状态机\n• 跨尺度反思与回溯\n(有效控制与稳态维持)", fill=C.green_s, stroke=C.green)

f.arrow(280, 175, 360, 175, "冲击")
f.arrow(580, 175, 660, 175, "匹配控制")

f.save("fig-ashby-requisite-variety")
print("ch092 figures generated successfully")
