# -*- coding: utf-8 -*-
"""figures_ch008.py — 第 8 章插图: 结构化输出与受约束解码"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# ---- 图 8-2 获取结构化输出的三级阶梯 (新画) ------------------------------
f = F(960, 430)
f.text(480, 32, "获取结构化输出的三级阶梯", 18, C.ink, 800)
f.text(480, 56, "自左向右：可靠性递增、对提示词的依赖递减、留给模型的自由度递减", 12.5, C.faint)

tiers = [
    (40, "① 提示词约定", C.amber, C.amber_s, C.amber_d,
     [("提示词写格式要求", "few-shot 示例 + 输出指令"),
      ("代码解析 + 失败重试", "正则 / json.loads 抢救")],
     "无硬保证 · 兼容一切 API"),
    (350, "② API 级约束", C.indigo, C.indigo_s, C.indigo_d,
     [("JSON Mode / json_schema", "response_format 参数"),
      ("tool_use 强制抽取", "tool_choice 锁定工具")],
     "供应商侧实现 · 云端 API"),
    (660, "③ 引擎级受约束解码", C.teal, C.teal_s, C.teal_d,
     [("Schema → 语法自动机", "GBNF · Outlines · XGrammar"),
      ("逐 Token 概率掩码", "非法 Token 的概率置零")],
     "语法级硬保证 · 本地推理首选"),
]
for x, label, acc, acc_s, acc_d, boxes, foot in tiers:
    f.group(x, 80, 270, 214, label, fill="#ffffff", stroke=acc, label_fill=acc_d)
    for i, (t, s) in enumerate(boxes):
        f.box(x + 20, 112 + i * 76, 230, 60, t, s, fill=acc_s, stroke=acc,
              tc=acc_d, fs=13, sub_fs=10.5)
    f.note(x + 20, 280, foot, 11, C.faint)
for x0 in (312, 622):
    f.arrow(x0, 187, x0 + 34, 187, color=C.faint, sw=1.8, label="更可靠",
            label_fs=10.5, label_dy=-10)

f.box(40, 318, 890, 52,
      "共同底线：语法合法 ≠ 语义正确 —— 生产环境仍需 Pydantic 语义校验 + 错误反馈修复循环",
      fill=C.red_s, stroke=C.red, tc=C.red_d, fs=14)
f.note(480, 408, "选择依据 = 数据价值 × 失败成本 × 部署环境（云端 API 还是自托管引擎），三级阶梯可组合使用",
       12, C.faint, anchor="middle")
f.save("fig-structured-landscape")
