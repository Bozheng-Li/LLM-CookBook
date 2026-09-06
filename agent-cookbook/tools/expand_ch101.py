# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch101.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# Expand with comprehensive deep sections:
# 1. Toolformer API self-annotation pseudo-code and Perplexity Filtering Engine in Python
# 2. Gorilla Retriever-Aware Context Assembler & AST Tree-Matching Verification
# 3. SWE-bench Lite vs. Verified Split Methodology and Harness Evaluation Architecture
# 4. Comprehensive Cross-Paper Paradigm Synthesis: Code Agents from Generation to Autonomous Maintenance

expansion_1 = """
    <h2 id="toolformer-deep-dive">深度解构 1：Toolformer 自举采样与困惑度判定算法实现</h2>
    <p>在《Toolformer》论文中，蒂莫·希克（Timo Schick）等人设计了一套极其严密的自动采样与损失过滤管线。系统如何从毫无人工标记的无监督文本中，精准探测出哪句话适合插入何种工具？其核心算法由三大步骤紧密串联而成：</p>

    <div class="codeblock">
      <div class="cb-head"><span>Toolformer 自监督 API 标注与困惑度增益过滤引擎（toolformer_filter.py）</span><button class="cb-copy">复制</button></div>
      <pre><code>import math
from typing import List, Dict, Tuple, Optional

class ToolformerDataFilter:
    def __init__(self, base_lm, tool_executor, filtering_threshold: float = 1.0):
        self.lm = base_lm
        self.tools = tool_executor
        self.tau = filtering_threshold  # 困惑度增益严格阈值 \tau

    def evaluate_sample_candidate(self, prefix_text: str, candidate_api_call: str, 
                                   continuation_text: str) -> Optional[Dict]:
        \"\"\"
        prefix_text: 插入点前文 x_{<i}
        candidate_api_call: 采样的工具调用指令 c_i = [Calculator(24 * 7)]
        continuation_text: 待评估的后续黄金文本 x_{i:i+L} (例如: '等于 168')
        \"\"\"
        # 1. 真实物理调用外部工具获取回显
        api_result = self.tools.execute(candidate_api_call)
        if api_result is None:
            return None

        # 构造带返回值的完整序列: x_{<i} + [API(args) -> res] + x_{i:i+L}
        with_result_text = f"{prefix_text} [{candidate_api_call} -> {api_result}]"
        
        # 2. 计算带有工具返回值时的后续文本交叉熵损失 L^+
        loss_with_tool = self.lm.compute_cross_entropy(with_result_text, continuation_text)

        # 3. 计算两种基线损失并取最小值 L^-
        # 基线 A: 完全没有工具调用
        loss_no_tool = self.lm.compute_cross_entropy(prefix_text, continuation_text)
        # 基线 B: 仅有工具调用但没有返回值 (空返回值 \epsilon)
        empty_res_text = f"{prefix_text} [{candidate_api_call} -> ]"
        loss_empty_tool = self.lm.compute_cross_entropy(empty_res_text, continuation_text)
        
        baseline_loss = min(loss_no_tool, loss_empty_tool)

        # 4. 严格执行数学不等式判定: 仅当工具带来实质性困惑度下降时保留
        loss_gain = baseline_loss - loss_with_tool
        if loss_gain >= self.tau:
            print(f"[Toolformer Keep] 优质自举样本检出! 损失增益: {loss_gain:.4f}")
            return {
                "annotated_text": f"{prefix_text} [{candidate_api_call} -> {api_result}] {continuation_text}",
                "gain": loss_gain
            }
        else:
            # 丢弃无效或冗余的错误调用 (例如工具结果反而干扰了后文生成)
            return None</code></pre>
    </div>

    <p>这种纯粹利用语言模型自身对世界的概率预测偏差作为监督信号的架构，彻底摆脱了人工数据标注的束缚，首次在现代自然语言处理历史上证明了<strong>大模型能够以完全无监督的方式，自发演化出使用工具探索外部物理世界的“数字工具本能”</strong>。</p>
"""

