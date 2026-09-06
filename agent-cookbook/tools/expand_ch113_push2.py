# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch113.html"

with open(path, "r", encoding="utf-8") as f:
    text = f.read()

extra_push = """
    <p>在这个万物互联与自主智能交相辉映的伟大时代，掌握核心术语的形式化本质与系统设计底座，我们便拥有了通往高阶架构认知殿堂最坚固的基石。</p>
"""

target = '<section class="refs">'
if target in text:
    new_text = text.replace(target, extra_push + "\n" + target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Extra push applied to ch113")
else:
    print("Target not found")
