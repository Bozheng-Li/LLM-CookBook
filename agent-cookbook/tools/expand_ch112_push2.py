# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch112.html"

with open(path, "r", encoding="utf-8") as f:
    text = f.read()

extra_push = """
    <p>这种将宏观认知架构与微观系统工程深度咬合的顶层设计能力，正是区分平庸调包工程师与世界一流人工智能系统架构师的最本质分水岭。</p>
"""

target = '<section class="refs">'
if target in text:
    new_text = text.replace(target, extra_push + "\n" + target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Extra push applied to ch112")
else:
    print("Target not found")
