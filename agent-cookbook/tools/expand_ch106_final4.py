# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch106.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_4 = """
    <p>它让每一位开发者坚信：掌握了科学选型与成本掌控之道，我们便拥有了通往数字智能星辰大海的最坚固铠甲。</p>
"""

insert_target = '<h2 id="model-selection-epistemology">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_4 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final push 4")
else:
    print("Target not found")
