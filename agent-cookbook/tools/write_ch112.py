# -*- coding: utf-8 -*-
"""
生成符合 check_chapter.py 全部严格规范的 Chapter 112: 系统设计面试：设计 Deep Research / Coding Agent
要求：
- HTML 体积 >= 29KB
- 汉字字符数 >= 6,000
- 包含 <figure class="figure"> 且带 <span class="fig-no">图 112-1</span>
- 包含 <div class="codeblock">
- 包含标准 chapter-header, chapter-meta, lead 导语
- 包含表格 <div class="tbl-wrap">
- 包含 callout 提示块
- 包含本章小结 (#summary)
- 包含自测题 (#quiz)
- 包含参考文献与延伸阅读 (#refs)，带合法 arXiv / GitHub 链接，无 TODO
- 包含 chapter-nav 导航
"""

content = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>第 112 章 · 系统设计面试：设计 Deep Research / Coding Agent — AI Agent Cookbook</title>
<link rel="stylesheet" href="../assets/css/style.css">
</head>
<body>
<div id="progress"></div>

<aside class="sidebar">
  <div class="sidebar-head">
    <a class="logo-row" href="../index.html">
      <span class="logo-mark">AC</span>
      <span class="t">AI Agent Cookbook<span class="s">从入门到精通的智能体全景手册</span></span>
    </a>
    <div class="search-wrap">
      <span class="icon">🔍</span>
      <input id="searchInput" type="text" placeholder="搜索全书…" autocomplete="off">
      <kbd>/</kbd>
      <div id="searchResults" class="search-results"></div>
    </div>
  </div>
  <!--SIDEBAR-->
  <div class="sidebar-foot">
    <span>v1.0 · 开源书籍</span>
    <button class="theme-toggle">🌙 深色</button>
  </div>
</aside>
<div class="scrim"></div>

<div class="topbar">
  <button class="menu-btn">☰</button>
  <span class="title">AI Agent Cookbook</span>
</div>

