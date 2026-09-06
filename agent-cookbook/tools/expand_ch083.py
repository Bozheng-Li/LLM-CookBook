import os

path = r"D:/agent-cookbook/chapters/ch083.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# Expand with comprehensive deep sections:
# 1. Truth Discovery & Bayesian Source Credibility Calculation Math & Python Implementation
# 2. Section-by-Section Long Report Assembly Engine with Transition Smoothing
# 3. 5 Catastrophic Failure Modes in Deep Web Research (SEO farm loops, paywall traps, hallucinated metrics)
# 4. End-to-end evaluation benchmark (GAIA / BrowseBench) for deep research

expansion_1 = """
    <h2 id="truth-discovery-math">多源事实冲突仲裁：贝叶斯真值发现（Truth Discovery）数学原理与实现</h2>
    <p>在开放互联网络中，针对同一个核心事实（例如某前沿大模型集群的 GPU 采购规模、某芯片的良品率），不同科技媒体、自媒体分析师和券商研报往往会给出大相径庭的数字。浅层的 RAG 系统往往会把所有搜索结果机械地拼在一起，导致大模型生成出「根据A机构报道规模为1万卡，但B机构指出规模为10万卡，C机构则认为是5000卡」的混乱综述，完全丧失了深度智库应有的专业研判价值。</p>
    <p>工业级 Deep Research 引入了经典的<strong>贝叶斯真值发现算法（Truth Discovery Algorithm）</strong>。其核心假设建立在一个互惠增强的逻辑之上：<strong>如果一个信源多次提供了被其他高权重信源印证的真实事实，该信源的先验信用权重就应该提升；反之，若某个事实断言得到了多个高信用信源的背书，该事实为真的后验概率就越接近于 1。</strong></p>
    
    <p>设 $S = \{s_1, s_2, ..., s_M\}$ 为参与本次调研的全部信源集合，$F = \{f_1, f_2, ..., f_N\}$ 为提取出的原子事实集合。信源 $s_m$ 对事实 $f_n$ 的置信权重 $w(s_m)$ 和事实本身的真值综合得分 $C(f_n)$ 满足如下交替迭代公式：</p>

    <p>$$C(f_n) = \sum_{s_m \in S(f_n)} w(s_m) \cdot \text{Sim}(f_n, \text{Claim}(s_m))$$</p>
    <p>$$w(s_m) = -\log \left( 1 - \frac{\sum_{f_n \in F(s_m)} C(f_n)}{|F(s_m)|} \right)$$</p>

    <p>通过多轮迭代直到信源权重收敛，系统能够自动将频繁发布营销噪音的自媒体权重降为极低，而将 IEEE、权威财报等严肃信源的权重自动推升至最高。以下给出轻量级真值发现仲裁器的工程实现：</p>

    <div class="codeblock">
      <div class="cb-head"><span>贝叶斯真值发现与事实冲突仲裁器（truth_discovery.py）</span><button class="cb-copy">复制</button></div>
      <pre><code>import math
from typing import Dict, List

class BayesianTruthDiscovery:
    def __init__(self, max_iter: int = 10, tol: float = 1e-4):
        self.max_iter = max_iter
        self.tol = tol

    def resolve_conflicting_facts(self, claims: List[Dict]) -> Dict[str, Any]:
        \"\"\"对同一实体的相互冲突断言执行真值迭代发现
        claims 结构: [{'source_domain': 'techcrunch.com', 'value': 10000, 'text': '...'}, ...]
        \"\"\"
        # 1. 初始化信源先验权重 (顶级域名有初始保底)
        sources = list(set(c["source_domain"] for c in claims))
        weights = {s: 1.0 for s in sources}
        for s in weights:
            if any(s.endswith(d) for d in [".edu", ".gov", ".org", "reuters.com", "bloomberg.com"]):
                weights[s] = 2.5  # 权威信源强先验

        fact_candidates = claims
        
        for iteration in range(self.max_iter):
            old_weights = weights.copy()
            
            # Step A: 更新事实断言的综合置信得分
            fact_scores = []
            for c in fact_candidates:
                s_weight = weights[c["source_domain"]]
                # 计算支持该取值的群体权重总和
                support_weight = sum(
                    weights[other["source_domain"]] 
                    for other in fact_candidates 
                    if abs(other["value"] - c["value"]) / max(c["value"], 1) < 0.15 # 允许 15% 浮动容差
                )
                fact_scores.append(support_weight)

            # Step B: 归一化事实得分并反向更新信源信用度
            max_score = max(fact_scores) if fact_scores else 1.0
            norm_scores = [sc / max_score for sc in fact_scores]

            for s in sources:
                s_facts = [norm_scores[i] for i, c in enumerate(fact_candidates) if c["source_domain"] == s]
                if s_facts:
                    avg_fact_quality = sum(s_facts) / len(s_facts)
                    # 避免对数发散
                    avg_fact_quality = min(max(avg_fact_quality, 0.01), 0.99)
                    weights[s] = -math.log(1.0 - avg_fact_quality + 1e-6)

            # 检查收敛条件
            delta = sum(abs(weights[s] - old_weights[s]) for s in sources)
            if delta < self.tol:
                break

        # 选取得分最高的断言作为胜出基准真值
        best_idx = fact_scores.index(max(fact_scores))
        winner = fact_candidates[best_idx]

        return {
            "accepted_value": winner["value"],
            "accepted_text": winner["text"],
            "endorsed_by": [c["source_domain"] for i, c in enumerate(fact_candidates) if fact_scores[i] >= max_score * 0.8],
            "confidence": round(norm_scores[best_idx], 3)
        }</code></pre>
    </div>
"""

