# 贡献指南

感谢你为《大模型技术 Cookbook》贡献内容。这个项目是一个纯静态知识站，目标是让复杂的大模型技术更容易学习、验证和落地。

## 开始之前

1. Fork 仓库并创建分支：

   ```bash
   git checkout -b docs/fix-attention-example
   ```

2. 使用静态服务器预览，不要直接依赖 `file://`：

   ```bash
   python -m http.server 8765 --directory .
   ```

3. 阅读 `tools/WRITING-GUIDE.md`，熟悉页面结构、组件和引用规范。

## 页面修改规范

- 知识点页面第二行保留 `<!-- cookbook:handcrafted -->`，否则运行生成器时可能被覆盖。
- 页面内交叉引用使用相对路径；外部资源使用可验证的 HTTPS URL。
- 公式使用项目现有的 KaTeX 约定，Mermaid 节点文本使用双引号包裹。
- 表格套在 `.table-wrap` 内，图片填写有意义的 `alt` 文本。
- 不要为了达到数量门槛堆砌空洞正文、重复图表或无关外链。
- 对快速变化的模型、框架、价格、版本和基准结果标注日期，并尽量链接官方来源。
- 不要把个人凭据、API Key、内部文档、缓存、备份目录或浏览器截图提交到仓库。

## 质量检查

提交前至少运行：

```bash
python tools/check.py all
python tools/check_rendering.py all
```

如果修改了链接、图片或脚本，建议再使用本机浏览器打开以下页面检查：

- 首页 `index.html`
- 修改过的知识点页面
- `glossary.html`
- `dependency.html`

检查搜索、主题切换、侧边栏、页面目录、Mermaid、公式、代码高亮和窄屏布局是否正常。

## Commit 约定

推荐使用简短、可读的 Conventional Commits 风格：

- `docs: 补充 RoPE 长上下文说明`
- `fix: 修复页面交叉链接`
- `style: 优化首页移动端排版`
- `chore: 更新目录索引`

一次提交尽量只解决一个主题，并在提交说明中写清影响范围。

## Pull Request

PR 描述请包含：

- 修改了哪些页面或公共资源；
- 为什么需要这项修改；
- 是否新增或更新外部来源；
- `tools/check.py` 和 `tools/check_rendering.py` 的结果；
- 如涉及视觉变更，附上截图或预览地址。

维护者会重点检查事实准确性、引用可追溯性、页面结构、移动端体验和是否引入不必要的重复内容。
