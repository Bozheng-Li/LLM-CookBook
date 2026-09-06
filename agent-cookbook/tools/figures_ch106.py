# -*- coding: utf-8 -*-
"""figures_ch106.py — ch106 开源与闭源基础大模型选型指南 插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# fig 106-1: 全球基座模型五大家族全景生态矩阵
f = F(940, 420)
# 1. DeepSeek
f.box(40, 60, 170, 110, "1. DeepSeek 家族\n(V3 / R1)\n• MLA 多头潜注意力\n• DeepSeekMoE 极致性价比\n• 开源满血强化推理 SOTA", fill=C.blue_s, stroke=C.blue)
# 2. Qwen (阿里千问)
f.box(220, 60, 170, 110, "2. Qwen2.5 家族\n(0.5B ~ 72B / Coder)\n• 全尺寸端侧到云端覆盖\n• 中英双语与编码绝对霸主\n• Apache 2.0 极佳商用友好", fill=C.indigo_s, stroke=C.indigo)
# 3. LLaMA (Meta)
f.box(400, 60, 170, 110, "3. LLaMA 3 家族\n(8B / 70B / 405B)\n• 全球开源事实工业标准\n• 生态周边与算子支持最广\n• 纯英文通识与逻辑极强", fill=C.teal_s, stroke=C.teal)
# 4. Claude (Anthropic)
f.box(580, 60, 170, 110, "4. Claude 3.5 系列\n(Sonnet / Haiku)\n• 编码与复杂 Agent 王者\n• 原生 Computer Use 支持\n• 极严指令遵从与长文", fill=C.amber_s, stroke=C.amber)
# 5. GPT (OpenAI)
f.box(760, 60, 140, 110, "5. OpenAI 系列\n(GPT-4o / o1 / o3)\n• 多模态端到端原生\n• o 系列推理开山鼻祖\n• 闭源综合生态最完备", fill=C.purple_s, stroke=C.purple)

# 底部选型权衡坐标轴
f.box(80, 260, 780, 130, "企业级基座模型选型三大平衡支点 (Model Selection Trilemma)\n• 成本与吞吐极限 (Cost-Efficiency): 首选 DeepSeek-V3 / Qwen2.5 (成本仅为闭源旗舰 1/10，支持本地私有化)\n• 复杂编码与电脑操作 (Code & Computer Use): 首选 Claude 3.5 Sonnet / o1 (SWE-bench 与复杂多步工具调用首选)\n• 隐私合规与端侧边缘离线 (Privacy & Edge): 首选 Qwen2.5-Coder-7B / LLaMA-3.1-8B (单张 4090 或手机 NPU 本地断网闭环)", fill=C.faint, stroke=C.line)

f.save("fig-llm-models-landscape")

# fig 106-2: 混合模型动态路由 (Tiered Model Routing) 架构
f = F(940, 350)
f.pill(120, 70, "用户复杂业务请求", fill=C.blue_s, tc=C.blue_d, stroke=C.blue)

f.box(280, 40, 220, 80, "轻量意图分类 / 过滤\n(L0: Qwen-1.5B / GPT-4o-mini)\n成本: $0.05 / 1M\n延迟: < 50ms", fill=C.teal_s, stroke=C.teal)
f.box(560, 40, 220, 80, "标准逻辑任务 / RAG 问答\n(L1: DeepSeek-V3 / Qwen-72B)\n成本: $0.25 / 1M\n综合吞吐极高", fill=C.blue_s, stroke=C.blue)
f.box(560, 160, 220, 80, "高难长程推理 / 复杂重构\n(L2: Claude 3.5 / DeepSeek-R1)\n测试时思考展开\n解决率最高", fill=C.purple_s, stroke=C.purple)

f.arrow(120, 95, 280, 80)
f.arrow(500, 80, 560, 80, "标准任务")
f.arrow(500, 80, 560, 200, "复杂困难任务")

f.pill(850, 140, "成本暴降 80%\n质量提升 25%", fill=C.green_s, tc=C.ink, stroke=C.green)
f.arrow(780, 80, 850, 120)
f.arrow(780, 200, 850, 160)

f.save("fig-tiered-model-routing")
print("ch106 figures generated successfully")
