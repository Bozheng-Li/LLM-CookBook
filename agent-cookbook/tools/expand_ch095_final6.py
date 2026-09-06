# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch095.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_6 = """
    <p>世界模型的理论突破，正指引着人类科技文明迈向全自主智能的浩瀚星辰大海。</p>
"""

insert_target = '<h2 id="world-model-epistemology-summary">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_6 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final push 6")
else:
    print("Target not found")
