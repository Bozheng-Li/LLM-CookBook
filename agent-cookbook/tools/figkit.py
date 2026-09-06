# -*- coding: utf-8 -*-
"""figkit — AI Agent Cookbook 统一 SVG 图表工具库.

用法:
    from figkit import *
    f = F(900, 420)
    b = f.box(60, 60, 200, 64, "用户请求", fill=C.indigo_s, stroke=C.indigo)
    f.arrow(...); f.save("my-figure")
生成 assets/figures/my-figure.svg
"""
import os

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "figures")

FONT = "'Segoe UI','PingFang SC','Microsoft YaHei','Noto Sans SC',sans-serif"
MONO = "'Cascadia Code',Consolas,monospace"


class C:
    """Palette — 与站点 CSS 变量一致(亮色)。"""
    ink = "#1c1e26"; soft = "#4a4d5a"; faint = "#7a7d8c"
    line = "#d2cec2"; line_soft = "#e7e4db"
    indigo = "#4f46e5"; indigo_s = "#eef0fd"; indigo_d = "#3730a3"
    teal = "#0d9488"; teal_s = "#e7f6f4"; teal_d = "#115e59"
    amber = "#d97706"; amber_s = "#fdf3e3"; amber_d = "#92400e"
    red = "#dc2626"; red_s = "#fdeeee"; red_d = "#991b1b"
    blue = "#2563eb"; blue_s = "#eaf0fe"; blue_d = "#1e40af"
    purple = "#7c3aed"; purple_s = "#f3e8ff"; purple_d = "#5b21b6"
    green = "#16a34a"; green_s = "#ecfaf0"
    gray_s = "#f4f2ec"; white = "#ffffff"


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
             .replace('"', "&quot;"))


def tw(text, fs):
    """估算文本宽度(px): CJK≈1.0em, ASCII≈0.55em。"""
    return sum((1.0 if ord(ch) > 0x2E80 else (0.62 if ch.isupper() or ch in "@&#%" else 0.55)) * fs for ch in text)


def wrap(text, width, fs):
    """按像素宽度粗略折行(CJK 友好)。返回行列表。"""
    lines, cur, curw = [], "", 0.0
    for ch in text:
        w = (1.0 if ord(ch) > 0x2E80 else 0.55) * fs
        if cur and curw + w > width:
            lines.append(cur); cur, curw = ch, w
        else:
            cur += ch; curw += w
    if cur:
        lines.append(cur)
    return lines


