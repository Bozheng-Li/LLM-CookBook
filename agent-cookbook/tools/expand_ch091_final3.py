import os

path = r"D:/agent-cookbook/chapters/ch091.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_3 = """
    <p>这种从形式化数学公理直达工业级代码工程的穿透力，正是本书赋予每一位求索者的终极思维武器，也是构建真正可信赖、高确定性超级智能体的必由之路。</p>
"""

insert_target = '<h2 id="theory-summary-perspective">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_3 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final push 3")
else:
    print("Target not found")
