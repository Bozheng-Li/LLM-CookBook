import os

path = r"D:/agent-cookbook/chapters/ch087.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

final_push_2 = """
    <p>在这个演进趋势下，前端开发正从过去“像素级手工搬砖”全面转向“规范定义与视觉监督”的全新高度。工程师只需要定义好核心业务状态机与设计系统规范，剩下的组件构建、响应式适配、跨浏览器兼容性检验与多模态回归测试，都可以完全托付给自闭环的 Web Agent 矩阵自主搞定。</p>
"""

insert_target = '<h2 id="production-checklist">'
if insert_target in text:
    new_text = text.replace(insert_target, final_push_2 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added final push 2")
