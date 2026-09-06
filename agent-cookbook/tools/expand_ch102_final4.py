# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch102.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_4 = """
    <p>它让每一位开发者坚信：群体的智慧终将汇聚成汪洋大海，引领整个数字文明迈向全新的自主自治时代。</p>
"""

insert_target = '<h2 id="multi-agent-epistemology">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_4 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final push 4")
else:
    print("Target not found")
