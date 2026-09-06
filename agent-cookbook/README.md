# AI Agent Cookbook 🤖📖

**从入门到精通的智能体全景手册 —— 一本图文并茂、可运行、有文献支撑的开源 Cookbook。**

> 架构 · 机制 · 训练与强化 · 工程实战 · 论文与项目全景
> **14 个部分 · 113 章 · 4 个附录 · 80+ 原创图解 · 8 个完整实战项目 · 100 篇论文地图**

[![Chapters](https://img.shields.io/badge/%E7%AB%A0%E8%8A%82-113%2B4-blue)](#-全书目录) [![Figures](https://img.shields.io/badge/%E5%8E%9F%E5%88%9B%E5%9B%BE%E8%A1%A8-80%2B-green)](assets/figures/) [![License](https://img.shields.io/badge/%E5%86%85%E5%AE%B9%E8%AE%B8%E5%8F%AF-CC%20BY--SA%204.0-orange)](LICENSE) [![Status](https://img.shields.io/badge/%E7%8A%B6%E6%80%81-v1.0%20%E6%8C%81%E7%BB%AD%E8%BF%AD%E4%BB%A3-success)](CHANGELOG.md)

---

## ✨ 这是什么

一本写给**聪明成年人**的 AI Agent 全景手册：

- **🧱 从地基到深水区**：Transformer 原理 → Agent Loop / ReAct / 工具调用 / 记忆 / RAG / 多智能体 → RLHF、DPO、RLVR、Agent RL 训练 → 生产架构与安全治理 → MDP 理论与论文精读。
- **🛠 可运行优先**：200 行手写最小 Agent、8 个完整实战项目、可复现的训练配置 —— 代码复制即可运行。
- **📊 原创图解**：每张架构图 / 流程图 / 时间线均以统一视觉语言用脚本生成（`tools/figkit.py`），开源可复用，拒绝截图拼贴。
- **📚 文献支撑**：每个关键论断标注论文出处（含 arXiv 编号），10 篇奠基论文逐篇精读，100 篇前沿论文分类地图。
- **🛡 安全是一等公民**：威胁模型、间接 Prompt 注入攻防、沙箱与权限、幻觉治理、合规。
- **🧭 为自学设计**：三条学习路径、每章小结 + 自测题、术语表、面试题库、里程碑自检。

**在线阅读**：克隆仓库后直接打开 `index.html`，或启动本地服务器：

```bash
git clone https://github.com/ai-agent-cookbook/ai-agent-cookbook.git
cd ai-agent-cookbook
python -m http.server 8080   # 打开 http://localhost:8080
```

支持**深浅双主题**、**全书全文搜索**（按 `/` 唤起）、**单页打印版**（`print.html`，可打印为 PDF）。

## 🗺 三条学习路径

| 你是 | 路径 | 时长 | 主线章节 |
|---|---|---|---|
| 🧱 开发者/学生 | 建立直觉，跑通第一个 Agent | 3-4 周 | Ch14-17 → Ch27 手写最小 Agent → Ch81-88 实战项目 |
| 🛠 工程师/架构师 | 交付可靠的生产系统 | 6-8 周 | 机制篇全读 → 框架选型 Ch26-37 → 评测 Ch50-57 → 安全 Ch58-65 |
| 🔬 研究者/算法 | 推进前沿，建立文献坐标系 | 8-10 周 | 训练篇 Ch38-49 → 理论篇 Ch91-98 → 论文库 Ch99-104 |

完整指南见 [第 2 章](chapters/ch002.html)。

## 📖 全书目录

<details open>
<summary><b>展开 14 个部分</b></summary>

| 部分 | 内容 | 章节 |
|---|---|---|
| **0 导论** | 为什么是 Agent、学习路径、通识与七十年简史 | Ch1-3 |
| **1 基础篇** | LLM 原理、Token 与采样、提示工程、结构化输出、Embedding、API 工程 | Ch4-13 |
| **2 核心机制篇** | Agent Loop、ReAct、工具调用、规划、记忆、RAG、反思、上下文工程、多智能体、人机协同 | Ch14-25 |
| **3 工程与框架篇** | 技术栈选型、200 行手写 Agent、LangGraph、OpenAI/Claude Agents SDK、AutoGen、CrewAI、MetaGPT、LlamaIndex、低代码、MCP、A2A | Ch26-37 |
| **4 训练与强化篇** | SFT、RLHF/PPO、DPO 家族、RLAIF、RLVR、工具使用训练、Agent RL、PRM/ORM、合成数据、蒸馏、Self-Play | Ch38-49 |
| **5 评测基准篇** | 评测方法论、SWE-bench、WebArena/OSWorld、GAIA/τ-bench、工具评测、安全评测、自建评测、LLM-as-Judge | Ch50-57 |
| **6 安全与对齐篇** | 威胁模型、Prompt 注入攻防、权限与沙箱、供应链、越狱、幻觉治理、对齐、合规治理 | Ch58-65 |
| **7 多模态与具身篇** | VLM Agent、GUI/Computer Use、移动与 OS Agent、具身 VLA、游戏、科学发现、语音 Agent | Ch66-72 |
| **8 前沿专题篇** | Deep Research、Coding Agent、Computer Use 前沿、长时程、世界模型、经济学、可观测性、规模化 | Ch73-80 |
| **9 实战项目篇** | 8 个完整项目（知识库/数据分析/深度研究/浏览器/代码审查/内容工厂/客服/本地化）+ 生产化 + 顶级产品拆解 | Ch81-90 |
| **10 理论基础篇** | MDP/POMDP、In-context RL、搜索与 MCTS、规划理论、BDI 遗产、贝叶斯决策、世界模型、涌现 | Ch91-98 |
| **11 论文库篇** | 阅读方法论、奠基十篇精读、机制/训练/评测安全论文地图、百篇前沿清单 | Ch99-104 |
| **12 项目与资源库篇** | 框架横评决策树、50 个必 Star 项目、数据集大全、课程书单、贡献指南 | Ch105-109 |
| **13 面试与速查篇** | 基础 50 题 + 进阶 50 题精解、系统设计面试、300 条术语表 | Ch110-113 |
| **附录** | A 大事记（1950-2026）· B 排错手册 · C Prompt/架构模板库 · D 参考资料总目 | AppA-D |

</details>

## 🚀 快速体验：30 行的最小 Agent

```python
from openai import OpenAI
import json

client = OpenAI()
tools = [{"type": "function", "function": {
    "name": "search", "description": "搜索外部信息",
    "parameters": {"type": "object",
                   "properties": {"query": {"type": "string"}}}}}]
messages = [{"role": "user", "content": "2020年奥斯卡最佳影片是哪部?"}]

for step in range(10):                       # 刹车: 步数上限
    r = client.chat.completions.create(
        model="gpt-4o-mini", messages=messages, tools=tools)
    msg = r.choices[0].message
    messages.append(msg)
    if not msg.tool_calls:                   # 模型决定完成
        print(msg.content); break
    for tc in msg.tool_calls:                # 执行并回填观察
        result = search(**json.loads(tc.function.arguments))
        messages.append({"role": "tool",
                         "tool_call_id": tc.id, "content": result})
```

循环 + 工具 + 观察回填 —— 这就是所有 Agent 框架的内核。完整讲解见 [第 15 章](chapters/ch015.html)。

## 📊 工程结构

```
ai-agent-cookbook/
├── index.html               # 首页(路径图/统计/全目录)
├── print.html               # 单页打印版(构建生成)
├── chapters/                # 113 章 + 4 附录(独立 HTML)
├── assets/
│   ├── css/style.css        # 设计系统(双主题/打印样式)
│   ├── js/app.js            # 搜索/导航/主题
│   ├── figures/             # 80+ 原创SVG图解
│   └── search-index.json    # 全文搜索索引(构建生成)
├── tools/
│   ├── figkit.py            # SVG图解生成库(统一视觉语言)
│   ├── figures_*.py         # 图解定义脚本
│   ├── build.py             # 构建:侧栏/目录/索引/打印版/统计
│   ├── check_chapter.py     # 章节质检闸门(15项硬指标)
│   └── toc.json             # 全书目录(唯一事实来源)
└── docs/                    # 写作规范与模板
```

常用命令：

```bash
python tools/build.py                        # 构建全站(侧栏注入/索引/打印版/统计)
python tools/check_chapter.py --all          # 全书质检
python tools/figures_a.py                    # 重新生成图解(另有 b/c/章节脚本)
```

## 🤖 这本书怎么写成的（多智能体流水线）

本书由一条**多智能体协作流水线**创作，其机制与本书所教的技术同源：

1. **规划**：`toc.json` 定义 113 章的标题/级别/摘要，作为唯一事实来源；
2. **写作**：多个专职写作智能体按统一风格指南（`docs/STYLE_GUIDE.md`）并行/串行撰写，每章必须引用真实文献；
3. **质检闸门**：`check_chapter.py` 对每章做 15 项硬性检查（字数/结构/图表/引用/链接/占位符），不通过不得合入；
4. **多身份盲审**：多轮独立评审智能体分别从**文字质量、图文样式、阅读观感、界面美观、图示准确性、事实精确度、语言风格**等维度评审（每轮全新上下文，互不知晓），意见回流修复，直至通过。

全部脚本开源在 `tools/`，欢迎审计与复用。

## 🤝 参与贡献

发现错误、建议新章节、改进图解——都欢迎！请阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。每章都有稳定锚点，提 Issue 时请注明章节号与小节标题。

## 📄 许可

- **文字内容与图解**：[CC BY-SA 4.0](LICENSE)（署名 — 相同方式共享，允许商用与翻译）
- **代码示例**：MIT

## 🙏 领域基石（部分）

本书站在这些公开成果之上：ReAct / ReWOO / Reflexion / Toolformer / Tree of Thoughts / MemGPT / Self-RAG / GraphRAG / RLHF·InstructGPT / DPO / DeepSeek-R1 / SWE-bench / WebArena / OSWorld / GAIA / AgentBench / MCP / LangGraph / AutoGen … 全部引用见 [附录 D](chapters/appd.html)。

---

<div align="center">

**如果这本书帮到了你，请给一个 ⭐ Star —— 这是对开源作者最直接的激励。**

</div>
