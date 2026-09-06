import os

path = r"D:/agent-cookbook/chapters/ch086.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

expansion_more = """
    <h2 id="androidworld-benchmark">移动端端侧评测实战：AndroidWorld 与 OSWorld 真实测试套件</h2>
    <p>为了精准度量移动端智能体在真实手机操作系统中的端到端任务达成率，业界权威基准主要采用 <strong>AndroidWorld</strong> 与 <strong>Mobile-Eval</strong>。这些基准完全摒弃了在虚拟模拟器中做脱机文字选择题的落后形式，而是通过真机自动化编排脚本，实时向真实 Android 手机下发包含跨应用转账、多条件日历预订、电商比价下单等上百个长程综合任务。</p>

    <div class="tbl-wrap">
      <table>
        <thead><tr><th>评测任务类别</th><th>典型真机测试案例</th><th>涉及的核心移动端能力</th><th>端侧 Agent 达标基准线</th></tr></thead>
        <tbody>
          <tr><td><strong>跨应用数据迁移 (Cross-App)</strong></td><td>「将微信群聊中发来的一条地址文本，复制并添加到高德地图的收藏夹中」</td><td>剪贴板读写、应用前后台切换、意图广播匹配</td><td>任务成功率 &ge; 82%</td></tr>
          <tr><td><strong>多条件动态表单填写 (Complex Form)</strong></td><td>「在飞猪 App 中预订下周三从杭州到北京、下午出发且票价在 800 元以内的二等座高铁票」</td><td>日历滑动选择器、多重筛选过滤、价格排序确认</td><td>任务成功率 &ge; 75%</td></tr>
          <tr><td><strong>动态权限与安全弹窗穿透 (Security Guard)</strong></td><td>「首次打开某社交 App，自动允许定位权限但拒绝访问通讯录与相册」</td><td>系统原生运行时权限弹窗拦截（Runtime Permissions）</td><td>准确率 &ge; 96%</td></tr>
          <tr><td><strong>端侧长程抗退化能力 (Endurance)</strong></td><td>连续自主执行 30 个不同独立任务，中间不重启操作系统与 Agent 守护进程</td><td>内存泄漏（Memory Leak）防护、Activity 栈溢出规避</td><td>无 LMK 崩溃，内存波动 &le; 10%</td></tr>
        </tbody>
      </table>
      <caption>表 86-4 · AndroidWorld 真实移动端基准评测矩阵与工业达标红线。覆盖复杂系统交互、长程耐受性与权限自愈。</caption>
    </div>

    <p>在研发持续集成流程中，团队应搭建由 10~20 台覆盖不同屏幕分辨率、不同芯片平台（高通骁龙、天玑、联发科）组成的<strong>移动端真机自动化农场（Device Farm）</strong>。每当对端侧小模型权重进行剪枝微调或修改剪枝启发式算法时，系统自动并行触发全量 AndroidWorld 测试集回归，确保在多样化异构手机生态中始终维持零退化的极高稳定性。</p>
"""

insert_target = '<h2 id="faq">'
if insert_target in text:
    new_text = text.replace(insert_target, expansion_more + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added AndroidWorld benchmark section")
else:
    print("Target not found")
