import os

path = r"D:/agent-cookbook/chapters/ch094.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_2 = """
    <p>这种在推理时刻不断探索可能世界与反事实路径的计算哲学，正在引领我们跨越感知智能的浅滩，向着通用人工智能的理性圣殿阔步前行。</p>
"""

insert_target = '<h2 id="system2-epistemology-summary">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_2 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final push 2 to ch094.html")
else:
    print("Target not found")
