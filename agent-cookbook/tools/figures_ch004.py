# -*- coding: utf-8 -*-
"""figures_ch004.py — 第 4 章插图: 注意力 Q/K/V 软检索 与 KV Cache"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# ---- 图 4-3 注意力的 Q/K/V: 一次软检索 ------------------------------------
f = F(920, 520)
f.text(460, 32, "注意力的 Q·K·V:一次可微分的『软检索』", 17, C.ink, 800)

# 句子条
sent = ["小猫", "追", "毛线球", "因为", "它", "无聊"]
x = 80
tok_cx = {}
for s in sent:
    w = tw(s, 13.5) + 26
    hl = (s == "它")
    f.box(x, 62, w, 38, s, fill=C.amber_s if hl else C.gray_s,
          stroke=C.amber if hl else C.line, tc=C.amber_d if hl else C.ink, fs=13.5)
    tok_cx[s] = x + w / 2
    x += w + 10
f.text(x + 10, 86, "← 以查询词『它』为例", 12, C.amber_d, 700, anchor="start")
f.elbow([(tok_cx["它"], 100), (tok_cx["它"], 124), (175, 124), (175, 148)], color=C.amber, sw=1.6)

# Q 框
f.box(70, 150, 210, 82, "① 查询向量 Q", "『它』想找:我指代的是谁?", fill=C.indigo_s, stroke=C.indigo, tc=C.indigo_d)

# K 列表
f.group(330, 140, 386, 268, "② 与每个词的键 K 打分 → softmax", fill="#ffffff", label_fill=C.soft)
keys = [("小猫", 0.62, C.indigo), ("追", 0.05, C.faint), ("毛线球", 0.18, C.teal),
        ("因为", 0.03, C.faint), ("无聊", 0.12, C.blue)]
ky = 186
for name, p, colr in keys:
    f.box(348, ky, 90, 34, name, fill="#ffffff", stroke=C.line, fs=12.5, weight=600)
    f.raw('<rect x="%d" y="%d" width="%d" height="14" rx="4" fill="%s" opacity="0.82"/>'
          % (452, ky + 10, p * 226, colr))
    f.text(452 + p * 226 + 10, ky + 21, "%.2f" % p, 11.5, C.soft, 700, anchor="start")
    ky += 44
f.arrow(284, 191, 326, 202, color=C.faint, sw=1.6)

# V 框
f.box(736, 178, 158, 186, "③ 值 V 加权混合", fill=C.teal_s, stroke=C.teal, tc=C.teal_d, fs=12.5)
f.mtext(815, 268, ["新表示 ≈", "0.62×[小猫]", "+ 0.18×[毛线球]", "+ …"], 11.5, C.teal_d, 600, 1.6)
f.arrow(718, 271, 734, 271, color=C.faint, sw=1.6)

# 输出框
out = f.box(330, 434, 380, 44, "④『它』的新表示:携带了『小猫』的语义", fill=C.green_s, stroke=C.green, tc="#166534", fs=12.5)
f.elbow([(815, 364), (815, 410), (520, 410), (520, 432)], color=C.faint, sw=1.5)
f.note(60, 458, "注意力权重经 softmax 归一化,", 12, C.faint, anchor="start")
f.note(60, 476, "按权重混合所有词的 V。", 12, C.faint, anchor="start")
f.note(460, 504, "每个词都对全句各做一次;多头注意力 = 并行多组 Q/K/V,各自学习不同的关系模式", 12, C.faint, anchor="middle")
f.save("fig-attention-qkv")

# ---- 图 4-4 KV Cache ----------------------------------------------------------------
f = F(920, 430)
f.text(460, 32, "KV Cache:用显存换时间的『增量生成』", 17, C.ink, 800)

# 左上: 无缓存
f.group(50, 58, 410, 170, "无缓存:每生成 1 个 Token,历史全部重算", fill="#ffffff", label_fill=C.red_d)
rows_nc = [("调用 1", 70, "算 T1"), ("调用 2", 140, "算 T1 T2"), ("调用 3", 210, "算 T1 T2 T3")]
yy = 100
for label, w, desc in rows_nc:
    f.text(72, yy + 13, label, 12, C.ink, 600, anchor="start")
    f.raw('<rect x="138" y="%d" width="%d" height="18" rx="5" fill="%s" opacity="0.75"/>' % (yy, w, C.red))
    f.text(138 + w + 10, yy + 14, desc, 11.5, C.soft, 600, anchor="start")
    yy += 40
f.text(255, 218, "前缀被一遍遍重复计算 → 浪费", 11.5, C.red_d, 700)

# 左下: 有缓存
f.group(50, 246, 410, 152, "有 KV Cache:历史的 K/V 存显存,只算新 Token", fill="#ffffff", label_fill=C.teal_d)
rows_c = [("调用 2", 44, "只算 T2 · 复用 K1"), ("调用 3", 44, "只算 T3 · 复用 K1 K2")]
yy = 288
for label, w, desc in rows_c:
    f.text(72, yy + 13, label, 12, C.ink, 600, anchor="start")
    f.raw('<rect x="138" y="%d" width="%d" height="18" rx="5" fill="%s" opacity="0.8"/>' % (yy, w, C.green))
    f.text(138 + w + 10, yy + 14, desc, 11.5, C.soft, 600, anchor="start")
    yy += 40
f.raw('<rect x="230" y="352" width="200" height="40" rx="8" fill="%s" stroke="%s"/>' % (C.teal_s, C.teal))
f.text(330, 376, "缓存: K1 K2 的 K/V", 11.5, C.teal_d, 700)

# 右侧: 代价与启示
f.group(500, 58, 380, 340, "代价与启示", fill="#ffffff")
f.mtext(522, 100, [
    "• 显存 ≈ 0.5 MB / Token(7B 模型",
    "  FP16,量级),随模型规模线性涨",
    "• 32K 上下文 ≈ 16 GB;200K ≈",
    "  100 GB → 必须多卡 / 量化 / GQA",
    "• prefill:一次性算完输入的 K/V,",
    "  可并行,受算力限制",
    "• decode:逐 Token 生成,受显存",
    "  带宽限制(访存瓶颈)",
    "• API 本质无状态 → 多轮对话每轮",
    "  重发全部历史,成本随轮次加速",
    "• Prompt Caching = 服务端替你",
    "  缓存 K/V,命中部分给折扣",
], 12, C.soft, 400, 1.62, anchor="start")
f.note(460, 420, "这就是 Agent 多轮循环成本随步数加速上涨的技术根源 —— 也是第 5 章『Token 经济学』的底层机制", 12, C.faint, anchor="middle")
f.save("fig-kv-cache")

print("figures_ch004 done")
