import os

path = r"D:/agent-cookbook/chapters/ch084.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push = """
    <p>与此同时，针对涉及多线程并发与分布式事务的深水区代码，Repo Agent 会在本地沙箱中注入竞态条件探针（ThreadSanitizer / Mutex Lock Analyzer），反复执行高频压力自测，彻底消灭死锁与脏读隐患，筑牢工业级交付的终极质量堤坝。</p>
"""

insert_target = '<h2 id="production-checklist">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Final push added")
