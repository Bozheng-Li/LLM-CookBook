# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch105.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_3 = """
    <p>唯有以开放包容的胸怀拥抱开源生态的繁荣，以严谨务实的工匠精神深耕企业生产现场，我们方能真正驾驭这股前所未有的智能伟力，赋能千行百业的数字化未来。</p>
"""

insert_target = '<h2 id="framework-epistemology-summary">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_3 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final push 3")
else:
    print("Target not found")
