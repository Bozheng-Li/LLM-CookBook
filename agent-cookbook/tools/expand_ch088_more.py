import os

path = r"D:/agent-cookbook/chapters/ch088.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

expansion_more = """
    <h2 id="deep-mitre-tactics">实战映射：MITRE ATT&CK 战术矩阵全周期自动化映射</h2>
    <p>为了使生成的渗透测试报告具备国际标准的公信力，红蓝对抗 Agent 在每一步动作执行时，必须严格在内存中对齐 <strong>MITRE ATT&amp;CK</strong> 企业级战术知识库。从初始访问（Initial Access）、执行（Execution）、持久化防御绕过（Defense Evasion）到凭证访问（Credential Access），智能体在生成报告时自动标注对应的唯一战术编号（例如 <code>T1190: Exploit Public-Facing Application</code> 或 <code>T1059: Command and Scripting Interpreter</code>）。</p>
    
    <p>这种高度标准化的战术映射能力，使得安全总监（CISO）不仅能看到「哪里有个漏洞」，更能一目了然看清「该漏洞在企业防御纵深体系中处于第几道防线，攻击者以此为跳板在几步之内可以威胁到核心生产数据库」。以此为输入，蓝队不仅能生成点对点的单点补丁，更能推动全局网络分段（Micro-segmentation）与零信任架构（Zero Trust）的深层次战略加固。</p>
"""

insert_target = '<h2 id="faq">'
if insert_target in text:
    new_text = text.replace(insert_target, expansion_more + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added MITRE tactics mapping")
else:
    print("Target not found")
