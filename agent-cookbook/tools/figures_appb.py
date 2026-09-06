# -*- coding: utf-8 -*-
"""figures_appb.py — 附录B 排错决策树"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

f = F(940, 480)
f.text(470, 30, "排错元流程:先看轨迹,再做猜测", 17, C.ink, 800)
sym = f.box(60, 80, 200, 56, "任务失败/行为怪异", "不要先改提示词", fill=C.gray_s, stroke=C.line, fs=13)
step1 = f.box(330, 80, 220, 56, "① 打开完整 Trace", "每步: 看到了什么/被要求/做了什么", fill=C.blue_s, stroke=C.blue, tc=C.blue_d, fs=12.5)
f.arrow(260, 108, 326, 108, color=C.faint)
d1 = f.diamond(700, 108, 220, 80, "哪一步出错?")
f.arrow(550, 108, 588, 108, color=C.faint)
plans = [("规划错: 分解/顺序荒谬", "查系统提示词·目标表达·上下文布局 → 第 18/23 章", C.indigo, C.indigo_s),
         ("行动错: 工具选错/参数错", "查 Schema 描述·few-shot·受约束解码 → 第 8/17 章", C.teal, C.teal_s),
         ("观察缺失: 工具报错/空结果", "查工具实现·超时·错误回填是否可行动 → 第 15/12 章", C.amber, C.amber_s)]
y = 190
for t, fix, colr, colr_s in plans:
    f.box(120, y, 330, 56, t, fill=colr_s, stroke=colr, tc=colr, fs=12.5)
    f.text(470, y + 33, fix, 12, C.soft, 400, anchor="start")
    f.elbow([(700, 148), (700, y + 28), (456, y + 28)], color=C.faint, sw=1.4)
    y += 72
f.box(120, y, 330, 52, "修复后: 失败样本 → 评测集", "把事故变成资产,永不再犯", fill=C.green_s, stroke=C.green, tc="#166534", fs=12.5)
f.elbow([(285, 190 + 3 * 72 - 72 + 56), (285, y - 2)], color=C.green, sw=1.6)
f.note(470, y + 80, "单点修复 ≠ 完成: 每次排错都应产出 ①评测样本 ②预防性规则(提示词/CI) 二者之一,最好都有", 12, C.faint)
f.save("fig-troubleshoot-flow")
print("ok")
