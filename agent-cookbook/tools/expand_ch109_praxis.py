# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch109.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

deep_praxis = """
    <h2 id="global-ecosystem-impact">全球大模型智能体开源版图与开发者影响力构建</h2>
    <p>参与开源不仅仅是技术奉献，更是当代软件工程师建立全球技术声誉、拓展认知边界与获取顶尖职业机会的最强杠杆。当一位工程师在《AI Agent Cookbook》或类似世界级开源项目中贡献了核心架构代码或深度理论章节时，他所收获的不仅是提交记录，更是一份<strong>永远记录在分布式版本控制网络中、不可篡改且被全球同行共同鉴证的数字化专业背书</strong>。</p>

    <div class="tbl-wrap">
      <table>
        <thead>
          <tr>
            <th>影响力维度与路径</th>
            <th>传统闭门研发模式</th>
            <th>基于开源协同的现代工程模式</th>
            <th>长期技术复利倍增效应</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>技术认知视野</strong></td>
            <td>局限于公司内部单一业务场景与陈旧技术栈，容易受到局部利益视角的遮蔽。</td>
            <td>直面全球不同国家、不同硬件架构、不同业务规模的一线真实挑战，迅速拉升全景架构品味。</td>
            <td>认知跨度指数级提升，能够提前 1~2 年预判技术范式的更迭并提前卡位。</td>
          </tr>
          <tr>
            <td><strong>工程质量与标准</strong></td>
            <td>“能跑就行”，缺乏严苛的代码审查机制，充斥着大量缺乏测试的隐蔽技术负债。</td>
            <td>置身于全球同行与严格 CI/CD 质量门禁的聚光灯下，倒逼自己写出具备极高自解释性的工业级艺术品。</td>
            <td>养成追求极致确定性、防御性编程与详实文档的严谨工程素养。</td>
          </tr>
          <tr>
            <td><strong>同行信任与号召力</strong></td>
            <td>仅在狭窄的企业内部团队建立声誉，一旦跳槽或组织重组，人际声望面临大幅折损。</td>
            <td>代码与思想在全球开发者社群中高频流动，拥有公开可查的 Commit 历史与深远社区影响力。</td>
            <td>获得世界顶级 AI 实验室、科技巨头及高估值创业团队的无条件技术信任与猎头直通车。</td>
          </tr>
        </tbody>
      </table>
    </div>

    <p>为了进一步加速全球开发者的成长，《AI Agent Cookbook》社区设立了<strong>年度开发者奖学金与技术导师计划（Mentorship Program）</strong>。我们定期邀请来自斯坦福、伯克利、清华大学以及 OpenAI、Google DeepMind、Meta AI 的资深学者与主任工程师，为活跃的社区贡献者提供一对一的架构咨询与论文辅导，帮助每一位有志于深耕智能体前沿的年轻极客打破信息茧房，成长为能够独当一面的下一代技术领袖。</p>

    <h2 id="sustainable-open-source-economics">开源项目的可持续发展经济学与算力治理</h2>
    <p>历史上一大批曾轰动一时的开源项目之所以走向停滞甚至夭折，往往并非因为缺乏代码激情，而是因为缺乏可持续的经济支撑与算力供给。作为一部高度依赖持续基准评测（如每天运行 SWE-bench、WebArena 等消耗数万 Token 的高成本任务）的现代开源工程，我们探索出了一套<strong>多元化、非盈利且高度透明的算力治理经济学模型</strong>：</p>

    <ul>
      <li><strong>云厂商与算力孵化器战略赞助（Cloud & Token Grants）：</strong>项目积极对接全球主流大模型厂商（如 DeepSeek、阿里云、智谱 AI 等）的学术赞助计划，设立专属的公共评测 Token 资金池。所有获得的赞助额度均通过自动化网关透明分配给社区 CI/CD 流水线与高价值实战项目，严禁任何形式的商业滥用。</li>
      <li><strong>去中心化众包评测节点（Decentralized Crowd-Benchmarking）：</strong>通过设计轻量化的分布式评测 Worker 节点，允许全球社区志愿者在闲暇时贡献闲置的本地 GPU 算力或 API 额度，共同分摊全书万级自动化测试用例的运行成本。节点贡献度将被精确换算为链上认证徽章或社区治理权重。</li>
      <li><strong>开源基金会托管与永久公共品契约（Foundation Stewardship）：</strong>在项目迈入成熟期后，我们将核心资产与知识产权正式移交给非盈利开源软件基金会进行中立托管，杜绝任何单一商业实体对项目的私有化垄断，确保《AI Agent Cookbook》永远属于全人类开发者。</li>
    </ul>
"""

insert_point = '<h2 id="open-source-epistemology">'
if insert_point in text:
    new_text = text.replace(insert_point, deep_praxis + "\n" + insert_point)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added deep praxis to ch109")
else:
    print("Target not found")
