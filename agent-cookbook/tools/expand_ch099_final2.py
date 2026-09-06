# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch099.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_2 = """
    <p>在这个信息爆炸的时代，深入精读具有范式转移意义的奠基之作，不仅能够让我们免受各种浅层工业营销包装术语的浮躁喧嚣干扰，更能让我们的工程设计深深扎根于坚不可摧的底层第一性原理之上。经典论文之所以永恒，正是因为它们在混沌未明的黎明破晓时刻，为全人类指明了通往智能本质的坚定航向。</p>
"""

insert_target = '<div class="callout note">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_2 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final push 2 to ch099.html")
else:
    print("Target not found")
