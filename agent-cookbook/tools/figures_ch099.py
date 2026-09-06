# -*- coding: utf-8 -*-
"""figures_ch099.py — ch099 基础架构与认知演进经典论文研读 插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# fig 99-1: 基础架构四大奠基性论文认知演进脉络
f = F(940, 420)
# 节点 1: Transformer
f.box(40, 60, 180, 110, "1. Transformer\nVaswani et al. (2017)\n• 自注意力机制 (Self-Attention)\n• 奠定全并行序列表征", fill=C.blue_s, stroke=C.blue)
# 节点 2: ReAct
f.box(260, 60, 180, 110, "2. ReAct 范式\nYao et al. (2022)\n• 思考与行动协同 (Thought-Action)\n• 打破推理与工具隔离", fill=C.indigo_s, stroke=C.indigo)
# 节点 3: Reflexion
f.box(480, 60, 180, 110, "3. Reflexion 反思\nShinn et al. (2023)\n• 语言强化学习 (Verbal RL)\n• 记忆缓冲与自我纠错", fill=C.amber_s, stroke=C.amber)
# 节点 4: Generative Agents
f.box(700, 60, 200, 110, "4. 斯坦福小镇\nPark et al. (2023)\n• 记忆流 (Memory Stream)\n• 检索、反思与长程规划", fill=C.teal_s, stroke=C.teal)

f.arrow(220, 115, 260, 115, "结构基石")
f.arrow(440, 115, 480, 115, "闭环反馈")
f.arrow(660, 115, 700, 115, "社会性涌现")

# 底部演进核心线索
f.box(100, 290, 740, 100, "认知演进的三大范式跃迁 (Paradigm Shifts in Agent Cognition)\n• 从静态模式匹配到动态交互闭环: Transformer 赋予表达能力，ReAct 赋予与现实握手的环境交互接口\n• 从前向开环执行到自省反馈迭代: Reflexion 将失败堆栈转化为语言标量反馈，突破单向生成的脆弱性\n• 从孤立单体决策到多智能体社会模拟: 斯坦福小镇验证了长时程情景记忆与社交感染力在硅基世界的涌现", fill=C.purple_s, stroke=C.purple)

f.save("fig-foundational-papers-evolution")

# fig 99-2: ReAct 与仅推理 (Reason-only) 及仅行动 (Act-only) 的对比拓扑
f = F(940, 360)
f.box(60, 100, 220, 150, "仅推理 (Reason-only / CoT)\n• 纯内部自言自语\n• 缺乏外部观察输入\n• 极易产生事实幻觉\n• 无法感知外部环境变动", fill=C.red_s, stroke=C.red)

f.box(360, 100, 220, 150, "仅行动 (Act-only)\n• 机械调用工具接口\n• 缺乏目标分解与规划\n• 试错成本极高\n• 无法在错误后反思归因", fill=C.amber_s, stroke=C.amber)

f.box(660, 100, 220, 150, "ReAct 协同模式 (Thought+Act)\n• 思考指导行动参数决策\n• 行动观察校正内部思考\n• 动静相宜，大幅抑制幻觉\n• 任务达成率实现倍增突破", fill=C.green_s, stroke=C.green)

f.arrow(280, 175, 360, 175, "融合")
f.arrow(580, 175, 660, 175, "协同跃迁")

f.save("fig-react-vs-baselines")
print("ch099 figures generated successfully")
