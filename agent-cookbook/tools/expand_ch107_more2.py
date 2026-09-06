# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch107.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

expansion_more_2 = """
    <h2 id="eval-pipeline-cost-optimization">高吞吐工业化评测降本战法：智能体判题农场的资源与并发治理</h2>
    <p>当评测规模扩展至数千个长程交互任务时，整个评测系统的运行成本与时间消耗将迅速演进为一个严重的分布式系统难题。例如，运行一次包含 500 个复杂实例的 SWE-bench Verified 全量评测，如果采用单机串行执行，不仅耗时超过 48 小时，而且一旦中途宿主机因 OOM 宕机，全部未保存的进度将毁于一旦。</p>
    
    <p>一线大厂成熟的<strong>「大规模分布式判题农场（Evaluation Farm）」</strong>架构，普遍建立在以下四大工程优化支柱之上：</p>
    
    <p><strong>① 容器镜像分层预热与本地缓存池（Warm Container Pool）：</strong>在启动评测前，评测集群的守护进程（Daemon）预先在本地拉取好各任务专属的基础 Docker 镜像（如 <code>django:eval-v1</code>），并预先克隆好 Git 代码仓库；当评测引擎派发任务时，通过 <code>docker run --volumes-from</code> 瞬间完成毫秒级挂载，将原本耗时数分钟的镜像下载与 <code>pip install</code> 依赖安装阶段彻底归零；</p>
    
    <p><strong>② 分布式任务分片与动态工作窃取（Work-Stealing Task Queue）：</strong>利用 Celery、RabbitMQ 或 Redis 搭建分布式评测任务队列。由 10~20 台异构 GPU/CPU 节点充当 Worker 消费者无状态并发拉取测试任务。当某个高难任务陷入耗时深水区时，其他空闲节点自动窃取后续轻量任务，将整体端到端评测流水线耗时从 48 小时极速压缩至 45 分钟以内；</p>
    
    <p><strong>③ 智能早停与假死断流探测（Early Stopping & Hang Detection）：</strong>在交互过程中，评测守护进程持续采样容器的 CPU 利用率与标准输出流。若检测到 Agent 连续 60 秒无任何新的 Token 输出或命令执行，或者连续 3 次发送完全相同的错误重试指令，守护进程强制下发 SIGKILL 信号触发早停并标记为“死锁失败（Action Deadlock）”，节省宝贵的 GPU 算力与并发槽位；</p>
    
    <p><strong>④ 结构化断言日志全量留存与可微分分析（Structured Diagnostic Telemetry）：</strong>每一个被评测任务的执行全过程（包含完整的上下文 Prompt 变化快照、环境交互回显、以及 Docker 容器的标准错误日志），被统一序列化为标准 JSON Lines（JSONL）格式转存至高吞吐对象存储中。这使得算法团队在复盘评测结果时，能够利用脚本秒级统计出当前版本模型究竟是因为“缺少某依赖”、“工具参数名写错”还是“超时”导致的失败，为下一轮提示词调优或模型 SFT 数据清洗提供精准到原子级的客观归因指导。</p>
"""

insert_target = '<div class="callout note">'
if insert_target in text:
    new_text = text.replace(insert_target, expansion_more_2 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added eval pipeline cost optimization to ch107.html")
else:
    print("Target not found")
