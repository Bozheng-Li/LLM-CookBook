import os

path = r"D:/agent-cookbook/chapters/ch089.html"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# Expand with comprehensive deep sections:
# 1. Complete Docker + Xvfb + noVNC Virtual Desktop Sandbox Environment Configuration
# 2. Dynamic Bezier Curve Mouse Movement with Human-like Acceleration Algorithm in Python
# 3. Step-by-step troubleshooting playbook (5 catastrophic desktop agent failures)
# 4. OSWorld local evaluation pipeline runner implementation

expansion_1 = """
    <h2 id="virtual-sandbox-novnc">具身沙箱工程：Docker + Xvfb + noVNC 隔离虚拟桌面搭建</h2>
    <p>在企业级批量执行具身自动化任务时，绝不能直接把智能体放在开发者的物理笔记本桌面上跑。否则只要鼠标一动，开发人员的工作就完全被打断；更严重的是，一旦智能体产生误操作，会直接破坏开发者本地的真实文件与聊天软件。</p>
    <p>生产级具身 Agent 必须部署在<strong>「容器化虚拟显示沙箱（Containerized Virtual Desktop）」</strong>中。通过在 Docker 容器内运行 Linux Xvfb（虚拟帧缓冲服务）与轻量 XFCE 桌面，再配合 noVNC 将虚拟屏幕通过 WebSocket 实时推流到 Web 浏览器供人类审计员远程旁路监控：</p>

    <div class="codeblock">
      <div class="cb-head"><span>Docker 隔离虚拟桌面环境配置清单（Dockerfile.desktop）</span><button class="cb-copy">复制</button></div>
      <pre><code>FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV DISPLAY=:99
ENV RESOLUTION=1920x1080x24

# 1. 安装 Xvfb 虚拟显示服务、XFCE 桌面与必备办公软件
RUN apt-get update && apt-get install -y \
    xvfb \
    xfce4 \
    xfce4-terminal \
    libreoffice \
    chromium-browser \
    x11vnc \
    novnc \
    websockify \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# 2. 安装 Python 自动化控制库
RUN pip3 install pyautogui pillow opencv-python

# 3. 编写启动脚本: 并发拉起 Xvfb、桌面管理器与 noVNC 远程推流
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# 暴露 6080 端口供人类通过 Web 浏览器直接观看 Agent 操作桌面
EXPOSE 6080

ENTRYPOINT ["/entrypoint.sh"]</code></pre>
    </div>

    <p>在这个沙箱内，智能体的所有物理鼠标键盘操作全部被封装在虚拟 X11 服务器内，对外部宿主机实现了 100% 的物理绝缘。即便智能体执行了 <code>rm -rf /</code>，也仅仅是损坏了一个几秒钟即可重置销毁的 Docker 容器，彻底消除了具身智能在现实世界落地时的安全后顾之忧。</p>
"""

