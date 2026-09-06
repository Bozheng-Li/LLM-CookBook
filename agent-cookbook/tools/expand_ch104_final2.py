# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch104.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_2 = """
    <p>在这个宏伟的交汇点上，具身物理现实、多模态时空因果与大规模自回归模型完成了全方位的哲学统一。机器人不再是冷冰冰的受控执行部件，而是演进成为能够感知环境细微波动、理解人类深层语义、在虚拟梦境中自我进化，并以优雅物理手足服务人类美好生活的真正智慧伙伴。</p>
"""

insert_target = '<h2 id="embodied-epistemology-summary">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_2 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final push 2")
else:
    print("Target not found")
