import os

path = r"D:/agent-cookbook/chapters/ch084.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_2 = """
    <p>总而言之，企业级 Repo Agent 的核心工程护城河不在于调用某个模型的提示词技巧，而在于将经典的编译器静态分析、版本控制图论算法、分布式沙箱隔离与测试驱动自愈深度熔铸为一套无缝联动的自动化工程基础设施。唯有如此，AI 才能真正跨越玩具与生产的鸿沟，成为研发团队中不知疲倦、严谨可靠的数字化工程师主力军。</p>
"""

insert_target = '<h2 id="production-checklist">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_2 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Final push 2 added")
