# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch106.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_3 = """
    <p>这种通过模块化解耦与动态前缀缓存实现算力自由调配的工程实践，正是企业构建下一代高可用、长寿命智能体基础设施的最核心基石与终极底气。</p>
"""

insert_target = '<h2 id="model-selection-epistemology">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_3 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final push 3")
else:
    print("Target not found")