expansion_2 = """
    <h2 id="section-by-section-assembly">万字长文装配流水线：分章流式撰写与平滑润色</h2>
    <p>产生一份结构严谨的万字行研报告，必须解决大语言模型生成长文本时的两大死穴：<strong>「后半程注意力溃缩与词汇贫乏」</strong>以及<strong>「跨章节之间的逻辑重复与脱节」</strong>。本系统设计了基于双向上下文锚点的<strong>「分章流水线组装器（Section Pipeline Assembler）」</strong>：</p>

    <div class="codeblock">
      <div class="cb-head"><span>分章流式长文装配器实现（report_assembler.py）</span><button class="cb-copy">复制</button></div>
      <pre><code>from typing import List, Dict

class ModularReportAssembler:
    def __init__(self, llm_client):
        self.llm = llm_client

    def assemble_mega_report(self, topic: str, sections_plan: List[Dict], global_blackboard: List[Dict]) -> str:
        completed_sections = []
        rolling_summary = "报告刚开始撰写，尚无前文内容。"

        for idx, sec in enumerate(sections_plan):
            title = sec["title"]
            required_points = sec["required_points"]
            
            # 1. 检索与当前小节强相关的原子证据
            relevant_evidence = [
                e for e in global_blackboard 
                if any(k.lower() in e["facts"].lower() for k in sec["keywords"])
            ][:8]

            evidence_prompt_text = "\\n".join([
                f"[证据 #{i+1}] ({e['source_title']}): {e['facts']}" 
                for i, e in enumerate(relevant_evidence)
            ])

            # 2. 注入前文动态摘要，保持语调连贯，严禁重复前文已论述过的案例
            section_prompt = f\"\"\"你正在撰写《{topic}》的第 {idx+1} 章节: 【{title}】。
前文各章要点摘要如下 (用于衔接过渡，切勿重复本章内容):
{rolling_summary}

本章重点论述要求:
{chr(10).join(['- ' + p for p in required_points])}

本章专属实证参考资料:
{evidence_prompt_text}

【写作要求】
- 篇幅约 2,000 ~ 3,000 字，深度挖掘底层因果关系。
- 必须承接上一小节的逻辑推演，在本章开头设计 1 句精炼的过渡衔接段落。
- 严格插入来源引用标记，如 [证据 #1]。
\"\"\"
            # 生成该章节正文
            section_content = self.llm.chat(section_prompt, "")
            completed_sections.append(f"## {title}\\n\\n{section_content}")

            # 3. 异步更新滚动摘要，提炼当前章节核心论断供下一章感知
            update_summary_prompt = f\"\"\"请用 150 字提炼以下章节的核心观点与关键数据:
{section_content[:1500]}\"\"\"
            new_chapter_summary = self.llm.chat(update_summary_prompt, "")
            rolling_summary += f\"\\n第{idx+1}章【{title}】核心结论: {new_chapter_summary}\"

        # 4. 全书终审润色: 生成中英文双语执行摘要 (Executive Summary) 与参考文献附录
        full_draft = "\\n\\n".join(completed_sections)
        exec_summary_prompt = f\"\"\"基于以下万字调研终稿，为跨国企业 CEO 提炼一份 800 字的高精炼中英双语执行摘要 (Executive Summary):\\n{full_draft[:6000]}\"\"\"
        exec_summary = self.llm.chat(exec_summary_prompt, "")

        return f"# 《{topic}》深度行业调研报告\\n\\n## 执行摘要 (Executive Summary)\\n\\n{exec_summary}\\n\\n{full_draft}"</code></pre>
    </div>
"""

