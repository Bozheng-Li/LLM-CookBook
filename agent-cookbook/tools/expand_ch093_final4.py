import os

path = r"D:/agent-cookbook/chapters/ch093.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_4 = """
    <p>它为人类迈向通用人工智能（AGI）的历史征程，铺就了一条坚不可摧的认知记忆科学大道。</p>
"""

insert_target = '<h2 id="memory-epistemology-summary">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_4 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final push 4")
else:
    print("Target not found")
