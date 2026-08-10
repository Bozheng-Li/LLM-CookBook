# -*- coding: utf-8 -*-
"""静态渲染风险扫描器。

用途：在没有浏览器运行时的环境里，提前发现会导致 KaTeX、Mermaid、Chart.js
或图片显示异常的 HTML 结构问题。它不替代真实浏览器截图验收，但比内容数量
检查更接近页面最终渲染链路。

用法：
  python tools/check_rendering.py all
  python tools/check_rendering.py pages/03-transformer/attention.html
"""
from __future__ import annotations

import glob
import html as html_lib
import os
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / "pages"

FORMULA_OPENERS = ("$$", "\\[", "\\(")
FORMULA_CLOSERS = ("$$", "\\]", "\\)")
IGNORED_TAGS = {"script", "noscript", "style", "textarea", "pre", "code", "option"}


class RenderParser(HTMLParser):
    """只收集与运行时渲染有关的结构，避免依赖第三方 HTML 包。"""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack: list[str] = []
        self.mermaids: list[dict] = []
        self.images: list[dict] = []
        self.canvases: list[dict] = []
        self.scripts: list[dict] = []
        self.styles: list[dict] = []
        self.formula_ignored: list[dict] = []
        self.current_mermaid: dict | None = None
        self.current_script: dict | None = None
        self.current_style: dict | None = None
        self.raw_chunks: list[str] = []
        self.visible_text: list[str] = []

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        attrs_d = dict(attrs)
        self.raw_chunks.append(self.get_starttag_text() or "")
        if tag == "img":
            self.images.append({"src": attrs_d.get("src", ""), "alt": attrs_d.get("alt"), "tag": self.getpos()[0]})
        elif tag == "canvas":
            self.canvases.append({"id": attrs_d.get("id", ""), "tag": self.getpos()[0]})
        elif tag == "script":
            self.current_script = {"src": attrs_d.get("src", ""), "text": "", "tag": self.getpos()[0]}
            self.scripts.append(self.current_script)
        elif tag == "style":
            self.current_style = {"text": "", "tag": self.getpos()[0]}
            self.styles.append(self.current_style)
        elif tag == "div" and attrs_d.get("class", "").split() and "mermaid" in attrs_d.get("class", "").split():
            self.current_mermaid = {"text": "", "tag": self.getpos()[0]}
            self.mermaids.append(self.current_mermaid)
        self.stack.append(tag)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if self.stack and self.stack[-1] == tag.lower():
            self.stack.pop()

    def handle_endtag(self, tag):
        tag = tag.lower()
        self.raw_chunks.append(f"</{tag}>")
        if tag == "script":
            self.current_script = None
        elif tag == "style":
            self.current_style = None
        elif tag == "div" and self.current_mermaid is not None:
            self.current_mermaid = None
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i] == tag:
                del self.stack[i:]
                break

    def handle_data(self, data):
        self.raw_chunks.append(data)
        if not any(t in IGNORED_TAGS for t in self.stack):
            self.visible_text.append(data)
        if self.current_mermaid is not None:
            self.current_mermaid["text"] += data
        if self.current_script is not None:
            self.current_script["text"] += data
        if self.current_style is not None:
            self.current_style["text"] += data
        if any(t in IGNORED_TAGS for t in self.stack):
            if any(mark in data for mark in ("$$", "\\[", "\\(", "\\]", "\\)")):
                self.formula_ignored.append({"tag": self.getpos()[0], "context": "/".join(self.stack), "text": data.strip()[:120]})


def resolve(arg: str) -> list[Path]:
    if arg == "all":
        return [Path(p) for p in sorted(glob.glob(str(PAGES / "**" / "*.html"), recursive=True))]
    p = Path(arg)
    if not p.is_absolute():
        p = ROOT / p
    if p.is_file():
        return [p]
    d = PAGES / arg
    if d.is_dir():
        return [Path(p) for p in sorted(glob.glob(str(d / "*.html")))]
    return []


