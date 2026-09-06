import os

path = r"D:/agent-cookbook/chapters/ch087.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

expansion_more = """
    <h2 id="webarena-benchmark">端到端能力量化：WebArena 与 VisualWebArena 基准对齐</h2>
    <p>为了精准量化 Web 前端与 GUI 智能体在面对复杂真实网站任务时的鲁棒性，学术界与工业界主要采用 <strong>WebArena</strong> 与 <strong>VisualWebArena</strong> 基准套件。这些基准在本地通过 Docker 镜像完整部署了真实且高度复杂的企业级开源项目（包括完整的 GitLab 仓库管理、GitPhoria 论坛系统、Postmill 社交发帖平台与开源电商系统 Shopping）。Agent 必须像真实的前端测试工程师一样，不仅要理解网页视觉布局，还要能自主完成点击、悬停、填写多步骤级联下拉框、拖拽滑块以及提交表单等长程闭环。</p>

    <div class="tbl-wrap">
      <table>
        <thead><tr><th>评测任务维度</th><th>测试考察重点</th><th>典型真实验收场景</th><th>Web Agent 达标基准</th></tr></thead>
        <tbody>
          <tr><td><strong>多步骤表单级联交互 (Multi-step Form)</strong></td><td>上下文状态传递、字段联动校验、错误提示识别</td><td>「在电商后台发布一件新商品，上传两张详情图并设定多规格阶梯价格」</td><td>端到端动作成功率 &ge; 78%</td></tr>
          <tr><td><strong>视觉目标精确导航 (Visual Target Nav)</strong></td><td>在密集的商品瀑布流中定位特定样式的图标</td><td>「点击右上角用户头像下拉菜单中带有小齿轮图标的‘高级安全设置’选项」</td><td>首次点击命中率 &ge; 88%</td></tr>
          <tr><td><strong>动态内容变更等待 (Dynamic Wait)</strong></td><td>AJAX / Fetch 异步更新侦测，避免过早误判</td><td>「点击生成报表后，等待 Loading 转圈消失并断言下载按钮变为可用状态」</td><td>无超时早退，判定准确率 &ge; 95%</td></tr>
          <tr><td><strong>跨页面上下文回溯 (Page History)</strong></td><td>浏览器前进、后退、刷新与局部状态持久化</td><td>「进入详情页修改地址后点击后退，确认列表页缓存已自动增量刷新」</td><td>状态同步无退化 &ge; 92%</td></tr>
        </tbody>
      </table>
      <caption>表 87-3 · VisualWebArena 真实 Web 环境基准评测矩阵。覆盖长程表单、视觉导航、动态异步与历史状态机。</caption>
    </div>

    <p>在研发持续集成流程中，团队应为 Web Agent 搭建轻量级端到端测试流水线。每当修改前端生成 Prompt 或调整视觉差分对齐阈值时，自动调度 30 个代表性 WebArena 任务进行全量回归。唯有在真实的浏览器 DOM、网络与样式引擎中历经千锤百炼，前端 Agent 才能真正胜任复杂商业软件的自动化交付重任。</p>
"""

insert_target = '<h2 id="faq">'
if insert_target in text:
    new_text = text.replace(insert_target, expansion_more + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added WebArena benchmark section")
else:
    print("Target not found")
