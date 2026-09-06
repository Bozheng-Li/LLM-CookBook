import os

path = r"D:/agent-cookbook/chapters/ch082.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

expansion_more = """
    <p>在面对千万级明细数据时，高阶分析师 Agent 还会自适应开启「自抽样蒙特卡洛检验（Bootstrap Resampling）」与「方差膨胀因子（VIF）」评估，在向决策者下结论前主动剔除多重共线性特征。这一整套统计推断前置管线，使得自动化分析报告从原先轻浮的「看图说话描述性统计」，一跃升级为具备因果推断可信度的严谨经营分析决策内参。</p>
"""

insert_target = '<h2 id="production-checklist">'
if insert_target in text:
    new_text = text.replace(insert_target, expansion_more + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added bootstrap paragraph")
