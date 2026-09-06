import os

path = r"D:/agent-cookbook/chapters/ch084.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

expansion_extra = """
    <h2 id="ast-refactoring-patterns">高级重构模式：AST 模式匹配与无损代码变换</h2>
    <p>在企业级重构中，往往需要批量将上千个源文件中的废弃 API 迁移至全新版本（例如将所有的旧版同步网络请求 <code>requests.get()</code> 批量平滑迁移至高性能异步调用 <code>httpx.AsyncClient().get()</code>）。如果仅仅依赖大语言模型逐文件盲目猜测重写，不仅耗费巨额 API 成本，更极易引入由于缩进错误或意外删减导致的灾难性语法崩溃。</p>

    <p>成熟的工程实践采用<strong>「声明式 AST 模式匹配与模型辅助（Rule-based AST Matcher + LLM-assisted Transform）」</strong>的混合双轨流水线：</p>
    <p><strong>第一步（模式匹配与锚点定位）：</strong>利用基于 AST 语法树的查询工具（如 AST-grep 或 LibCST），在秒级时间内全库精准命中所有需要改动的代码调用节点，并抽取出局部代码切片与其上下文函数体。</p>
    <p><strong>第二步（局部受限上下文变换）：</strong>将精准裁剪出的代码片段（约 15~30 行）送入专精代码模型，要求其仅针对语法树的目标子节点完成异步重写并注入异常捕获守卫（Try-Catch Guard）。</p>
    <p><strong>第三步（无损节点替换与格式化）：</strong>将模型返回的重写节点重新缝合回原始 AST 语法树中，最后通过代码格式化工具（如 Black、Ruff 或 Prettier）自动执行标准化对齐与空行整理。这种「语法树骨架锁死、模型仅填补血肉」的工业级混编架构，既发挥了大模型理解复杂语义的强大智能，又保留了传统编译器确定性语法树分析的坚固安全性，在大规模跨工程批量重构战役中立下了汗马功劳。</p>
"""

insert_target = '<h2 id="faq">'
if insert_target in text:
    new_text = text.replace(insert_target, expansion_extra + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added AST refactoring patterns")
else:
    print("Target not found")
