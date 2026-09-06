# -*- coding: utf-8 -*-
"""figures_ch080.py — ch080 规模化插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# ---- fig 80-1: 工业级 Agent 队列与网关分流架构 ----
f = F(940, 420)
f.text(470, 32, "大规模 Agent 架构: 动态队列、限流与分布式网关", 18, C.ink, 800)

c1 = f.box(60, 110, 160, 90, "流量入口 (Gateway)", "反向代理 · 鉴权\n租户分流 · 幂等校验", fill=C.indigo_s, stroke=C.indigo)
c2 = f.box(280, 110, 180, 90, "优先级队列池", "VIP / 标准 / 批处理\nRedis / Celery / Kafka", fill=C.amber_s, stroke=C.amber)
c3 = f.box(520, 110, 180, 90, "Worker 弹性调度集群", "长跑容器 · 沙箱池\n动态弹性伸缩 (HPA)", fill=C.teal_s, stroke=C.teal)
c4 = f.box(760, 110, 130, 90, "LLM 网关集群", "供应商多活负载均衡\n速率限制 · 故障熔断", fill=C.purple_s, stroke=C.purple)

f.arrow(220, 155, 280, 155, "请求入队", C.soft)
f.arrow(460, 155, 520, 155, "拉取调度", C.soft)
f.arrow(700, 155, 760, 155, "受控调用", C.soft)

# 底部反馈与状态外存
f.raw('<rect x="110" y="250" width="720" height="90" rx="8" fill="#fafaf7" stroke="%s" stroke-dasharray="6 4"/>' % C.line)
f.text(470, 275, "外部持久化状态与分布式锁 (State Store & Distributed Locks)", 12.5, C.indigo_d, 800)
f.text(470, 298, "· PostgreSQL / Redis 维护不可变事件流与状态机快照 (第76章)", 10.5, C.ink)
f.text(470, 318, "· 分布式租约锁保障同一任务单实例执行，杜绝脑裂并发竞态", 10.5, C.ink)

f.note(470, 375, "可靠性三原则: 一切外部请求可排队、一切中间状态可持久化、一切关键操作具备幂等重试保护", 11.5, C.indigo, anchor="middle")
f.save("fig-scaling-gateway")

# ---- fig 80-2: 限流退避与熔断降级阶梯 ----
f = F(940, 380)
f.text(470, 32, "流量过载防护: 自适应限流、指数退避与优雅降级", 18, C.ink, 800)

b1 = f.box(60, 110, 180, 110, "① 令牌桶限流 (429防线)", "严格控制各下游供应商\nRPM / TPM 配额边界", fill=C.teal_s, stroke=C.teal)
b2 = f.box(300, 110, 180, 110, "② 带抖动的指数退避", "Full Jitter Backoff\n消除集群共振重试风暴", fill=C.blue_s, stroke=C.blue)
b3 = f.box(540, 110, 180, 110, "③ 熔断器切流 (Circuit Breaker)", "连续错误超标秒级跳闸\n自动切换多活备用模型", fill=C.amber_s, stroke=C.amber)
b4 = f.box(780, 110, 110, 110, "④ 优雅降级", "关闭思考\n转静态兜底", fill=C.red_s, stroke=C.red)

f.arrow(240, 165, 300, 165, "", C.soft)
f.arrow(480, 165, 540, 165, "", C.soft)
f.arrow(720, 165, 780, 165, "", C.soft)

f.note(470, 260, "抖动退避公式: sleep = min(cap, base * 2^attempt) * random(0, 1) — 彻底打破并发客户端整齐划一的重试雪崩", 11.5, C.faint, anchor="middle")
f.note(470, 290, "终极兜底: 面对大面积外部瘫痪，系统自动收缩外围长链功能，确保核心文本问答与关键业务不中断", 11.5, C.indigo_d, anchor="middle")
f.save("fig-scaling-circuit-breaker")
