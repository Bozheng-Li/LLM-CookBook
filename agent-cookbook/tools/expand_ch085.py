import os

path = r"D:/agent-cookbook/chapters/ch085.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# Expand with comprehensive deep sections:
# 1. Advanced Idempotency Key Implementation with Redis Mutex Locks & Token Bucket (Python Code)
# 2. Playwright Robust DOM + VLM Vision Hybrid Locator Implementation (Python Code)
# 3. Step-by-step catastrophic failure playbook (Deadlocks, compensation cascading failures, race conditions)

expansion_1 = """
    <h2 id="idempotency-engine">深入实操：基于 Redis 分布式锁与令牌桶的高性能幂等引擎</h2>
    <p>在超高并发的企业级支付与库存扣减流水线中，仅仅靠应用层生成一个随机字符串远远无法满足苛刻的幂等性要求。当两个并发工作流 Worker 同时接收到对同一笔订单的扣款指令时，若加锁逻辑存在哪怕 1 毫秒的竞态条件时间窗口（Race Condition），系统就会发生灾难性的并发重复扣款。</p>
    <p>生产级架构必须采用<strong>「基于 Redis Lua 脚本的原子化幂等互斥锁（Atomic Idempotency Mutex Lock）」</strong>。以下代码展示了工业级分布式幂等管理器的严密实现：</p>

    <div class="codeblock">
      <div class="cb-head"><span>分布式原子幂等锁与状态持久化管理器（idempotency_manager.py）</span><button class="cb-copy">复制</button></div>
      <pre><code>import hashlib, json, time
from typing import Optional, Dict, Any

class DistributedIdempotencyManager:
    def __init__(self, redis_client):
        self.redis = redis_client
        # 原子化获取锁与检查历史结果的 Lua 脚本
        self.acquire_lua = \"\"\"
        local key = KEYS[1]
        local token = ARGV[1]
        local ttl = tonumber(ARGV[2])
        
        local current = redis.call('GET', key)
        if current then
            return current -- 返回已存在的状态或计算结果
        else
            redis.call('SET', key, token, 'EX', ttl)
            return 'ACQUIRED'
        end
        \"\"\"

    def generate_token(self, tenant_id: str, action_type: str, business_id: str, params: Dict[str, Any]) -> str:
        \"\"\"生成确定性的业务唯一性幂等指纹 (SHA-256)\"\"\"
        raw_payload = f"{tenant_id}:{action_type}:{business_id}:{json.dumps(params, sort_keys=True)}"
        return "idem_" + hashlib.sha256(raw_payload.encode('utf-8')).hexdigest()

    def execute_idempotent_action(self, token: str, action_func, ttl_seconds: int = 86400) -> Dict[str, Any]:
        \"\"\"受分布式原子幂等保护的业务执行包装器\"\"\"
        lock_key = f"lock:idempotency:{token}"
        
        # 1. 执行原子判定
        res = self.redis.eval(self.acquire_lua, 1, lock_key, "PROCESSING", ttl_seconds)
        
        if res != b"ACQUIRED" and res != "ACQUIRED":
            # 命中缓存: 说明此前已执行过或正在并发执行中
            cached_val = res.decode('utf-8') if isinstance(res, bytes) else res
            if cached_val == "PROCESSING":
                raise BlockingIOError("并发拦截: 相同业务操作正在执行中，请勿重复提交！")
            print(f"[Idempotency Cache Hit] 命中已完成历史记录，直接复用上一次结果。")
            return json.loads(cached_val)

        # 2. 首次获取成功，执行底层业务调用
        try:
            action_result = action_func()
            # 将成功结果回写至 Redis，使后续所有重复重试均可命中结果缓存
            self.redis.set(lock_key, json.dumps(action_result), ex=ttl_seconds)
            return action_result
        except Exception as e:
            # 业务执行抛错，立即清理未决锁，允许后续纠正重试
            self.redis.delete(lock_key)
            raise e</code></pre>
    </div>
"""