expansion_3 = """
    <h2 id="deep-failure-modes">实战避坑手册：Deep Research 五大典型滑铁卢及治理</h2>
    <p>复刻 Deep Research 绝非易事。系统在互联网长程深潜中，会遇到各种恶意对抗与噪声陷阱。以下是研发团队必须具备的五大防线：</p>

    <p><strong>① 灾难场景一：陷入 SEO 内容农场的递归死循环（Content Farm Infinite Loops）。</strong><br>
    <em>现象：</em>当调研某个冷门技术时，Google 搜索返回的前 10 个结果全是由 AI 批量洗稿生成的内容农场（如各色采集站）。Agent 在这些互相引用的假网页中疯狂递归，浪费上万 Token 提取出一堆同质化的车轱辘话。<br>
    <em>对策：</em>建立<strong>「文本信息熵与词汇多样性在线探针」</strong>：在爬虫提取出正文后，计算其文本信息熵（Shannon Entropy）与重复 n-gram 比例；若重复度超过 35% 或域名命中内容农场黑名单，直接丢弃该链接并终止该分支的递归展开。</p>

    <p><strong>② 灾难场景二：学术付费墙与反爬 JavaScript 动态渲染黑洞（Paywall & JS Blackhole）。</strong><br>
    <em>现象：</em>遇到 Nature、Science 或金融数据库时，普通爬虫抓到的内容全是「请登录阅读全文」或空白页面，导致关键证据缺失。<br>
    <em>对策：</em>设计<strong>「多级降级抓取路由（Fallback Scraper Mesh）」</strong>：优先使用轻量级 Jina Reader；若检测到登录拦截，立即路由至配备真实 Cookie 与学术认证代理的 Playwright 无头集群；若目标仍为付费墙，则自动改道搜索其在 arXiv 预印本、ResearchGate 或各大高校公开知识库中的开源开放获取（Open Access）副本。</p>

    <p><strong>③ 灾难场景三：虚构历史与过时数据充当最新现状（Stale Data Anachronism）。</strong><br>
    <em>现象：</em>提问「2025 年某技术最新进展」，Agent 爬到了一篇 2019 年的老文章，在报告中宣称「该技术目前仍处于实验室概念阶段，尚未有量产产品」。<br>
    <em>对策：</em>在检索阶段强制追加<strong>「时间窗口限定（Temporal Search Anchoring）」</strong>：在搜索引擎 API 中强制附带 <code>tbs=qdr:y1</code>（近一年内）；并在抽取事实时强制抽取文本中的发布年份与更新时间，对未注明时间的网页断言施加惩罚折扣。</p>

    <p><strong>④ 灾难场景四：长程任务中途意外断网引发的状态归零（State Loss on Crash）。</strong><br>
    <em>现象：</em>调研任务已经执行了 18 分钟、爬了 45 个网页，在第 4 阶段撰写时网络突发抖动中断，整个进程退出，用户只能重新从头开始。<br>
    <em>对策：</em>贯彻第 76 章长程 Agent 的<strong>「快照检查点机制（Snapshot Checkpointing）」</strong>：每一批网页爬取和事实抽取完成后，系统自动将全局黑板与已探索 URL 序列化写入 Redis 或持久化 SQLite。一旦容器异常重启，系统能瞬间从最近的检查点恢复上下文，续跑未完成的章节。</p>

    <p><strong>⑤ 灾难场景五：引文标记错乱与张冠李戴（Citation Hallucination）。</strong><br>
    <em>现象：</em>报告中写着「该方案能降低 40% 成本 [3]」，但文末参考文献 [3] 实际上是一篇讨论环境保护的论文。<br>
    <em>对策：</em>在最终交付渲染前，部署<strong>「引文后置硬对齐检查器」</strong>：利用轻量模型对报告中出现的每一处 <code>[x]</code> 引用进行二次比对，提取引用句与参考文献摘要，计算余弦相似度；若相似度低于 0.65，强行阻断并回退至重修状态，彻底捍卫智库报告的公信力。</p>
"""

insert_target = '<h2 id="faq">'
if insert_target in text:
    new_text = text.replace(insert_target, expansion_1 + "\n" + expansion_2 + "\n" + expansion_3 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Successfully expanded ch083.html with truth discovery, assembly and failure modes")
else:
    print("Target not found")
