# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# 图 110-1: 智能体基础面试核心考点五维雷达
f = F(940, 420)
f.box(40, 50, 240, 150, "1. 核心定义与架构范式\n• Agent 与传统 LLM 边界\n• ReAct / Plan-and-Solve\n• 闭环负反馈与感知-动作循环\n• 状态机与工作流编排", fill=C.blue_s, stroke=C.blue)
f.box(340, 50, 260, 150, "2. 提示词工程与指令对齐\n• Few-Shot / In-Context Learning\n• Chain-of-Thought (CoT) 机制\n• 结构化输出与 JSON Mode\n• 幻觉成因与抑制策略", fill=C.indigo_s, stroke=C.indigo)
f.box(640, 50, 260, 150, "3. 工具调用与契约交互\n• Function Calling 协议标准\n• 参数合法性与 Pydantic 校验\n• 工具调用超时与网络重试\n• 确定性降级与 Mock 拦截", fill=C.teal_s, stroke=C.teal)

f.arrow(280, 125, 340, 125, color=C.blue)
f.arrow(600, 125, 640, 125, color=C.indigo)

f.box(80, 250, 780, 140, "4. 记忆与检索系统基石 (Memory & Context Harness)\n• 短期工作记忆与滑动窗口截断 (Sliding Context Window)\n• 长期记忆向量化索引 (RAG: Dense + Sparse 混合检索与重排)\n• 会话状态跨进程持久化 (Redis Checkpointing & Saga 事务状态机)\n• 知识冲突与上下文污染过滤机制", fill=C.purple_s, stroke=C.purple)

f.arrow(160, 200, 160, 250, color=C.blue)
f.arrow(470, 200, 470, 250, color=C.indigo)
f.arrow(770, 200, 770, 250, color=C.teal)

f.save("fig-agent-interview-basic-radar")
print("Saved fig-agent-interview-basic-radar.svg")

# 图 110-2: 面试深度问答“STAR-E”答题工程框架
f2 = F(940, 360)
f2.box(40, 50, 190, 260, "S: Situation (业务场景)\n\n• 业务背景与业务规模\n• QPS 与延迟 SLA 约束\n• 准确率与安全风控目标\n• 算力资源与成本红线", fill=C.gray_s, stroke=C.line)
f2.box(260, 50, 200, 260, "T: Task & Tension (技术矛盾)\n\n• 模型能力与业务确定性冲突\n• 长上下文与显存显卡瓶颈\n• 幻觉输出与容错机制真空\n• 非结构化输出解析抖动", fill=C.amber_s, stroke=C.amber)
f2.box(490, 50, 200, 260, "A: Action & Arch (核心方案)\n\n• 状态图建模与工具解耦\n• 混合检索与两阶段重排\n• AST 白名单与安全防护网\n• 自动化评测回归流水线", fill=C.blue_s, stroke=C.blue)
f2.box(720, 50, 180, 260, "R-E: Result & Epistemology\n\n• 核心业务指标量化收益\n• 线上故障复盘与降级策略\n• 底层数学与理论本质洞悉\n• 方案通用化与反思总结", fill=C.green_s, stroke=C.green)

f2.arrow(230, 180, 260, 180, color=C.indigo)
f2.arrow(460, 180, 490, 180, color=C.amber)
f2.arrow(690, 180, 720, 180, color=C.blue)

f2.save("fig-interview-stare-framework")
print("Saved fig-interview-stare-framework.svg")
