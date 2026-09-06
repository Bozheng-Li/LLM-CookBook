# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch104.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_5 = """
    <p>它让每一位开发者和研究者坚信：科技的真正伟力，正在于让智慧从虚拟走向现实、让梦想化为触手可及的灿烂黎明。</p>
"""

insert_target = '<h2 id="embodied-epistemology-summary">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_5 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final push 5")
else:
    print("Target not found")
