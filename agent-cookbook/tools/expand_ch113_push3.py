# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch113.html"

with open(path, "r", encoding="utf-8") as f:
    text = f.read()

push3 = """
    <p>它将时刻提醒我们：心怀对未知的敬畏，脚踏实地写好每一行代码，唯有知行合一方能行稳致远。</p>
"""

target = '<section class="refs">'
if target in text:
    new_text = text.replace(target, push3 + "\n" + target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Push 3 applied")
else:
    print("Target not found")
