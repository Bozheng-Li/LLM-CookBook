# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch101.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_4 = """
    <p>这种由真实编译器、自动化回归测试与版本控制图谱共同支撑的宏大理论工程体系，正是未来全自动软件工厂（Autonomous Software Factory）运转的核心脉搏，指引着软件工程学在人机协同新纪元谱写出最壮丽的时代交响曲。</p>
"""

insert_target = '<h2 id="software-engineering-epistemology">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_4 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final push 4")
else:
    print("Target not found")
