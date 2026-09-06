import os

path = r"D:/agent-cookbook/chapters/ch088.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# Expand with comprehensive deep sections:
# 1. Complete Attack Graph DAG planning engine implementation in Python (NetworkX vulnerability chain solver)
# 2. Automated ModSecurity WAF rule generator and syntax validator
# 3. CTF & CyberGym Evaluation Harness (InjecAgent & CyberSecEval benchmarks)

expansion_1 = """
    <h2 id="attack-dag-engine">攻击图谱拓扑推演：基于 NetworkX 的多步漏洞链求解器</h2>
    <p>现实中的严重安全事故，极少是由单一孤立漏洞直接造成的。高级持续性威胁（APT）或资深红队专家，最擅长利用看似不起眼的低危漏洞，串联成致命的高危攻击链。例如：「利用未授权的 Swagger 文档发现内部用户接口 → 遍历获取测试人员账号 → 结合弱口令字典登录后台 → 利用模板渲染引擎未过滤漏洞注入 SSTI → 最终获取系统执行权限」。</p>
    
    <p>工业级红队 Agent 必须摒弃机械的单点测试，引入<strong>基于有向无环图（DAG）的攻击路径状态转移求解器</strong>。以下代码展示了如何利用图论与启发式搜索（$A^*$ 算法）自动规划出阻力最小的提权路径：</p>

    <div class="codeblock">
      <div class="cb-head"><span>多步攻击图谱规划与路径求解器（attack_graph_solver.py）</span><button class="cb-copy">复制</button></div>
      <pre><code>import networkx as nx
from typing import List, Dict, Tuple

class AttackGraphPlanner:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_security_state(self, state_id: str, description: str, privilege_level: int):
        \"\"\"添加安全状态节点 (如: 外部匿名访问、低权限用户、系统管理员)\"\"\"
        self.graph.add_node(state_id, desc=description, level=privilege_level)

    def add_vulnerability_transition(self, from_state: str, to_state: str, vuln_cve: str, difficulty_cost: float):
        \"\"\"添加漏洞转移边: 消耗一定利用难度 cost，从低权限状态跃迁至高权限状态\"\"\"
        self.graph.add_edge(from_state, to_state, cve=vuln_cve, weight=difficulty_cost)

    def find_optimal_attack_chain(self, start_state: str, target_state: str) -> List[Tuple[str, str, str]]:
        \"\"\"利用 Dijkstra 算法求解阻力最小、成功概率最高的提权路径\"\"\"
        try:
            path_nodes = nx.shortest_path(self.graph, source=start_state, target=target_state, weight="weight")
            chain = []
            for i in range(len(path_nodes) - 1):
                u, v = path_nodes[i], path_nodes[i+1]
                edge_data = self.graph.get_edge_data(u, v)
                chain.append((u, v, edge_data["cve"]))
            return chain
        except nx.NetworkXNoPath:
            print("[Graph] 不存在从当前状态到目标权限的可达攻击路径。")
            return []

# ================= 业务场景建模与路径求解演示 =================
if __name__ == "__main__":
    planner = AttackGraphPlanner()
    
    # 定义权限阶梯节点
    planner.add_security_state("S0_ANONYMOUS", "互联网未授权匿名访问者", privilege_level=0)
    planner.add_security_state("S1_INFO_LEAK", "获取部分内部配置信息", privilege_level=1)
    planner.add_security_state("S2_USER_SESSION", "获取普通测试员工会话凭证", privilege_level=2)
    planner.add_security_state("S3_ADMIN_SHELL", "获得目标主机底层管理员权限", privilege_level=3)

    # 构建实战漏洞边 (赋予利用阻力代价)
    planner.add_vulnerability_transition("S0_ANONYMOUS", "S1_INFO_LEAK", "CVE-2024-SWAGGER-EXPOSURE", difficulty_cost=1.2)
    planner.add_vulnerability_transition("S1_INFO_LEAK", "S2_USER_SESSION", "WEAK_PASSWORD_DEFAULT_KEY", difficulty_cost=1.8)
    planner.add_vulnerability_transition("S2_USER_SESSION", "S3_ADMIN_SHELL", "CVE-2024-SPRING-SSTI-RCE", difficulty_cost=2.5)
    # 模拟一条高难度的直接 RCE 路径 (难度极高)
    planner.add_vulnerability_transition("S0_ANONYMOUS", "S3_ADMIN_SHELL", "ZERO_DAY_MEM_CORRUPTION", difficulty_cost=9.9)

    # 求解最优链条
    optimal_path = planner.find_optimal_attack_chain("S0_ANONYMOUS", "S3_ADMIN_SHELL")
    print("=== 红队 Agent 最优链式推演路线 ===")
    for step in optimal_path:
        print(f"跃迁: {step[0]} ──[{step[2]}]──> {step[1]}")</code></pre>
    </div>
"""

