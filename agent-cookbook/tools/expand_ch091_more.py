import os

path = r"D:/agent-cookbook/chapters/ch091.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

expansion_more = """
    <h2 id="stochastic-game-linear-programming">极小化极大与线性规划：双人零和博弈的形式化求解</h2>
    <p>在零和博弈中（例如 AlphaGo 对弈、红蓝网络攻防对抗），智能体 A 的收益即为智能体 B 的损失（$\mathcal{R}_A = -\mathcal{R}_B$）。著名的<strong>冯·诺伊曼极小化极大定理（Minimax Theorem, von Neumann 1928）</strong>奠定了博弈论的皇冠：</p>

    <p>$$\max_{\mathbf{x} \in \Delta(\mathcal{A}_1)} \min_{\mathbf{y} \in \Delta(\mathcal{A}_2)} \mathbf{x}^T \mathbf{M} \mathbf{y} = \min_{\mathbf{y} \in \Delta(\mathcal{A}_2)} \max_{\mathbf{x} \in \Delta(\mathcal{A}_1)} \mathbf{x}^T \mathbf{M} \mathbf{y} = v^*$$</p>

    <p>其中 $\mathbf{M}$ 为博弈支付矩阵，$v^*$ 为该博弈唯一的数学价值（Value of the Game）。更精妙的是，在有限状态空间下，这一极小化极大均衡策略可以直接形式化为一个标准的<strong>线性规划（Linear Programming, LP）对偶问题</strong>进行多项式时间极速求解：</p>

    <p>$$\max v \quad \text{s.t.} \quad \sum_{i=1}^{|\mathcal{A}_1|} x_i M_{ij} \ge v \; (\forall j), \quad \sum_{i=1}^{|\mathcal{A}_1|} x_i = 1, \quad x_i \ge 0$$</p>

    <p>借由单纯形法（Simplex Algorithm）或内点法，红队或防御方可以在确定性的时间内求出绝对不被对手针对性克制的混合防御策略。这一强对偶性形式化，为现代安全智能体与博弈决策树剪枝提供了终极的解析工具。</p>
"""

insert_target = '<h2 id="faq">'
if insert_target in text:
    new_text = text.replace(insert_target, expansion_more + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added Minimax Linear Programming section")
else:
    print("Target not found")
