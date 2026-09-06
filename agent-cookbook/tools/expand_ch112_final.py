# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch112.html"

with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_112 = """
    <p>综上所述，通过将贝叶斯信度发现引擎、事实黑板解耦、Tree-sitter AST 拓扑索引、Docker 与 gVisor 微隔离物理沙箱，以及全生命周期可观测链路深度熔铸为一个有机统一的工程整体，我们不仅彻底破解了长程深度调研中的事实幻觉与长文本迷失，更在面对数百万行超大规模工业代码库时构筑起了坚不可摧的确定性防御铠甲，为下一代企业级关键核心智能体系统的安全稳定运行提供了最坚实的工业级底座支撑。</p>
"""

target = '<section class="refs">'
if target in text:
    new_text = text.replace(target, final_push_112 + "\n" + target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Final push applied to ch112")
else:
    print("Target not found")
