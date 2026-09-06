# -*- coding: utf-8 -*-
"""figures_ch076.py — ch076 长时程 Agent 插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# ---- fig 76-1: 长时程任务的上下文折叠与分层衰减 ----
f = F(940, 420)
f.text(470, 32, "长时程任务的上下文折叠与衰减模型 (Context Folding)", 18, C.ink, 800)

# 历史时间轴
b1 = f.box(60, 100, 200, 110, "遥远历史 (Past Epochs)", "30 步前 / 数小时前\n原始对话与冗余工具日志", fill=C.gray_s, stroke=C.line)
b2 = f.box(370, 100, 200, 110, "近景历史 (Recent Steps)", "最近 3-5 步交互\n保留精准参数与报错输出", fill=C.amber_s, stroke=C.amber)
b3 = f.box(680, 100, 200, 110, "当下焦点 (Active Frame)", "当前子目标与下一步计划\n高频读写的工作区内存", fill=C.teal_s, stroke=C.teal)

f.arrow(260, 155, 370, 155, "", C.soft)
f.arrow(570, 155, 680, 155, "", C.soft)

# 折叠算子
f.raw('<rect x="110" y="250" width="720" height="110" rx="10" fill="#fafaf7" stroke="%s" stroke-dasharray="6 4"/>' % C.line)
f.text(470, 275, "上下文折叠三级压缩算子 (Tiered Compaction)", 13, C.indigo_d, 800)
f.text(470, 300, "① 结构化事实沉淀: 将百行工具输出浓缩为「原子结论清单」并丢弃中间文本", 10.5, C.ink)
f.text(470, 320, "② 意图路线图归档: 保留已完成里程碑的成功证据与未完成任务队列 (第25/46章)", 10.5, C.ink)
f.text(470, 340, "③ 外部化存储外挂: 详细日志刷入持久化数据库，仅在上下文保留可按需检索的索引句柄", 10.5, C.ink)

f.note(470, 395, "核心法则: 上下文长度不随任务物理时间线性增长，必须在长跑中维持「常数级工作内存」", 11.5, C.indigo, anchor="middle")
f.save("fig-context-folding")

# ---- fig 76-2: 状态机 Checkpointing 与断点恢复 ----
f = F(940, 380)
f.text(470, 32, "状态快照 (Checkpointing) 与任务恢复流转", 18, C.ink, 800)

s1 = f.box(60, 110, 160, 90, "阶段 1: 初始化", "加载目标与约束\n生成检查点 0", fill=C.teal_s, stroke=C.teal)
s2 = f.box(280, 110, 180, 90, "阶段 2: 复杂执行", "多步工具调用\n写环境与中间表", fill=C.indigo_s, stroke=C.indigo)
s3 = f.box(520, 110, 180, 90, "阶段 3: 检查点存盘", "持久化状态机快照\n(内存+环境状态)", fill=C.purple_s, stroke=C.purple)
s4 = f.box(760, 110, 130, 90, "阶段 4: 终局交付", "验收通过\n生成报告", fill=C.teal_s, stroke=C.teal)

f.arrow(220, 155, 280, 155, "", C.soft)
f.arrow(460, 155, 520, 155, "", C.soft)
f.arrow(700, 155, 760, 155, "正常推进", C.teal)

# 崩溃与恢复
f.elbow([(610, 200), (610, 270), (370, 270), (370, 200)], "突发异常 / 进程崩溃 / API中断", C.red, label_pos=1)
f.note(470, 315, "断点恢复机制: 从最近合法 Checkpoint 无损重建内存状态机，重放未确认动作，零重复消耗", 11.5, C.red, anchor="middle")
f.note(470, 345, "持久化契约: 包含 (Agent内部状态 + 环境快照ID + 外部API幂等凭证)，三者严格一致方可安全恢复", 11.5, C.ink, anchor="middle")
f.save("fig-checkpoint-recovery")
