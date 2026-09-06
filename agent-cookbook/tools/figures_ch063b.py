# -*- coding: utf-8 -*-
"""figures_ch063b.py — ch063 引用核对流水线插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

f = F(940, 380)
f.text(470, 32, "引用核对流水线:让每个主张可追溯", 18, C.ink, 800)
b1 = f.box(60, 100, 170, 110, "① 主张抽取", "把回答拆成\n原子事实主张", fill=C.indigo_s, stroke=C.indigo)
b2 = f.box(290, 100, 180, 110, "② 来源核对", "每个主张找出处:\n检索结果/知识库", fill=C.teal_s, stroke=C.teal)
b3 = f.box(530, 100, 180, 110, "③ 矛盾裁决", "支持 / 矛盾 / 无据\n(NLI 或规则)", fill=C.amber_s, stroke=C.amber)
b4 = f.box(770, 100, 120, 110, "④ 标注输出", "带引用标记\n+ 置信标注", fill=C.purple_s, stroke=C.purple)
f.arrow(230, 155, 290, 155, "", C.soft)
f.arrow(470, 155, 530, 155, "", C.soft)
f.arrow(710, 155, 770, 155, "", C.soft)
f.note(80, 250, "产物分级: [已核实] 支持且可点开出处 · [单源] 只有一个来源 · [无据] 找不到出处 — 降级为「模型认为」")
f.note(80, 276, "成本控制: 核对只在「高风险主张」上做全量(数字/日期/专名/因果), 低风险主张批量抽检")
f.note(80, 310, "与第57章Judge的分工: 核对流水线查「可验证一致性」(客观), Judge评「语义质量」(主观) — 勿混用", 11.5, C.indigo_d)
f.save("fig-citation-pipeline")
