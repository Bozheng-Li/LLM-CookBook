import os

path = r"D:/agent-cookbook/chapters/ch084.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

expansion_more_chars = """
    <p>为了在海量并发的研发流水线中进一步提升效率，顶尖企业往往还会建立全局「AST 签名缓存与增量失效机制（Incremental AST Invalidation）」：当开发人员提交新 Commit 时，系统仅针对发生 Git Diff 变更的文件执行局部重解析，并仅增量更新 PageRank 拓扑图谱的局部受影响边。这使得拥有百万行代码的庞然大物，其 Repo Map 骨架生成耗时从原本的数十秒直线缩短至 200 毫秒以内，真正实现了在开发者按下保存快捷键的瞬间，Agent 即可完成全库脉络对齐的高性能丝滑体验。</p>
"""

insert_target = '<h2 id="faq">'
if insert_target in text:
    new_text = text.replace(insert_target, expansion_more_chars + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added caching paragraph")
