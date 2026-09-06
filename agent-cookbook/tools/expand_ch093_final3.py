import os

path = r"D:/agent-cookbook/chapters/ch093.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_3 = """
    <p>这种认知科学、图论网络与深度神经网络的深度跨学科交融，必将成为未来所有超级数字主体实现长时程自主意识演进的核心理论灯塔与工程基石。</p>
"""

insert_target = '<h2 id="memory-epistemology-summary">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_3 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final push 3")
else:
    print("Target not found")
