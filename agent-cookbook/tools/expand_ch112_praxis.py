# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch112.html"

with open(path, "r", encoding="utf-8") as f:
    text = f.read()

deep_praxis_sections = """
    <h2 id="deep-research-verification-harness">深度研报质量评估体系与自动化裁判（Evals & Auto-Judge）</h2>
    <p>在设计 Deep Research 这类开放域生成智能体时，最困难的系统挑战是如何在离线和线上持续度量研报的质量与真实性。传统的 BLEU 或 ROUGE 等词汇重叠指标在此类长篇研报生成任务中完全失效。我们必须构建一套<strong>多维度量化自动裁判矩阵（Multi-Dimensional Auto-Judge Matrix）</strong>：</p>

    <div class="tbl-wrap">
      <table>
        <thead>
          <tr>
            <th>评测评估维度</th>
            <th>定义与度量物理含义</th>
            <th>自动化判定方法与工程实现</th>
            <th>工业合格红线门槛</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>事实忠实度 (Faithfulness)</strong></td>
            <td>研报中陈述的事实是否完全源自一手检索证据，有无脑补。</td>
            <td>NLI（自然语言推理）蕴含模型逐句断言检测，计算蕴含比例。</td>
            <td>$\ge 98\%$（严禁任何关键数值或主语虚构）。</td>
          </tr>
          <tr>
            <td><strong>论点完备度 (Completeness)</strong></td>
            <td>是否全面覆盖用户意图所涉及的核心技术路线与产业环节。</td>
            <td>基于黄金行业专家知识图谱进行实体覆盖度（Recall）计算。</td>
            <td>$\ge 85\%$ 的核心实体与关键指标覆盖。</td>
          </tr>
          <tr>
            <td><strong>逻辑连贯性 (Coherence)</strong></td>
            <td>章节间转折、论据论点承接是否自然流畅，有无前后自相矛盾。</td>
            <td>跨章节主张（Claims）矛盾图谱检测，计算图拓扑冲突环路数。</td>
            <td>冲突环路数（Conflict Cycles）必须严格为 0。</td>
          </tr>
          <tr>
            <td><strong>信息密度比 (Information Density)</strong></td>
            <td>有效事实与数字占比，杜绝无意义车轱辘话与格式套话。</td>
            <td>每千字中命名实体（NER）与精确数字的出现频次密度统计。</td>
            <td>实体密度 $\ge 45 \text{ Entities / 1K Tokens}$。</td>
          </tr>
        </tbody>
      </table>
    </div>

    <p>自动化评测流水线通过将上述四项指标加权整合，计算端到端研报综合品质得分 $Q_{report} = 0.4 \cdot S_{faith} + 0.3 \cdot S_{comp} + 0.2 \cdot S_{cohere} + 0.1 \cdot S_{density}$。任何低于 85 分的生成版本将被系统打回，触发局部章节的反思自愈与事实重抽。</p>

    <h2 id="repo-agent-ast-graph-algorithms">Repo Coding Agent 底层符号拓扑图算法与上下文精准修剪</h2>
    <p>在超大型代码仓库中，单纯依靠文本匹配极易把面试者拖入上下文爆炸与性能死锁的泥潭。工业级代码助手之所以能够精准定位跨文件的深层调用关系，核心在于依托 <strong>Tree-sitter 与图算法构建的代码全景拓扑图谱</strong>：</p>

    <ul>
      <li><strong>AST 抽象语法树增量解析：</strong>利用 Tree-sitter 对仓库中所有源文件进行多语言语法树抽取。提取出所有的符号声明节点（函数声明 <code>FunctionDeclaration</code>、类声明 <code>ClassDeclaration</code>、接口定义 <code>InterfaceDeclaration</code>）与符号引用节点（调用表达式 <code>CallExpression</code>、继承关系 <code>Heritage</code>）。</li>
      <li><strong>有向调用依赖图构建（Directed Dependency Call Graph）：</strong>将整个仓库抽象为有向图 $G = (V, E)$，其中节点 $v \in V$ 为函数或类实体，有向边 $e = (u, v) \in E$ 表示模块 $u$ 中调用或引用了模块 $v$。图的权重根据引用频次与文件物理路径距离进行动态调整。</li>
      <li><strong>基于个性化 PageRank 的关键骨架抽取（Personalized PageRank）：</strong>当用户提交一个 Issue 报错堆栈时，将报错涉及的入口函数作为初始正向随机游走的种子节点（Seeds）。执行多轮 Personal PageRank 迭代计算：
      $$\mathbf{p}_{t+1} = (1 - \alpha) \mathbf{M} \mathbf{p}_t + \alpha \mathbf{s}$$
      收敛后，得分最高的 Top-K 节点构成了与该 Bug 强相关的<strong>核心代码骨架拓扑（Repo Map Skeleton）</strong>。将其格式化为精简的类型签名与 Docstring 摘要送入 Prompt，既保留了全局依赖视野，又将无谓的代码行消耗压缩了 90% 以上。</li>
    </ul>

    <h2 id="production-governance-and-sla-resilience">全生命周期 SLA 韧性治理与大模型服务故障容灾</h2>
    <p>任何优秀的系统设计方案都必须经受生产环境真实故障的残酷洗礼。在大模型供应商频繁遭遇网络抖动、模型推理速率大幅波动（Throttling）或区域断网的极端现实面前，智能体系统必须构筑<strong>全生命周期的多维容灾防线</strong>：</p>

    <ul>
      <li><strong>跨供应商多云热备容灾路由（Multi-Cloud Disaster Recovery Gateway）：</strong>网关层配置跨模型供应商（如 OpenAI, Anthropic, DeepSeek, 阿里云等）的动态健康探测心跳。当主力模型在连续 5 次请求中发生超时或 5xx 错误时，熔断器（Circuit Breaker）自动进入半开状态，将后续流量在 100ms 内瞬时平滑无缝切换至热备降级模型集群，同时自动适配对应的 Prompt 格式与 Tokenizer。</li>
      <li><strong>长事务持久化检查点与会话断点接续（Checkpoint Resumption）：</strong>严禁将智能体的状态保存在单机易失内存中。每一次工具执行完毕后，当前完整的执行图状态、变量环境与事实黑板，均通过强一致性事务原子写入分布式数据库（PostgreSQL/Redis）。一旦底层工作节点物理宕机，集群调度器（Kubernetes）在另一台物理机拉起新 Pod 后，智能体能够精准从上一个检查点瞬间复苏并继续前行，实现零数据丢失与用户无感。</li>
      <li><strong>数据合规、隐私脱敏与审计冷备（Compliance & Privacy Isolation）：</strong>在任何外部网页抓取或代码补丁生成过程中，内置的高性能正则与敏感词检测引擎（Data Loss Prevention, DLP）实时扫描员工个人身份信息（PII）、企业内网密码凭据与 API 私钥。所有敏感数据在进入大模型推理前必须被物理掩码（Masking），所有交互轨迹永久保存在具备不可篡改特性的审计日志中，全面符合 GDPR 与企业信息安全最高合规标准。</li>
    </ul>
"""

insert_target = '<h2 id="deep-interview-tradeoffs-epistemology">'
if insert_target in text:
    new_text = text.replace(insert_target, deep_praxis_sections + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Expanded ch112 successfully with deep praxis sections")
else:
    print("Insert target not found")
