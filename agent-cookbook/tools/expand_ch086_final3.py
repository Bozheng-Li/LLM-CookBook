import os

path = r"D:/agent-cookbook/chapters/ch086.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_3 = """
    <p>这种端云一体化的全新架构体系，不仅大幅降低了企业运营超大规模云端集群的昂贵算力开销，更赋予了终端设备在完全离线断网环境下依然从容运转的强大韧性。</p>
"""

insert_target = '<h2 id="production-checklist">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_3 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final conclusion push 3")
