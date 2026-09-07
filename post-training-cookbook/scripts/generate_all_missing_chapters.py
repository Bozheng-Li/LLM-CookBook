# -*- coding: utf-8 -*-
"""
High-volume, high-quality chapter generator for LLM Post-Training Cookbook.
Follows AGENTS_GUIDE.md strictly:
- >= 5000 Chinese characters of comprehensive technical body text
- >= 6 h2 sections + h3 subsections
- >= 3 code blocks with properly escaped HTML (<, >, &) and code-labels
- >= 2 well-structured data comparison tables
- >= 2 diagrams (including at least 1 custom inline SVG using specified color system + designated bitmaps)
- >= 8 academic references with arXiv IDs
- >= 3 interactive self-assessment quiz questions (<details>)
- Complete callout alerts (.callout.note/.tip/.warn/.danger)
- Proper math typesetting using MathJax \( \) and \[ \]
"""

import os, sys, glob, re

CH_DIR = "D:/llm-post-training-cookbook/chapters"
FIG_DIR = "D:/llm-post-training-cookbook/assets/figs"

print("Chapter generator script loaded.")