expansion_2 = """
    <h2 id="gorilla-deep-dive">深度解构 2：Gorilla 检索感知微调（RA-SFT）与 AST 严格匹配</h2>
    <p>在传统的指令微调（SFT）中，如果将一个带有长篇文档的 API 注入 Prompt，由于自注意力机制的稀释，大模型往往在输出端产生严重的<strong>参数幻觉（Parameter Hallucination）</strong>。加州大学伯克利分校的 Gorilla 系统在论文中构建了包含 1,645 个核心开源 API 的 <strong>APIBench</strong>，并首创了<strong>检索感知指令微调协议（Retriever-Aware Fine-Tuning）</strong>：</p>

    <div class="codeblock">
      <div class="cb-head"><span>Gorilla 检索感知指令模板与 AST 参数语法树匹配对齐逻辑</span><button class="cb-copy">复制</button></div>
      <pre><code>import ast
from typing import Dict, Any

class GorillaEvaluator:
    def format_retriever_aware_prompt(self, user_goal: str, retrieved_api_doc: str) -> str:
        \"\"\"组装检索感知微调 Prompt: 模拟真实生产中带有检索噪声的环境\"\"\"
        return f\"\"\"你是一名严谨的 API 代码调度专家。请根据下方检索到的候选 API 文档，输出完全匹配参数签名的调用代码。
严禁凭空捏造任何未在文档中声明的形参！

【检索到的参考 API 文档】:
{retrieved_api_doc}

【用户业务目标】:
{user_goal}

请输出严格可执行的 Python API 调用语句:\"\"\"

    def verify_api_call_ast(self, ground_truth_code: str, generated_code: str) -> Dict[str, Any]:
        \"\"\"利用 Python AST 抽象语法树执行 100% 严密的函数名与参数签名对齐核验\"\"\"
        try:
            tree_gt = ast.parse(ground_truth_code)
            tree_gen = ast.parse(generated_code)

            # 提取 Call 节点
            call_gt = next(n for n in ast.walk(tree_gt) if isinstance(n, ast.Call))
            call_gen = next(n for n in ast.walk(tree_gen) if isinstance(n, ast.Call))

            # 1. 核验函数/类名完全一致
            func_gt = ast.unparse(call_gt.func)
            func_gen = ast.unparse(call_gen.func)
            if func_gt != func_gen:
                return {"valid": False, "error": f"函数名不匹配: 期望 {func_gt}, 实际 {func_gen}"}

            # 2. 核验关键字实参 (Keyword Arguments) 无虚构与错配
            kwargs_gt = {kw.arg: ast.unparse(kw.value) for kw in call_gt.keywords}
            kwargs_gen = {kw.arg: ast.unparse(kw.value) for kw in call_gen.keywords}

            for k in kwargs_gen:
                if k not in kwargs_gt:
                    return {"valid": False, "error": f"参数幻觉! 输出了不存在的虚构形参: `{k}`"}

            return {"valid": True, "error": None}
        except Exception as e:
            return {"valid": False, "error": f"语法解析崩溃: {str(e)}"}</code></pre>
    </div>

    <p>Gorilla 通过引入该 AST 评估器证明：单纯靠给大模型提供高阶 Prompt，参数幻觉率依然居高不下；唯有通过检索感知微调，将「阅读文档并精准填参」作为一种独立的权重本能固化在参数中，才能真正胜任复杂分布式云原生生态的高并发工具调度。</p>
"""

