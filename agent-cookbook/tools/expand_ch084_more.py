import os

path = r"D:/agent-cookbook/chapters/ch084.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

expansion_3 = """
    <h2 id="swe-bench-harness">工业级评测实战：构建本地 SWE-bench 自动化测试流水线</h2>
    <p>为了精准度量软件工程智能体在处理真实生产 Issue 时的工业可用度，团队必须搭建贴合实际工程环境的持续评测流水线。SWE-bench（Software Engineering Benchmark）精选了来自开源社区（如 <code>django, sympy, flask, requests, scikit-learn</code>）成千上万个真实的 GitHub PR 与 Issue 案例。在本地评测套件中，系统不仅需要评测补丁能否打入，更需要严格验证两大核心黄金断言：</p>
    
    <p><strong>① PASS_TO_PASS（防退化不变性检验）：</strong>原本在基线版本上就能够通过的所有单元测试用例，在应用 Agent 生成的代码补丁后，必须仍然 100% 保持通过。任何引发旧功能测试红灯的代码修改，将被直接判为 0 分并判定为引入了严重回归缺陷。</p>
    <p><strong>② FAIL_TO_PASS（缺陷精准修复检验）：</strong>原工单作者为复现该 Issue 专门编写的全新测试用例（在修复前原本断言失败），在打入补丁后必须全部成功转绿，证明 Bug 确实被根治而非仅仅绕过。</p>

    <div class="codeblock">
      <div class="cb-head"><span>SWE-bench 本地轻量化评估脚本（swe_evaluator.py）</span><button class="cb-copy">复制</button></div>
      <pre><code>import json, subprocess
from typing import Dict, Any

class SWEBenchLocalHarness:
    def __init__(self, task_metadata_path: str):
        with open(task_metadata_path, "r", encoding="utf-8") as f:
            self.tasks = json.load(f)

    def evaluate_task_patch(self, repo_path: str, task: Dict[str, Any], agent_patch: str) -> Dict[str, Any]:
        \"\"\"在容器内执行严谨的双向回归检验 (FAIL_TO_PASS & PASS_TO_PASS)\"\"\"
        # 1. 应用 Agent 提交的 Git Diff 补丁
        patch_file = "/tmp/agent.patch"
        with open(patch_file, "w", encoding="utf-8") as f:
            f.write(agent_patch)

        apply_cmd = ["git", "apply", "--whitespace=fix", patch_file]
        res = subprocess.run(apply_cmd, cwd=repo_path, capture_output=True, text=True)
        if res.returncode != 0:
            return {"resolved": False, "reason": f"Patch application failed: {res.stderr}"}

        # 2. 运行 FAIL_TO_PASS 新增用例测试 (验证缺陷是否真正被根除)
        test_cmd = f"pytest {task['test_patch_target']} -q"
        test_run = subprocess.run(test_cmd, shell=True, cwd=repo_path, capture_output=True, text=True)
        if test_run.returncode != 0:
            return {"resolved": False, "reason": "Target bug test still failing"}

        # 3. 运行全量原有基线回归测试 (验证无功能退化)
        base_cmd = "pytest tests/base/ -q"
        base_run = subprocess.run(base_cmd, shell=True, cwd=repo_path, capture_output=True, text=True)
        if base_run.returncode != 0:
            return {"resolved": False, "reason": "Regression detected: Base tests broken!"}

        print(f"✅ 任务 {task['instance_id']} 完美解决！双向断言全部绿灯！")
        return {"resolved": True, "reason": "All assertions satisfied"}</code></pre>
    </div>

    <p>在日常迭代时，架构团队应为 Repo Agent 建立自动化每日构建看板（Daily Build Board），监控其在 Python、TypeScript、Go 等多种主力技术栈上的一次性成功率与平均修复时长。通过不断在真枪实弹的开源 Issue 中磨砺，代码智能体才能从「只能写写算法题的玩具」真正蜕变为能够独立值守运维、自动提 PR 修复线上生产告警的虚拟工程师。</p>
"""

insert_target = '<h2 id="faq">'
if insert_target in text:
    new_text = text.replace(insert_target, expansion_3 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added SWE-bench harness section")
else:
    print("Target not found")
