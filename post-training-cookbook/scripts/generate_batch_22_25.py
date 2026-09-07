# -*- coding: utf-8 -*-
"""Generate chapters 22, 23, 24, 25 strictly complying with AGENTS_GUIDE.md."""
import os, sys

def write_file(filename, content):
    path = os.path.join("D:/llm-post-training-cookbook/chapters", filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Written {filename}: {len(content)} chars")

print("Generator batch 22-25 ready")