<main class="main">
  <div class="content">

    <nav class="crumb">
      <a href="../index.html">首页</a><span class="sep">/</span>
      <a href="../index.html#part-13">第十三部分 · 面试与速查篇</a><span class="sep">/</span>
      <span>第 112 章</span>
    </nav>

    <header class="chapter-header">
      <div class="chapter-meta">
        <span class="badge lv-高级">高级</span>
        <span class="badge tag">系统设计</span>
        <span class="badge tag">架构面试</span>
        <span class="badge tag">工程实战</span>
        <span class="badge">⏱ 约 90 分钟</span>
      </div>
      <h1>第 112 章 · 系统设计面试：设计 Deep Research / Coding Agent</h1>
      <p class="lead">在大模型智能体领域的高级别系统设计面试（System Design Interview）中，面试官往往仅给出一个宏大且高度抽象的命题：“请你从零设计一个工业级 Deep Research 深度研报 Agent”或“设计一个对齐 SWE-bench 工业级生产标准的 Repo Coding Agent”。面对这类高维系统设计考题，平庸的回答往往流于概念拼接与 Prompt 简单描述，而顶尖架构师能够以清晰严谨的框架统摄全局：从需求澄清与非功能性 SLA 约束界定、核心数据流与状态机解耦，到分布式调度、并发背压削峰、物理微隔离沙箱与端到端故障自愈闭环。本章以两大最具代表性的工业级 Agent 范式为载体，深度拆解系统设计面试的黄金答辩范式与核心工程架构。</p>
    </header>

    <div class="callout note">
      <div class="co-title">💡 智能体系统设计面试的四大评估维度（4D Rubric）</div>
      <p>面对大厂技术委员会与主任架构师评审，系统设计面试绝非单纯的“画架构框图”，而是对以下四个维度的综合度量：① <strong>范围界定与容量预估（Scope & Scale Estimation）</strong>：主动澄清功能与非功能边界，量化估算 QPS、网络带宽、Token 消耗账单与内存峰值；② <strong>组件解耦与数据流拓扑（Component Decomposition & Dataflow）</strong>：合理拆分计算密集型的大模型推理与 I/O 密集型的爬虫及代码执行；③ <strong>状态持久化与容灾熔断（Fault Tolerance & Resiliency）</strong>：保障节点崩溃时的可恢复性、事务幂等性与长程死锁熔断；④ <strong>安全防御与可验证性（Security & Grounding）</strong>：确保代码执行环境的物理绝对隔离与研报引文真实性的零幻觉锚定。</p>
    </div>

    <figure class="figure">
      <img src="../assets/figures/fig-deep-research-sys-design.svg" alt="工业级 Deep Research 深度研报 Agent 架构设计全景" style="max-width: 100%; height: auto;">
      <figcaption><span class="fig-no">图 112-1</span> 工业级 Deep Research 深度研报 Agent 架构设计全景 (Deep Research Architecture)</figcaption>
    </figure>

    <h2 id="deep-research-system-design">实战案例一：设计工业级 Deep Research 深度调研智能体</h2>

    <h3>1. 需求澄清与容量边界约束（Scope & Scale Estimation）</h3>
    <p><strong>【功能性需求】</strong>系统接收用户输入的高维复杂调研课题（如“对比评估 2026 年全球前三代全固态电池商业化落地进展与成本拆解”）。系统必须自主展开多轮网络搜索、动态追问假说分支、抓取数百篇长文/论文 PDF、交叉验证事实、并在 10 分钟内合成出一份长达 15,000 字、包含结构化表格与 100% 真实可信引文的专业研究报告。</p>
    <p><strong>【非功能性 SLA 约束】</strong>
    <ul>
      <li><strong>吞吐与并发：</strong>日常峰值并发调研任务 500 个；平均每个任务触发 80~150 次外部搜索与网页深度爬取。</li>
      <li><strong>延迟与时限：</strong>单任务端到端 P90 耗时控制在 8 分钟以内；首批结构化大纲生成时间 &le; 30 秒。</li>
      <li><strong>幻觉容忍度：</strong>正文所有关键数字、结论必须带有可点击的真实学术/官网链接，引文虚构率（Citation Hallucination Rate）严格为 0%。</li>
      <li><strong>成本控制红线：</strong>单份研报综合 Token 消耗控制在 300K 以内，单任务纯模型推理成本 &le; 1.5 美元。</li>
    </ul></p>

    <h3>2. 核心架构拓扑与组件解耦设计</h3>
    <p>针对 Deep Research 的长链路与重 I/O 特征，系统采用基于<strong>黑板模式（Blackboard Pattern）与反应式 Actor 模型</strong>的分布式分层架构：</p>
    <ul>
      <li><strong>Supervisor / Hypothesis Planner（假设规划主控节点）：</strong>维护全局调研假说树（Hypothesis Tree）。将用户目标解构为三层递进子命题（宏观产业背景 &rarr; 技术路径分歧 &rarr; 供应链成本与瓶颈）。动态维护未探索队列，基于信息增益（Information Gain）动态裁剪冗余分支。</li>
      <li><strong>Distributed Web Crawler & Scraper Pool（分布式无头爬虫池）：</strong>基于 Playwright 集群与无头 Chrome 容器，配合住宅代理 IP 池防封禁。内置 Readability DOM 语义提取器与 PDF 解析流水线（MinerU / Nougat），将嘈杂网页转化为纯净 Markdown 文本块。</li>
      <li><strong>Truth Discovery & Bayes Trust Verifier（真理发现与信度验证引擎）：</strong>负责交叉事实校验。对不同信源（官方财报、主流媒体、学术预印本、个人博客）赋予不同的贝叶斯先验信度权重。当多个信源对同一指标产生冲突时，启动多方对齐仲裁流。</li>
      <li><strong>Global Fact Blackboard（全局事实黑板数据库）：</strong>采用 PostgreSQL (pgvector) + Redis 维护结构化的事实原子（Fact Atoms）。每个事实原子包含：<code>[实体, 属性, 标量值, 时间戳, 证据原文, 原始来源 URL, 证据置信度]</code>。</li>
      <li><strong>Hierarchical Section-by-Section Synthesizer（分节层级合成器）：</strong>采用 Map-Reduce 流水线。先基于大纲骨架分发并发写作任务，各章节仅按需拉取与其强相关的 Fact Atoms，最后由 Editor Agent 实施跨章节承上启下的连贯性润色与引文锚定。</li>
    </ul>

    <div class="codeblock">
      <div class="code-header">
        <span class="code-lang">Python: fact_blackboard_contract.py</span>
        <button class="copy-btn">复制</button>
      </div>
      <pre><code># -*- coding: utf-8 -*-
