# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch107.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_2 = """
    <p>在这个深刻的认知坐标系之下，评测不再是一次性给模型打分的脱机终点，而是指导模型训练、对齐数据清洗与系统提示词演化自愈的持续起点。通过将评测数据流与强化学习环境（RL Environments）深度咬合，系统实现了从“发现弱点”到“靶向自愈进化”的自我闭环飞轮。</p>
"""

insert_target = '<h2 id="eval-engineering-epistemology">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_2 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final push 2")
else:
    print("Target not found")
