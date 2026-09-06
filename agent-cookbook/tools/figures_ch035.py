# -*- coding: utf-8 -*-
"""figures_ch035.py — ch035 低代码光谱插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

f = F(960, 380)
f.text(480, 32, "低代码光谱:从纯画布到纯代码", 17, C.ink, 800)
f.arrow(70, 120, 890, 120, color=C.faint, sw=2, both=True)
f.text(80, 100, "纯画布", 12.5, C.teal, 800, anchor="start")
f.text(880, 100, "纯代码", 12.5, C.amber, 800, anchor="end")
stops = [
    ("Coze\n渠道Bot", 170, C.teal),
    ("Dify\n知识库应用", 300, C.blue),
    ("Flowise\n链式实验", 420, C.purple),
    ("n8n+自定义\nAPI 节点", 560, C.indigo),
    ("混合形态\n平台做壳\n代码做芯", 680, C.indigo),
    ("LangGraph /\n自研运行时", 810, C.amber),
]
for label, x, colr in stops:
    f.raw('<circle cx="%d" cy="120" r="9" fill="%s"/>' % (x, colr))
    for i, ln in enumerate(label.split("\n")):
        f.text(x, 152 + i * 15, ln, 11, colr, 700)
# 实用区
f.raw('<rect x="500" y="70" width="230" height="14" rx="7" fill="%s" opacity="0.6"/>' % C.indigo_s)
f.text(615, 64, "最宽实用区", 11, C.indigo_d, 700)
f.note(480, 250, "混合形态: 流程编排/渠道/权限面板交给平台; 检索策略/业务规则/高危闸门封装为自己的 API 节点", 12.5, C.ink, 600)
f.note(480, 290, "毕业路径内置: 复杂度上涨时,逻辑逐步从画布搬进芯; 壳永远可换,芯是资产", 12.5, C.soft)
f.note(480, 340, "对照第26章: 业务逻辑写成纯函数不 import 框架 —— 同一条纪律的低代码版", 12, C.faint)
f.save("fig-lowcode-spectrum")
print("done")
