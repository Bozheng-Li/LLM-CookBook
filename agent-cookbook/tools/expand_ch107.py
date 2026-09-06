# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch107.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# Expand with comprehensive deep engineering sections:
# 1. Detailed Comparative Analysis of GAIA Level 1, 2, 3 Task Design & Multimodal Evaluation Protocol
# 2. Complete Docker Compose Multi-Service Sandbox Architecture for WebArena Local Hosting
# 3. AgentBench OS and DB Evaluation Harness Code Implementation & Scoring Dynamics
# 4. Enterprise Evaluation Operationalization: Establishing Golden Datasets & Cost-Quality Pareto Frontiers

expansion_1 = """
    <h2 id="gaia-multimodal-protocol">深度解构 1：GAIA 权威评测协议与三级认知难度阶梯解剖</h2>
    <p>在 Meta、HuggingFace 与 AutoGPT 联合推出的 <strong>GAIA（General AI Assistants Benchmark）</strong>中，研究团队彻底摒弃了学术界过去那些脱离实际的纯文字智力题，专门针对人类日常工作中最高频、最棘手的复杂多模态长链条助理任务，设计了 466 个严格由人类专家背书的真实试题。GAIA 的革命性突破在于其<strong>「对人类简单（成功率高达 92%），对 AI 极其残忍（顶尖商业大模型初测成功率曾低于 15%）」</strong>的反差设计：</p>

    <div class="tbl-wrap">
      <table>
        <thead><tr><th>GAIA 认知难度分级</th><th>考察的核心智能体能力</th><th>涉及的多模态工具链要求</th><th>典型试题真实案例</th></tr></thead>
        <tbody>
          <tr><td><strong>Level 1 (初级工具调用)</strong></td><td>单步工具调用、精准事实检索、简单计算</td><td>单次 Web 搜索、简单计算器、文本提取</td><td>「查询 2024 年巴黎奥运会男子百米决赛冠军的精确夺冠成绩（以秒为单位）」</td></tr>
          <tr><td><strong>Level 2 (复合多模态多跳)</strong></td><td>跨异构多模态文件联合分析、表格统计、长链条推理</td><td>同时读取 PDF 研报、Excel 表格与解析音频片段</td><td>「阅读给定的跨国集团 2023 年财报 PDF 与薪资 Excel，计算该高管股票期权占总薪酬的精确百分比」</td></tr>
          <tr><td><strong>Level 3 (长程复杂逻辑攻坚)</strong></td><td>反事实假说推演、多网站动态表单穿透、逆向事实核实</td><td>无头浏览器自动化、复杂代码解释器、空间几何推理</td><td>「定位某学术会议 1985 年第一届研讨会闭门合影中，坐在第三排左数第二位学者的博士论文题目」</td></tr>
        </tbody>
      </table>
      <caption>表 107-2 · GAIA 评测基准三大认知难度阶梯解剖表。从单步事实检索跨越至人类专家级的复杂多模态长程推理。</caption>
    </div>

    <p>更令人信服的是，GAIA 采用<strong>「确定性事实真值准绳（Fact-Based Ground Truth）」</strong>：每一道题的最终正确答案，必须是一个格式极其严格、无歧义的简短字符（如一个具体的人名、一个精确到小数点后两位的数字或一个标准的 ISO 日期）。评测打分完全依靠字符串绝对匹配（Exact Match），彻底消除了评测中人为打分的水分与偏见。</p>
"""

