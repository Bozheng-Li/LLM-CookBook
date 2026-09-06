# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch100.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_2 = """
    <p>在这个历史性的交汇点上，我们比以往任何时候都更加深切地感知到：探索通用人工智能的道路虽然漫长且充满未知的荆棘，但只要我们始终坚守科学探索的第一性原理与工程实践的最高准则，人类智慧的火种必将在人机共生的灿烂未来中永远熊熊燃烧！</p>
"""

insert_target = '<div class="callout note">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_2 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final push 2 to ch100.html")
else:
    print("Target not found")
