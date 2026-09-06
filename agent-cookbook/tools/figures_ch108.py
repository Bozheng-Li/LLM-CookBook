# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figkit import *

# 图 108-1: 智能体系统化认知进阶与资源拓扑网络 (Learning Pathways & Resource Topology)
f = F(940, 440)
f.box(40, 50, 260, 160, "1. 顶会公开课与核心原著\n• Stanford CS224N / CS25\n• Berkeley CS294/285\n• Sutton 《Reinforcement Learning》\n• Russell & Norvig 《AIMA》\n• 高等认知科学与信息论教材", fill=C.blue_s, stroke=C.blue)
f.box(340, 50, 260, 160, "2. 工业界技术报告与核心博客\n• OpenAI / Anthropic Research 博客\n• Lilian Weng (OpenAI) 智能体长文\n• Eugene Yan: System Design 经验集\n• Chip Huyen: AI Engineering 专栏\n• Hugging Face & DeepLearning.AI", fill=C.indigo_s, stroke=C.indigo)
f.box(640, 50, 260, 160, "3. 开源极客社群与前沿实验室\n• GitHub Trending & Papers With Code\n• Discord: LangChain / AutoGen / CrewAI\n• Reddit: r/LocalLLaMA, r/MachineLearning\n• X (Twitter) AI 头部研究员圈子\n• 国内头部智库与 Agent 开发社区", fill=C.teal_s, stroke=C.teal)

f.arrow(300, 130, 340, 130, color=C.blue)
f.arrow(600, 130, 640, 130, color=C.indigo)

f.box(80, 260, 780, 140, "4. 理论到实战的知行合一闭环进阶法则 (The Praxis Loop)\n• 论文复现 (Paper Reproduction) -> 定位关键数学公式与伪代码实现细节\n• 架构拆解 (System Decomposition) -> 逆向分析开源框架调度机制与中间件\n• 压测复盘 (Load & Failure Analysis) -> 构建故障注入与边界条件回归防护网\n• 社区回哺 (Open Source Contribution) -> 提交 RFC 提案、修复核心 Bug 与工程落地", fill=C.purple_s, stroke=C.purple)

f.arrow(170, 210, 170, 260, color=C.blue)
f.arrow(470, 210, 470, 260, color=C.indigo)
f.arrow(770, 210, 770, 260, color=C.teal)

f.save("fig-learning-resources-topology")
print("Saved fig-learning-resources-topology.svg")

# 图 108-2: 智能体研发工程知识树全景 (Agent Knowledge Radar & Skill Matrix)
f2 = F(940, 360)
f2.box(40, 50, 190, 260, "底层数学与算力基座\n\n• 概率论与贝叶斯推断\n• 凸优化与随机梯度下降\n• MDP 强化学习形式化\n• CUDA / GPU 内存分布\n• vLLM / PagedAttention\n• KV 缓存压缩调度", fill=C.gray_s, stroke=C.line)
f2.box(260, 50, 200, 260, "认知架构与推理引擎\n\n• ReAct / Plan-and-Solve\n• Tree / Graph of Thoughts\n• 蒙特卡洛树搜索 (MCTS)\n• Reflexion 经验回溯池\n• 上下文动态修剪与滑动窗\n• 神经符号系统与约束求解", fill=C.blue_s, stroke=C.blue)
f2.box(490, 50, 200, 260, "分布式系统与高并发工程\n\n• 事件驱动 Actor 模型\n• 幂等性与分布式锁 (Redis)\n• Saga 长事务补偿协议\n• gRPC / SSE 高吞吐流式\n• OpenTelemetry 全链路追踪\n• 向量索引 (HNSW / IVFFlat)", fill=C.green_s, stroke=C.green)
f2.box(720, 50, 180, 260, "安全隔离与治理合规\n\n• 间接提示词注入攻防\n• 差分隐私与数据脱敏\n• Linux gVisor / Firecracker\n• AST 白名单代码沙箱\n• 责任归属与审计追踪\n• 确定性自动化判题 Harness", fill=C.red_s, stroke=C.red)

f2.arrow(230, 180, 260, 180, color=C.indigo)
f2.arrow(460, 180, 490, 180, color=C.green)
f2.arrow(690, 180, 720, 180, color=C.red)

f2.save("fig-agent-knowledge-radar")
print("Saved fig-agent-knowledge-radar.svg")
