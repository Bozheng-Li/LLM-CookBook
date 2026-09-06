# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch097.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_4 = """
    <p>这种在时间之河中保持自我一致性与无限扩展性的宏大理论范式，为我们拉开了迈向真正自主演化通用人工智能系统的序幕，指引着智能体科技跨越静态局限、向着永恒进化的知识之海扬帆远航。</p>
"""

insert_target = '<h2 id="continual-learning-epistemology">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_4 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final push 4")
else:
    print("Target not found")
