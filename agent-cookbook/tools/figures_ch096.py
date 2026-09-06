# -*- coding: utf-8 -*-
"""figures_ch096.py — ch096 神经符号 AI 与混合系统 插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# fig 96-1: 神经符号双轨混合推理架构
f = F(940, 420)
# 轨 A: 连接主义神经网络
f.box(40, 60, 360, 200, "连接主义: 连续感知与直觉 (Connectionist)", fill=C.blue_s, stroke=C.blue)
f.pill(120, 110, "大语言模型 / VLM", fill=C.white, stroke=C.blue)
f.pill(300, 110, "连续高维表示 R^d", fill=C.white, stroke=C.indigo)
f.box(60, 160, 320, 70, "• 鲁棒处理非结构化模糊多模态输入\n• 强大的常识泛化与类比联想能力\n• 致命弱点: 幻觉失真、无确定性保证", fill=C.faint, stroke=C.line)

# 轨 B: 符号主义逻辑系统
f.box(540, 60, 360, 200, "符号主义: 严密逻辑与形式约束 (Symbolic)", fill=C.purple_s, stroke=C.purple)
f.pill(620, 110, "一阶谓词逻辑 FOL", fill=C.white, stroke=C.purple)
f.pill(800, 110, "SMT 求解器 (Z3 / Lean)", fill=C.white, stroke=C.teal)
f.box(560, 160, 320, 70, "• 100% 确定性推理、可解释、可审计\n• 严格保证安全约束与公理不变量\n• 致命弱点: 符号落地困难、缺乏容错", fill=C.faint, stroke=C.line)

# 中间桥梁
f.arrow(400, 120, 540, 120, "模糊感知符号化 (Grounding)", color=C.red)
f.arrow(540, 180, 400, 180, "形式化定理反哺约束 (Filter)", color=C.green)

# 底部可微逻辑与程序综合
f.box(100, 290, 740, 100, "神经符号融合四大范式 (Neuro-Symbolic Integration Matrix)\n• 符号作为输入/输出: LLM 生成代码调用 Z3 SMT 求解器 (Program-Aided / PoT)\n• 知识注入训练: 神经符号逻辑网络 (LTN / Logic Tensor Networks), 将一阶谓词损失软化可微\n• 混合认知闭环: 神经网络负责语义假设提出，形式化求解器负责死逻辑一票否决", fill=C.amber_s, stroke=C.amber)

f.save("fig-neuro-symbolic-arch")

# fig 96-2: 逻辑张量网络 (LTN) 软逻辑松弛连续化
f = F(940, 350)
f.box(60, 100, 220, 150, "经典离散一阶谓词逻辑\n• 蕴涵: A -> B\n• 合取: A ∧ B\n• 析取: A ∨ B\n(真值严格取 {0, 1} 二值)", fill=C.red_s, stroke=C.red)

f.box(360, 100, 220, 150, "t-范数软逻辑松弛 (t-norm)\n• Lukasiewicz / Product\n• 软合取: T(x, y) = x * y\n• 软蕴涵: I(x, y) = min(1, 1-x+y)\n(将布尔真值连续化为 [0, 1])", fill=C.indigo_s, stroke=C.indigo)

f.box(660, 100, 220, 150, "端到端可微损失反传\nLoss = 1 - Sat(Knowledge)\n• 知识作为确定性惩罚项\n• 驱动神经网络权重收敛\n(将先验硬公理灌入权重)", fill=C.green_s, stroke=C.green)

f.arrow(280, 175, 360, 175, "数学松弛")
f.arrow(580, 175, 660, 175, "梯度反传")

f.save("fig-ltn-soft-logic-loss")
print("ch096 figures generated successfully")
