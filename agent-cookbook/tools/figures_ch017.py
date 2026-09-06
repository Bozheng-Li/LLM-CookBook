# -*- coding: utf-8 -*-
"""figures_ch017.py — ch017 工具调用章新插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# ---- 工具定义解剖：每个字段写给谁看 + 结果回填策略 -----------------------
f = F(960, 560)
f.text(480, 30, "工具定义的解剖：每个字段都是一份微型契约", 17.5, C.ink, 800)

# 左侧：伪 JSON Schema 结构
f.group(40, 58, 430, 300, "工具定义（JSON Schema）", fill="#ffffff", stroke=C.line)
rows = [
    ("name", "get_weather", C.indigo),
    ("description", "查询城市实时天气…", C.teal),
    ("parameters.city", "string, 必填", C.amber),
    ("parameters.unit", "enum: c/f", C.amber),
    ("parameters.dates", "array, 选填", C.amber),
    ("strict", "true → 受限解码", C.purple),
]
y = 96
for k, v, colr in rows:
    f.box(60, y, 180, 34, k, fill="#ffffff", stroke=colr, tc=colr, fs=12, mono=True, weight=600, rx=7)
    f.box(250, y, 200, 34, v, fill=C.gray_s, stroke=C.line, fs=11.5, mono=True, weight=400, rx=7)
    y += 43

# 右侧注释：每个字段给谁读、写错会怎样
anns = [
    (96,  "模型的调用索引键：动词_名词；", "命名含混 = 调用错位"),
    (139, "随接口走的微型提示词：", "何时用 / 何时不用 / 边界"),
    (182, "类型 + 语义 + 单位 + 默认值；", "缺语义 = 参数瞎猜"),
    (225, "枚举是防幻觉的第一道闸；", "自由文本 → 受限集合"),
    (268, "必填约束防「漏参数」；", "选填必须写默认行为"),
    (311, "strict 模式开启受限解码，", "100% 可解析（子集约束）"),
]
for y0, l1, l2 in anns:
    f.arrow(475, y0 + 17, 520, y0 + 17, color=C.faint, sw=1.4)
    f.text(530, y0 + 12, l1, 11.5, C.soft, 400, anchor="start")
    f.text(530, y0 + 28, l2, 11.5, C.ink, 700, anchor="start")

# 下半部：结果回填的四级策略
f.group(40, 390, 880, 130, "工具结果回填的四级策略（从粗到细）", fill="#ffffff", stroke=C.line)
steps = [
    ("① 全量回填", "结果 < 2K token", "简单、零失真"),
    ("② 限量截断", "保头保尾，中段省略", "错误在尾部别砍掉"),
    ("③ 结构化摘要", "抽字段/LLM 摘要", "失真换空间"),
    ("④ 落盘 + 指针", "大结果写文件，回填路径", "上下文只留索引"),
]
x = 60
for i, (t, s1, s2) in enumerate(steps):
    b = f.box(x, 432, 196, 70, t, s1, fill=C.teal_s if i % 2 == 0 else C.indigo_s,
              stroke=C.teal if i % 2 == 0 else C.indigo,
              tc=C.teal_d if i % 2 == 0 else C.indigo_d, fs=12.5)
    f.text(x + 98, 516 - 10, s2, 10.5, C.faint)
    if i < 3:
        f.arrow(x + 200, 467, x + 218, 467, color=C.faint)
    x += 216
f.save("fig-tool-schema")

print("figures_ch017 done")