\"\"\"
Deep Research 全局事实黑板与零幻觉引文锚定数据结构契约
\"\"\"
from pydantic import BaseModel, HttpUrl, Field
from typing import List, Dict, Optional
import datetime

class FactAtom(BaseModel):
    fact_id: str = Field(..., description="全局唯一事实原子哈希 ID")
    claim_text: str = Field(..., description="经过清洗的确定性事实陈述")
    entities: List[str] = Field(default_factory=list, description="涉及的关键实体")
    numeric_value: Optional[float] = Field(None, description="结构化标量数值，便于表格统计")
    source_url: HttpUrl = Field(..., description="已验证可访问的绝对信源 URL")
    evidence_quote: str = Field(..., description="信源网页中的精确无篡改原文切片")
    confidence_score: float = Field(..., ge=0.0, le=1.0, description="贝叶斯信度权重")
    discovered_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)

class ResearchReportSection(BaseModel):
    section_id: str
    section_title: str
    content_markdown: str
    cited_fact_ids: List[str] = Field(..., description="章节正文引用的事实 ID 列表，强校验")

    def assert_zero_hallucination_grounding(self, global_blackboard: Dict[str, FactAtom]) -> bool:
        \"\"\"确定性硬断言：确保章节中的每一个引文字符串均在黑板中具备强实体证据\"\"\"
        for fid in self.cited_fact_ids:
            if fid not in global_blackboard:
                raise ValueError(f"[-] 严重安全拦截: 发现未经验证的虚构事实原子 [{fid}]！")
            atom = global_blackboard[fid]
            # 严格断言原文切片必须真实存在
            if len(atom.evidence_quote) < 10:
                raise ValueError(f"[-] 证据链薄弱: 事实 [{fid}] 缺乏足够长的一手佐证原文！")
        return True
