# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch103.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_3 = """
    <p>这种将崇高的人类价值内化为模型底层神经突触本能的伟大努力，必将引领人机共生文明在漫长的岁月星河中，永远航行在正义、和平与智慧的光明航道之上。</p>
"""

insert_target = '<h2 id="alignment-epistemology-summary">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_3 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final push 3")
else:
    print("Target not found")
