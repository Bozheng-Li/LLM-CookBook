import os

path = r"D:/agent-cookbook/chapters/ch090.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

expansion_more = """
    <h2 id="part-9-milestone-review">实战篇全景里程碑回眸：十战十捷的工程大满贯</h2>
    <p>随着本章全知科研助理与文献挖掘 Agent 的圆满落地，<strong>AI Agent Cookbook 第九部分·实战篇（第 81 章至第 90 章）正式迎来辉煌收官！</strong>回顾这整整十个横跨各行各业的超级实战项目，我们构建起了一幅前所未有的工业级智能体落地工程全景画卷：</p>
    
    <div class="tbl-wrap">
      <table>
        <thead><tr><th>项目序号与章节</th><th>实战核心领域</th><th>突破的核心技术壁垒</th><th>交付的工业级生产模块</th></tr></thead>
        <tbody>
          <tr><td><strong>项目 1 (第81章)</strong></td><td>个人知识库问答 Agent</td><td>父子文档分块、BM25 + BGE 向量混合检索与 RRF 融合</td><td>带严格忠实性契约与精准引用编号的 Streamlit 生产工作台</td></tr>
          <tr><td><strong>项目 2 (第82章)</strong></td><td>自动化数据分析师</td><td>动态 Schema 剪枝、CTE 语法树自愈重试与四重沙箱隔离</td><td>带 Z-score 异常检测与斯皮尔曼相关性归因的 Python 数据智能引擎</td></tr>
          <tr><td><strong>项目 3 (第83章)</strong></td><td>复刻 Deep Research</td><td>假设树演进剪枝、贝叶斯真值发现（Truth Discovery）与长文装配</td><td>支持深度递归探索与反向事实核验的万字行研报告生成系统</td></tr>
          <tr><td><strong>项目 4 (第84章)</strong></td><td>企业级代码助手与 Repo Agent</td><td>Tree-sitter Repo Map 符号拓扑压缩与 SEARCH/REPLACE 精准补丁</td><td>Git Worktree 物理隔离沙箱与基于 SWE-bench 的双向测试自愈环</td></tr>
          <tr><td><strong>项目 5 (第85章)</strong></td><td>企业工作流自动化 Agent</td><td>API 与 GUI RPA 双轨融合、分布式 Saga 事务补偿与幂等性令牌</td><td>具备人机协同（HITL）审批门禁与毫秒级防重复扣款的业务调度器</td></tr>
          <tr><td><strong>项目 6 (第86章)</strong></td><td>端侧移动端轻量化 Agent</td><td>无障碍 UI 树三级剪枝、GBNF 语法约束解码与 Q4_K_M 极限量化</td><td>Android 原生 Kotlin 无障碍服务与动态温控休眠自调节引擎</td></tr>
          <tr><td><strong>项目 7 (第87章)</strong></td><td>全栈前端与 GUI 测试 Agent</td><td>Figma 原子化拆解、Playwright 无头沙箱与 SSIM 结构相似性比对</td><td>MSW 契约拦截桩与支持响应式多视口热力图差分自愈的 Web 引擎</td></tr>
          <tr><td><strong>项目 8 (第88章)</strong></td><td>渗透测试与红蓝对抗 Agent</td><td>NetworkX 攻击图谱推演、带外 OOB DNSLog 无害化验证与 RoE 约束</td><td>动态 ModSecurity WAF 虚拟补丁预检与代码级防御加固闭环</td></tr>
          <tr><td><strong>项目 9 (第89章)</strong></td><td>具身操作系统 Agent</td><td>千分比相对归一化空间坐标、三次贝塞尔拟真手势与两帧差分比对</td><td>Docker+Xvfb 隔离虚拟桌面与具备物理 Panic Button 的外设驱动器</td></tr>
          <tr><td><strong>项目 10 (第90章)</strong></td><td>全知科研助理与文献挖掘</td><td>双向引用滚雪球、Louvain 演化拓扑社群聚类与 Nougat 公式转录</td><td>学术引文零幻觉真实性断言与前沿科研假说消融实验生成执行器</td></tr>
        </tbody>
      </table>
      <caption>表 90-4 · 第九部分实战篇十个核心工业级项目全景对账表。从纯软件算法到物理桌面、从底层二进制到高层战略研究，全方位打通智能体实战全生命周期。</caption>
    </div>

    <p>这十个硬核项目绝非停留在“调包演示”的玩具级别，而是每一个都凝聚了一线大厂在面对高并发、网络抖动、幻觉失控、内存溢出与安全合规时的真实血泪避坑战法。这为读者跨入下一阶段——<strong>第十部分理论篇（第 91 章至第 98 章）探究智能体的数学物理本质与博弈论基石</strong>，铺就了最扎实、最底气十足的实操基石！</p>
"""

insert_target = '<h2 id="faq">'
if insert_target in text:
    new_text = text.replace(insert_target, expansion_more + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added Part 9 milestone review section")
else:
    print("Target not found")
