# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch097.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_2 = """
    <p>在这个深刻的演化视界中，终身学习不再仅仅是一种被动的防御补丁，而是智能体主动构建世界因果图谱的积极探索机制。无论面对外部知识的爆炸性更迭，还是多变复杂物理环境的非平稳冲击，具备持续适应能力的智能体系统都展现出了无与伦比的生命力与工程韧性。</p>
"""

insert_target = '<h2 id="continual-learning-epistemology">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_2 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final push 2")
else:
    print("Target not found")
