# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch104.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_4 = """
    <p>这种由海量多模态数据驱动、由形式化因果规律守护的全新技术体系，必将成为指引人类文明跨向星际探索与深空开发的坚固科技翅膀，在宇宙的壮丽史诗中留下最深邃的印记。</p>
"""

insert_target = '<h2 id="embodied-epistemology-summary">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_4 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final push 4")
else:
    print("Target not found")
