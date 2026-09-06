# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch097.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_3 = """
    <p>与此同时，基于多任务正向迁移（Positive Forward Transfer）的增量泛化机制，使得智能体在攻克全新领域的未知难题时，能够以前所未有的速度触类旁通、借梯登高，形成滚雪球般的智力飞跃循环。</p>
"""

insert_target = '<h2 id="continual-learning-epistemology">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_3 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final push 3")
else:
    print("Target not found")