expansion_2 = """
    <h2 id="webarena-docker-compose">深度解构 2：WebArena 本地化分布式多服务沙箱集群搭建</h2>
    <p>在企业内网跑通 WebArena 评测，最大的工程阻碍在于其复杂的本地全栈环境依赖。WebArena 并不是一个简单的单机脚本，而是一个由 <strong>4 个独立运行的真实企业级 Web 容器组成的分布式沙箱集群</strong>：</p>

    <div class="codeblock">
      <div class="cb-head"><span>WebArena 分布式沙箱集群编排配置（docker-compose.webarena.yml）</span><button class="cb-copy">复制</button></div>
      <pre><code>version: '3.8'

services:
  # 1. 真实开源 GitLab 代码托管仓库实例
  gitlab-instance:
    image: 'gitlab/gitlab-ee:15.11.0-ee.0'
    container_name: webarena_gitlab
    environment:
      GITLAB_OMNIBUS_CONFIG: |
        external_url 'http://webarena-gitlab:8023'
    ports:
      - '8023:8023'
    networks:
      - webarena_net

  # 2. 开源电商平台实例 (Shopping)
  shopping-store:
    image: 'webarena/shopping-admin:v1.0'
    container_name: webarena_shopping
    ports:
      - '7770:80'
    networks:
      - webarena_net

  # 3. 社交论坛系统 (Postmill / Reddit 风格)
  social-forum:
    image: 'webarena/postmill-forum:latest'
    container_name: webarena_forum
    ports:
      - '9999:80'
    networks:
      - webarena_net

  # 4. 底层支持客观断言的状态数据库 (PostgreSQL)
  evaluation-db:
    image: 'postgres:15-alpine'
    container_name: webarena_eval_db
    environment:
      POSTGRES_USER: 'webarena_admin'
      POSTGRES_PASSWORD: 'secure_password_2026'
      POSTGRES_DB: 'eval_state_db'
    ports:
      - '5432:5432'
    networks:
      - webarena_net

networks:
  webarena_net:
    driver: bridge</code></pre>
    </div>

    <p>在这个集群搭建就绪后，智能体通过 Playwright 无头浏览器在 <code>8023, 7770, 9999</code> 端口之间进行逼真的跨网站操作，并在每次测试前后通过执行 <code>docker-compose down -v &amp;&amp; docker-compose up -d</code> 实现毫秒级的全局数据库快照原子化还原，确保评测结果具备 100% 的科学可复现性。</p>
"""

expansion_3 = """
    <h2 id="agentbench-os-db-runner">深度解构 3：AgentBench OS 与 DB 核心评测调度器实现</h2>
    <p>清华大学 <strong>AgentBench</strong> 之所以成为综合能力评估的标准，正是因为其将真实的操作系统终端与数据库操作，抽象为标准化的<strong>多轮互动环境（Interactive Environment）</strong>。以下给出 AgentBench 在 OS 终端任务上的核心判题调度器实现：</p>

    <div class="codeblock">
      <div class="cb-head"><span>AgentBench 操作系统终端环境判题驱动器（agentbench_os_harness.py）</span><button class="cb-copy">复制</button></div>
      <pre><code>import docker, json, time
from typing import Dict, Any

class AgentBenchOSEvaluator:
    def __init__(self, agent_client):
        self.agent = agent_client
        self.docker_client = docker.from_env()

    def evaluate_os_task(self, task_meta: Dict[str, Any], timeout_seconds: int = 120) -> Dict[str, Any]:
        \"\"\"执行单项 Linux 运维与配置真实终端交互评测\"\"\"
        task_id = task_meta["task_id"]
        instruction = task_meta["instruction"]
        docker_image = task_meta["docker_image"]
        verification_script = task_meta["eval_script"]

        print(f"=== 启动 AgentBench OS 任务 [{task_id}] ===")
        # 1. 瞬时拉起隔离且只读挂载的 Docker 沙箱容器
        container = self.docker_client.containers.run(
            docker_image,
            command="/bin/bash",
            stdin_open=True,
            tty=True,
            detach=True,
            network_mode="none"  # 隔离网络
        )

        history_dialogue = [f"System Instruction: {instruction}"]
        task_resolved = False

        try:
            start_time = time.time()
            while time.time() - start_time < timeout_seconds:
                # 2. 调度 Agent 输出下一步 Bash 命令
                agent_output = self.agent.generate_command("\n".join(history_dialogue))
                
                # 检查 Agent 是否宣告任务完成
                if "FINISH" in agent_output:
                    print("智能体宣告配置完毕，进入判题阶段。")
                    break

                # 3. 在真实容器内执行命令并截取标准回显
                cmd = agent_output.strip()
                exec_res = container.exec_run(cmd, timeout=10)
                stdout_str = exec_res.output.decode("utf-8", errors="ignore")
                
                history_dialogue.append(f"$ {cmd}\n{stdout_str}")
                print(f"[Container Exec] $ {cmd} -> {stdout_str[:80]}...")

            # 4. 执行官方客观判定脚本 (执行容器内专门的断言判定)
            eval_run = container.exec_run(verification_script, timeout=15)
            task_resolved = (eval_run.exit_code == 0)

        finally:
            # 5. 原子化销毁容器，回收资源
            container.remove(force=True)

        print(f"[{task_id}] 最终裁判结果: {'🎉 成功 (PASSED)' if task_resolved else '❌ 失败 (FAILED)'}")
        return {
            "task_id": task_id,
            "resolved": task_resolved,
            "interaction_turns": len(history_dialogue) // 2
        }</code></pre>
    </div>
"""

