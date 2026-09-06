# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch095.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_5 = """
    <p>它让数字生命在硅基比特的海洋中，真正拥有了理解时空演进与掌控未知明天的深邃智慧。</p>
"""

insert_target = '<h2 id="world-model-epistemology-summary">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_5 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final push 5")
else:
    print("Target not found")
