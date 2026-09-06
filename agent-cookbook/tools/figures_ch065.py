# -*- coding: utf-8 -*-
"""figures_ch065.py — ch065 治理合规插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

f = F(940, 380)
f.text(470, 32, "Agent 事故响应时钟: T+0 到 T+30d", 18, C.ink, 800)
marks = [
    (110, "T+0",    "发现/告警", "快照留证, 会话冻结"),
    (250, "T+10m",  "止血", "降级阶梯上调, 熔断会话"),
    (400, "T+1h",   "定性", "影响面评估, 分级上报"),
    (550, "T+24h",  "初报", "内部干系人, 监管时限评估"),
    (700, "T+7d",   "根因", "防线追问, 修复方案"),
    (860, "T+30d",  "复盘闭环", "矩阵回写, 条款更新"),
]
f.arrow(70, 300, 930, 300, "", C.ink, sw=2.5)
for x, t, name, act in marks:
    f.raw('<circle cx="%d" cy="300" r="7" fill="%s"/>' % (x, C.indigo))
    f.text(x, 282, t, 11.5, C.indigo_d, 800)
    f.text(x, 266, name, 11.5, C.ink, 800)
    for i, ln in enumerate(act.split(", ")):
        f.text(x, 340 + i * 16, ln, 9.5, C.faint)
f.note(470, 226, "时钟的目标不是「快」而是「不跳步」— 每格都有交付物, 缺格的复盘等于没复盘", 11.5, C.faint, anchor="middle")
f.save("fig-incident-clock")
