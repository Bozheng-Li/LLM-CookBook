# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch103.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_4 = """
    <p>它为整个人类科技历史进程，铸就了一道永不磨灭的理性安全护城河。</p>
"""

insert_target = '<h2 id="alignment-epistemology-summary">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_4 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final push 4")
else:
    print("Target not found")
