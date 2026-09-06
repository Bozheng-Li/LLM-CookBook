# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch098.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_2 = """
    <p>回顾现代计算机科学奠基人阿兰·图灵（Alan Turing）在 1950 年的旷世预言：“我们只能看到前方不远处的有限景致，但那里有数不尽的伟业正等待着我们去创造与开拓。”智能体理论探索的征程才刚刚拉开帷幕，真理的殿堂永远属于那些敢于在复杂未知中坚守理性、求真务实的勇敢探索者。</p>
"""

insert_target = '<div class="callout note">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_2 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final push 2 to ch098.html")
else:
    print("Target not found")
