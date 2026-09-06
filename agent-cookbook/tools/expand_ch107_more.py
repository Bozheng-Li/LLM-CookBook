# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch107.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

expansion_more = """
    <h2 id="eval-metric-taxonomy">评测度量衡科学：从执行率到 pass^k 泛化能力的统计学推导</h2>
    <p>在严肃评估智能体时，很多团队经常犯的统计学低级错误是：只让智能体对每道题执行一次采样（Single Trial），然后简单计算通过率。然而由于大语言模型在采样过程中存在非零的温度系数（Temperature），单次跑分具有极大的<strong>随机抽样方差（Sampling Variance）</strong>。某次跑分 75% 的模型，在下次随机复测时可能会暴跌至 60%。</p>
    
    <p>现代权威评测套件普遍推行由 Kulman 等人提出的 <strong>$\text{pass}^k$ 稳定性度量衡</strong> 与 <strong>无偏估计量公式</strong>：</p>

    <p>设针对每一个测试任务，我们独立让智能体生成 $n$ 次完整解答（例如 $n = 10$），其中有 $c$ 次成功通过了测试。为了计算智能体在至多允许尝试 $k$ 次时（$k \le n$）能够成功解决问题的期望概率 $\text{pass}@k$，作者严格给出了最小方差无偏估计量（Unbiased Estimator）算式：</p>

    <p>$$\text{pass}@k = \mathbb{E}_{\text{Tasks}} \left[ 1 - \frac{\binom{n - c}{k}}{\binom{n}{k}} \right]$$</p>

    <div class="tbl-wrap">
      <table>
        <thead><tr><th>统计学度量指标</th><th>数学定义与物理含义</th><th>在企业级生产系统中的意义</th><th>推荐的生产达标红线</th></tr></thead>
        <tbody>
          <tr><td><strong>pass@1 (一次性成功率)</strong></td><td>单次尝试即通过测试的概率</td><td>衡量智能体的单步精确度与成本（用户体验最直接指标）</td><td>通用核心生产任务 pass@1 &ge; 70%</td></tr>
          <tr><td><strong>pass@5 (重试自愈能力)</strong></td><td>允许在失败后基于报错反思重试 5 次的成功率</td><td>衡量智能体结合 Reflexion 机制后的自愈修复极限潜能</td><td>复杂长程攻坚任务 pass@5 &ge; 90%</td></tr>
          <tr><td><strong>pass^k 稳定性衰减率</strong></td><td>$\text{pass}@1 / \text{pass}@5$ 的比值</td><td>衡量模型是依赖真才实学稳定解决，还是靠瞎蒙撞大运（比值越接近 1 越稳健）</td><td>稳定性比值 &ge; 0.82</td></tr>
        </tbody>
      </table>
      <caption>表 107-3 · 智能体可靠性统计学核心指标矩阵。全面揭示单次偶然成功与高可靠确定性交付的本质分野。</caption>
    </div>
"""

insert_target = '<div class="callout note">'
if insert_target in text:
    new_text = text.replace(insert_target, expansion_more + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added eval metric taxonomy section to ch107.html")
else:
    print("Target not found")
