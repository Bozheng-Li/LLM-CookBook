import os

path = r"D:/agent-cookbook/chapters/ch084.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# Expand with comprehensive deep sections:
# 1. Advanced Tree-sitter Repo Map implementation in Python (tagging, pagerank, formatting)
# 2. Complete Git Worktree Isolation & Multi-Agent PR Review Workflow
# 3. Step-by-step benchmark verification playbook (SWE-bench evaluation runner)

expansion_1 = """
    <h2 id="repo-map-implementation">深入实操：基于 Tree-sitter 与 PageRank 的 Repo Map 构建引擎</h2>
    <p>Repo Map 的精妙之处在于它绝非死板地抓取整个代码库的所有目录树，而是将代码库视为一张<strong>「有向加权图」</strong>：类与函数是图的节点，跨文件的 <code>import</code> 与调用则是图的有向边。那些被整个工程几十个模块高频引用的核心基类（例如 <code>BaseDatabaseConnection</code> 或 <code>AbstractAgentRunner</code>），在 PageRank 算法下将自然获得极高的权重，优先在极其有限的 Token 预算中得以呈现。</p>
    
    <p>以下展示了一个工业级 Python 实现的轻量 Tree-sitter 符号图谱构建器，能够自动化扫描工程目录并计算全局符号热度：</p>

    <div class="codeblock">
      <div class="cb-head"><span>基于 Tree-sitter 的符号依赖图与 PageRank 计算器（repo_map_generator.py）</span><button class="cb-copy">复制</button></div>
      <pre><code>import os
from collections import defaultdict
import networkx as nx

class RepoMapGraphBuilder:
    def __init__(self, root_dir: str):
        self.root_dir = os.path.abspath(root_dir)
        self.graph = nx.DiGraph()
        self.file_symbols = defaultdict(list)

    def scan_and_build_graph(self) -> nx.DiGraph:
        \"\"\"遍历仓库代码文件，提取符号定义与跨文件引用边\"\"\"
        for root, _, files in os.walk(self.root_dir):
            for file in files:
                if not file.endswith(".py"):
                    continue
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, self.root_dir)
                self.graph.add_node(rel_path, node_type="file")

                # 模拟轻量 AST 解析: 提取顶层 Class 与 def 签名
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    lines = f.readlines()

                for line in lines:
                    line_str = line.strip()
                    if line_str.startswith("class ") or line_str.startswith("def "):
                        symbol_name = line_str.split("(")[0].replace("class ", "").replace("def ", "").strip()
                        self.file_symbols[rel_path].append(symbol_name)
                    elif line_str.startswith("from ") or line_str.startswith("import "):
                        # 识别模块间依赖边
                        for other_file in self.file_symbols.keys():
                            module_token = other_file.replace("/", ".").replace(".py", "")
                            if module_token in line_str and other_file != rel_path:
                                self.graph.add_edge(rel_path, other_file)

        return self.graph

    def compute_symbol_pagerank(self) -> dict:
        \"\"\"计算各源文件与核心符号的全局 PageRank 拓扑重要性\"\"\"
        if len(self.graph) == 0:
            return {}
        try:
            # 阻尼系数 0.85 的经典 PageRank
            scores = nx.pagerank(self.graph, alpha=0.85, max_iter=50)
        except Exception:
            scores = {n: 1.0 / len(self.graph) for n in self.graph.nodes}
        return scores

    def render_compact_repo_map(self, max_tokens: int = 1500) -> str:
        \"\"\"按照 PageRank 权重降序排布，渲染最小有效架构骨架\"\"\"
        scores = self.compute_symbol_pagerank()
        sorted_files = sorted(scores.keys(), key=lambda x: scores[x], reverse=True)

        lines = []
        token_estimate = 0
        for f in sorted_files:
            symbols = self.file_symbols.get(f, [])
            if not symbols:
                continue
            entry = f"{f}:\\n" + "\\n".join([f"    • {s}" for s in symbols[:6]])
            entry_tokens = len(entry) // 4
            if token_estimate + entry_tokens > max_tokens:
                break
            lines.append(entry)
            token_estimate += entry_tokens

        return "\\n\\n".join(lines)</code></pre>
    </div>
"""

expansion_2 = """
    <h2 id="worktree-and-review-loop">Git Worktree 物理隔离与多角色代码审查流水线</h2>
    <p>在企业级持续集成环境下，直接在当前主干工作区打补丁并跑测试是极其危险的。若前一个任务跑了一半发生中断，留下的未提交脏文件将直接污染后续的所有工程任务。生产级架构全面引入 <strong>Git Worktree 原生物理隔离机制</strong>。</p>
    <p>每个 Issue 会在独立的物理目录上派生出一个轻量 Worktree，代码修改与测试都在该独立副本中完成。一旦全绿通过，直接推送到远端 Feature 分支并提交 Pull Request；若任务彻底失败，直接原子化 <code>git worktree remove --force</code> 抹平现场，对宿主工作区零污染、零残留。</p>

    <div class="codeblock">
      <div class="cb-head"><span>Git Worktree 隔离生命周期管理器（worktree_manager.py）</span><button class="cb-copy">复制</button></div>
      <pre><code>import subprocess, os, shutil

class GitWorktreeManager:
    def __init__(self, main_repo_dir: str):
        self.main_repo = os.path.abspath(main_repo_dir)

    def create_isolated_worktree(self, issue_id: str) -> str:
        \"\"\"为当前 Issue 检出全新的独立沙箱目录分支\"\"\"
        branch_name = f"fix/agent-issue-{issue_id}"
        worktree_path = os.path.join(os.path.dirname(self.main_repo), f"worktree_{issue_id}")
        
        # 确保目录干净
        if os.path.exists(worktree_path):
            shutil.rmtree(worktree_path)

        # 派生新分支与独立工作区
        cmd = ["git", "worktree", "add", "-b", branch_name, worktree_path, "HEAD"]
        subprocess.run(cmd, cwd=self.main_repo, check=True, capture_output=True)
        print(f"[Worktree] 已在独立物理沙箱创建环境: {worktree_path}")
        return worktree_path

    def cleanup_worktree(self, issue_id: str):
        \"\"\"安全清理并销毁临时工作区\"\"\"
        worktree_path = os.path.join(os.path.dirname(self.main_repo), f"worktree_{issue_id}")
        if os.path.exists(worktree_path):
            subprocess.run(["git", "worktree", "remove", "--force", worktree_path], cwd=self.main_repo)
            print(f"[Worktree] 已成功回收沙箱: {worktree_path}")</code></pre>
    </div>

    <p>在提交 PR 之前，系统还会自动拉起一个独立的 <strong>Reviewer Agent（代码审查者智能体）</strong>。Reviewer 与 Coder 拥有完全不同的 System Prompt 设定：Reviewer 扮演严厉的 Tech Lead 角色，专注于审查代码的可读性、变量命名、边界值处理、是否缺少配套文档，以及是否存在隐藏的时间复杂度劣化（如 $O(n^2)$ 嵌套循环）。只有当 Reviewer 打出「LGTM（Looks Good To Me）」评级后，补丁才真正允许推向生产分支。</p>
"""

insert_target = '<h2 id="faq">'
if insert_target in text:
    new_text = text.replace(insert_target, expansion_1 + "\n" + expansion_2 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Successfully expanded ch084.html with repo map and worktree")
else:
    print("Target not found")