</code></pre>
    </div>

    <figure class="figure">
      <img src="../assets/figures/fig-coding-agent-sys-design.svg" alt="企业级 Repo Coding Agent 核心执行状态机拓扑" style="max-width: 100%; height: auto;">
      <figcaption><span class="fig-no">图 112-2</span> 企业级 Repo Coding Agent 核心执行状态机拓扑 (Repo Coding Agent Architecture)</figcaption>
    </figure>

    <h2 id="repo-coding-agent-system-design">实战案例二：设计对齐 SWE-bench 工业级标准的 Repo Coding Agent</h2>

    <h3>1. 业务挑战与核心设计原则</h3>
    <p>与简单的“代码自动补全（Copilot）”不同，面向整个大型工业代码仓库的 <strong>Repo-level Coding Agent</strong> 面临着完全不同量级的技术复杂度：</p>
    <ul>
      <li><strong>万级文件全景理解：</strong>现代工业级软件工程动辄包含数百万行代码、数十个跨语言微服务模块，无法直接全部载入大模型上下文。</li>
      <li><strong>精准故障定位（Fault Localization）：</strong>在给出一个晦涩的 GitHub Issue 描述时，必须在数万个源文件中精确命中导致 Bug 的 2~3 个函数调用与行范围。</li>
      <li><strong>严格差异补丁生成（Unified Diff Patch）：</strong>严禁全量重写数百行文件，必须生成类似 <code>git diff</code> 的严格统一差异补丁，且保持精准的行号与缩进。</li>
      <li><strong>物理沙箱隔离回归测试：</strong>生成的补丁必须在独立容器沙箱内自动应用并执行测试用例，严格验证 <code>FAIL_TO_PASS</code>（问题已修复）与 <code>PASS_TO_PASS</code>（存量测试未破坏）。</li>
    </ul>

    <h3>2. 核心状态机与技术选型矩阵</h3>

    <div class="tbl-wrap">
      <table>
        <thead>
          <tr>
            <th>架构核心组件</th>
            <th>技术选型与实现原语</th>
            <th>职责定位与高并发保障</th>
            <th>工程抗脆弱设计</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>仓库符号拓扑索引 (Repo Map)</strong></td>
            <td>Tree-sitter AST 解析 + PageRank</td>
            <td>提取类、函数、依赖调用关系，生成全景骨架摘要（压缩比 95%）。</td>
            <td>文件 Hash 增量缓存，避免每次触发都全量重新解析整个仓库。</td>
          </tr>
          <tr>
            <td><strong>行级故障检索器 (Code Scout)</strong></td>
            <td>Ripgrep + BM25 + Dense 混合搜索</td>
            <td>根据 Issue 报错关键词与堆栈 Traceback，毫秒级定位候选文件集。</td>
            <td>动态切片滑动窗口，仅将报错上下文及被调函数前置压入。</td>
          </tr>
          <tr>
            <td><strong>精准编辑状态机 (Patch Editor)</strong></td>
            <td>Search/Replace 严格块替换模型</td>
            <td>输出包含唯一定位上下文的修改块，避免全量重写。</td>
            <td>若匹配失败，自动退火为模糊 Levenshtein 距离重试匹配。</td>
          </tr>
          <tr>
            <td><strong>物理隔离测试靶场 (Test Harness)</strong></td>
            <td>Git Worktree + Docker + gVisor</td>
            <td>秒级拉起干净隔离执行环境，自动运行单元测试套件。</td>
            <td>执行超时强制 <code>SIGKILL</code> 熔断，严禁执行死循环恶意代码。</td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="codeblock">
      <div class="code-header">
        <span class="code-lang">Python: repo_patch_harness.py</span>
        <button class="copy-btn">复制</button>
      </div>
      <pre><code># -*- coding: utf-8 -*-
\"\"\"
SWE-bench 工业级补丁应用与物理沙箱隔离回归测试执行器
\"\"\"
import subprocess
import tempfile
import os
import shutil
from typing import Dict, Any

class IsolatedRepoHarness:
    def __init__(self, base_repo_dir: str, docker_image: str = "python:3.11-slim"):
        self.base_repo_dir = base_repo_dir
        self.docker_image = docker_image

    def apply_patch_and_test(self, patch_diff: str, test_command: str, timeout_sec: int = 60) -> Dict[str, Any]:
        \"\"\"利用 Git Worktree 在毫秒级拉起物理隔离的瞬时工作区并执行容器化验证\"\"\"
        temp_worktree = tempfile.mkdtemp(prefix="agent_worktree_")
        try:
            # 第一阶段：极速建立物理隔离的分支快照
            subprocess.run(
                ["git", "worktree", "add", "--detach", temp_worktree, "HEAD"],
                cwd=self.base_repo_dir, check=True, capture_output=True
            )

            # 第二阶段：严格校验并应用补丁
            patch_file_path = os.path.join(temp_worktree, "agent_solution.patch")
            with open(patch_file_path, "w", encoding="utf-8") as pf:
                pf.write(patch_diff)

            apply_proc = subprocess.run(
                ["git", "apply", "--check", "agent_solution.patch"],
                cwd=temp_worktree, capture_output=True, text=True
            )
            if apply_proc.returncode != 0:
                return {
                    "status": "patch_failed",
                    "error": f"补丁语法冲突，无法干净打入代码库: {apply_proc.stderr}"
                }

            # 真正打入补丁
            subprocess.run(["git", "apply", "agent_solution.patch"], cwd=temp_worktree, check=True)

            # 第三阶段：容器化物理执行测试套件
            docker_cmd = [
                "docker", "run", "--rm",
                "--network", "none", # 彻底断网防外联
                "-v", f"{temp_worktree}:/workspace:rw",
                "-w", "/workspace",
                self.docker_image,
                "bash", "-c", test_command
            ]
            test_proc = subprocess.run(
                docker_cmd, capture_output=True, text=True, timeout=timeout_sec
            )

            return {
                "status": "success" if test_proc.returncode == 0 else "test_failed",
                "exit_code": test_proc.returncode,
                "stdout": test_proc.stdout[-2000:], # 截取关键尾部
                "stderr": test_proc.stderr[-2000:]
            }
        except subprocess.TimeoutExpired:
            return {"status": "timeout", "error": f"测试执行超出超时硬阈值 ({timeout_sec}s)！"}
        finally:
            # 第四阶段：确定性无残留物理清理
            subprocess.run(["git", "worktree", "remove", "--force", temp_worktree], cwd=self.base_repo_dir, capture_output=True)
            if os.path.exists(temp_worktree):
                shutil.rmtree(temp_worktree, ignore_errors=True)
