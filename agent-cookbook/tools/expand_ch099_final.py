# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch099.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push = """
    <h2 id="paper-reading-methodology">学术文献研读的方法论跃迁：如何从经典中提炼下一代 Agent 架构</h2>
    <p>在人工智能领域，阅读顶级论文绝不应仅仅停留在“记诵结论与跑通开源 Demo”的初级层面上。真正的顶级系统架构师在研读一篇开创性论文时，通常采用<strong>「逆向工程与假设推演」三步批判法</strong>：</p>
    
    <p><strong>第一步（时代背景与理论天花板逆推）：</strong>作者在发表该论文的那个历史节点，学术界正普遍面临什么无法逾越的共同痛苦？例如在研读 Transformer 时，必须深刻体会到当年使用两层双向 LSTM 训练长文本时，GPU 计算利用率低下、训练周期长达数周、且长距离依赖必然衰退的绝望感。唯有深切体察到旧范式的致命缺陷，才能真正领会新机制为何能够掀起滔天巨浪。</p>
    
    <p><strong>第二步（寻找核心简洁性与奥卡姆剃刀）：</strong>最伟大的论文往往具有惊人的简洁性。《Attention Is All You Need》彻底删掉了循环与卷积，仅保留点积；《ReAct》仅仅在输出格式中插入了一个 <code>Thought:</code>；《Reflexion》仅仅将错误日志拼回了 Prompt；《Generative Agents》仅仅用一个三项加权线性公式计算记忆重要性。这种“大道至简”的设计哲学提醒我们：很多复杂的堆砌工程往往是方向错误的遮羞布，真正具备革命性突破的架构，往往能够用极其优雅纯粹的简单机制击穿最复杂的认知壁垒。</p>
    
    <p><strong>第三步（前瞻性推演与边界反思）：</strong>这篇论文成功掩盖了什么新的次生矛盾？例如 Transformer 带来了注意力平方复杂度与 KV-Cache 显存膨胀难题（进而催生了第 13 章的线性注意力与第 78 章的缓存经济学）；ReAct 带来了调用工具超时与上下文污染问题；Reflexion 带来了自欺欺人伪反思的风险；Generative Agents 带来了高昂的 Token 账单与社交漂移。学会在论文的掌声中敏锐捕捉下一代技术的潜在痛点，正是每一位研究者从跟随者蜕变为领航者的核心秘密武器。</p>
"""

insert_target = '<div class="callout note">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added paper reading methodology to ch099.html")
else:
    print("Target not found")
