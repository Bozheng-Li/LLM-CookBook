# -*- coding: utf-8 -*-
"""figures_ch033.py — ch033 MetaGPT 插图"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

f = F(960, 440)
f.text(480, 30, "MetaGPT:软件公司 SOP 的 Agent 化——结构化消息是脊柱", 17, C.ink, 800)

roles = [("产品经理", "输出: PRD\n(结构化文档)", 70, C.blue),
         ("架构师", "输出: 设计文档\n+ 接口列表", 290, C.teal),
         ("工程师×N", "输出: 代码\n(按接口分包)", 510, C.indigo),
         ("QA", "输出: 测试报告", 730, C.amber)]
rb = []
for name, desc, x, colr in roles:
    b = f.box(x, 80, 180, 84, name, desc, fill=C.white, stroke=colr, tc=colr, fs=12.5)
    rb.append(b)
    if x > 70:
        f.arrow(x - 40, 122, x - 4, 122, color=C.faint)

# 消息总线
f.box(200, 240, 560, 60, "共享消息池(订阅机制)", "每个角色只订阅自己「上游角色」的产出 —— 发布/订阅解耦",
      fill=C.indigo_s, stroke=C.indigo, tc=C.indigo_d, fs=12.5)
for b in rb:
    f.elbow([(b["cx"], 164), (b["cx"], 236)], color=C.faint, sw=1.2)

f.note(480, 340, "与对话式协作的本质区别: 角色间交换的是「结构化文档」而非聊天消息", 12.5, C.ink, 600)
f.note(480, 386, "SOP(标准操作程序)把自由度压到最低 → 可预测性最高; 代价: 场景泛化能力弱", 12, C.faint)
f.note(480, 420, "Human 无限轮对话 = 每轮都重新理解; MetaGPT = 一次对齐,全程执行", 12, C.faint)
f.save("fig-metagpt-sop")
print("done")
