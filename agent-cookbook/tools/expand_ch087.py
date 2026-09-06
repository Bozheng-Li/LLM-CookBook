import os

path = r"D:/agent-cookbook/chapters/ch087.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# Expand with comprehensive deep sections:
# 1. OpenCV + scikit-image SSIM Pixel-by-Pixel Diff Implementation in Python (Heatmap Generator)
# 2. Complete MSW Mock Service Worker Interception Template & Mock Schema Generator
# 3. Production Playwright Multi-browser matrix test runner

expansion_1 = """
    <h2 id="ssim-diff-engine">深入实操：基于 OpenCV 与 scikit-image 的像素差分引擎</h2>
    <p>在自动化前端自愈流水线中，仅仅告诉大模型「视觉比对失败了」是完全不够的。大模型无法从纯文字中脑补出视觉像素偏离了多少。系统必须自动化生成一张<strong>「带红色轮廓高亮框（Bounding Box Mask）的视觉差分合成图」</strong>，让多模态视觉模型（VLM）能够通过眼睛瞬间定位缺陷坐标。</p>
    
    <p>以下代码展示了集成在测试沙箱中的像素级差分引擎实现，能够计算两张截图的精确 SSIM 分数并高亮异常排版区域：</p>

    <div class="codeblock">
      <div class="cb-head"><span>像素级视觉差分与热力图定位器（visual_diff_engine.py）</span><button class="cb-copy">复制</button></div>
      <pre><code>import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
from typing import Tuple, List, Dict

class VisualDiffEngine:
    def __init__(self, ssim_threshold: float = 0.95):
        self.threshold = ssim_threshold

    def compare_and_generate_diff_map(self, baseline_path: str, current_path: str, diff_output_path: str) -> Dict[str, Any]:
        \"\"\"计算两张网页截图的结构相似度，并生成红色高亮差异图\"\"\"
        # 1. 以灰度与彩色模式分别加载图片
        img_base = cv2.imread(baseline_path)
        img_curr = cv2.imread(current_path)

        # 确保尺寸一致 (若不一致则自适应补白边或裁剪对齐)
        h1, w1 = img_base.shape[:2]
        h2, w2 = img_curr.shape[:2]
        max_h, max_w = max(h1, h2), max(w1, w2)
        
        base_padded = np.ones((max_h, max_w, 3), dtype=np.uint8) * 255
        curr_padded = np.ones((max_h, max_w, 3), dtype=np.uint8) * 255
        base_padded[:h1, :w1] = img_base
        curr_padded[:h2, :w2] = img_curr

        gray_base = cv2.cvtColor(base_padded, cv2.COLOR_BGR2GRAY)
        gray_curr = cv2.cvtColor(curr_padded, cv2.COLOR_BGR2GRAY)

        # 2. 计算 SSIM 与差分图像
        score, diff = ssim(gray_base, gray_curr, full=True)
        diff = (diff * 255).astype("uint8")

        # 3. 阈值化与轮廓检测，圈定差异发生区域
        thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        diff_bboxes = []
        annotated_img = curr_padded.copy()

        for c in contours:
            area = cv2.contourArea(c)
            if area > 40:  # 过滤微小噪点
                x, y, w, h = cv2.boundingRect(c)
                diff_bboxes.append({"x": int(x), "y": int(y), "w": int(w), "h": int(h)})
                # 用鲜艳的红色矩形框标出视觉差异
                cv2.rectangle(annotated_img, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # 4. 保存高亮差分图供 VLM 复审
        cv2.imwrite(diff_output_path, annotated_img)

        passed = score >= self.threshold
        print(f"[Visual Diff] SSIM得分: {score:.4f} | 检出差异缺陷区域数: {len(diff_bboxes)}")

        return {
            "passed": passed,
            "ssim_score": round(float(score), 4),
            "diff_count": len(diff_bboxes),
            "diff_image_path": diff_output_path,
            "bounding_boxes": diff_bboxes[:8]
        }</code></pre>
    </div>
"""

