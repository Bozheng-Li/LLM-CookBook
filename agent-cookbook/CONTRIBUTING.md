# 贡献指南（CONTRIBUTING）

感谢你对《AI Agent Cookbook》的兴趣！本书是「活的书」：技术演化到哪里，它就更新到哪里。以下是参与方式与质量标准。

## 如何报告问题

1. **技术错误**（公式错误、代码不能跑、论文引用错误）：开 Issue，标题格式 `[Err] Ch016 · 2.3 节 · 描述`；
2. **表述问题**（翻译不准、示例难懂）：标题格式 `[Wording] ChXXX · 简述`；
3. **内容建议**（希望覆盖的主题）：标题格式 `[Request] 主题`。先搜索是否已有同类 Issue。

Issue 中请附上：章节锚点、引文（如为错误）、以及（如适用）可复现的代码或论文出处。

## 如何贡献章节

本书接受两类 PR：

- **修订类**：修正现有章节的错误或改进表述——直接修改对应 `chapters/chXXX.html`；
- **新增类**：补充新章节——先开 Issue 讨论定位，避免与现有章节重复。

### 质量闸门（强制）

所有 PR 必须通过以下检查，CI 会自动执行：

```bash
python tools/check_chapter.py --all        # 15 项硬指标:字数/结构/图/表/代码/引用/链接
python tools/build.py                      # 构建不报错,链接与图片全部有效
```

### 新增章节流程

1. 阅读 `docs/STYLE_GUIDE.md`（写作规范）与 `docs/chapter-template.html`（骨架模板）；
2. 在 `tools/toc.json` 登记章节（id/标题/摘要/级别/标签）——这是全书唯一事实来源；
3. 撰写章节：≥4000 汉字、≥1 图（优先用 `tools/figkit.py` 生成 SVG）、≥1 表、≥1 段可运行代码、≥4 条真实文献；
4. 代码中的 `<`/`>`/`&` 必须转义为 `&lt;`/`&gt;`/`&amp;`；
5. 运行质检与构建，通过后提交 PR。

### 图解规范

图解统一用 `tools/figkit.py` 生成（保证视觉语言一致）：

```python
import sys; sys.path.insert(0, "tools")
from figkit import *
f = F(900, 400)
f.box(60, 60, 200, 60, "模型", "决策中枢", fill=C.indigo_s, stroke=C.indigo)
f.arrow(260, 90, 340, 90, label="调用")
f.save("fig-my-figure")   # 输出 assets/figures/fig-my-figure.svg
```

不接受外部截图拼贴（版权与清晰度原因）；确需引用论文原图时，请用文字+自绘 SVG 重绘并注明「依据 XXX 重绘」。

## 风格底线

- 结论先行；每个论断给依据；不确定的数字写「量级」而非伪精确；
- 术语双语（「检索增强生成（RAG）」），此后可用缩写；
- 禁止空洞排比与 AI 腔；禁止编造论文/项目/数据——这是本书的硬红线；
- 引用格式：`作者 (年份). «标题». venue. arXiv:xxxx.xxxxx`。

## 评审流程

PR 将经过两级评审：①自动化闸门（脚本）；②内容评审（维护者 + LLM 辅助核查引用真实性）。通过后合并，并在 `CHANGELOG.md` 记录。

## 授权

贡献即同意你的内容以 CC BY-SA 4.0（文字/图解）与 MIT（代码）双许可发布。
