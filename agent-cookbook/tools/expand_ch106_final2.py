# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch106.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_2 = """
    <p>在这个日新月异的技术坐标系中，基座模型不是一成不变的神圣图腾，而是智能体系统不断更换、按需调度的算力引擎。只要架构本身具备足够的解耦度与韧性，任何更新、更强、更便宜的模型诞生，都将瞬间化为整个系统爆发式进化的全新推进剂。</p>
"""

insert_target = '<h2 id="model-selection-epistemology">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_2 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final push 2")
else:
    print("Target not found")
