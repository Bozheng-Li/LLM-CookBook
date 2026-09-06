# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch096.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_3 = """
    <p>这种将连续感知经验与确定性逻辑理性熔铸于一体的系统形态，必将照亮下一代通用可信智能体的未来之路。</p>
"""

insert_target = '<h2 id="nesy-epistemology-summary">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_3 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final push 3")
else:
    print("Target not found")
