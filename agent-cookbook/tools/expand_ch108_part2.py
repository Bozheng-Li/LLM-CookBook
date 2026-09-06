# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch108.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

extra_content = """
    <p>此外，在建立终身学习网络时，技术人员应主动构建<strong>个人专属的认知卡片库与知识索引（Zettelkasten / Obsidian Knowledge Base）</strong>。将分散在学术论文中的形式化定义、工业级博客中的故障复盘、开源项目中的精妙设计模式以及自身生产实战中的血泪踩坑经验，通过双向反向链接（Bidirectional Backlinks）相互串联。当一个工程师的知识网络形成了高密度的自洽图谱时，面对任何未知的新型系统挑战，都能迅速调动跨领域的认知原语进行类比重构与快速突破。</p>
"""

target = '<section class="refs">'
if target in text:
    new_text = text.replace(target, extra_content + "\n" + target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added extra content")