expansion_2 = """
    <h2 id="playwright-vlm-locator">GUI RPA 进阶：Playwright 与多模态视觉自愈定位器</h2>
    <p>传统的自动化脚本往往严重依赖单一的 CSS 或 XPath 选择器。当目标系统的管理后台进行热更新、前端打包器为类名重新生成随机哈希（如 <code>.button-x8a9b</code> 变为 <code>.button-k7m2c</code>）时，传统的脚本会无情地报出 <code>TimeoutError: Element not found</code>。高可用 RPA Agent 必须无缝集成<strong>「DOM 无障碍树 + 视觉 OCR + VLM 坐标回归」</strong>的三轨自愈定位器：</p>

    <div class="codeblock">
      <div class="cb-head"><span>多模态视觉自愈 UI 定位器（resilient_locator.py）</span><button class="cb-copy">复制</button></div>
      <pre><code>import base64
from typing import Tuple

class ResilientUILocator:
    def __init__(self, page, vlm_client):
        self.page = page
        self.vlm = vlm_client

    def click_button_with_self_healing(self, primary_selector: str, visual_intent: str) -> bool:
        \"\"\"优先 DOM 选择器定位，失败时无缝切换至多模态视觉空间坐标自愈点击\"\"\"
        # 轨 1: 尝试原生无障碍 / DOM 快速点击
        try:
            self.page.wait_for_selector(primary_selector, timeout=3000)
            self.page.click(primary_selector)
            print(f"[Locator Track 1] DOM 快速点击成功: {primary_selector}")
            return True
        except Exception:
            print(f"[Locator Fallback] 原生选择器 {primary_selector} 失效，启动多模态视觉空间自愈...")

        # 轨 2: 截取当前全屏页面图像送入 VLM 视觉大模型
        screenshot_bytes = self.page.screenshot(full_page=False)
        b64_img = base64.b64encode(screenshot_bytes).decode('utf-8')

        vlm_prompt = f\"\"\"请在当前页面截图中，精确定位描述为【{visual_intent}】的按钮中心点。
返回格式必须严格为 JSON 归一化百分比坐标: {{"x_pct": 0.45, "y_pct": 0.62}}\"\"\"

        coords = self.vlm.predict_coordinates(b64_img, vlm_prompt)
        
        # 换算为视口真实像素物理坐标
        viewport_size = self.page.viewport_size
        target_x = int(viewport_size["width"] * coords["x_pct"])
        target_y = int(viewport_size["height"] * coords["y_pct"])

        print(f"[Locator Track 2] 视觉大模型预测命中坐标: ({target_x}, {target_y})，执行模拟物理点击...")
        self.page.mouse.click(target_x, target_y)
        return True</code></pre>
    </div>
"""

