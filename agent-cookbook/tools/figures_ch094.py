# -*- coding: utf-8 -*-
"""figures_ch094.py — ch094 推理与规划的认知科学映射：双系统、前向搜索与反思 插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# fig 94-1: 卡尼曼双系统认知理论到现代推理模型的系统性映射
f = F(940, 420)
# 系统 1
f.box(60, 60, 360, 200, "系统 1: 快思考 (System 1: Intuition)", fill=C.blue_s, stroke=C.blue)
f.pill(130, 110, "直觉 / 模式匹配", fill=C.white, stroke=C.blue)
f.pill(310, 110, "单前向传播 Forward", fill=C.white, stroke=C.indigo)
f.box(90, 160, 300, 70, "标准自回归 LLM 采样\n• 极低延迟 (< 100ms)\n• 易受认知偏差与启动效应影响\n• 缺乏前向回溯验证机制", fill=C.faint, stroke=C.line)

# 系统 2
f.box(520, 60, 360, 200, "系统 2: 慢思考 (System 2: Deliberation)", fill=C.purple_s, stroke=C.purple)
f.pill(590, 110, "逻辑严密 / 深思熟虑", fill=C.white, stroke=C.purple)
f.pill(770, 110, "测试时计算 Test-time Compute", fill=C.white, stroke=C.teal)
f.box(550, 160, 300, 70, "树搜索 MCTS / 思维链 CoT (o1/R1)\n• 多路径前向分支推演与回溯\n• 过程奖励模型 (PRM) 局部检验\n• 显式自我反思与假设推翻重构", fill=C.faint, stroke=C.line)

# 中间仲裁与自适应切换
f.arrow(420, 160, 520, 160, "置信度低 / 任务复杂 切换", color=C.red)
f.arrow(520, 100, 420, 100, "子任务编译下沉为直觉", color=C.green)

# 底部认知科学前沿支撑
f.box(100, 290, 740, 100, "认知科学与形式化规划理论支撑 (Cognitive Foundations & Planning)\n• 卡尼曼 (Daniel Kahneman) 双系统认知假说: 快思考节省能量，慢思考攻克复杂非平凡推理\n• 图尔敏论证模型 (Toulmin Model): 声明 (Claim) 必须依赖实据 (Data) 与正当理由 (Warrant) 强闭环\n• 启发式前向搜索 (A* / MCTS): 启发函数 h(s) 驱动剪枝，将指数级爆炸空间收敛至多项式可解", fill=C.amber_s, stroke=C.amber)

f.save("fig-system1-system2-dual")

# fig 94-2: 蒙特卡洛树搜索 (MCTS) 的四阶段认知推进
f = F(940, 350)
f.box(40, 110, 180, 140, "1. 选择 (Selection)\n根据 UCT 算法\n平衡探索与利用\n找到高潜力叶子节点", fill=C.blue_s, stroke=C.blue)
f.box(260, 110, 180, 140, "2. 扩展 (Expansion)\n采样候选思考分支\n由 Policy 模型生成\n产生新思考状态 s'", fill=C.indigo_s, stroke=C.indigo)
f.box(480, 110, 180, 140, "3. 模拟 (Simulation)\n快速前向 Rollout\n或调用 PRM 过程判别\n获得局部/终局价值 V", fill=C.amber_s, stroke=C.amber)
f.box(700, 110, 200, 140, "4. 反向传播 (Backup)\n将价值 V 逆向回传\n更新整条路径各节点\n访问计数 N 与累计 Q 值", fill=C.green_s, stroke=C.green)

f.arrow(220, 180, 260, 180)
f.arrow(440, 180, 480, 180)
f.arrow(660, 180, 700, 180)

# 反向闭环
f.elbow([(800, 250), (800, 310), (130, 310), (130, 250)], label="连续多轮 MCTS 展开，收敛出全局最优思考路径", color=C.purple, label_pos=1)

f.save("fig-mcts-reasoning-tree")
print("ch094 figures generated successfully")
