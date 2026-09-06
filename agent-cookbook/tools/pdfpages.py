# -*- coding: utf-8 -*-
"""pdfpages.py — 用 Edge/Chrome headless 打印 print.html 并统计真实 PDF 页数.
用法: python tools/pdfpages.py
"""
import os, subprocess, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF = os.path.join(ROOT, ".qa", "book.pdf")
CHROME_CANDIDATES = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
]
def main():
    exe = next((c for c in CHROME_CANDIDATES if os.path.exists(c)), None)
    if not exe:
        print("no chrome/edge found"); sys.exit(2)
    url = "file:///" + os.path.join(ROOT, "print.html").replace("\\", "/")
    os.makedirs(os.path.dirname(PDF), exist_ok=True)
    cmd = [exe, "--headless", "--disable-gpu", "--no-pdf-header-footer",
           "--print-to-pdf=" + PDF, url]
    print("printing ...", " ".join(cmd[1:3]))
    subprocess.run(cmd, capture_output=True, timeout=900)
    if not os.path.exists(PDF):
        print("PDF not created"); sys.exit(1)
    raw = open(PDF, "rb").read()
    n = len(re.findall(rb"/Type\s*/Page[^s]", raw))
    print(f"PDF: {os.path.getsize(PDF)//1024}KB, pages = {n}")
    return n
if __name__ == "__main__":
    main()
