# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch111.html"

with open(path, "r", encoding="utf-8") as f:
    text = f.read()

rich_qa_deep = """
    <h3>Q53: 强化学习后训练中出现的“策略熵坍缩（Entropy Collapse）”是什么现象？有哪些工程治理方案？</h3>
    <p><strong>【核心考点】</strong>探索退化、模式坍缩、KL 散度正则化、温度退火调度与经验多样性回放。</p>
    <p><strong>【参考回答】</strong>在对大模型智能体进行强化学习（PPO 或 GRPO）迭代训练时，随着梯度多轮更新，策略网络往往会过快地收敛到某一种看似能够稳定获得正向局部奖励的刻板输出模式上。此时，模型动作分布的香农熵 $H(\pi_\theta) = -\sum_a \pi_\theta(a \mid s) \log \pi_\theta(a \mid s)$ 剧烈暴跌至接近于 0，模型彻底丧失了在广阔状态空间中继续探索更新颖、更优解的能力，这种现象即为<strong>策略熵坍缩（Entropy Collapse）</strong>。
    工业级系统治理方案：
    <ul>
      <li><strong>显式熵奖励惩罚项（Entropy Bonus Regulation）：</strong>在总优化损失函数中强行引入带自适应权重的熵最大化正则项 $L_{total} = L_{RL} + \beta \cdot H(\pi_\theta)$。当监测到策略输出的 Token 熵过低时，动态调大 $\beta$ 权重，强迫采样器向均匀分布靠拢，维持解的多样性。</li>
      <li><strong>动态参考策略 KL 散度锚定（Dynamic KL Penalty Controller）：</strong>在奖励中动态扣除当前策略与未微调初始基座参考策略（$\pi_{ref}$）之间的 KL 散度：$R'(s, a) = R(s, a) - \alpha \cdot D_{KL}(\pi_\theta \parallel \pi_{ref})$。采用非线性 PID 控制器动态调节 $\alpha$，当策略漂移过快时激进惩罚，当探索停滞时放松束缚。</li>
      <li><strong>暗经验回放与温度扰动（Dark Experience Replay & Temperature Jittering）：</strong>在训练 Batch 中强制混入 15%~20% 的通用高质量无偏监督微调（SFT）数据；同时在并发环境 Rollout 采样时，引入高斯扰动的动态采样温度（如 $T \sim \mathcal{N}(0.8, 0.15)$），从环境生成侧打破僵化共振。</li>
    </ul></p>

    <h3>Q54: 面对长思维链模型（如 DeepSeek-R1, OpenAI o1）在特定场景下的“过度思考（Over-thinking）”，如何实施轻量化蒸馏与早停？</h3>
    <p><strong>【核心考点】</strong>测试期计算过载、无效冗余回溯、知识蒸馏与长度感知奖惩函数设计。</p>
    <p><strong>【参考回答】</strong>长思维链模型在解决极其简单的直觉性任务（如简单的字符串反转、常见事实检索）时，往往依然固执地生成数千 Token 的内部漫长推理与反复自问自答，导致响应延迟高达数十秒且产生巨大的算力浪费。针对这一工业痛点的高阶治理架构包括：
    <ul>
      <li><strong>任务复杂度动态路由器（Tier-0 Complexity Gating）：</strong>在请求入口部署一个参数量极小（如 0.5B~1.5B）的前置轻量级判别器，对 Prompt 进行单次前向打分。将简单直觉任务直接直通给无长思考的快速模型（System 1），仅将高歧义、强逻辑证明类任务分派给长思维链模型（System 2）。</li>
      <li><strong>长度感知正则化后训练（Length-aware Reward Shaping）：</strong>在强化学习训练目标中引入与输出 Token 长度 $L$ 挂钩的非线性阻尼惩罚项：$R_{final} = R_{accuracy} - \gamma \cdot \max(0, L - L_{threshold})$。当模型在正确解答题目的同时消耗了超额的 Token，其综合奖励将被大幅扣减，倒逼模型学会“该快则快，该慢则慢”的自适应推理弹性。</li>
      <li><strong>显式反思链截断蒸馏（Pruned CoT Distillation）：</strong>利用高质量启发式规则或强模型对 R1 生成的长思维轨迹进行后处理清洗：剥离其间无效的无意义口癖与机械式重复反思，保留核心跳跃步骤，将其格式化为精炼紧凑的 SFT 数据集对中小尺寸模型进行定向蒸馏。</li>
    </ul></p>

    <h2 id="fault-injection-and-resilience-engineering">模块六：高并发混沌故障现场复盘与防御工程实录（Q95 - Q100）</h2>

    <h3>Q95: 现场复盘：某电商大促活动中，数十万并发 Agent 引发了下游 ERP 系统的“雪崩式锁死”，请给出完整排障链路。</h3>
    <p><strong>【核心考点】</strong>非幂等高并发并发击穿、缺乏分布式背压缓冲、惊群效应、熔断与限流拓扑。</p>
    <p><strong>【参考回答】</strong><strong>【故障还原】</strong>大促期间，数万名用户的购物助手 Agent 并发为用户扫描最优优惠组合，并几乎在同一秒内调用 ERP 下单扣减库存 API。由于网络微小抖动，部分 Agent 遭遇 504 超时，触发了客户端默认的无退避并发重试。瞬间产生的数十万次重复写入打爆了 ERP 数据库连接池，行级排他锁队列堆积数万长连接，引发全站级雪崩。
    <strong>【深度排查与四级止血重构】</strong>：
    <ol>
      <li><strong>第一道防线：Redis Lua 原子幂等性令牌（Idempotency Key）：</strong>为每一次任务交互生成全局唯一的 SHA-256 签名（由用户 ID + 购物车内容哈希 + 时间戳窗口组成）。在请求进入 ERP 网关前，通过 Redis Lua 脚本执行原子 <code>SETNX</code> 与过期时间锁定。重复到达的相同请求直接在最外层网关被返回排队中，严禁下穿至核心数据库。</li>
      <li><strong>第二道防线：抖动全指数退避算法（Full Jitter Exponential Backoff）：</strong>强制重构 Agent 的工具调用重试逻辑，等待时间公式为：
      $$t_{sleep} = \text{random}(0, \, \min(t_{max}, \, t_{base} \cdot 2^{attempt}))$$
      通过引入完全随机的离散抖动，将并发集中的惊群峰值流量平滑拉伸至数十秒的时间轴上，彻底消除共振波峰。</li>
      <li><strong>第三道防线：分布式令牌桶全局自适应背压（Adaptive Backpressure）：</strong>在 Agent 集群与 ERP 之间插入 Kafka 异步缓冲削峰队列。网关根据下游 ERP 的实时响应延迟（P99 Latency）与 CPU 负载动态调整出队速率。一旦下游响应延迟突破 500ms，立即触发自适应限流与降级提示。</li>
      <li><strong>第四道防线：混沌工程回归验证（Chaos Engineering）：</strong>在预发环境中模拟注入 30% 丢包率、数据库随机慢查询与断网分区故障，验证全链路降级网关是否能够按预期平稳自愈，严禁带病上线。</li>
    </ol></p>

    <div class="codeblock">
      <div class="code-header">
        <span class="code-lang">Python: distributed_resilience_gate.py</span>
        <button class="copy-btn">复制</button>
      </div>
      <pre><code># -*- coding: utf-8 -*-
\"\"\"
工业级高并发防击穿幂等网关与自适应抖动重试器
\"\"\"
import time
import random
import hashlib
from typing import Dict, Any, Optional

class DistributedResilienceGate:
    def __init__(self, base_delay: float = 0.5, max_delay: float = 8.0, max_retries: int = 3):
        self.base_delay = base_delay
        self.max_delay = max_delay
        self.max_retries = max_retries
        self._mock_redis_locks = set()

    def generate_idempotency_token(self, payload: Dict[str, Any]) -> str:
        raw_str = f"{payload.get('user_id')}-{sorted(payload.items())}"
        return hashlib.sha256(raw_str.encode('utf-8')).hexdigest()

    def try_acquire_lock(self, token: str) -> bool:
        \"\"\"模拟 Redis Lua 原子的 SET token 1 EX 60 NX 操作\"\"\"
        if token in self._mock_redis_locks:
            return False
        self._mock_redis_locks.add(token)
        return True

    def execute_with_full_jitter_retry(self, tool_func, *args, **kwargs) -> Any:
        token = self.generate_idempotency_token(kwargs)
        if not self.try_acquire_lock(token):
            raise RuntimeError(f"[-] 幂等拦截: 重复的并发请求命中锁槽位 [{token[:8]}]，已拦截下穿！")

        for attempt in range(self.max_retries):
            try:
                return tool_func(*args, **kwargs)
            except Exception as e:
                if attempt == self.max_retries - 1:
                    raise e
                # Full Jitter 指数抖动休眠
                backoff_limit = min(self.max_delay, self.base_delay * (2 ** attempt))
                sleep_duration = random.uniform(0, backoff_limit)
                time.sleep(sleep_duration)
</code></pre>
    </div>

    <h3>Q96: 如何设计跨进程、跨节点的智能体全链路可观测性追踪（OpenTelemetry Distributed Tracing）？</h3>
    <p><strong>【核心考点】</strong>TraceId / SpanId 上下文透传、W3C Baggage 规范、语义约定（Semantic Conventions）、时延归因瀑布图。</p>
    <p><strong>【参考回答】</strong>智能体系统是一类典型的长链路异步混合架构：一次用户请求可能经过前置路由模型、多次并发向量数据库召回、数轮工具调用 API、以及多次大模型推理。若缺乏统一的链路追踪标准，排查一次线上高延迟或偶发幻觉无异于大海捞针。工业级方案基于 <strong>OpenTelemetry 协议标准</strong> 构筑端到端分布式可观测体系：
    <ul>
      <li><strong>W3C 规范 TraceContext 注入与透传：</strong>在入口处生成全局唯一的 <code>TraceId</code>。在任何发起下游网络调用（HTTP Header, gRPC Metadata, Redis 消息头）的地方，强行注入 <code>traceparent</code> 与 <code>tracestate</code> 字段，确保跨多进程调度与消息队列消费时链路上下文绝不断裂。</li>
      <li><strong>LLM 专属 Semantic Conventions 结构化语义打标：</strong>在每个大模型推理 Span 内部，结构化记录标准属性：<code>gen_ai.system</code> (如 deepseek/openai)、<code>gen_ai.request.model</code>、<code>gen_ai.usage.prompt_tokens</code>、<code>gen_ai.usage.completion_tokens</code>、以及当前推理的采样参数。</li>
      <li><strong>分层 Span 拓扑建模：</strong>顶层为全局用户 Task Span；其下分叉出 <code>Planner.Plan</code>、<code>Tool.Execute</code>、<code>Retriever.Search</code> 等平行或嵌套的子 Span。不仅记录耗时，更记录每一次工具执行前后的输入输出 Diff 与状态校验结果。</li>
      <li><strong>性能异常与长尾归因瀑布看板：</strong>通过 Jaeger 或 Tempo 渲染出微秒级精度的执行瀑布图，快速定位系统耗时瓶颈究竟是出在向量索引的倒排拉取上，还是由于网络拥塞导致大模型首字延迟（TTFT）激增。</li>
    </ul></p>
"""

target = '<section class="refs">'
if target in text:
    new_text = text.replace(target, rich_qa_deep + "\n" + target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added rich deep additions to ch111")
else:
    print("Target not found")
