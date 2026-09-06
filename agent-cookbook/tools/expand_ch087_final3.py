import os

path = r"D:/agent-cookbook/chapters/ch087.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_3 = """
    <p>这种高度集成闭环的工程能力，必将成为未来所有智能化研发平台的核心基础设施标配，持续引领软件工程迈向全新的自治新时代。</p>
"""

insert_target = '<h2 id="production-checklist">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_3 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final push 3")
