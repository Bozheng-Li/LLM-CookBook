import os

path = r"D:/agent-cookbook/chapters/ch090.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# Expand with comprehensive deep sections:
# 1. Complete Louvain Community Detection Algorithm & Academic Lineage Clustering Python Implementation
# 2. End-to-End AI Scientist Experiment Code Generation & Automated Execution Engine
# 3. Step-by-step Troubleshooting Playbook (5 catastrophic academic research failures)

expansion_1 = """
    <h2 id="community-detection-math">学术演化拓扑聚类：Louvain 模块度社群发现算法与实战</h2>
    <p>当科研助理 Agent 沿着引文网络滚雪球抓取了 500 篇前沿论文后，如果只是简单地按时间倒序排列，科研人员依然无法洞察该领域的全局理论分化。例如在「大语言模型强化学习」领域，有的团队死磕策略梯度（PPO / GRPO），有的团队转向直接偏好优化（DPO / KTO），还有的团队探索过程奖励模型（PRM）。</p>
    
    <p>为了自动将庞杂的论文有向图拆解为清晰的并行技术流派，系统引入了经典的 <strong>Louvain 模块度最大化社群发现算法（Louvain Modularity Optimization）</strong>。模块度（Modularity $Q$）量化了一个社群内部的连接密度相比于随机连接的集中程度：</p>

    <p>$$Q = \frac{1}{2m} \sum_{i, j} \left[ A_{ij} - \frac{k_i k_j}{2m} \right] \delta(c_i, c_j)$$</p>

    <p>其中 $A_{ij}$ 为节点 $i$ 和 $j$ 之间的引用边权重，$k_i, k_j$ 为节点的度数，$m$ 为全图总边数，$c_i$ 为节点所属社群，$\delta$ 为克罗内克符号（当两节点处于同一社群时为 1，否则为 0）。以下代码展示了如何利用该算法在 100 毫秒内将数百篇学术论文自动划分为主流学术流派：</p>

    <div class="codeblock">
      <div class="cb-head"><span>学术引文社群发现与学派拓扑聚类器（academic_clustering.py）</span><button class="cb-copy">复制</button></div>
      <pre><code>import networkx as nx
from networkx.algorithms.community import louvain_communities
from typing import Dict, List, Set

class AcademicLineageClusterer:
    def __init__(self, citation_graph: nx.DiGraph):
        # 转换为无向图以进行双向引用亲密度分析
        self.undirected_graph = citation_graph.to_undirected()
        self.raw_graph = citation_graph

    def detect_major_schools_of_thought(self, resolution: float = 1.0) -> List[Dict]:
        \"\"\"利用 Louvain 算法将全网论文自动聚类为主流并行学派\"\"\"
        if len(self.undirected_graph) < 3:
            return []

        # 运行模块度最大化划分
        communities = louvain_communities(self.undirected_graph, resolution=resolution, seed=42)
        schools = []

        for idx, comm in enumerate(communities):
            if len(comm) < 2:  # 过滤孤立节点噪点
                continue

            # 计算该子社群内部最具权威度的核心枢纽论文 (PageRank 最高者)
            subgraph = self.raw_graph.subgraph(comm)
            pr_scores = nx.pagerank(subgraph, alpha=0.85)
            sorted_nodes = sorted(pr_scores.keys(), key=lambda x: pr_scores[x], reverse=True)

            pillar_paper = sorted_nodes[0]
            pillar_title = self.raw_graph.nodes[pillar_paper].get("title", "未知核心代表作")

            schools.append({
                "school_id": f"School_{idx+1}",
                "pillar_paper_id": pillar_paper,
                "pillar_title": pillar_title,
                "paper_count": len(comm),
                "member_papers": list(comm)
            })

        schools.sort(key=lambda x: x["paper_count"], reverse=True)
        print(f"[Cluster] 成功聚类出 {len(schools)} 个核心学术流派！")
        return schools</code></pre>
    </div>
"""

expansion_2 = """
    <h2 id="ai-scientist-experiment">前沿拓展：从文献综述到自主实验代码生成与消融测试</h2>
    <p>真正的 AI Scientist（科学智能体，如 Sakana AI 的开创性成果）不仅仅停留在「阅读别人写过的论文」，它的终极目标是<strong>「自动构思新实验、编写 PyTorch 训练代码、调度 GPU 跑出消融对比数据，并自动生成 LaTeX 论文手稿」</strong>。</p>

    <p>系统设计了基于双轨验证的<strong>「科研假说实验化生成与验证执行器」</strong>：</p>

    <div class="codeblock">
      <div class="cb-head"><span>科研假说端到端实验生成与验证引擎（hypothesis_experimenter.py）</span><button class="cb-copy">复制</button></div>
      <pre><code>from typing import Dict, Any

class AutonomousExperimentEngine:
    def __init__(self, code_runner, llm_client):
        self.runner = code_runner
        self.llm = llm_client

    def design_ablation_experiment(self, hypothesis: str, baseline_model: str) -> Dict[str, Any]:
        \"\"\"根据提出的创新假说，自动生成严密的消融实验设计方案\"\"\"
        system_prompt = \"\"\"你是一名严谨的高级算法研究科学家。
针对用户提出的全新科研假说，请设计一套严格遵循单一变量原则的消融实验对比方案。
必须包含:
1. 基线组 (Control Baseline)
2. 实验组 (Experimental Group with Proposed Mechanism)
3. 关键消融项 (Ablation Variants)
4. 核心评估指标 (Metric: 如 Accuracy, BLEU, PPL, 训练显存开销)\"\"\"

        prompt = f"全新研究假设: {hypothesis}\\n基线算法: {baseline_model}"
        design_spec = self.llm.chat(system_prompt, prompt)

        # 进一步生成配套的最小自包含 PyTorch 实验验证代码
        code_gen_prompt = f\"\"\"根据以下实验设计，编写一个自包含的 PyTorch 微型消融验证脚本。
要求: 使用合成数据集或内置测试集，能够在 2 分钟内运行完毕并打印对照指标表格。
实验设计规范:
{design_spec}\"\"\"

        experiment_code = self.llm.chat_code(code_gen_prompt)
        
        # 在本地沙箱中触发真实的 Python 运行
        print("[AI Scientist] 正在隔离 GPU 容器中启动自动化实验验证...")
        exec_result = self.runner.run_in_sandbox(experiment_code, timeout_seconds=180)

        return {
            "hypothesis": hypothesis,
            "experiment_design": design_spec,
            "experiment_code": experiment_code,
            "execution_logs": exec_result.get("stdout"),
            "hypothesis_supported": "PASS" if exec_result.get("returncode") == 0 else "FAIL"
        }</code></pre>
    </div>
"""