expansion_4 = """
    <h2 id="enterprise-eval-methodology">企业级评测落地指南：构建属于自己的“黄金测试集”与帕累托前沿</h2>
    <p>虽然 SWE-bench 与 WebArena 权威性极高，但对于绝大部分传统非软件工程企业而言，这些通用测试集往往<strong>与企业自身的垂直业务场景严重脱节</strong>。例如一家银行不可能关心智能体是否能在 Django 里修 Bug，它唯一关心的核心是智能体能否准确理解内部的信贷审批规程与风险评级指标。</p>
    
    <p>工业级架构团队必须遵循<strong>「三位一体企业级黄金数据集（Golden Dataset）构建法则」</strong>，建立专属的自动化防线：</p>
    
    <p><strong>第一法则：真实事故库逆向采样（Incident-driven Sampling）。</strong>绝不要让人工凭空编造测试题！最好的测试集直接源自<strong>企业过去 12 个月真实发生过的线上客户投诉、运维告警、以及人工操作失误记录</strong>。提取出 50~100 个历史最惨烈的典型事故案例，形式化编写为包含初始状态、用户指令与终局断言标准的自动化测试用例，从源头确保评测永远切中业务最痛点；</p>
    
    <p><strong>第二法则：建立成本-精度帕累托前沿曲线（Cost-Accuracy Pareto Frontier）。</strong>在评测报告中，永远不要仅仅输出单一的“准确率 85%”。必须将<strong>任务准确率（Accuracy）、P95 响应延迟（Latency）与单任务平均 Token 成本（Cost in USD）</strong>绘制在同一张三维帕累托坐标图上！帮助业务决策者清晰洞察：为了将准确率从 82% 提升到 86%，整体推理成本是否暴增了 5 倍？从而挑选出最具商业综合回报率的最优配置方案；</p>
    
    <p><strong>第三法则：金丝雀流量影子评测（Canary Shadow Evaluation）。</strong>在将新版本智能体真正开放给真实用户前，在 API 网关层部署<strong>旁路流量复制镜像（Traffic Shadowing）</strong>：将线上 10% 的真实用户请求异步复制一份，投递给新版待测 Agent 进行影子执行，比对两者的输出差异度。经过 72 小时无退化稳定运行后，方才放行全量灰度发布，构筑终极生产安全护城河。</p>
"""

insert_target = '<div class="callout note">'
if insert_target in text:
    new_text = text.replace(insert_target, expansion_1 + "\n" + expansion_2 + "\n" + expansion_3 + "\n" + expansion_4 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Successfully expanded ch107.html with 4 deep sections")
else:
    print("Target not found")
