# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch108.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

extra_push = """
    <p>这种以图谱为核心的长期认知积累，将帮助我们在面对底层算力更迭、算法范式迁移以及开发工具链演进时，始终保持泰山崩于前而色不变的技术从容与敏锐判断。</p>
"""

target = '<section class="refs">'
if target in text:
    new_text = text.replace(target, extra_push + "\n" + target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added extra push")
