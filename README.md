# AI & LLM 技术全景知识库系列 (AI & LLM Cookbook Series)

> 一套系统化、工业级、从算法底层到高阶自主智能体的中文开源技术巨著合集。

[![GitHub stars](https://img.shields.io/github/stars/Bozheng-Li/LLM-CookBook?style=flat-square)](https://github.com/Bozheng-Li/LLM-CookBook/stargazers)
[![License](https://img.shields.io/badge/License-CC%20BY--SA%204.0-orange?style=flat-square)](LICENSE)
[![GitHub Pages](https://img.shields.io/badge/在线阅读-GitHub%20Pages-2ea44f?style=flat-square)](https://bozheng-li.github.io/LLM-CookBook/)

---

## 📚 双旗舰知识库架构索引

本仓库现已升级为**双旗舰知识库体系**，两本书在代码目录、在线阅读路由与工程构建上实现完全的物理隔离与独立维护：

```
LLM-CookBook/
├── index.html                   # 双书旗舰总入口导航门户
├── llm-cookbook/                # 📘 第一部：《大模型技术 Cookbook》（大模型底层原理与工程基座）
│   ├── index.html               # 第一部独立主页
│   ├── pages/                   # 16 个核心专题（预训练/后训练/推理加速/治理）
│   └── assets/                  # 第一部专用静态资源与图表
└── agent-cookbook/              # 🤖 第二部：《AI 智能体全景手册》（千页自主智能体全景典籍）
    ├── index.html               # 第二部独立主页
    ├── chapters/                # 113 个核心正文章节 + 4 大理论附录 (117篇)
    ├── assets/figures/          # 245 幅统一调色盘原创 SVG 矢量架构图谱
    ├── judge/                   # 8 重独立身份 Judge 串行盲审验收报告
    └── tools/                   # 构建脚本 (build.py)、检查器 (check_chapter.py)、测试器
```

---

### 📘 第一部：大模型技术 Cookbook (LLM Cookbook)
- **定位**：大语言模型算法底层原理、预训练、后训练对齐（SFT/RLHF/DPO）、推理加速与 LLMOps 基础设施。
- **在线阅读**：[打开《大模型技术 Cookbook》](https://bozheng-li.github.io/LLM-CookBook/llm-cookbook/index.html)
- **核心模块**：
  - 00-02：数学基础与序列表示
  - 03-04：Transformer 核心机制与现代架构演进 (MoE / 旋转位置编码)
  - 05-07：GPU 算子系统、预训练与后训练对齐
  - 08-10：推理期计算扩展、效率量化部署与 RAG 检索
  - 11-15：生产治理与动手实战（从零写 Tokenizer、miniGPT 到全栈部署）

---

### 🤖 第二部：AI 智能体全景手册 (AI Agent Cookbook)
- **定位**：涵盖智能体认知架构、复杂规划决策、工具调用契约、长期记忆检索、分布式事务、多智能体协同、10 大全栈实战项目、形式化数学理论、前沿论文精读与高频面试题库的千页全景手册。
- **排版规模**：**113 章核心正文 + 4 大高阶附录 (117 篇独立篇章)** · **1,173 印刷页** · **815,027 正文汉字** · **245 幅原创矢量架构图谱** · **10 大全栈工业项目**。
- **在线阅读**：[打开《AI 智能体全景手册》](https://bozheng-li.github.io/LLM-CookBook/agent-cookbook/index.html)
- **核心知识地图**：
  1. **导论篇（Ch001-008）**：智能体定义演进、闭环负反馈机理、分类学与历史发展。
  2. **认知篇（Ch009-026）**：ReAct、Plan-and-Solve、Reflexion、思维树（ToT）、MCTS 树搜索、测试期计算扩展律（TTC）。
  3. **工具篇（Ch027-040）**：OpenAPI 契约、GBNF 语法掩码、Pydantic 强校验、安全沙箱防御。
  4. **记忆篇（Ch041-050）**：工作内存滑动窗口、稠密稀疏混合检索、RRF 排名融合、HippoRAG 激活扩散网络。
  5. **生产篇（Ch051-070）**：Saga 长事务补偿、Redis 幂等锁、Radix Tree 缓存复用、OpenTelemetry 分布式追踪。
  6. **评测篇（Ch071-080）**：SWE-bench、WebArena、GAIA、AgentBench 自动化状态断言基准评测。
  7. **实战篇（Ch081-090）**：10 大企业级全栈实战（RAG、数据分析师、Deep Research、Repo 助手、Workflow RPA、端侧轻量化、前端测试、渗透测试、具身操作、科研助理）。
  8. **理论篇（Ch091-098）**：MDP / POMDP / 博弈论形式化证明、贝尔曼最优性压缩映射定理、控制论与耗散结构、认知心理学、世界模型（RSSM/Dreamer）、神经符号 AI 与终身学习。
  9. **论文篇（Ch099-104）**：40 篇核心奠基学术原著深度逐字研读与架构解构。
  10. **资源与面试篇（Ch105-113）**：开源框架选型、模型路由网关、基础/进阶 100 道高频面试题精解、系统设计答辩、300 条权威术语速查表。

---

## 🚀 本地启动与离线阅读

两本书的所有 HTML、样式表、JavaScript 交互、搜索索引与矢量插图均为**纯静态无后端依赖**，克隆后可直接本地极速离线阅读：

```bash
# 1. 克隆仓库
git clone https://github.com/Bozheng-Li/LLM-CookBook.git
cd LLM-CookBook

# 2. 本地启动静态服务器
python -m http.server 8000
```
在浏览器中打开 `http://localhost:8000/` 即可通过总入口任意切换畅读两本手册。

---

## 📜 开源许可与社区共建

本项目遵循 **[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.zh)**（知识共享署名-相同方式共享 4.0 国际许可协议）。欢迎来自全球的开发者提交 Issue、RFC 提案与 Pull Request！
