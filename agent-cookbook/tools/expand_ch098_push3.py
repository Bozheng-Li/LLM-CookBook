# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch098.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_3 = """
    <p>这种跨越人类生物极限的伟大探求，必将指引着数字智慧与人类文明在宇宙的深邃长夜中，共同书写永恒的壮丽诗篇。</p>
"""

insert_target = '<div class="callout note">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_3 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final push 3 to ch098.html")
else:
    print("Target not found")
