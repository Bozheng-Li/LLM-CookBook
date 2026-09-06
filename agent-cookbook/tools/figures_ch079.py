# -*- coding: utf-8 -*-
"""figures_ch079.py — ch079 可观测性插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# ---- fig 79-1: OpenTelemetry GenAI 调用链树状结构 ----
f = F(940, 420)
f.text(470, 32, "OpenTelemetry GenAI 规范: 树状链路追踪 (Span Hierarchy)", 18, C.ink, 800)

# Root Span
root = f.box(60, 80, 820, 60, "Root Span: gen_ai.workflow (用户总请求 / Agent 执行)", "trace_id=9a4f..., duration=4.2s, total_tokens=3250", fill=C.indigo_s, stroke=C.indigo)

# Layer 1
s1 = f.box(100, 170, 360, 65, "Child Span 1: gen_ai.system (Prompt 渲染与规划)", "duration=450ms, input_tokens=1200", fill=C.teal_s, stroke=C.teal)
s2 = f.box(500, 170, 360, 65, "Child Span 2: gen_ai.agent.step (工具调度决策)", "duration=3500ms, model=claude-3-7", fill=C.amber_s, stroke=C.amber)

# Layer 2 under Span 2
s3 = f.box(530, 260, 320, 55, "Grandchild Span 2.1: gen_ai.tool.call (SQL 检索)", "tool=db_query, latency=82ms", fill=C.purple_s, stroke=C.purple)
s4 = f.box(530, 330, 320, 55, "Grandchild Span 2.2: gen_ai.client.call (最终生成)", "model=claude-3-7, output_tokens=380", fill=C.blue_s, stroke=C.blue)

f.arrow(100, 140, 100, 170, "", C.soft)
f.arrow(500, 140, 500, 170, "", C.soft)
f.arrow(530, 235, 530, 260, "", C.soft)
f.arrow(530, 235, 530, 330, "", C.soft)

f.note(470, 405, "语义约定价值: 统一属性名 (gen_ai.system, gen_ai.request.model 等)，实现跨厂商追踪与监控仪表盘零改造迁移", 11.5, C.indigo_d, anchor="middle")
f.save("fig-otel-trace")

# ---- fig 79-2: Tracing 到在线评测的闭环飞轮 ----
f = F(940, 380)
f.text(470, 32, "可观测性与在线评测飞轮 (Traces to Evaluation Flywheel)", 18, C.ink, 800)

b1 = f.box(60, 110, 170, 110, "① 生产全量采样", "Langfuse / LangSmith\n捕获真实链路数据", fill=C.indigo_s, stroke=C.indigo)
b2 = f.box(280, 110, 170, 110, "② 异常与差评筛选", "用户点踩 / 运行时报错\n高延迟 / 越界消耗", fill=C.red_s, stroke=C.red)
b3 = f.box(500, 110, 170, 110, "③ 淬炼成 Eval 样本", "清洗脱敏入库\n构造黄金测试用例", fill=C.amber_s, stroke=C.amber)
b4 = f.box(720, 110, 160, 110, "④ CI 门禁回归测试", "升级 Prompt/模型\n自动化验收变绿", fill=C.teal_s, stroke=C.teal)

f.arrow(230, 165, 280, 165, "", C.soft)
f.arrow(450, 165, 500, 165, "", C.soft)
f.arrow(670, 165, 720, 165, "", C.soft)

f.elbow([(800, 220), (800, 300), (145, 300), (145, 220)], "安全上线部署 → 闭环进化", C.teal, label_pos=1)

f.note(470, 345, "系统演化法则: 可观测性绝不仅用于死后验尸，更是将每一次线上翻车事故转化为永久免疫力的核心孵化器", 11.5, C.indigo_d, anchor="middle")
f.save("fig-observability-flywheel")
