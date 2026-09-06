# -*- coding: utf-8 -*-
"""figures_ch093.py — ch093 智能体记忆理论：认知心理学、外挂图谱与工作记忆容量 插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# fig 93-1: 阿特金森-谢弗林三级记忆模型到 LLM 智能体映射
f = F(940, 420)
# 1. 感觉记忆
f.box(40, 70, 160, 120, "1. 感觉记忆\nSensory Memory\n毫秒级离散感知\n未受注意迅速衰退", sub="原始输入 / VDI 视频流", fill=C.blue_s, stroke=C.blue)
# 2. 短期 / 工作记忆
f.box(250, 70, 190, 120, "2. 工作记忆\nWorking Memory\n米勒 7±2 组块限制\n巴德利多成分模型", sub="KV-Cache / 当前 Prompt 窗口", fill=C.indigo_s, stroke=C.indigo)
# 3. 长期记忆
f.box(490, 70, 210, 120, "3. 长期记忆\nLong-term Memory\n无限容量持久化存储\n巩固与外挂图谱表征", sub="向量库 / 语义三元组 / 外部存储", fill=C.purple_s, stroke=C.purple)
# 4. 动作执行与输出
f.pill(820, 130, "动作输出\nAction Output", fill=C.green_s, stroke=C.green)

f.arrow(200, 130, 250, 130, "注意选择 (Attention)")
f.arrow(440, 100, 490, 100, "精细复述与固化 (Encoding)")
f.arrow(490, 160, 440, 160, "线索激活与提取 (Retrieval)")
f.arrow(440, 130, 760, 130)

# 底部艾宾浩斯遗忘曲线与记忆生命周期管理
f.box(100, 280, 740, 110, "认知神经记忆生命周期与外挂图谱拓扑 (Cognitive Memory Lifecycle)\n• 艾宾浩斯遗忘曲线 (Ebbinghaus): 记忆强度随时间指数衰减 R = e^(-t/S)，需周期性间隔复述刷新\n• 图谱知识融合 (Knowledge Graph): 实体-关系-实体 (SPO 三元组) 消除单纯向量相似度的语义断层\n• 工作记忆容量瓶颈: 基于巴德利 (Baddeley) 模型的中央执行系统，动态调度视空画板与语音回路", fill=C.amber_s, stroke=C.amber)

f.save("fig-cognitive-memory-arch")

# fig 93-2: 艾宾浩斯遗忘与记忆衰减指数曲线
f = F(940, 360)
f.pill(120, 70, "原始交互事件发生", fill=C.blue_s, tc=C.blue_d, stroke=C.blue)

f.box(60, 150, 200, 80, "即时高保真快照\nR_0 = 1.0 (完整记忆)\n存放于工作记忆 KV-Cache", fill=C.teal_s, stroke=C.teal)
f.box(310, 150, 200, 80, "无复述自然遗忘\nR(t) = e^(-t/S)\n未被提及的事实逐渐淡化", fill=C.red_s, stroke=C.red)
f.box(560, 150, 220, 80, "外挂图谱间隔强化\n周期性反思与摘要提纯\n稳定性 S 跃升，遗忘减速", fill=C.green_s, stroke=C.green)

f.arrow(120, 95, 160, 150)
f.arrow(260, 190, 310, 190, "时间流逝")
f.arrow(510, 190, 560, 190, "强化触发")

f.pill(850, 190, "永久知识固化\n(Semantic Graph)", fill=C.purple_s, tc=C.purple_d, stroke=C.purple)
f.arrow(780, 190, 800, 190)

f.save("fig-ebbinghaus-memory-decay")
print("ch093 figures generated successfully")
