# -*- coding: utf-8 -*-
"""figures_ch078.py — ch078 Agent 经济学插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# ---- fig 78-1: 成本、延迟、质量不可能三角 ----
f = F(940, 420)
f.text(470, 32, "Agent 经济学的「不可能三角」与权衡平衡", 18, C.ink, 800)

# 三角形三顶点
f.raw('<polygon points="470,80 180,320 760,320" fill="none" stroke="%s" stroke-width="2.5" stroke-dasharray="6 4"/>' % C.line)

# 顶点标注
p_q = f.box(370, 60, 200, 60, "卓越质量 (Quality)", "长链思考 · 多路采样 · 深度自省", fill=C.teal_s, stroke=C.teal)
p_c = f.box(80, 290, 200, 60, "极低成本 (Cost)", "小模型 · 严格截断 · 批量异步", fill=C.amber_s, stroke=C.amber)
p_l = f.box(660, 290, 200, 60, "极速响应 (Latency)", "单步流式 · 贪婪解码 · 缓存命中", fill=C.indigo_s, stroke=C.indigo)

# 边的权衡
f.text(250, 180, "高昂资费账单\n(如 o3 多重前瞻)", 11, C.red, 700)
f.text(690, 180, "重型流水线延迟\n(如 Deep Research)", 11, C.red, 700)
f.text(470, 345, "能力缩水与格式失真 (低端小模型单步)", 11, C.red, 700)

f.note(470, 395, "架构师的核心职责: 不存在全拿的银弹方案，必须依据具体业务形态在三角平面上动态寻优", 11.5, C.indigo_d, anchor="middle")
f.save("fig-agent-trilemma")

# ---- fig 78-2: 多级缓存与模型路由流水线 ----
f = F(940, 380)
f.text(470, 32, "工业级成本优化架构: 缓存分层与级联路由漏斗", 18, C.ink, 800)

r1 = f.box(60, 110, 180, 100, "① 语义缓存 (L1)", "精确/模糊哈希命中\n0 成本 · 5ms 极速", fill=C.teal_s, stroke=C.teal)
r2 = f.box(280, 110, 180, 100, "② 边缘轻量模型 (L2)", "3B~8B 专用小模型\n过滤 60% 基础任务", fill=C.blue_s, stroke=C.blue)
r3 = f.box(500, 110, 180, 100, "③ 旗舰通用模型 (L3)", "Claude 3.7 / GPT-4o\n处理复杂规划与多步", fill=C.indigo_s, stroke=C.indigo)
r4 = f.box(720, 110, 160, 100, "④ 推理增强核心 (L4)", "o3 / DeepSeek-R1\n仅攻坚最高危难关", fill=C.purple_s, stroke=C.purple)

f.arrow(240, 160, 280, 160, "未命中", C.soft)
f.arrow(460, 160, 500, 160, "复杂度超阈", C.soft)
f.arrow(680, 160, 720, 160, "高危攻坚", C.soft)

f.note(470, 270, "阶梯漏斗效应: 80% 的高频简单流量在 L1/L2 被极低成本截流，仅有 5% 的深水区任务触达高昂的 L4 推理层", 11.5, C.indigo_d, anchor="middle")
f.note(470, 305, "综合成本收益: 整体系统平均调用成本降低 75%~85%，同时维持媲美全量旗舰模型的顶级交付质量", 11.5, C.faint, anchor="middle")
f.save("fig-cost-funnel")