expansion_3 = """
    <h2 id="deep-troubleshooting-playbook">实战避坑手册：工作流与 RPA 五大生产灾难与根治方案</h2>
    <p>自动化 Agent 接管企业核心经营流水线后，任何细小的工程疏漏都可能造成数以万计的资金损失或客户投诉。以下深入复盘五大典型故障与架构防御方案：</p>

    <p><strong>① 灾难场景一：长时间挂起导致的数据库死锁与连接池耗尽（Hanging Locks &amp; Pool Starvation）。</strong><br>
    <em>现象：</em>在工作流第一步开启了本地数据库事务并对某行加排他锁（<code>SELECT ... FOR UPDATE</code>），第二步调用了第三方银行外部 API。此时银行接口发生长达 30 秒的超时等待，导致本地数据库连接被长时间霸占，上百个并发请求迅速将整个微服务的数据库连接池彻底打爆。<br>
    <em>根治手段：</em>严格贯彻 <strong>长事务解耦与短平快事务原则</strong>。绝不允许在持有底层数据库行级物理锁的同时发起任何跨网络的 RPC、HTTP 或 RPA 操作；所有需要跨系统协调的资源，统一改用「基于乐观锁的预占状态标记（如 <code>status='PENDING'</code>）」，并在本地数据库事务极速提交释放物理锁后，再发起耗时的外部通信。</p>

    <p><strong>② 灾难场景二：逆向补偿顺序混乱引发的逻辑悖论（Out-of-Order Compensation）。</strong><br>
    <em>现象：</em>三步工作流按「1.创建用户 → 2.绑定卡片 → 3.首充100元」推进。第 3 步扣款失败后，补偿器却并发异步先执行了「删除用户」，导致后执行的「解绑卡片」因外键约束失败抛出异常，整个补偿流程卡死报错。<br>
    <em>根治手段：</em>在代码调度器中硬编码<strong>「严格逆向栈（LIFO Stack）单线程串行推进」</strong>。补偿序列必须严格按照正向成功的倒序串行执行，每一个前置补偿返回 HTTP 200 确认后，方可推进下一个补偿操作，从拓扑数学上消除外键因果倒置漏洞。</p>

    <p><strong>③ 灾难场景三：Windows 屏幕锁屏休眠导致的无头 RPA 截屏全黑（Black Screen of Death）。</strong><br>
    <em>现象：</em>部署在内网虚拟机的桌面 RPA 任务在白天测试完美，到了凌晨无人值守批量跑批时，截获的页面截图全是一片漆黑，所有视觉与 OCR 操作全线失败。<br>
    <em>根治手段：</em>部署<strong>「虚拟显示服务与防休眠守护守护进程（No-Sleep Keep-Alive Service）」</strong>：在 Windows 注册表中禁用锁屏屏保与节能睡眠模式；或者在 Linux 宿主机上利用 <code>Xvfb (X Virtual Framebuffer)</code> 为每个 RPA 容器虚拟一个永远常驻内存的独立图形显示上下文，彻底杜绝操作系统电源管理引起的屏幕黑屏。</p>

    <p><strong>④ 灾难场景四：幽灵级联重试打爆下游脆弱老系统（Thundering Herd on Legacy Systems）。</strong><br>
    <em>现象：</em>某内网部署在老旧小型机上的金蝶 ERP 在早高峰遭遇 2 秒微小卡顿，Agent 集群自动发起了固定重试，数十个工作流同时高频重发请求，瞬间将本就脆弱的老系统彻底打瘫痪，引发长达两小时的宕机事故。<br>
    <em>根治手段：</em>在重试模块中强制启用 <strong>全抖动指数退避算法（Exponential Backoff with Full Jitter）</strong>与<strong>全局自适应断路器（Circuit Breaker）</strong>：重试间隔按 $T_{wait} = \text{Random}(0, \min(M, T_{base} \times 2^{attempt}))$ 随机散开，并在探测到下游错误率突破 30% 时瞬间熔断，保护遗留核心资产。</p>

    <p><strong>⑤ 灾难场景五：敏感凭证被大模型打印在控制台日志中（Secret Leakage in Logs）。</strong><br>
    <em>现象：</em>为了便于排查报错，工程师把整个 <code>context</code> 打印到了 stdout，导致企业网银支付网关的 <code>client_secret</code> 和用户身份证号随日志流落入第三方日志分析平台。<br>
    <em>根治手段：</em>在日志拦截器层强制部署<strong>「敏感键脱敏过滤器（Sensitive Masking Interceptor）」</strong>：自动识别并过滤包含 <code>password, secret, token, card_no, cvv</code> 的键值，自动替换为 <code>******</code>，严守合规底线。</p>
"""

insert_target = '<h2 id="faq">'
if insert_target in text:
    new_text = text.replace(insert_target, expansion_1 + "\n" + expansion_2 + "\n" + expansion_3 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Successfully expanded ch085.html")
else:
    print("Target not found")
