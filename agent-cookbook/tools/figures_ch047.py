# -*- coding: utf-8 -*-
"""figures_ch047.py — ch047 合成数据工程插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# ---- fig 47-1: 数据飞轮 ----
f = F(940, 420)
f.text(470, 32, "数据飞轮:让训练数据在循环里自我再生", 18, C.ink, 800)
b1 = f.box(60, 110, 180, 110, "① 部署/交互", "生产流量 · 用户任务", fill=C.indigo_s, stroke=C.indigo)
b2 = f.box(290, 110, 180, 110, "② 轨迹采集", "成功/失败/用户反馈", fill=C.teal_s, stroke=C.teal)
b3 = f.box(520, 110, 180, 110, "③ 筛洗与转化", "质检 · 去污染 · 成对构造", fill=C.amber_s, stroke=C.amber)
b4 = f.box(750, 110, 140, 110, "④ 训练迭代", "SFT/DPO/RL", fill=C.purple_s, stroke=C.purple)
f.arrow(240, 150, 290, 150, "", C.soft)
f.arrow(470, 150, 520, 150, "", C.soft)
f.arrow(700, 150, 750, 150, "", C.soft)
# 回路
f.elbow([(820, 220), (820, 320), (470, 320), (470, 260), (150, 260), (150, 220)], "更强模型回到线上", C.red, label_pos=1)
f.text(470, 385, "飞轮的四个轴承: 采集埋点(别等要数据才埋) · 隐私脱敏(第61章) · 质量闸门(劣质数据负收益) · 分布监控(第39章)", 11.5, C.faint, anchor="middle")
f.save("fig-data-flywheel")

# ---- fig 47-2: Evol-Instruct 指令进化 ----
f = F(940, 400)
f.text(470, 32, "Evol-Instruct: 一颗种子长成一片难度分布", 18, C.ink, 800)
seed = f.box(60, 150, 170, 80, "种子指令", "「查一下上周的销售额」", fill=C.teal_s, stroke=C.teal)
evo = [
    (290, 60,  C.blue,   "深化 Deepening", "加约束: 按品类拆分\n只统计退货订单"),
    (290, 160, C.indigo, "广化 Widening", "换域: 同结构换成\n库存周转率分析"),
    (290, 260, C.purple, "推理进化 Reasoning", "加多跳: 对比三周趋势\n归因异常波动"),
    (290, 360-40, C.amber, "组合进化 In-Context", "给示例学格式:\n按业务周报体输出"),
]
for x, y, colr, t, d in evo:
    b = f.box(x, y, 230, 72, t, None, fill=C.white, stroke=colr)
    f.text(x + 115, y - 10, t, 13, colr, 800)
    for i, ln in enumerate(d.split("\n")):
        f.text(x + 115, y + 36 + i * 16, ln, 11, C.ink)
    f.arrow(230, 190, x, y + 36, "", C.soft)
out = f.box(580, 130, 150, 130, "进化语料池", None, fill=C.amber_s, stroke=C.amber)
f.elbow([(520, 96), (620, 96), (620, 130)], "", C.soft)
f.elbow([(520, 196), (580, 196)], "", C.soft)
f.elbow([(520, 296), (620, 296), (620, 260)], "", C.soft)
f.elbow([(520, 356), (640, 356), (640, 260)], "", C.soft)
qa = f.box(780, 130, 120, 130, "回答 +\n校验器", None, fill=C.purple_s, stroke=C.purple)
f.arrow(730, 195, 780, 195, "", C.soft)
f.save("fig-evol-instruct")
