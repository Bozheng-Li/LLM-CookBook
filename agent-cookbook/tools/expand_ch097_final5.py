# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch097.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_5 = """
    <p>它让每一行写入记忆的代码、每一个被吸收沉淀的技能，都成为构筑超级智能永恒基石的坚固力量。</p>
"""

insert_target = '<h2 id="continual-learning-epistemology">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_5 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final push 5")
else:
    print("Target not found")
