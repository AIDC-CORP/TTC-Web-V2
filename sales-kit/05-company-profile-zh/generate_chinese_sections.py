#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
High-fidelity Vietnamese to Simplified Chinese Generator for TTC Company Profile
Reads 05-company-profile/section*.py, applies structural and semantic Chinese translations,
and outputs 05-company-profile-zh/section*_zh.py.
"""

import os
import re

SRC_DIR = "/home/aidc-tdt/AIDC/TTC-Web-V2/sales-kit/05-company-profile"
DST_DIR = "/home/aidc-tdt/AIDC/TTC-Web-V2/sales-kit/05-company-profile-zh"

def clean_legacy_pages(content):
    """Remove unused legacy page strings to prevent confusion."""
    content = re.sub(r'PAGE_\d+_LEGACY\s*=\s*r""".*?"""\n*', '', content, flags=re.DOTALL)
    content = re.sub(r'PAGE_\d+_VISUAL\s*=\s*r""".*?"""\n*', '', content, flags=re.DOTALL)
    return content

print("Translation script template ready.")
