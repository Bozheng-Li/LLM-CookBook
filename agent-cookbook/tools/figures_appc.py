# -*- coding: utf-8 -*-
"""figures_appc.py — 附录C 模板地图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

f = F(960, 380)
f.text(480, 30, "模板库与开发流程的对应关系", 17, C.ink, 800)
stages = [("构建", C.indigo, C.indigo_s, "模板1 通用Agent\n模板2 编码Agent\n模板3 研究子任务\n模板4 客服Agent"),
          ("评测", C.teal, C.teal_s, "模板5 LLM评审\n模板6 事实核查"),
          ("上线", C.amber, C.amber_s, "清单7 工具Schema\n清单8 架构自查")]
x = 60
for name, colr, colr_s, items in stages:
    f.box(x, 70, 250, 46, name + " 阶段", fill=colr_s, stroke=colr, tc=colr, fs=14)
    f.box(x + 20, 140, 210, 130, "", fill="#ffffff", stroke=C.line, rx=10)
    f.mtext(x + 125, 166, items.split("\n"), 11.5, C.ink, 400, 1.75)
    if x < 600:
        f.arrow(x + 252, 93, x + 296, 93, color=C.faint)
    x += 300
f.note(480, 320, "闭环: 上线后的失败样本回流评测集 → 触发模板迭代 → 再过评测 → 再上线(第 13 章评测闭环)", 12, C.faint)
f.note(480, 350, "模板永远配合所处章节的机制知识使用 —— 单独抄模板 = 只拿到鱼,没拿到渔", 12, C.faint)
f.save("fig-template-map")
print("ok")