def line_count(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


def strip_non_formula_regions(raw: str) -> str:
    # Mermaid、代码和脚本中的美元符号不应参与 KaTeX 配对检查。
    raw = re.sub(r'<div\b[^>]*class=["\'][^"\']*\bmermaid\b[^"\']*["\'][^>]*>.*?</div>', " ", raw, flags=re.I | re.S)
    raw = re.sub(r'<(?:script|style|pre|code|textarea|noscript)\b[^>]*>.*?</(?:script|style|pre|code|textarea|noscript)>', " ", raw, flags=re.I | re.S)
    return raw


def formula_risks(raw: str, parser: RenderParser) -> list[str]:
    risks: list[str] = []
    cleaned = strip_non_formula_regions(raw)
    # display delimiters必须成对；\( 与 \) 也单独检查。
    pairs = [("$$", "$$", "$$"), ("\\[", "\\]", r"\\[...\\]"), ("\\(", "\\)", r"\\(...\\)")]
    for left, right, label in pairs:
        opens = cleaned.count(left)
        closes = cleaned.count(right)
        if opens != closes:
            risks.append(f"公式分隔符不成对 {label}: {opens}/{closes}")
    # 只在可见正文中检查单美元；代码、脚本、Mermaid 已被解析器排除。
    inline_text = re.sub(r"\$\$.*?\$\$", " ", "".join(parser.visible_text), flags=re.S)
    # KaTeX 的 inline 公式允许跨 HTML 节点；这里只报告极低置信度的奇数情况，
    # 避免把美元金额、属性文本或混合标签误报成坏公式。
    dollars = re.findall(r"(?<!\\)\$", inline_text)
    if len(dollars) % 2 and len(dollars) <= 3:
        risks.append(f"单美元公式疑似不成对: {len(dollars)} 个")
    if parser.formula_ignored:
        risks.append(f"公式落在 KaTeX 忽略标签内: {len(parser.formula_ignored)} 处")
    return risks


def mermaid_risks(parser: RenderParser) -> list[str]:
    risks: list[str] = []
    for idx, item in enumerate(parser.mermaids, 1):
        src = html_lib.unescape(item["text"]).strip()
        if not src:
            risks.append(f"Mermaid #{idx} 为空")
            continue
        first = src.splitlines()[0].strip()
        known = ("flowchart", "graph ", "sequenceDiagram", "stateDiagram", "mindmap", "pie", "timeline", "classDiagram", "journey", "erDiagram", "quadrantChart", "gantt", "gitGraph", "xychart")
        if not any(first.startswith(x) for x in known):
            risks.append(f"Mermaid #{idx} 首行无法识别: {first[:60]}")
        if "&amp;" in item["text"] or "&lt;" in item["text"] or "&gt;" in item["text"]:
            risks.append(f"Mermaid #{idx} 含 HTML 实体，需确认 Mermaid 语法解码")
        if re.search(r"(?<!<)<br\s*/?>(?!>)", src, flags=re.I):
            # Mermaid htmlLabels支持br，但不同图类型兼容性不同，只提示不判错。
            risks.append(f"Mermaid #{idx} 使用 HTML <br>，需重点截图确认")
        if "&" in src and "&amp;" not in item["text"]:
            risks.append(f"Mermaid #{idx} 含未转义 &，可能触发 Mermaid 解析问题")
    return risks


def chart_risks(parser: RenderParser) -> list[str]:
    risks: list[str] = []
    script_text = "\n".join(s["text"] for s in parser.scripts)
    for canvas in parser.canvases:
        cid = canvas["id"]
        if not cid:
            risks.append(f"Canvas 缺少 id（第 {canvas['tag'][0]} 行）")
            continue
        # 允许通过 getElementById、querySelector 或直接 canvas 上下文初始化。
        mentions = [
            re.search(rf"getElementById\(\s*['\"]{re.escape(cid)}['\"]\s*\)", script_text),
            re.search(rf"querySelector\(\s*['\"]#{re.escape(cid)}['\"]\s*\)", script_text),
            re.search(rf"['\"]{re.escape(cid)}['\"]", script_text),
        ]
        if not any(mentions):
            risks.append(f"Canvas #{cid} 未找到脚本引用")
        if "new Chart" not in script_text:
            risks.append(f"Canvas #{cid} 所在页没有 new Chart")
        # 主题切换时 render.js 依赖该数组重绘自定义图表；没有注册会导致暗色主题不更新。
        if any(mentions) and "CB_CHARTS" not in script_text:
            risks.append(f"Canvas #{cid} 创建后未注册 CB_CHARTS，主题切换可能不重绘")
    return risks


def image_risks(path: Path, parser: RenderParser) -> list[str]:
    risks: list[str] = []
    for idx, img in enumerate(parser.images, 1):
        src = img["src"]
        if not src:
            risks.append(f"图片 #{idx} 缺少 src")
            continue
        if img["alt"] is None:
            risks.append(f"图片 #{idx} 缺少 alt: {src[:80]}")
        if src.startswith(("http://", "https://", "data:", "//")):
            continue
        target = (path.parent / src).resolve()
        if not target.exists():
            risks.append(f"本地图片不存在: {src}")
    return risks


def analyze(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8", errors="ignore")
    parser = RenderParser()
    try:
        parser.feed(raw)
        parser.close()
    except Exception as exc:
        return {"fatal": f"HTML 解析失败: {exc}", "risks": []}
    risks = []
    risks += formula_risks(raw, parser)
    risks += mermaid_risks(parser)
    risks += chart_risks(parser)
    risks += image_risks(path, parser)
    if not re.search(r'<script[^>]+src=["\'][^"\']*render\.js["\']', raw, flags=re.I):
        risks.append("未加载 assets/js/render.js")
    if parser.mermaids and not re.search(r"mermaid@", raw, flags=re.I):
        risks.append("存在 Mermaid 容器但未加载 Mermaid CDN")
    if any("$$" in s["text"] or "\\[" in s["text"] for s in parser.scripts):
        risks.append("脚本字符串中出现公式分隔符，需确认不是误触发 KaTeX")
    return {
        "fatal": "",
        "risks": risks,
        "mermaid": len(parser.mermaids),
        "formula_ignored": len(parser.formula_ignored),
        "canvas": len(parser.canvases),
        "images": len(parser.images),
    }


def main() -> int:
    args = sys.argv[1:] or ["all"]
    files: list[Path] = []
    for arg in args:
        files.extend(resolve(arg))
    files = [p for p in files if p.name != "index.html"]
    if not files:
        print("no files matched:", args)
        return 1
    ok = 0
    total_risks = 0
    for path in files:
        result = analyze(path)
        rel = path.relative_to(ROOT).as_posix()
        if result.get("fatal"):
            print(f"ERR {rel}: {result['fatal']}")
            total_risks += 1
            continue
        risks = result["risks"]
        if risks:
            print(f"GAP {rel}: Mermaid={result['mermaid']} Canvas={result['canvas']} Img={result['images']} 风险={len(risks)}")
            for risk in risks:
                print(f"  - {risk}")
            total_risks += len(risks)
        else:
            ok += 1
            print(f"OK  {rel}: Mermaid={result['mermaid']} Canvas={result['canvas']} Img={result['images']}")
    print("-" * 100)
    print(f"静态无风险 {ok}/{len(files)}；风险条目 {total_risks}")
    return 0 if total_risks == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
