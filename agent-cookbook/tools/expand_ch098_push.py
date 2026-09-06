# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch098.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push = """
    <p>在这个波澜壮阔的历史转折点上，我们比以往任何时候都更加确信：构建安全可信的超级智能体，绝不仅仅是一场追求浮点算力与模型参数规模的工程竞赛，而是一场触及生命本质、心智结构与宇宙秩序的崇高哲学探险。我们写下的每一行严谨代码、推导的每一个形式化公式、设立的每一道安全防护护栏，都在为人类文明平稳跨入人机共生新纪元铺就一块坚不可摧的基石。</p>
"""

insert_target = '<div class="callout note">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final push to ch098.html")
else:
    print("Target not found")
