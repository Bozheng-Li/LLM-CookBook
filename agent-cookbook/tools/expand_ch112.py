# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch112.html"

with open(path, "r", encoding="utf-8") as f:
    text = f.read()

deep_engineering_sections = """
    <h2 id="deep-research-data-and-state-infra">Deep Research 底层分布式存储与高并发去重流水线</h2>
    <p>在面对数百个并发深度调研任务时，最容易遭遇的系统瓶颈往往不是大模型本身的吞吐，而是海量外部非结构化网页的抓取风暴、重复拉取以及网络 I/O 阻塞。为了保障系统的稳健运行，必须设计一套分层的<strong>分布式缓存、布隆过滤器去重与混合向量索引架构</strong>：</p>

    <div class="tbl-wrap">
      <table>
        <thead>
          <tr>
            <th>存储组件与分层</th>
            <th>底层技术栈选型</th>
            <th>存储数据模型与生命周期</th>
            <th>高并发与一致性保障机制</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>分布式 URL 访问布隆过滤</strong></td>
            <td>Redis Bloom Filter (Scalable)</td>
            <td>URL 规范化哈希（去除 UTM 参数、锚点），TTL 7 天。</td>
            <td>位数组无锁并发检测，误判率严格控制在 0.01% 以下。</td>
          </tr>
          <tr>
            <td><strong>网页正文与快照分层缓存</strong></td>
            <td>MinIO / AWS S3 + Redis 元数据</td>
            <td>原始 HTML 快照与经过 Readability 清洗的 Markdown。</td>
            <td>两级缓存机制：热点网页驻留 Redis 内存，冷数据落盘对象存储。</td>
          </tr>
          <tr>
            <td><strong>事实原子稠密向量索引</strong></td>
            <td>Qdrant / Milvus (HNSW 索引)</td>
            <td>BGE-M3 1024 维稠密向量 + 标量元数据 Payload。</td>
            <td>按任务 ID 物理分区（Partition Key），查询时在内存分区内极速检索。</td>
          </tr>
          <tr>
            <td><strong>长流程状态机断点快照</strong></td>
            <td>PostgreSQL (JSONB) + WAL</td>
            <td>全局假说树状态、当前探索深度、已消耗 Token 账单。</td>
            <td>强事务 ACID 保障，节点崩溃重启后从最新 Checkpoint 瞬时恢复。</td>
          </tr>
        </tbody>
      </table>
    </div>

    <p>在信息增益（Information Gain）评估中，我们建立了一套严格的<strong>动态停机数学判决准则（Stopping Criterion）</strong>。令 $H_t$ 表示当前关于课题的全局事实熵，新抓取的网页集合 $D_{new}$ 产生的事实原子更新为 $\Delta F$。当连续两次迭代的信息增益满足以下条件时，规划器强制触发收敛终结，停止无效探索：</p>
    $$\mathcal{IG}(D_{new}) = \sum_{f \in \Delta F} \text{Surprisal}(f) \cdot \text{Trust}(Source(f)) < \epsilon_{threshold}$$
    <p>通过这套自适应数学阻尼机制，既杜绝了由于陷入偏僻死胡同导致的无效死循环，又确保了在 Token 预算约束内将有限的算力聚焦于高信息密度的核心证据链上。</p>

    <h2 id="coding-agent-self-healing-and-flakiness">Repo Coding Agent 复杂边界与测试不稳定（Flaky Tests）治理</h2>
    <p>在真实的工业级软件工程场景中，大模型生成的补丁极少能一次性完美通过所有测试。卓越的 Repo Coding Agent 必须具备一套严密的<strong>自愈状态机与测试不稳定治理策略</strong>：</p>

    <div class="tbl-wrap">
      <table>
        <thead>
          <tr>
            <th>典型失败边界场景</th>
            <th>常见诱发根因分析</th>
            <th>传统粗暴处理方式</th>
            <th>工业级 Coding Agent 智能自愈决策链路</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>补丁语法冲突 (Patch Reject)</strong></td>
            <td>大模型生成的上下文行号与最新文件版本不一致。</td>
            <td>直接抛出异常并判定任务彻底失败。</td>
            <td><strong>三阶段退火匹配：</strong>从精确行匹配退火至基于 AST 节点锚定，若仍失败则调用轻量级模型重新生成仅包含目标函数的最小上下文块。</td>
          </tr>
          <tr>
            <td><strong>偶发不稳定测试 (Flaky Tests)</strong></td>
            <td>测试用例依赖随机数、系统时钟、未释放的网络端口。</td>
            <td>误将环境偶发错误归咎于代码补丁错误，陷入瞎改。</td>
            <td><strong>双盲环境基线对齐：</strong>在应用补丁前先在干净基线分支执行该测试。若基线同样报错，则将该测试标记为 Flaky 并从核心评价断言集中动态剔除。</td>
          </tr>
          <tr>
            <td><strong>超时与死锁 (Execution Timeout)</strong></td>
            <td>模型引入了未终止的 <code>while</code> 循环或线程锁争用。</td>
            <td>沙箱挂起直至整体任务超时崩溃。</td>
            <td><strong>进程树硬限制与堆栈提取：</strong>触发 <code>SIGKILL</code> 强杀前，先发送 <code>SIGQUIT</code> 捕获完整的线程 Dump 与调用堆栈，将其注入错误重试 Prompt 中指导模型自愈。</td>
          </tr>
          <tr>
            <td><strong>破坏存量业务 (Regression Failure)</strong></td>
            <td>修好了 Issue 目标 Bug，但破坏了其他模块既有功能。</td>
            <td>无法辨别全局影响面，盲目提交交付。</td>
            <td><strong>分层回归测试靶场：</strong>严格执行 <code>PASS_TO_PASS</code> 门禁。若存量测试发生回归，强制将 Git 工作区重置至上一稳定检查点，重新生成探索分支。</td>
          </tr>
        </tbody>
      </table>
    </div>

    <h2 id="capacity-planning-and-hardware-sizing">容量规划与硬件资源预估（Capacity & Hardware Sizing）</h2>
    <p>在系统设计的容量规划环节，必须给出经得起推敲的量化测算数据。假设企业内部服务 5,000 名研发工程师，峰值同时并发运行 100 个 Repo Coding Agent 任务：</p>
    <ul>
      <li><strong>CPU 与内存配额计算：</strong>每个 Agent 在执行构建与测试时分配 2 个物理 CPU 核心与 4GB 物理内存。峰值并发需要物理节点资源为 $100 \times 2 = 200 \text{ Cores}$，内存 $100 \times 4\text{GB} = 400\text{GB}$。采用 5 台 64 核 128GB 的标准物理服务器组成 Kubernetes 计算集群即可从容支撑。</li>
      <li><strong>存储 IOPS 与网络吞吐：</strong>采用本地 NVMe SSD 搭建分布式文件缓存。利用 Git Worktree 共享只读 Object 库，每个沙箱的磁盘写入峰值限制在 50MB。100 个并发仅产生 5GB 瞬时写开销，完全在企业级 NVMe 的数十万 IOPS 承受范围内。</li>
      <li><strong>大模型推理 Token 峰值带宽：</strong>单个 Coding 任务平均产生 8 轮交互，每轮上下文约 16K Tokens，总输出约 2K Tokens。峰值并发下总上下文吞吐需求为：
      $$\text{Token Throughput} \approx \frac{100 \times 16,000}{60} \approx 26,666 \text{ Tokens/sec}$$
      通过在底层集群部署两台配备 8 卡 H800/H20 的 vLLM / SGLang 推理服务器，配合跨多轮请求的 <strong>Radix Tree 前缀缓存复用</strong>，实际首字预填充计算量（Prefill Load）可直接骤降 85% 以上，实现惊人的硬件成本优化。</li>
    </ul>
"""

insert_point = '<h2 id="deep-interview-tradeoffs-epistemology">'
if insert_point in text:
    new_text = text.replace(insert_point, deep_engineering_sections + "\n" + insert_point)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Expanded ch112 successfully with deep engineering sections")
else:
    print("Insert point not found")