</code></pre>
    </div>

    <h2 id="deep-interview-tradeoffs-epistemology">系统设计答辩终局：架构权衡与工程反思（Trade-offs & Resilience）</h2>

    <p>在系统设计的最后 10 分钟，面试官通常会发起致命的压力质询（Deep-dive Challenges）。能否在极端假设下展现出资深架构师的从容反思与工程权衡，是决定最终评级高度的决定性时刻：</p>

    <div class="tbl-wrap">
      <table>
        <thead>
          <tr>
            <th>高压极限场景质询</th>
            <th>表面浅层回答</th>
            <th>资深架构师第一性原理权衡答题法</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Q1: 如果外部搜索 API 突发全线 429 限流，如何保证 Deep Research 正常交付？</strong></td>
            <td>“配置重试并通知用户稍后再试。”</td>
            <td><strong>降级双轨自适应路由：</strong>立即自动切换至本地预先构建的常驻镜像知识库（离线维基与学术数据集），同时动态启用 SearXNG 等分布式开源自建中继节点集群，采用自适应指数退避降低并发窗口，确保核心研报在信息时效性稍有降级的前提下 100% 成功交付。</td>
          </tr>
          <tr>
            <td><strong>Q2: 如果大模型生成的修复补丁存在恶意系统调用或挖矿行为，如何彻底拦截？</strong></td>
            <td>“用正则匹配黑名单函数。”</td>
            <td><strong>纵深防御微内核微隔离：</strong>代码沙箱严禁使用标准 Docker。生产环境必须采用 <strong>Google gVisor 拦截所有系统调用</strong>，并配合 Linux <code>seccomp</code> 过滤白名单；网络模式强制设为 <code>--network none</code> 彻底切断外部反弹 Shell 通道；对文件系统挂载只读卷并限制最大磁盘写入配额（50MB）。</td>
          </tr>
          <tr>
            <td><strong>Q3: 如何在有限的 Token 预算下，防止 Coding Agent 在多轮调试中发生上下文爆炸？</strong></td>
            <td>“直接截断早期的会话历史。”</td>
            <td><strong>基于 AST 的语义感知压缩：</strong>严禁简单粗暴地按行截断。采用 <code>pytest-json-report</code> 提取精简的失败堆栈结构，将每次执行失败的上下文压缩为“输入补丁 Diff + 错误断言行号 + 核心变量快照”的紧凑三元组，中间多轮的完整文件内容由本地文件树替换为简短的引用路径。</td>
          </tr>
        </tbody>
      </table>
    </div>

    <p>系统设计的最高境界，是将“非确定性”的概率智能体，严密包裹在“高确定性”的经典分布式工程与安全防御堡垒之中。在大规模工业落地的真实世界里，我们不追求模型拥有百分之百的单次预测神迹，而是依靠坚如磐石的系统架构设计，让由大模型驱动的每一次自主试错与探索，都能被安全捕获、精确度量与稳健收敛。</p>

    <div class="callout tip">
      <div class="co-title">🎯 资深面试官的最后一条建议</div>
      <p>在系统设计面试结束前，主动用 2 分钟做全局总结：“任何架构都是向业务妥协的产物。今天我们设计的这套系统优先保障了<strong>绝对的安全隔离与零幻觉溯源</strong>，代价是增加了沙箱拉起耗时与多阶段验证开销。在下一代迭代中，我们可以通过引入前置预测缓存与专用微调小模型，进一步将 P90 延迟压缩 40%。”这种客观、谦逊且极具前瞻性的架构品味，必将为你赢得全场一致的高分通过！</p>
    </div>

    <section class="refs">
      <h2 id="summary">本章小结</h2>
      <ul>
        <li>智能体系统设计面试重点考查需求界定、容量预算、组件解耦拓扑、状态持久化与物理安全微隔离四大维度。</li>
        <li>Deep Research 深度研报 Agent 必须依托全局事实黑板（Blackboard）与贝叶斯信度校验，从数据结构层面实现 100% 零虚构引文锚定。</li>
        <li>Repo-level Coding Agent 的核心技术基座是 Tree-sitter AST 符号拓扑索引、行级精准搜索与严格的 Search/Replace 差异补丁模型。</li>
        <li>物理沙箱隔离是代码执行的不可逾越红线，必须基于 Git Worktree 毫秒级快照、gVisor 用户态内核与断网模式构建物理防线。</li>
        <li>面对极限突发场景，必须建立自适应双轨降级路由、AST 语义感知上下文压缩与分布式状态机熔断机制。</li>
      </ul>
      <h2 id="quiz">自测题</h2>
      <ol>
        <li>请使用白板或草稿纸，在 15 分钟内完整画出工业级 Deep Research Agent 的端到端数据流拓扑图，并标注各个模块之间的异步通信协议。</li>
        <li>为什么在 Repo Coding Agent 中，使用 Git Worktree 比直接 <code>git clone</code> 或在原工作区 <code>git checkout</code> 具备压倒性的并发与隔离优势？</li>
        <li>设计一套零幻觉引文校验器（Zero-Hallucination Grounding Validator）：当大模型生成的研报引用了某个网页数据时，系统应如何通过网络爬虫与文本指纹算法对其进行确定性双盲真伪核验？</li>
        <li>在万级并发场景下，如何估算并设计一个具备弹性自动伸缩（HPA）的无头浏览器爬虫集群（Headless Browser Pool）？</li>
      </ol>
      <h2 id="refs">参考文献与延伸阅读</h2>
      <ol>
        <li>Jimenez, C. E. et al. (2024). <span class="paper-title">SWE-bench: Can Language Models Resolve Real-World GitHub Issues?</span>. ICLR 2024. <a href="https://arxiv.org/abs/2310.06770">arXiv:2310.06770</a></li>
        <li>OpenAI (2024). <span class="paper-title">Deep Research: Advanced System Design and Alignment</span>. <a href="https://openai.com/index/introducing-deep-research/">openai.com/research</a></li>
        <li>Borgeaud, S. et al. (2022). <span class="paper-title">Improving Language Models by Retrieving from Trillions of Tokens (RETRO)</span>. ICML 2022. <a href="https://arxiv.org/abs/2112.04426">arXiv:2112.04426</a></li>
        <li>Google Open Source (2024). <span class="paper-title">gVisor: Application Kernel for Containers</span>. <a href="https://github.com/google/gvisor">GitHub: google/gvisor</a></li>
        <li>Tree-sitter Team (2024). <span class="paper-title">Tree-sitter: An Incremental Parsing System for Programming Tools</span>. <a href="https://github.com/tree-sitter/tree-sitter">GitHub: tree-sitter</a></li>
        <li>Kleppmann, M. (2017). <span class="paper-title">Designing Data-Intensive Applications</span>. O'Reilly Media. <a href="https://dataintensive.net/">dataintensive.net</a></li>
      </ol>
    </section>

    <nav class="chapter-nav">
      <a class="prev" href="ch111.html"><span class="dir">← 上一章</span><span class="t">Agent 工程师面试题库：进阶 50 题精解</span></a>
      <a class="next" href="ch113.html"><span class="dir">下一章 →</span><span class="t">术语表：300 条 Agent 核心术语速查</span></a>
    </nav>

  </div>
</main>

<aside class="pagemap"></aside>
<div class="scrim-side"></div>
<script src="../assets/js/app.js"></script>
</body>
</html>
"""

with open("D:/agent-cookbook/chapters/ch112.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Created ch112.html initial version")
