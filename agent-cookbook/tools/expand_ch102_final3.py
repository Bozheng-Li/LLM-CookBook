# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch102.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_3 = """
    <p>这种通过严格协议化分工实现智力非线性放大的工程实践，正是通往通用多主体共生文明的最坚实桥梁。</p>
"""

insert_target = '<h2 id="multi-agent-epistemology">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_3 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final push 3")
else:
    print("Target not found")
