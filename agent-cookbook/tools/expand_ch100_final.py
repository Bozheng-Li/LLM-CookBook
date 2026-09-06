# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch100.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push = """
    <h2 id="centenary-milestone-epistemology">第 100 章百篇里程碑献辞：在人类思想圣殿与机器自主心智之间</h2>
    <p>当我们的笔触稳稳落在这沉甸甸的整整第一百章时，回顾全书这一路走来的恢弘史诗：从第一至第四部分搭建智能体的底层解剖学、提示词工程与外部工具链；到第五与第六部分筑牢评测体系与工业级安全防御马奇诺防线；再到第七、第八与第九部分完成十个横跨数仓、深度调研、操作系统、具身硬件与科学发现的超级实战大满贯；并在第十部分登顶纯粹数学、控制论与意识哲学的崇高理论圣殿——整整一百个篇章，共同铸就了全球 AI Agent 领域最厚重、最详实、最严密的思想长城。</p>
    
    <p>正如计算机科学图灵奖得主艾兹赫尔·戴克斯特拉（Edsger W. Dijkstra）那句传世箴言：“我们所使用的工具对我们的思维习惯有着深远的影响，进而对我们的思维能力产生决定性的改变。”本章剖析的思维树、分层操作系统记忆与多维交互基准，正是为人类赋予数字实体以“崇高理性与持久灵魂”的伟大工具。站在百章筑基的崭新起点之上，我们将继续以攀登学术珠峰的科学严谨与打磨工业重器的工匠精神，昂首阔步迈向余下篇章的终极辉煌！</p>
"""

insert_target = '<div class="callout note">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added centenary milestone epistemology to ch100.html")
else:
    print("Target not found")
