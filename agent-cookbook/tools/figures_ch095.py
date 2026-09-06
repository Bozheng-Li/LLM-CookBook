# -*- coding: utf-8 -*-
"""figures_ch095.py — ch095 世界模型与环境表征：RSSM、Dreamer 与潜空间动力学 插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# fig 95-1: RSSM 递归状态空间模型架构
f = F(940, 420)
# 确定性状态路径
f.box(60, 60, 200, 90, "确定性循环状态\nh_t = f(h_{t-1}, z_{t-1}, a_{t-1})\n(GRU / RNN 状态)", fill=C.blue_s, stroke=C.blue)
f.box(370, 60, 200, 90, "后续循环状态\nh_{t+1} = f(h_t, z_t, a_t)\n(时序因果记忆推进)", fill=C.blue_s, stroke=C.blue)
f.arrow(260, 105, 370, 105, "动作 a_{t-1}")

# 随机状态路径 (先验 vs 后验)
f.box(60, 210, 200, 100, "随机后验状态 (训练时)\nz_t ~ q(z_t | h_t, x_t)\n(结合真实图像 x_t 编码)", fill=C.indigo_s, stroke=C.indigo)
f.box(370, 210, 200, 100, "随机先验状态 (想象时)\n\\hat{z}_{t+1} ~ p(z_{t+1} | h_{t+1})\n(无观测纯梦境推演)", fill=C.purple_s, stroke=C.purple)

f.arrow(160, 150, 160, 210, "输入真实观测 x_t")
f.arrow(470, 150, 470, 210, "脱离物理现实推演")

# KL 散度约束
f.arrow(260, 260, 370, 260, "KL 散度对齐", color=C.red)

# 右侧输出解码与梦境规划
f.box(660, 60, 220, 110, "多任务解码预测头 (Decoders)\n• 重构观测 \\hat{x}_t (像素/文本)\n• 预测即时奖励 \\hat{r}_t\n• 预测折扣延续概率 \\hat{\\gamma}_t", fill=C.amber_s, stroke=C.amber)
f.box(660, 210, 220, 100, "梦境中演员-评论家 (Dreamer)\n• Actor 策略在潜空间推演\n• Critic 利用梦境轨迹训练\n(零真实物理交互成本)", fill=C.green_s, stroke=C.green)

f.arrow(570, 105, 660, 105)
f.arrow(570, 260, 660, 260)

# 底部物理映射
f.box(100, 335, 740, 75, "世界模型三大核心哲学命题 (World Model Triad)\n• 潜空间紧凑表征: 摒弃像素级重构细节，仅保留与控制任务强相关的几何因果因果状态\n• 确定性与随机性解耦: 确定性 h 维护长程历史上下文，随机性 z 刻画物理世界的本质不确定性", fill=C.faint, stroke=C.line)

f.save("fig-rssm-world-model-arch")

# fig 95-2: 现实交互与潜空间梦境轨迹想象对比
f = F(940, 350)
f.box(40, 90, 240, 160, "真实物理环境交互\n(Real Environment Loop)\n• 高昂时间成本 (1秒仅能跑1秒)\n• 物理硬件磨损与安全碰撞风险\n• 样本采样效率极低 (Sample-inefficient)\n(受限于物理因果律)", fill=C.red_s, stroke=C.red)

f.box(350, 90, 240, 160, "潜空间内部梦境生成\n(Latent Imagination Loop)\n• 纯 GPU 矩阵计算 (> 100,000 FPS)\n• 零真实损耗，可模拟高危边缘极端工况\n• 策略在幻象梦境中直接收敛\n(DreamerV1 ~ V3 范式)", fill=C.green_s, stroke=C.green)

f.box(660, 90, 240, 160, "知识迁移至真实物理世界\n(Zero-shot Sim-to-Real)\n• 在梦境中训练成熟的 Policy\n• 直接部署至机器人/桌面 Agent\n• 少量交互数据回流微调世界模型\n(数据飞轮闭环)", fill=C.blue_s, stroke=C.blue)

f.arrow(280, 170, 350, 170, "世界模型训练")
f.arrow(590, 170, 660, 170, "策略物理部署")

f.save("fig-dreamer-latent-imagination")
print("ch095 figures generated successfully")
