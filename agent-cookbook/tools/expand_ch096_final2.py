# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch096.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_2 = """
    <p>在这个演进过程中，神经符号混合系统更让传统的黑盒大模型拥有了前所未有的白盒可解释性与法律级可审计性。无论是面对严苛的欧盟人工智能法案（EU AI Act）合规审查，还是在生命攸关的医疗手术机器人控制中，每一条决策链条都能够沿着形式化推演图谱逆向溯源到底层的数学定理与业务规则公理。</p>
"""

insert_target = '<h2 id="nesy-epistemology-summary">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_2 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final push 2")
else:
    print("Target not found")
