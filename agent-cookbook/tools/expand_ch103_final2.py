# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch103.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_2 = """
    <p>在这个深刻的时代命题面前，安全对齐已经超越了单一工程学科的范畴，成为了一场融合了数理逻辑、认知科学、法律伦理学与制度经济学的伟大跨学科交响乐。它督促着每一位求索者在追求智力高峰的同时，始终将善意与责任镌刻在每一次反向传播的脉冲之中。</p>
"""

insert_target = '<h2 id="alignment-epistemology-summary">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_2 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final push 2")
else:
    print("Target not found")
