#!/usr/bin/env python3
"""Compile and validate the approved 36-page English company profile."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent
TEX = ROOT / "05-company-profile-en.tex"
PDF = ROOT / "05-company-profile-en.pdf"


def main() -> None:
    if not TEX.exists():
        raise SystemExit(f"Missing approved source: {TEX}")

    for _ in range(2):
        subprocess.run(
            ["xelatex", "-interaction=nonstopmode", "-halt-on-error", TEX.name],
            cwd=ROOT,
            check=True,
        )

    info = subprocess.check_output(["pdfinfo", PDF.name], cwd=ROOT, text=True)
    match = re.search(r"^Pages:\s+(\d+)$", info, flags=re.MULTILINE)
    pages = int(match.group(1)) if match else 0
    if pages != 36:
        raise SystemExit(f"Expected 36 pages, generated {pages}")

    print(f"Validated: {PDF} ({pages} A4 pages)")


if __name__ == "__main__":
    main()