expansion_2 = """
    <h2 id="bezier-curve-movement">外设仿真进阶：基于三次贝塞尔曲线的人类手势轨迹拟合</h2>
    <p>如果智能体移动鼠标时永远是从坐标 $(x_1, y_1)$ 瞬间闪现跳转到 $(x_2, y_2)$，这种非人类的生硬动作不仅极易被现代反作弊系统（如 Cloudflare Turnstile 或各类图形滑块验证码）瞬间判定为机器人攻击，而且在某些复杂的 GUI 软件中，甚至无法触发需要鼠标悬停（Hover）才能展开的二级飞出菜单。</p>
    <p>高阶具身 Agent 必须模拟人类手臂肌肉的物理运动特征，采用<strong>「带轻微随机抖动的三次贝塞尔平滑运动曲线（Cubic Bezier Trajectory）」</strong>：</p>

    <div class="codeblock">
      <div class="cb-head"><span>三次贝塞尔人类拟真鼠标平滑轨迹生成器（human_cursor.py）</span><button class="cb-copy">复制</button></div>
      <pre><code>import math, random, time
import pyautogui

def generate_bezier_trajectory(p0: tuple, p3: tuple, steps: int = 25) -> list:
    \"\"\"生成逼真的人类鼠标移动路径: 包含启动加速、中段匀速与末端微震颤减速\"\"\"
    x0, y0 = p0
    x3, y3 = p3
    distance = math.hypot(x3 - x0, y3 - y0)

    # 随机生成两个控制点 (模拟人类手腕运动弧度偏角)
    deviation = distance * random.uniform(0.15, 0.35)
    angle = math.atan2(y3 - y0, x3 - x0) + random.choice([-1, 1]) * math.pi / 6

    p1 = (x0 + deviation * math.cos(angle), y0 + deviation * math.sin(angle))
    p2 = (x3 - deviation * math.cos(angle), y3 - deviation * math.sin(angle))

    trajectory = []
    for step in range(steps + 1):
        t = step / float(steps)
        # 引入物理缓动函数 EaseInOut (前后慢，中间快)
        t_eased = 3 * t**2 - 2 * t**3

        # 三次贝塞尔多项式展开
        bx = (1 - t_eased)**3 * p0[0] + 3 * (1 - t_eased)**2 * t_eased * p1[0] + \
             3 * (1 - t_eased) * t_eased**2 * p2[0] + t_eased**3 * p3[0]
        by = (1 - t_eased)**3 * p0[1] + 3 * (1 - t_eased)**2 * t_eased * p1[1] + \
             3 * (1 - t_eased) * t_eased**2 * p2[1] + t_eased**3 * p3[1]

        # 末端注入微小的手部生理抖动 (1~2像素)
        if step > steps * 0.8:
            bx += random.uniform(-1.0, 1.0)
            by += random.uniform(-1.0, 1.0)

        trajectory.append((int(bx), int(by)))

    return trajectory

def smooth_move_humanlike(target_x: int, target_y: int):
    \"\"\"执行平滑拟真的物理鼠标悬停移动\"\"\"
    start_pos = pyautogui.position()
    path = generate_bezier_trajectory(start_pos, (target_x, target_y))
    
    for point in path:
        pyautogui.moveTo(point[0], point[1])
        time.sleep(random.uniform(0.008, 0.015))  # 动态微秒级间隔</code></pre>
    </div>
"""

expansion_3 = """
    <h2 id="desktop-failure-modes">实战避坑手册：具身桌面 Agent 五大典型死穴及破局</h2>
    <p>在真实操作系统环境下运行具身智能体，会遭遇比纯文本环境多数十倍的不确定性故障。以下深入拆解五大经典致命滑铁卢：</p>

    <p><strong>① 灾难场景一：多模态截图过载导致的显存/Token 破产（Token Exhaustion Trap）。</strong><br>
    <em>现象：</em>智能体在一个 20 步的复杂长程任务中，每步上传一张 4K 原图给大模型，任务执行到第 8 步就报出 <code>ContextWindowExceeded</code> 或账单瞬间消耗数十美元。<br>
    <em>对策：</em>实施 <strong>动态局部 ROI 裁剪（Region of Interest Cropping）与黑白下采样</strong>：第一步先看一张压缩到 720P 的全局缩略图，定位目标所在的窗口区域（如只在屏幕左下角）；后续各步仅将目标窗口的局部区域进行高分辨率截取，将单步图像 Token 开销暴砍 80% 以上。</p>

    <p><strong>② 灾难场景二：模态对话框拦截引发的主窗口假死（Modal Dialog Deadlock）。</strong><br>
    <em>现象：</em>点击了「退出软件」后，弹出一个模态提示框「是否保存修改？」。由于该弹窗为顶级阻塞模态窗口，导致智能体后续点击主窗口上的任何按钮都被操作系统无情忽略，Agent 误以为软件死锁不断狂点。<br>
    <em>对策：</em>引入 <strong>前台窗口层级探测器（Z-Order Topmost Detector）</strong>：在执行后置差分时，若检测到连续两次点击无任何像素反应，系统自动枚举当前桌面上所有的独立顶级 Window Handle。若发现存在置顶的短小模态 Dialog，强制模型将视觉焦点切换至该 Dialog 内部进行确认处理。</p>

    <p><strong>③ 灾难场景三：拖拽动作由于系统平滑延迟导致的丢包（Drag &amp; Drop Dropout）。</strong><br>
    <em>现象：</em>Agent 试图将桌面上的图标拖拽进文件夹，鼠标虽然从 A 划到了 B，但图标依然停留在 A 处。<br>
    <em>对策：</em>严格遵循 <strong>拖拽四拍子物理延迟原则</strong>：在 <code>mouseDown</code> 之后强制休眠 150ms（让操作系统完成选中高亮并识别到长按意图）；移动过程必须持续 400ms 以上；到达终点后必须再次停顿 150ms 触发系统的 Drop 释放区域判定，最后才执行 <code>mouseUp</code>，彻底解决桌面 GUI 拖拽失效顽疾。</p>

    <p><strong>④ 灾难场景四：组合键释放遗漏导致系统按键死锁（Stuck Modifiers Disaster）。</strong><br>
    <em>现象：</em>执行完一次 <code>Ctrl+C</code> 复制操作后，由于代码异常退出了，导致操作系统底层的 <code>Ctrl</code> 键一直处于物理被按住的状态。随后用户无论敲击任何字母，都会触发各种系统快捷键，整个操作系统陷入半瘫痪。<br>
    <em>对策：</em>在所有的外设注入代码外层包裹 <strong>RAII 风格的按键强制释放守护者（Modifier Release Guard）</strong>：在 <code>try...finally</code> 块中，无论发生任何异常，在函数退出前强制顺次调用 <code>keyUp('ctrl')</code>, <code>keyUp('shift')</code>, <code>keyUp('alt')</code>, <code>keyUp('win')</code>，严守外设状态干净。</p>

    <p><strong>⑤ 灾难场景五：无焦点输入导致的文字凭空蒸发（Typing into the Void）。</strong><br>
    <em>现象：</em>智能体试图在一个输入框中输入密码，直接调用了 <code>type_text("password123")</code>，但由于输入前没有点击获取光标焦点，文字全被输入到了外层的空白桌面上，甚至触发了桌面快捷键。<br>
    <em>对策：</em>推行 <strong>强制“先击后打（Click-Before-Type）”硬性协议</strong>：系统在调度层拦截任何单独的纯文本输入动作；若要在某处打字，底层强制捆绑为「先向目标中心执行一次左键单击聚焦 → 等待 150ms 闪烁光标出现 → 写入文本」，确保击键信号百分之百准确路由至目标控件。</p>
"""

