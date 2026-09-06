import os

path = r"D:/agent-cookbook/chapters/ch081.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

expansion_3 = """
    <h2 id="production-checklist">生产落地交付检查清单与硬件容量评估指南</h2>
    <p>在将个人知识库 Agent 推向生产环境并支撑团队数百人乃至上万用户日常使用时，工程架构师必须对照以下交付清单逐项核验，确保服务具备高可用与弹性容灾能力：</p>

    <div class="tbl-wrap">
      <table>
        <thead><tr><th>评估维度</th><th>核心指标 / 推荐阈值</th><th>监控巡检方案</th><th>容灾降级应对策略</th></tr></thead>
        <tbody>
          <tr><td><strong>端到端首字延迟 (TTFT)</strong></td><td>P95 &lt; 1200ms，P99 &lt; 2000ms</td><td>集成 OpenTelemetry APM 全链路分布式追踪</td><td>当 Rerank 队列积压超过阈值时，自动降级为纯 RRF 融合打分，跳过 Cross-Encoder</td></tr>
          <tr><td><strong>检索召回精度 (Recall@5)</strong></td><td>标准基准集 &gt; 92%</td><td>周度自动化金标数据集回归评估（RAGAS）</td><td>触发自动告警，回滚最近的切片策略并审查新近摄取文档的解析质量</td></tr>
          <tr><td><strong>向量存储资源占用</strong></td><td>每 10 万切片占用约 400MB 内存 (以 1024 维 HNSW 为基准)</td><td>Prometheus 监控 Milvus / Qdrant 节点内存水线</td><td>开启标量量化（SQ8）或乘积量化（PQ），降低 70% 显存消耗</td></tr>
          <tr><td><strong>多租户隔离与安全合规</strong></td><td>100% 具备租户 ID 与 ACL 标签前置硬隔离</td><td>自动化安全红蓝对抗扫描（第 58 章）</td><td>未携带有效用户签名或权限令牌的请求直接在 API 网关层拒绝（403 Forbidden）</td></tr>
          <tr><td><strong>冷热数据生命周期管理</strong></td><td>近 90 天活跃文档常驻内存，历史归档冷存</td><td>基于访问频次的时间滑动窗口与 LRU 淘汰</td><td>冷数据转存至低成本 S3 对象存储，按需异步召回与重构索引</td></tr>
        </tbody>
      </table>
      <caption>表 81-2 · 个人/企业级知识库问答 Agent 生产交付质量验收标准。涵盖性能、精度、资源、合规与运维五大维度。</caption>
    </div>

    <p>在硬件选型与集群规划方面，推荐采用微服务分层解耦拓扑：</p>
    <p><strong>① 接入与网关层：</strong>2 节点 4 核 8G 云主机，负责运行 FastAPI / Streamlit、处理 JWT 鉴权、限流（Token Bucket）与 SSE 长连接代理。</p>
    <p><strong>② 模型与推理计算层：</strong>配置 1 台具备单张 NVIDIA L4 或 A10G（24GB 显存）的 GPU 实例。利用 vLLM 部署量化版 BGE-M3 向量模型与 BGE-Reranker-Large 重排模型，支持单机每秒处理并发检索重排请求超过 150 QPS。</p>
    <p><strong>③ 数据持久化引擎层：</strong>采用轻量高可用的 Qdrant 或 Milvus 分布式集群存储切片向量，搭配 PostgreSQL 存储父文档原始内容与用户对话审计日志，配合 Redis 缓存高频热点 Query 检索结果，使得常见重复提问的响应时间压低至 50 毫秒以内。</p>
"""

insert_target = '<h2 id="faq">'
if insert_target in text:
    new_text = text.replace(insert_target, expansion_3 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Successfully added production checklist to ch081.html")
else:
    print("Target not found")
