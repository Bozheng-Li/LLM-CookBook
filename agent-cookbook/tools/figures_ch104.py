# -*- coding: utf-8 -*-
"""figures_ch104.py — ch104 具身智能与多模态世界模型核心论文研读 插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# fig 104-1: 具身智能与多模态世界模型三大里程碑演进
f = F(940, 420)
# 1. PaLM-E
f.box(40, 60, 260, 150, "1. 具身多模态通用大脑: PaLM-E\nDriess et al. (Google 2023)\n• 562B 参数跨模态大一统\n• 连续传感器流 (状态/图像) 词元化\n• 兼备互联网通识与机器人具身操作", fill=C.blue_s, stroke=C.blue)

# 2. RT-2
f.box(340, 60, 260, 150, "2. 视觉-语言-动作三位一体: RT-2\nBrohan et al. (DeepMind 2023)\n• VLA 架构开创之作\n• 物理末端动作离散词元化 (Action Token)\n• 互联网知识向物理现实的涌现迁移", fill=C.indigo_s, stroke=C.indigo)

# 3. Sora / World Simulator
f.box(640, 60, 260, 150, "3. 视频生成式世界模拟器: Sora\nOpenAI (2024)\n• 时空潜补丁 (Spacetime Patches)\n• 扩散 Transformer (DiT 架构)\n• 涌现物理常识与三维几何一致性", fill=C.teal_s, stroke=C.teal)

# 底部演进核心线索
f.box(100, 260, 740, 130, "具身智能与物理世界表征的三重跃迁 (Embodied & World Modeling Triad)\n• 跨模态统一表征 (PaLM-E): 彻底打破文字、视觉与本体感受器壁垒，证明了多模态联合训练不稀释推理\n• 动作即语言词元 (RT-2): 将机械臂 6DoF 物理位姿直接映射为普通文本词表 Token，实现端到端闭环驱动\n• 大规模时空世界模拟 (Sora): 从隐空间动力学演化为包含光影物理、三维连续性与物体持久性的终极因果沙盒", fill=C.amber_s, stroke=C.amber)

f.save("fig-embodied-world-papers")

# fig 104-2: RT-2 动作词元化 (Action Tokenization) 与端到端推理
f = F(940, 360)
f.box(40, 90, 220, 160, "多模态多维输入\n• 摄像头 RGB 图像 x_t\n• 自然语言指令:\n  '把可乐罐移向小狗玩偶'\n(视觉 + 文本跨模态输入)", fill=C.blue_s, stroke=C.blue)

f.box(320, 90, 260, 160, "VLA 通用大模型主干\n(PaLI-X 55B / PaLM-E)\n• 跨模态自注意力特征融合\n• 自回归逐 Token 采样预测\n• 复用海量互联网先验常识", fill=C.indigo_s, stroke=C.indigo)

f.box(640, 90, 260, 160, "物理控制离散词元输出\n`1 128 92 241 180 120 1`\n• 空间位移 (dx, dy, dz)\n• 姿态欧拉角 (droll, dpitch, dyaw)\n• 夹爪开合状态 (gripper_state)", fill=C.green_s, stroke=C.green)

f.arrow(260, 170, 320, 170, "Token 编码")
f.arrow(580, 170, 640, 170, "自回归生成")

f.save("fig-rt2-action-tokenization")
print("ch104 figures generated successfully")