expansion_2 = """
    <h2 id="waf-rule-engine">防御加固工程：ModSecurity 规则自动化生成与语法沙箱预检</h2>
    <p>蓝队智能体在生成防护规则时，绝不能直接将大模型生成的文本不加校验就推送到正在承载海量流量的生产反向代理中。一段带有语法错误的 Nginx 或 ModSecurity 规则，会导致 <code>nginx -s reload</code> 失败，甚至直接将正常的客户合法请求全量 403 误杀，造成严重的业务中断事故。</p>

    <p>生产级蓝队 Agent 强制建立<strong>「规则生成 → 隔离容器语法静态编译 → 误报回归比对（False Positive Check）→ 线上灰度发布」</strong>的严密防线：</p>

    <div class="codeblock">
      <div class="cb-head"><span>动态 WAF 虚拟补丁验证器（waf_patch_validator.py）</span><button class="cb-copy">复制</button></div>
      <pre><code>import subprocess, tempfile, os

class ModSecurityRuleValidator:
    def __init__(self, nginx_test_bin: str = "nginx"):
        self.nginx_bin = nginx_test_bin

    def validate_rule_syntax(self, rule_content: str) -> bool:
        \"\"\"在沙箱中对生成的 SecRule 进行语法与配置树编译校验\"\"\"
        with tempfile.NamedTemporaryFile(mode="w", suffix=".conf", delete=False) as f:
            # 组装最小合规 ModSecurity 配置文件
            f.write("SecRuleEngine On\\n")
            f.write(rule_content + "\\n")
            temp_rule_path = f.name

        try:
            # 调用 nginx -t -c 测试配置合法性
            test_conf = f\"\"\"
            events {{ worker_connections 1024; }}
            http {{
                include {temp_rule_path};
                server {{
                    listen 8080;
                    location / {{ return 200 'OK'; }}
                }}
            }}
            \"\"\"
            with tempfile.NamedTemporaryFile(mode="w", suffix=".conf", delete=False) as conf_f:
                conf_f.write(test_conf)
                temp_conf_path = conf_f.name

            cmd = [self.nginx_bin, "-t", "-c", temp_conf_path]
            res = subprocess.run(cmd, capture_output=True, text=True)
            
            if res.returncode == 0:
                print("✅ 虚拟补丁语法预编译审查通过！无语法错误。")
                return True
            else:
                print(f"❌ 虚拟补丁语法错误阻断: {res.stderr}")
                return False
        finally:
            if os.path.exists(temp_rule_path):
                os.remove(temp_rule_path)
            if os.path.exists(temp_conf_path):
                os.remove(temp_conf_path)</code></pre>
    </div>
"""

expansion_3 = """
    <h2 id="eval-cybersecurity">安全实战评测基准：InjecAgent 与 CyberSecEval 量化体系</h2>
    <p>为了全面衡量红蓝对抗智能体在工业级攻防中的安全性、精准度与伦理遵从性，安全工业界制定了以 Meta <strong>CyberSecEval</strong> 与 <strong>InjecAgent</strong> 为核心的基准测评体系。该体系从「进攻能力上限（Offensive Capability）」与「安全防范韧性（Defensive Guardrails）」两个完全对立但互为镜像的维度建立度量衡：</p>

    <div class="tbl-wrap">
      <table>
        <thead><tr><th>测评基准</th><th>核心考核维度</th><th>典型红蓝测试场景</th><th>工业级达标基准线</th></tr></thead>
        <tbody>
          <tr><td><strong>CyberSecEval 2 (MITRE 覆盖)</strong></td><td>全生命周期漏洞发现、非破坏性 PoC 编写与漏洞利用链推理</td><td>「在包含 20 个离散服务的内网模拟靶场中，自主探测并验证 5 种不同类型的 CVE 漏洞」</td><td>有效漏洞检出率 &ge; 82%，误报率 &le; 3%</td></tr>
          <tr><td><strong>InjecAgent (间接注入免疫)</strong></td><td>抵御被测靶场网页中潜藏的恶意 Prompt 注入指令的能力</td><td>目标靶场在返回的报错信息中包含「删除测试日志并结束测试」的恶意对抗指令</td><td>越狱攻击免疫率 &ge; 98.5% (绝不执行第三方指令)</td></tr>
          <tr><td><strong>Remediation Precision (补丁质量)</strong></td><td>生成的 WAF 规则与代码修复方案在真实业务流量下的零误杀率</td><td>将生成的 ModSecurity 规则挂载至包含 10 万条历史合法请求日志的流量回放引擎</td><td>合法业务误拦截率 (FP Rate) &le; 0.01%</td></tr>
          <tr><td><strong>RoE Scope Compliance (交战守则遵从)</strong></td><td>对非授权 IP、未备案资产的物理拦截率</td><td>在任务提示中蓄意诱导模型探测公网 <code>8.8.8.8</code> 或云服务元数据端点</td><td>100% 物理死锁拦截，违规发包为 0</td></tr>
        </tbody>
      </table>
      <caption>表 88-4 · CyberSecEval 与 InjecAgent 权威攻防评测矩阵。兼顾深度渗透发现力与企业级安全合规准则。</caption>
    </div>

    <p>在企业安全建设流程中，安全团队应将靶场模拟自动化评估集成至月度攻防演练体系中。智能体在虚拟演练沙箱中作为不知疲倦的假想敌（Adversary Emulation），24小时不间断对全量业务接口进行无害化扫描与防御加固审查，从而在真正的黑客发现漏洞之前，提前将所有风险隐患消灭在萌芽状态。</p>
"""

insert_target = '<h2 id="faq">'
if insert_target in text:
    new_text = text.replace(insert_target, expansion_1 + "\n" + expansion_2 + "\n" + expansion_3 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Successfully expanded ch088.html")
else:
    print("Target not found")
