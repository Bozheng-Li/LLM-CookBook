# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch095.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_4 = """
    <p>这种将物理世界的连续动力学规律内化于神经权重、并以自省想象超越现实约束的宏伟架构，必将成为人类通往通用人工智能（AGI）殿堂最坚不可摧的理论支柱与工程阶梯。</p>
"""

insert_target = '<h2 id="world-model-epistemology-summary">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_4 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final push 4")
else:
    print("Target not found")