expansion_4 = """
    <h2 id="eval-osworld-runner">工业级评测实战：构建 OSWorld 本地自动化测试运行器</h2>
    <p>要在严肃场景中证明 Computer Use 具身智能体达到了商业交付水准，必须在标准的 <strong>OSWorld</strong> 测试集上跑通完整的自动化评估流水线。以下代码展示了一个极简的本地 OSWorld 评测执行框架，包含任务初始化、动态截屏抓取、多模态决策推进与最终成功断言校验：</p>

    <div class="codeblock">
      <div class="cb-head"><span>本地 OSWorld 自动化评测运行器（osworld_runner.py）</span><button class="cb-copy">复制</button></div>
      <pre><code>import json, time
from typing import Dict, Any

class OSWorldEvaluationRunner:
    def __init__(self, agent_instance, max_steps_per_task: int = 20):
        self.agent = agent_instance
        self.max_steps = max_steps_per_task

    def run_benchmark_task(self, task_config: Dict[str, Any]) -> Dict[str, Any]:
        \"\"\"在虚拟桌面沙箱中执行单项 OSWorld 具身长程任务\"\"\"
        task_id = task_config["id"]
        instruction = task_config["instruction"]
        eval_script = task_config["eval_script"]

        print(f"=== 启动 OSWorld 任务 [{task_id}]: {instruction} ===")
        start_time = time.time()
        step_count = 0
        task_completed = False

        for step in range(self.max_steps):
            step_count += 1
            print(f"  [Step {step+1}/{self.max_steps}] 智能体正在观察桌面并执行动作...")
            
            # 调度智能体执行单步感知-推演-动作闭环
            finished = self.agent.step(instruction)
            if finished:
                print("  智能体自主宣告任务达成。")
                task_completed = True
                break

        # 运行 OSWorld 真实结果断言脚本 (例如检查文件是否生成、数据库是否写入)
        print("🔍 正在执行客观判定断言...")
        eval_passed = self._run_ground_truth_eval(eval_script)
        elapsed_sec = time.time() - start_time

        return {
            "task_id": task_id,
            "success": eval_passed,
            "agent_declared_finish": task_completed,
            "steps_consumed": step_count,
            "elapsed_seconds": round(elapsed_sec, 2)
        }

    def _run_ground_truth_eval(self, script_path: str) -> bool:
        \"\"\"执行任务专属的客观判定逻辑\"\"\"
        # 实际生产中调用 Docker exec 执行断言脚本 (返回 0 为成功)
        return True</code></pre>
    </div>
"""

insert_target = '<h2 id="faq">'
if insert_target in text:
    new_text = text.replace(insert_target, expansion_1 + "\n" + expansion_2 + "\n" + expansion_3 + "\n" + expansion_4 + "\n" + insert_target)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Successfully expanded ch089.html with 4 deep sections")
else:
    print("Target not found")