class F:
    def __init__(self, w, h, bg="#ffffff"):
        self.w, self.h, self.bg = w, h, bg
        self.el = []
        self._mid = 0

    # ---------- low level ----------
    def raw(self, s):
        self.el.append(s)

    def _marker(self, color):
        self._mid += 1
        i = "m%d" % self._mid
        self.raw('<marker id="%s" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7.5" markerHeight="7.5" orient="auto-start-reverse"><path d="M0,0.6 L9.5,5 L0,9.4 z" fill="%s"/></marker>' % (i, color))
        return i

    def text(self, x, y, s, fs=13, fill=C.ink, weight=400, anchor="middle", mono=False, style=""):
        fam = MONO if mono else FONT
        self.raw('<text x="%s" y="%s" font-family="%s" font-size="%s" fill="%s" font-weight="%s" text-anchor="%s" style="%s">%s</text>'
                 % (round(x, 1), round(y, 1), fam, fs, fill, weight, anchor, style, esc(s)))
        return self

    def mtext(self, x, y, lines, fs=13, fill=C.ink, weight=400, lh=1.45, anchor="middle", mono=False):
        """多行文本(以首个 y 为第一行基线)。"""
        for i, ln in enumerate(lines):
            self.text(x, y + i * fs * lh, ln, fs, fill, weight, anchor, mono)
        return self

    # ---------- shapes ----------
    def box(self, x, y, w, h, title="", sub=None, fill=C.white, stroke=C.line,
            tc=None, fs=13.5, rx=10, weight=700, dash=None, sw=1.4, sub_fs=11, mono=False):
        tc = tc or C.ink
        d = ' stroke-dasharray="%s"' % dash if dash else ""
        self.raw('<rect x="%s" y="%s" width="%s" height="%s" rx="%s" fill="%s" stroke="%s" stroke-width="%s"%s/>'
                 % (x, y, w, h, rx, fill, stroke, sw, d))
        lines = title.split("\n") if title else []
        if lines:
            block = len(lines) * fs * 1.35 + ((fs * 1.7) if sub else 0)
            y0 = y + h / 2 - block / 2 + fs
            self.mtext(x + w / 2, y0, lines, fs, tc, weight, 1.35, mono=mono)
            if sub:
                self.text(x + w / 2, y0 + (len(lines) - 1) * fs * 1.35 + fs * 1.55, sub, sub_fs, C.faint, 400)
        return {"cx": x + w / 2, "cy": y + h / 2, "x": x, "y": y, "w": w, "h": h,
                "right": (x + w, y + h / 2), "left": (x, y + h / 2),
                "top": (x + w / 2, y), "bottom": (x + w / 2, y + h / 2)}

    def pill(self, cx, cy, text, fill=C.indigo_s, tc=None, fs=12, weight=700, stroke="none"):
        tc = tc or C.indigo_d
        w = tw(text, fs) + 22
        h = fs + 12
        self.raw('<rect x="%s" y="%s" width="%s" height="%s" rx="%s" fill="%s" stroke="%s"/>'
                 % (cx - w / 2, cy - h / 2, w, h, h / 2, fill, stroke))
        self.text(cx, cy + fs * 0.36, text, fs, tc, weight)
        return {"cx": cx, "cy": cy, "left": (cx - w / 2, cy), "right": (cx + w / 2, cy), "w": w, "h": h}

    def badge(self, cx, cy, n, fill=C.indigo, tc="#fff", r=11, fs=12):
        self.raw('<circle cx="%s" cy="%s" r="%s" fill="%s"/>' % (cx, cy, r, fill))
        self.text(cx, cy + fs * 0.36, str(n), fs, tc, 800)
        return self

    def diamond(self, cx, cy, w, h, text, fill=C.amber_s, stroke=C.amber, fs=12, tc=None):
        pts = "%s,%s %s,%s %s,%s %s,%s" % (cx, cy - h / 2, cx + w / 2, cy, cx, cy + h / 2, cx - w / 2, cy)
        self.raw('<polygon points="%s" fill="%s" stroke="%s" stroke-width="1.4"/>' % (pts, fill, stroke))
        for i, ln in enumerate(text.split("\n")):
            self.text(cx, cy + (i - (len(text.split("\n")) - 1) / 2) * fs * 1.3 + fs * 0.36, ln, fs, tc or C.amber_d, 700)
        return {"cx": cx, "cy": cy, "right": (cx + w / 2, cy), "left": (cx - w / 2, cy),
                "top": (cx, cy - h / 2), "bottom": (cx, cy + h / 2)}

    def cylinder(self, cx, cy, w, h, title, fill=C.teal_s, stroke=C.teal, fs=12.5):
        ry = min(10, h / 4)
        top = cy - h / 2
        self.raw('<path d="M%s,%s a%s,%s 0 0 1 %s,0 v%s a%s,%s 0 0 1 -%s,0 z" fill="%s" stroke="%s" stroke-width="1.4"/>'
                 % (cx - w / 2, top, w / 2, ry, w, h - ry, w / 2, ry, w, fill, stroke))
        self.raw('<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="none" stroke="%s" stroke-width="1.4"/>'
                 % (cx, top, w / 2, ry, stroke))
        self.mtext(cx, cy - (len(title.split("\n")) - 1) * fs * 0.65 + fs * 0.36 - ry * 0.4,
                   title.split("\n"), fs, C.teal_d, 700)
        return {"cx": cx, "cy": cy, "top": (cx, top), "bottom": (cx, cy + h / 2),
                "left": (cx - w / 2, cy), "right": (cx + w / 2, cy)}

    def docicon(self, x, y, w=30, h=38, fill=C.blue_s, stroke=C.blue):
        self.raw('<path d="M%s,%s h%s l%s,%s v%s h-%s z" fill="%s" stroke="%s" stroke-width="1.3"/>'
                 % (x, y, w - 8, 8, 8, h, w, fill, stroke))
        for i in range(3):
            self.raw('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="1.6"/>'
                     % (x + 5, y + 12 + i * 7, x + w - 9, y + 12 + i * 7, stroke))

    def person(self, cx, cy, r=13, fill=C.purple_s, stroke=C.purple):
        self.raw('<circle cx="%s" cy="%s" r="%s" fill="%s" stroke="%s" stroke-width="1.4"/>'
                 % (cx, cy - r * 0.9, r * 0.62, fill, stroke))
        self.raw('<path d="M%s,%s a%s,%s 0 0 1 %s,0 z" fill="%s" stroke="%s" stroke-width="1.4"/>'
                 % (cx - r, cy + r * 1.5, r, r * 1.1, r * 2, fill, stroke))
        return self

    def gear(self, cx, cy, r=12, fill=C.soft):
        import math
        pts = []
        for i in range(16):
            rad = r if i % 2 == 0 else r * 0.72
            a = math.pi * 2 * i / 16
            pts.append("%s,%s" % (round(cx + rad * math.cos(a), 1), round(cy + rad * math.sin(a), 1)))
        self.raw('<polygon points="%s" fill="%s"/>' % (" ".join(pts), fill))
        self.raw('<circle cx="%s" cy="%s" r="%s" fill="#fff"/>' % (cx, cy, r * 0.38))
        return self

    # ---------- connectors ----------
    def arrow(self, x1, y1, x2, y2, label=None, color=C.soft, sw=1.8, dash=None,
              label_fs=11.5, label_fill=None, label_dy=-8, both=False, curve=0):
        m = self._marker(color)
        mk = ' marker-start="url(#%s)"' % m if both else ""
        d = ' stroke-dasharray="%s"' % dash if dash else ""
        if curve:
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2
            nx, ny = -(y2 - y1), (x2 - x1)
            n = max(1e-6, (nx * nx + ny * ny) ** .5)
            cxp, cyp = mx + nx / n * curve, my + ny / n * curve
            self.raw('<path d="M%s,%s Q%s,%s %s,%s" fill="none" stroke="%s" stroke-width="%s"%s marker-end="url(#%s)"%s/>'
                     % (x1, y1, cxp, cyp, x2, y2, color, sw, d, m, mk))
            lx, ly = (x1 + 2 * cxp + x2) / 4, (y1 + 2 * cyp + y2) / 4
        else:
            self.raw('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s"%s marker-end="url(#%s)"%s/>'
                     % (x1, y1, x2, y2, color, sw, d, m, mk))
            lx, ly = (x1 + x2) / 2, (y1 + y2) / 2
        if label:
            self.text(lx, ly + label_dy, label, label_fs, label_fill or color, 600,
                      style='paint-order:stroke;stroke:#ffffff;stroke-width:4px;')
        return self

    def elbow(self, pts, label=None, color=C.soft, sw=1.8, dash=None, label_pos=0, label_fs=11.5):
        """pts: [(x,y),...] 折线箭头, label 放在第 label_pos 段中点。"""
        m = self._marker(color)
        d = ' stroke-dasharray="%s"' % dash if dash else ""
        pstr = " ".join("%s,%s" % (p[0], p[1]) for p in pts)
        self.raw('<polyline points="%s" fill="none" stroke="%s" stroke-width="%s"%s marker-end="url(#%s)"/>'
                 % (pstr, color, sw, d, m))
        if label:
            a, b = pts[label_pos], pts[label_pos + 1]
            self.text((a[0] + b[0]) / 2, (a[1] + b[1]) / 2 - 8, label, label_fs, color, 600,
                      style='paint-order:stroke;stroke:#ffffff;stroke-width:4px;')
        return self

    # ---------- containers ----------
    def group(self, x, y, w, h, label="", fill="#fafaf7", stroke=C.line, dash="6 4", label_fill=None, fs=12.5, rx=12):
        self.raw('<rect x="%s" y="%s" width="%s" height="%s" rx="%s" fill="%s" stroke="%s" stroke-width="1.3" stroke-dasharray="%s"/>'
                 % (x, y, w, h, rx, fill, stroke, dash))
        if label:
            self.text(x + 14, y + 20, label, fs, label_fill or C.faint, 700, anchor="start")
        return self

    def lane(self, x, y, w, h, label, fill=C.gray_s, head_fill=C.indigo_s, head_tc=C.indigo_d, w_head=150):
        """泳道: 左侧标题头。"""
        self.raw('<rect x="%s" y="%s" width="%s" height="%s" rx="10" fill="%s" stroke="%s" stroke-width="1.2"/>'
                 % (x, y, w, h, "#ffffff", C.line_soft))
        self.raw('<rect x="%s" y="%s" width="%s" height="%s" rx="10" fill="%s"/>' % (x, y, w_head, h, fill))
        self.raw('<rect x="%s" y="%s" width="%s" height="%s" rx="10" fill="%s"/>'
                 % (x + w_head - 10, y, 10, h, "#ffffff"))
        self.mtext(x + w_head / 2, y + h / 2 - (len(label.split("\n")) - 1) * 8 + 4.5, label.split("\n"), 13, head_tc, 800)
        return {"x": x + w_head, "y": y, "w": w - w_head, "h": h, "cy": y + h / 2}

    # ---------- meta ----------
    def note(self, x, y, text, fs=11.5, color=C.faint, anchor="start"):
        self.text(x, y, text, fs, color, 400, anchor,
                  style='paint-order:stroke;stroke:#ffffff;stroke-width:3px;')
        return self

    def save(self, name):
        os.makedirs(OUT, exist_ok=True)
        svg = ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d">'
               '<defs></defs><rect width="%d" height="%d" fill="%s"/>%s</svg>'
               % (self.w, self.h, self.w, self.h, self.w, self.h, self.bg, "\n".join(self.el)))
        # markers must live in defs -> they are appended inline; ok since unique per file
        path = os.path.join(OUT, name + ".svg")
        with open(path, "w", encoding="utf-8") as f:
            f.write(svg)
        print("saved", name, "(%dx%d)" % (self.w, self.h))
        return path


def chevron_flow(f, x, y, w, h, steps, gap=8, fill=C.indigo_s, stroke=C.indigo, tc=None, fs=13):
    """横向步骤条, steps: [str], 返回各步中心。"""
    n = len(steps)
    sw = (w - gap * (n - 1)) / n
    centers = []
    for i, s in enumerate(steps):
        sx = x + i * (sw + gap)
        f.box(sx, y, sw, h, s, fill=fill if i % 2 == 0 else C.teal_s,
              stroke=stroke if i % 2 == 0 else C.teal, tc=tc, fs=fs, rx=9)
        centers.append((sx + sw / 2, y + h / 2))
        if i:
            f.arrow(sx - gap - 2, y + h / 2, sx + 2, y + h / 2, color=C.faint, sw=1.6)
    return centers
