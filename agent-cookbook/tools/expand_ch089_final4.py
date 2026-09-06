import os

path = r"D:/agent-cookbook/chapters/ch089.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_4 = """
    <p>这种全方位的软硬件与人机工程系统融合，标志着人机交互正式步入了以通用视觉为中枢、以物理世界外设为载体的全新具身纪元。</p>
"""

insert_target = '<h2 id="production-readiness">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_4 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final conclusion 4")
else:
    print("Target not found")
