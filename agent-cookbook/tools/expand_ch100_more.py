# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch100.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

expansion_more = """
    <h2 id="future-architectural-implications">未来展望：从独立论著到下一代自主操作系统（Agent OS）的合流</h2>
    <p>纵观 ToT、MemGPT 与 AgentBench 这三篇横跨算法、系统与评测的里程碑论著，我们清晰地看到了一条从单体 Prompt 技巧向<strong>完整的下一代「智能体操作系统（Agentic Operating System, AOS）」演进的宏伟技术脉络</strong>：</p>
    
    <p>传统的计算机操作系统（如 Linux 或 Windows）是以物理 CPU、内存与磁盘为核心调度对象的；而下一代 Agent OS 则直接以<strong>大模型的大脑注意力、短期工作记忆（Context Window）与外部工具世界</strong>为核心调度对象：</p>
    <p><strong>① 进程与线程调度（Process Scheduling）：</strong>正如现代操作系统通过时间片轮转（Round-Robin）调度并发任务，Agent OS 将借鉴 ToT 的树搜索剪枝与优先级队列，在有限的 GPU 算力预算下，动态调度数十个并发推演分支，把推理 Token 优先倾斜给最具潜力的关键解决步骤；</p>
    <p><strong>② 虚拟内存子系统（Virtual Memory Management）：</strong>MemGPT 确立的自发换页中断机制将全面固化为底层中间件标准。未来的智能体不再需要开发者手工拼接历史对话，底层的内存管理器会自动根据访问频次、语义重要性与遗忘半衰期，在 SRAM（KV-Cache 高速显存）、DRAM（本地 Redis）与冷存储（分布式向量数据库）之间实现无感透明的多级缓存流动；</p>
    <p><strong>③ 驱动与外设抽象层（HAL / Device Drivers）：</strong>AgentBench 探索的 8 大沙箱环境正在演进为标准化的机器可读接口（MCP, Model Context Protocol，第 23 章）。无论是数据库、命令行、浏览器还是物理外设，都将通过统一的沙箱隔离层暴露给智能体，实现跨平台通用交互。</p>

    <div class="tbl-wrap">
      <table>
        <thead><tr><th>传统计算机操作系统概念</th><th>经典代表实现 (Linux/Windows)</th><th>对应的新一代 Agent OS 架构映射</th><th>代表性前沿学术论著</th></tr></thead>
        <tbody>
          <tr><td><strong>中央处理器 (CPU)</strong></td><td>x86 / ARM 物理执行单元</td><td>大语言模型 (LLM) 推理与注意力生成中枢</td><td>Transformer (Vaswani 2017)</td></tr>
          <tr><td><strong>内存管理单元 (MMU)</strong></td><td>物理分页表、TLB 快表、缺页中断</td><td>上下文分层调度、MemGPT 自发换页与工作记忆</td><td>MemGPT (Packer 2023)</td></tr>
          <tr><td><strong>进程控制块与规划 (PCB / Scheduler)</strong></td><td>CFS 完全公平调度器、多级反馈队列</td><td>思维树前沿搜索 (ToT)、MCTS 状态空间剪枝</td><td>Tree of Thoughts (Yao 2023)</td></tr>
          <tr><td><strong>基准性能跑分套件</strong></td><td>SPEC CPU、UnixBench、Geekbench</td><td>多域沙箱环境交互达成率客观基准</td><td>AgentBench (Liu 2023)</td></tr>
        </tbody>
      </table>
      <caption>表 100-4 · 传统计算机体系结构与现代 Agent OS 完整技术映射矩阵。见证计算机科学经典理论在大模型时代的壮丽重生。</caption>
    </div>

    <p>这一波澜壮阔的合流趋势雄辩地证明：人工智能的发展从来不是孤立的算法独角戏，而是与计算机体系结构、编译原理与操作系统理论血脉相连的宏大系统工程。站在全书整整第 100 章的辉煌历史坐标上，我们比以往任何时刻都更加清晰地坚信：掌握了思维规划的深度、分层记忆的广度与真实环境交互的硬度，我们便握住了通往未来通用自治超级智能体的金钥匙！</p>
"""

insert_target = '<div class="callout note">'
if insert_target in text:
    new_text = text.replace(insert_target, expansion_more + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added future architectural implications section")
else:
    print("Target not found")
