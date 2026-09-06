# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch101.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_7 = """
    <p>这种人机共创的新范式，不仅极大地解放了全球数千万开发人员在低级琐碎样板代码上的精力内耗，更让全人类在探索高深算法与构建宏大软件工程的征途中，拥有了最忠诚、最敏捷的智慧副驾与数字先锋。</p>
"""

insert_target = '<h2 id="software-engineering-epistemology">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_7 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final push 7")
else:
    print("Target not found")