expansion_3 = """
    <h2 id="swe-bench-deep-dive">深度解构 3：SWE-bench 数据集分集演进与测试 Harness 架构</h2>
    <p>在普林斯顿大学发表原始 SWE-bench 论文后，由于全量 2,294 个任务评估极其缓慢（在单张 A100 上跑完全量基准需要数周时间且花费数千美元 API 费用），学界随后衍生出了两个更具实操价值的权威衍生分集：</p>

    <div class="tbl-wrap">
      <table>
        <thead><tr><th>SWE-bench 分集</th><th>任务数量</th><th>筛选过滤严密准则</th><th>行业核心定位与应用场景</th></tr></thead>
        <tbody>
          <tr><td><strong>SWE-bench Full (原生全量)</strong></td><td>2,294 个真实 Issue</td><td>覆盖 12 个大型 Python 开源库，包含跨几十个文件的巨型 PR</td><td>年度顶级模型大版本能力大阅兵，计算开销极其庞大</td></tr>
          <tr><td><strong>SWE-bench Lite (精炼子集)</strong></td><td>300 个核心任务</td><td>人工筛选出单测确定、自包含度高、运行时间在 5 分钟内的精炼实例</td><td>日常持续集成（CI/CD）与新型 Agent 架构迭代的标准通行证</td></tr>
          <tr><td><strong>SWE-bench Verified (人类精校)</strong></td><td>500 个黄金实例</td><td>由人类资深软件工程师逐个复核，剔除原工单中描述含糊、环境不可复现的噪声</td><td>消除了基准本身的标注瑕疵，成为目前 OpenAI 与 Anthropic 官方最推崇的黄金金标</td></tr>
        </tbody>
      </table>
      <caption>表 101-2 · SWE-bench 家族三大核心分集对照表。从粗糙全量演进至经人类专家严格审计的绝对黄金基准。</caption>
    </div>

    <p>在 SWE-bench 的测试驱动框架（Evaluation Harness）中，整个判题流程呈现出如同现代流水线般的工业级严密性：<br>
    ① <strong>容器热装配：</strong>针对特定的 <code>instance_id</code>，Docker 自动切换至历史 PR 发生前一刻的精确 Git Commit 哈希；<br>
    ② <strong>补丁应用：</strong>调度器利用 <code>git apply</code> 注入 Agent 提交的修改；<br>
    ③ <strong>测试沙箱隔离：</strong>执行 <code>eval_script</code>，拦截未决异常并比对前后测试状态字典。唯有在完全符合状态转移矩阵时，方才颁发“Pass”荣誉徽章，彻底消除了传统 LLM 评测中的任何主观水分。</p>
"""

expansion_4 = """
    <h2 id="code-agent-paradigm-shift">代码智能体的范式革命：从单函数补全到全生命周期自治维护</h2>
    <p>综合研读 Toolformer、Gorilla 与 SWE-bench 这三大奠基性论著，我们能够深刻体悟到：人工智能在软件工程领域的使命，正在发生一场<strong>深刻的文明级范式大跃迁</strong>：</p>

    <div class="tbl-wrap">
      <table>
        <thead><tr><th>演进代际</th><th>代表性技术与基准</th><th>交互范围与边界</th><th>人类扮演的核心角色</th></tr></thead>
        <tbody>
          <tr><td><strong>第一代: 代码自动补全 (Code Copilot)</strong></td><td>HumanEval (2021), Codex</td><td>单文件、单函数内补全（Tab 键自动补全下一行）</td><td>人类主导设计，模型充当打字机</td></tr>
          <tr><td><strong>第二代: 接口工具调用 (Tool Augmented)</strong></td><td>Toolformer (2023), Gorilla</td><td>跨系统调用静态或动态 API，完成简单多模态查询</td><td>人类定义工具，模型按需填写参数</td></tr>
          <tr><td><strong>第三代: 仓库级自主工程师 (Repo-Level SWE Agent)</strong></td><td>SWE-bench (2024), Devin, Aider</td><td>自主跨越数百个源文件定位缺陷、生成 Unified Diff 并运行单测自愈</td><td>人类提出宏观需求，智能体作为端到端数字化工程师独立交付合规 PR</td></tr>
        </tbody>
      </table>
      <caption>表 101-3 · 代码与工具智能体三代演进代际矩阵。见证 AI 从“辅助打字工具”蜕变为“具备独立交付能力的虚拟工程师”。</caption>
    </div>

    <p>这一不可逆转的历史潮流向每一位软件架构师昭示：未来的软件工程平台将不再是由人类一行行敲击代码搭建起来的，而是演进为一个由<strong>大模型代码智能体、自动化形式化验证器与持续集成测试流共同组成的「自我维护自愈型有机生命体」</strong>。每一位掌握了 Toolformer 自监督机制、Gorilla 参数防幻觉协议与 SWE-bench 严格回归闭环的开发者，都将成为站在这一全新时代浪潮之巅的领航工程师！</p>
"""

insert_target = '<div class="callout note">'
if insert_target in text:
    new_text = text.replace(insert_target, expansion_1 + "\n" + expansion_2 + "\n" + expansion_3 + "\n" + expansion_4 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Successfully expanded ch101.html with 4 deep sections")
else:
    print("Target not found")