expansion_2 = """
    <h2 id="msw-mock-system">脱机沙箱与契约驱动：MSW 网络模拟拦截架构</h2>
    <p>在组件开发阶段，如果组件一挂载就发起真实的 <code>fetch('/api/v1/orders')</code>，沙箱必然会由于内网鉴权失败或网络不通而直接报 500/401 错误，使组件瞬间掉入 Error 态，导致视觉测试完全无法覆盖正常的成功态（Happy Path）。</p>
    <p>生产级前端 Agent 强制使用 <strong>MSW（Mock Service Worker）契约驱动架构</strong>。系统在生成 React 代码的同时，依据 OpenAPI 规范自动合成一套运行在浏览器 Service Worker 层的拦截脚本，无需修改任何业务代码即可实现无缝假数据注入：</p>

    <div class="codeblock">
      <div class="cb-head"><span>自动化 MSW 网络拦截桩生成范式（handlers.ts）</span><button class="cb-copy">复制</button></div>
      <pre><code>import { http, HttpResponse, delay } from 'msw';

export const handlers = [
  // 模拟分页订单列表查询接口
  http.get('/api/v1/orders', async ({ request }) => {
    // 模拟真实的 150ms 网络延迟与加载动效
    await delay(150);

    return HttpResponse.json({
      code: 0,
      message: 'success',
      data: {
        total: 128,
        items: [
          {
            order_id: 'ORD-9821',
            customer_name: '智算未来科技有限公司',
            amount: 45200.0,
            status: 'PAID',
            created_at: '2026-09-06 14:30:00'
          },
          {
            order_id: 'ORD-9822',
            customer_name: '极速先锋数字传媒',
            amount: 12800.0,
            status: 'PENDING',
            created_at: '2026-09-06 15:10:22'
          }
        ]
      }
    });
  }),

  // 模拟异常与边界值测试
  http.post('/api/v1/orders/:id/refund', async () => {
    return new HttpResponse(null, { status: 403, statusText: 'Insufficient Privileges' });
  })
];</code></pre>
    </div>
    <p>借由 MSW，Agent 可以在几秒钟内自由切换「正常加载态」、「海量数据分页态」、「空数据缺省态」以及「网络崩溃报错态」四大极端场景，自动化截取并审查全部 4 个维度的视觉呈现，将单元测试的覆盖率拉升至近乎 100% 的极高水准。</p>
"""

expansion_3 = """
    <h2 id="cross-browser-playwright">多内核浏览器矩阵测试：Chromium, Firefox 与 WebKit</h2>
    <p>前端领域存在臭名昭著的<strong>浏览器引擎兼容性地狱（Browser Engine Fragmentation）</strong>：某段 Flex 弹性盒模型排版在 Google Chrome（Blink 引擎）上完美贴合，但在苹果 Safari（WebKit 引擎）上却由于 <code>gap</code> 属性或日期解析差异直接被挤爆截断；在 Mozilla Firefox（Gecko 引擎）上又可能因滚动条占用宽度导致出现诡异的双滚动条。</p>

    <p>工业级 Web 前端 Agent 在 Playwright 自动化测试流水线中，强制配置<strong>三核并行回归矩阵</strong>：</p>

    <div class="codeblock">
      <div class="cb-head"><span>Playwright 三核并发浏览器审计脚本（matrix_runner.py）</span><button class="cb-copy">复制</button></div>
      <pre><code>from playwright.sync_api import sync_playwright
import concurrent.futures

def audit_single_browser(browser_type_name: str, target_url: str) -> dict:
    \"\"\"在特定内核的浏览器中执行渲染与排版审查\"\"\"
    errors = []
    with sync_playwright() as p:
        browser_launcher = getattr(p, browser_type_name)
        browser = browser_launcher.launch(headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 800})
        
        page.on("pageerror", lambda err: errors.append(f"[{browser_type_name}] {str(err)}"))

        try:
            page.goto(target_url, wait_until="networkidle", timeout=6000)
            # 捕获是否有元素发生异常水平滚动溢出
            scroll_w = page.evaluate("() => document.documentElement.scrollWidth")
            client_w = page.evaluate("() => document.documentElement.clientWidth")
            overflowed = scroll_w > client_w
        finally:
            browser.close()

    return {
        "browser": browser_type_name,
        "overflowed": overflowed,
        "errors": errors
    }

def run_cross_browser_test_suite(url: str) -> bool:
    \"\"\"并行拉起 Chromium, Firefox, WebKit 三大内核全面验收\"\"\"
    engines = ["chromium", "firefox", "webkit"]
    all_clean = True

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        futures = {executor.submit(audit_single_browser, e, url): e for e in engines}
        for future in concurrent.futures.as_completed(futures):
            res = future.result()
            if res["overflowed"] or res["errors"]:
                print(f"❌ 浏览器兼容性警报: {res['browser']} 发生异常或布局溢出！")
                all_clean = False
            else:
                print(f"✅ {res['browser']} 内核兼容性完全达标。")

    return all_clean</code></pre>
    </div>
"""

insert_target = '<h2 id="faq">'
if insert_target in text:
    new_text = text.replace(insert_target, expansion_1 + "\n" + expansion_2 + "\n" + expansion_3 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Successfully expanded ch087.html")
else:
    print("Target not found")
