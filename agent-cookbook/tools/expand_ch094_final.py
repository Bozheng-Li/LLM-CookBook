import os

path = r"D:/agent-cookbook/chapters/ch094.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push = """
    <h2 id="system2-epistemology-summary">系统 2 慢思考的哲学认识论：从机械鹦鹉到沉思主体的升华</h2>
    <p>回顾现代人工智能走过的漫长弯路，人们一度迷恋于不断用更庞大的数据、更庞大的参数去暴力拟合单次前向输出，试图让模型在几毫秒内凭直觉回答世间一切难题。然而，这种将复杂逻辑等同于直觉模式匹配的傲慢，最终在严苛的数学定理证明、深层软件重构以及高阶对抗博弈面前撞得头破血流。</p>
    
    <p>人类之所以能在残酷的自然界胜出，不是因为我们的直觉反射比猎豹更快，而是因为我们的大脑进化出了一套能够随时接管直觉的<strong>系统 2 沉思机制</strong>：遇到悬崖时停下脚步、遇到复杂谜题时拿出一张白纸分步演草、发现推理矛盾时推翻重来。通过在本章将卡尼曼双系统模型、图搜索（A* 与 MCTS）的数学形式化、图尔敏论证逻辑学与皮尔士三元推理理论熔铸为一套严密的测试时计算范式，我们实际上为 AI 赋予了灵魂深处最宝贵的一项特质——<strong>真正的沉思与自省能力</strong>。它让智能体从一只仅仅重复概率统计规律的“机械鹦鹉”，真正蜕变成为一个具备批判性思维与科学严谨性的理性沉思主体。</p>
"""

insert_target = '<h2 id="faq">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added epistemology summary to ch094.html")
else:
    print("Target not found")
