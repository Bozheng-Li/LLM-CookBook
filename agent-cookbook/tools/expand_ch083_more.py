import os

path = r"D:/agent-cookbook/chapters/ch083.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

expansion_more = """
    <h2 id="eval-gaia">深度调研能力量化评测：基于 GAIA 与 BrowseBench 的基准对齐</h2>
    <p>评估一个 Deep Research 系统的好坏，绝不能依靠人类专家随机浏览几篇文章的主观感受。工业界目前公认最具权威性的长程多步调研基准是 <strong>GAIA（General AI Assistants Benchmark）</strong>与 <strong>BrowseBench</strong>。这两个评测基准专门设计了需要多层网页跳跃、复杂跨源推理、逆向事实核实才能获得正确答案的高难度挑战题。</p>
    
    <div class="tbl-wrap">
      <table>
        <thead><tr><th>评测基准</th><th>核心评测维度</th><th>典型考题案例</th><th>Deep Research 达标红线</th></tr></thead>
        <tbody>
          <tr><td><strong>GAIA Level 3 (长程复杂任务)</strong></td><td>跨网页多模态聚合、长链条因果推演、反事实辨析</td><td>「查找某诺贝尔奖得主 1985 年在某期刊发表的第一篇论文中，图 3 所示的化学反应催化剂名称及其当年合成成本」</td><td>复杂链路正确率 &ge; 42% (超越普通人类平均水平)</td></tr>
          <tr><td><strong>BrowseBench (动态网页探索)</strong></td><td>表单交互、分页爬取、动态 DOM 逆向与弹窗穿透</td><td>「在某跨国物流查询系统中输入 5 个不同提单号，综合对比其各自在新加坡港的清关滞留平均时长」</td><td>端到端动作成功率 &ge; 85%</td></tr>
          <tr><td><strong>Citation Grounding Rate (引文真实度)</strong></td><td>引用标记的真实存在性、对应段落支持度、无死链率</td><td>对全篇报告中的 50 个引文角标逐个执行自动抓取与 NLI 蕴涵检验</td><td>有效真实引用率 &ge; 98.5% (严禁任何幽灵虚构链接)</td></tr>
          <tr><td><strong>Coverage & Depth (覆盖度与深度)</strong></td><td>对比人类首席分析师报告的核心论点完备性比率</td><td>覆盖政策影响、产业链上下游、5 年技术路线预测与风险提示</td><td>核心论点覆盖度 &ge; 90%</td></tr>
        </tbody>
      </table>
      <caption>表 83-3 · Deep Research 工业级核心评测基准与达标门槛。涵盖多步推理、动态交互、引文可信度与领域覆盖度。</caption>
    </div>

    <p>在研发流水线中，团队应将 GAIA 子集集成进 GitHub Actions CI/CD 流水线中。任何对 Prompt、爬虫并发策略或假设树剪枝算法的代码修改，都必须跑通 30 个代表性长程基准题目，且在真实性与完备性指标上没有负向回归，方可允许合并部署至生产集群。这种严谨的评测驱动开发（EDD）模式，是确保系统智库输出始终维持在行业一流梯队的根本保障。</p>
"""

insert_target = '<h2 id="faq">'
if insert_target in text:
    new_text = text.replace(insert_target, expansion_more + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added GAIA evaluation section")
else:
    print("Target not found")
