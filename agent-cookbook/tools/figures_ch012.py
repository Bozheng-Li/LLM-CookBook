# -*- coding: utf-8 -*-
"""figures_ch012.py — 第 12 章插图：退避与令牌桶机制、成本护栏流水线"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# ---- 图 12-2 指数退避与令牌桶（新画） --------------------------------------
f = F(960, 470)
f.text(480, 30, "重试与限流：一对互补的机制", 17, C.ink, 800)
f.text(480, 52, "限流在「发出之前」本地排队，退避在「被打回之后」再试——前者防雪崩，后者保恢复", 12, C.faint)

# 左半：指数退避 + 抖动
f.group(28, 72, 452, 286, "指数退避 + 抖动（收到 429 / 5xx 之后）",
        fill="#ffffff", stroke=C.indigo, label_fill=C.indigo_d, fs=13)
f.elbow([(60, 300), (450, 300)], color=C.faint, sw=1.6)
xs = [78, 128, 200, 306, 428]
labels = ["尝试 1", "尝试 2", "尝试 3", "尝试 4", "放弃/降级"]
for i, (x, lb) in enumerate(zip(xs, labels)):
    colr = C.red if i < 3 else (C.amber if i == 3 else C.gray_s)
    f.raw('<circle cx="%d" cy="300" r="7" fill="%s"/>' % (x, colr))
    f.text(x, 324, lb, 10.5, C.ink, 700)
for i in range(4):
    x1, x2 = xs[i] + 8, xs[i + 1] - 8
    f.arrow(x1, 300, x2, 300, color=C.indigo, sw=1.4)
    f.text((x1 + x2) / 2, 284, ["等 1s", "等 2s", "等 4s", "等 8s"][i], 11.5, C.indigo_d, 700)
f.text(78, 262, "间隔 ×2 指数拉长，抖动防止同步重试", 11, C.faint, 400, anchor="start")
f.box(48, 344, 200, 56, "等待时间公式",
      "min(cap, base*2^n) * U(0.5,1.5)", fill=C.indigo_s, stroke=C.indigo,
      tc=C.indigo_d, fs=12.5, sub_fs=11, mono=True)
f.box(264, 344, 196, 56, "只重试可重试错误",
      "429/500/502/503/超时", fill=C.teal_s, stroke=C.teal,
      tc=C.teal_d, fs=12, sub_fs=11, mono=True)

# 右半：令牌桶
f.group(508, 72, 424, 286, "客户端令牌桶（发出请求之前）",
        fill="#ffffff", stroke=C.teal, label_fill=C.teal_d, fs=13)
f.cylinder(600, 200, 130, 124, "", fill=C.teal_s, stroke=C.teal)
for tx, ty in [(572, 172), (604, 182), (628, 162), (586, 208), (620, 200), (598, 230)]:
    f.raw('<circle cx="%d" cy="%d" r="7.5" fill="%s"/>' % (tx, ty, C.teal))
f.text(600, 282, "桶深 b：突发容量", 11.5, C.teal_d, 700)
f.arrow(512, 122, 548, 152, label="以 r 枚/秒匀速注入", color=C.blue, sw=1.6)
f.text(512, 108, "（对齐 RPM / TPM 配额）", 10.5, C.faint, 400, anchor="start")
f.arrow(700, 200, 862, 200, label="请求先取 1 枚", color=C.indigo, sw=1.8)
f.text(786, 176, "（按成本加权取 n 枚）", 10.5, C.faint)
f.box(700, 240, 214, 52, "桶空 → 本地排队", "而不是把 429 打到服务端", fill=C.amber_s,
      stroke=C.amber, tc=C.amber_d, fs=12.5, sub_fs=10.5)
f.note(706, 318, "平均速率 = r，突发容忍 = b", 11, C.faint, anchor="start")

f.box(28, 376, 904, 56, "一句结论：退避负责「失败后的礼貌」，限流负责「失败前的自觉」——两者都做在客户端",
      "重试不加抖动 = 定时轰炸；限流不留突发 = 吞吐白丢。务必在压测里同时验证两条路径。",
      fill=C.gray_s, stroke=C.line, tc=C.ink, fs=13, sub_fs=11, weight=600)
f.save("fig-retry-bucket")

# ---- 图 12-3 成本核算与预算护栏（新画） ------------------------------------
f = F(960, 430)
f.text(480, 30, "成本核算与预算护栏：先记账，再谈省钱", 17, C.ink, 800)
f.text(480, 52, "usage 是唯一事实来源：每次调用的输入/输出 token 都要落账，护栏才有依据", 12, C.faint)

f.box(40, 88, 168, 76, "① 发起调用前", "预估成本：输入 + max_tokens 输出", fill=C.blue_s, stroke=C.blue, tc=C.blue_d, fs=13, sub_fs=10.5)
f.box(240, 88, 168, 76, "② 响应返回", "读取 usage：prompt / completion", fill=C.indigo_s, stroke=C.indigo, tc=C.indigo_d, fs=13, sub_fs=10.5)
f.box(440, 88, 168, 76, "③ 按价目换算", "输入/输出分列计价，缓存折价", fill=C.teal_s, stroke=C.teal, tc=C.teal_d, fs=13, sub_fs=10.5)
f.cylinder(762, 128, 176, 88, "账本 Ledger", fill=C.teal_s, stroke=C.teal)
f.text(762, 196, "按 request / task / 用户 / 天聚合", 10.5, C.faint)
f.arrow(208, 126, 240, 126, color=C.faint)
f.arrow(408, 126, 440, 126, color=C.faint)
f.arrow(608, 126, 672, 126, color=C.faint)

f.diamond(300, 268, 190, 92, "预算检查\n（余额还够吗？）")
f.arrow(762, 172, 762, 226, color=C.faint)
f.elbow([(762, 226), (762, 268), (395, 268)], color=C.faint)
f.elbow([(205, 268), (124, 268), (124, 164)], color="#16a34a", sw=1.6)
f.text(150, 244, "余量充足 → 继续服务", 11.5, "#166534", 700)

f.box(470, 212, 200, 48, "≥ 80% 预算：告警", "停掉非关键批量任务", fill=C.amber_s, stroke=C.amber, tc=C.amber_d, fs=12.5, sub_fs=10.5)
f.box(470, 286, 200, 48, "≥ 100%：降级", "换小模型 / 缩上下文", fill=C.red_s, stroke=C.red, tc=C.red_d, fs=12.5, sub_fs=10.5)
f.box(710, 212, 214, 48, "熔断：转人工/排队", "写审计日志，禁止静默失败", fill=C.red_s, stroke=C.red, tc=C.red_d, fs=12.5, sub_fs=10.5)
f.arrow(395, 250, 470, 236, color=C.amber, sw=1.5)
f.arrow(395, 280, 470, 304, color=C.red, sw=1.5)
f.elbow([(580, 310), (644, 310), (644, 236), (710, 236)], color=C.red, sw=1.5)

f.note(40, 372, "三层护栏各管一层：单次调用上限（max_tokens）→ 任务预算（一个 Agent 会话的花费上限）→ 全局预算（按用户/按天的熔断线）。", 12, C.ink, anchor="start")
f.note(40, 396, "省钱顺序：缓存命中 → 缩上下文 → 换小模型 → 批处理半价 → 级联路由；组合拳可把成本压低一个量级。", 12, C.soft, anchor="start")
f.save("fig-cost-guardrail")