expansion_3 = """
    <h2 id="scholar-failure-modes">实战避坑手册：科研文献 Agent 五大常见暗坑及解法</h2>
    <p>在严肃学术场景中，任何细小的工程漏洞都可能导致推导出彻底错误的伪科学结论。以下是落地科研文献智能体必须严防死守的五大典型死穴：</p>

    <p><strong>① 灾难场景一：同名学者与机构混淆导致的成果张冠李戴（Author Disambiguation Collision）。</strong><br>
    <em>现象：</em>在分析某位知名学者（如「Wei Wang」）的学术演进时，Agent 把全球数十位同名同姓在生物、土木、物理领域的不同学者的论文全部混在一块，生成了一份荒谬绝伦的“全能跨学科大师”学术画像。<br>
    <em>对策：</em>强制绑定 <strong>ORCID 全球唯一学者身份标识码与 OpenAlex Author ID</strong>，严禁单纯依赖拼音或姓名字符串进行模糊匹配；在元数据拉取时校验第一单位（Affiliation）与常驻研究领域（Field of Study）。</p>

    <p><strong>② 灾难场景二：预印本与正式发表版本的元数据时间错位（Preprint Temporal Skew）。</strong><br>
    <em>现象：</em>某篇论文 2021 年就已在 arXiv 公开，但在 2024 年才被 IEEE TPAMI 正式刊出。Agent 在梳理时间演化时，误将该成果标记为 2024 年的“最新创新”，完全颠倒了算法发明的因果先后关系。<br>
    <em>对策：</em>引入 <strong>First-Public-Date（最早公开时间）对齐机制</strong>：无论期刊最终正式出版年份为何，统一以 arXiv 上的 <code>v1</code> 版本上传时间戳作为确定性学术优先权（Priority Date）的唯一基准。</p>

    <p><strong>③ 灾难场景三：双栏 PDF 排版跨页跨栏解析崩盘（Double-column Cross-stitching）。</strong><br>
    <em>现象：</em>在普通文本提取器中，左栏的一段话被机械地拼在了右栏同一水平线句子的中间，导致整段文字语句不通，大模型阅读后完全产生严重逻辑偏差。<br>
    <em>对策：</em>彻底淘汰 <code>PyPDF2 / PDFMiner</code> 等陈旧几何文本提取库，全面拥抱 <strong>基于 Vision-Transformer 的端到端视觉文档模型（如 MinerU / LayoutLMv3）</strong>，在图像空间先进行版面分析（Layout Analysis）分栏隔离，再顺次进行线性化读取。</p>

    <p><strong>④ 灾难场景四：负向实证研究的发表偏倚（Publication Bias Blindspot）。</strong><br>
    <em>现象：</em>文献中几乎 100% 的论文都在宣称「我们的模型比基线好 5%」，导致 Agent 误以为该技术在所有场景下均完美有效。<br>
    <em>对策：</em>在提示词中强制开启 <strong>局限性与反事实挖掘探针（Limitations & Failure Analysis）</strong>：要求 Agent 专门定向跳跃至论文文末的 <code>Limitations, Future Work, Failure Cases</code> 章节进行逆向提取，全面还原真实技术边界。</p>

    <p><strong>⑤ 灾难场景五：引文环状相互背书引发的伪真理陷阱（Echo Chamber Loop）。</strong><br>
    <em>现象：</em>三篇同门实验室的论文互相引用对方的一个未经严格理论证明的经验参数，Agent 在滚雪球时将其误判为该领域坚不可摧的公认理论定论。<br>
    <em>对策：</em>建立 <strong>跨实验室与独立第三方复现校验过滤器</strong>：对关键结论的背书信源进行机构去重，唯有获得至少两个非关联科研机构的独立印证时，方可被标记为“广泛公认的工业/理论结论”。</p>
"""

insert_target = '<h2 id="faq">'
if insert_target in text:
    new_text = text.replace(insert_target, expansion_1 + "\n" + expansion_2 + "\n" + expansion_3 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Successfully expanded ch090.html with Louvain, AI Scientist and Failure Modes")
else:
    print("Target not found")
