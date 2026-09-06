# -*- coding: utf-8 -*-
import os

path = r"D:/agent-cookbook/chapters/ch106.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

expansion_more = """
    <h2 id="cross-paradigm-selection-principles">模型选型的六大黄金法则：从技术狂热回归商业理性</h2>
    <p>综合研读当今全球五大基础大模型家族的综合特质，我们可以将复杂的工程评估凝练为指导企业技术决策的<strong>六大黄金选型法则</strong>：</p>
    
    <p><strong>第一法则：场景驱动而非跑分驱动（Task Over MMLU）。</strong>坚决摒弃“哪个模型 MMLU 榜单第一就选谁”的盲目冲动。MMLU 测量的是通识选择题记忆，而 Agent 落地考验的是严格 JSON 输出遵从度、多轮状态纠偏反思与错误堆栈定位。必须在企业自身真实的业务沙箱测试集上进行独立客观评测，以真实完成率作为唯一定海神针；</p>
    
    <p><strong>第二法则：多级混合而非单一死锁（Mesh Over Monolith）。</strong>没有任何一个单一模型能够在成本、速度、逻辑与多模态所有维度全部占优。一个成熟的企业级架构，必然是“小模型当前哨分类、中模型当工蜂干活、大模型当专家破局”的多层动态混合网格体系；</p>
    
    <p><strong>第三法则：重视前缀缓存经济学（Cache-Aware Architecture）。</strong>在设计智能体提示词时，必须将所有静态不变的内容（如包含数十个工具的 JSON Schemas、企业背景知识）尽可能推至 Prompt 最前端，并确保多次请求完全复用相同前缀。在启用 Prefix Caching 的现代推理引擎中，这能直接将 80% 的首字计算成本和时间抹去；</p>
    
    <p><strong>第四法则：开源闭源双轨备份（Dual-Vendor Redundancy）。</strong>在生产级关键业务中，严禁单点依赖某一家商业云厂商的 API。一旦发生国际政策突变、服务宕机或偶发性 429 限频，系统必须具备在 1 秒内无缝切流至本地自建开源 Qwen 集群的熔断自愈能力，守住业务连续性红线；</p>
    
    <p><strong>第五法则：结构化对齐高于自由文采（Schema Over Rhetoric）。</strong>在 Agent 执行流水线中，优美华丽的文学辞藻往往是有害的冗余噪声，确定性、零冗余、严格对齐 Pydantic 规范的结构化输出才是生命线。因此在微调或选型时，应优先挑选经过严格 Function Calling 对齐清洗的专用模型（如 Qwen-Coder 系列）；</p>
    
    <p><strong>第六法则：持续度量而非一锤定音（Continuous Benchmark）。</strong>全球大模型的迭代周期目前缩短至 2~3 个月。上个月表现最好的模型，下个月就可能被全新开源架构反超。技术团队必须搭建自动化的 CI/CD 评测流水线，定期对全量业务基准进行自动化回归跑分，动态微调路由权重，使系统永远航行在性价比最高的最优曲线上。</p>
"""

insert_target = '<div class="callout note">'
if insert_target in text:
    new_text = text.replace(insert_target, expansion_more + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Added selection principles section to ch106.html")
else:
    print("Target not found")
