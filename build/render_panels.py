#!/usr/bin/env python3
"""Render the annotated panel plates referenced by build/cards/panel_refs.json.

    python3 build/render_panels.py

Reads the FSI Pilot Training Manual and writes one WebP per referenced page into
images/panels/ptm-<page>.webp. Needs a throwaway venv:

    python3 -m venv /tmp/pdfvenv && /tmp/pdfvenv/bin/pip install pypdfium2 Pillow
    /tmp/pdfvenv/bin/python build/render_panels.py

The source PDF is NOT in this repo (it is git-ignored, and it is FSI's document).
Only re-run this if panel_refs.json gains pages or the scale/quality changes;
the rendered output is committed so a normal build needs neither the PDF nor a venv.

scale 2.0 -> ~1584x1224, quality 80 -> ~115 KB. The plates are line art with
small callout labels, so resolution matters more than it would for photos; the
app displays them scaled down and full-size on tap.
"""
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PDF = ROOT.parent / 'Pilot Training Manual.pdf'
OUT = ROOT / 'images' / 'panels'
SCALE = 2.0
QUALITY = 80


def main():
    try:
        import pypdfium2 as pdfium
    except ImportError:
        sys.exit('pypdfium2 not installed — see the docstring for the venv recipe')
    if not PDF.exists():
        sys.exit(f'source PDF not found: {PDF}')

    refs = json.loads((ROOT / 'build' / 'cards' / 'panel_refs.json').read_text())
    OUT.mkdir(parents=True, exist_ok=True)
    doc = pdfium.PdfDocument(str(PDF))

    total = 0
    for r in refs:
        img = doc[r['page'] - 1].render(scale=SCALE).to_pil().convert('RGB')
        path = OUT / f"ptm-{r['page']}.webp"
        img.save(path, format='WEBP', quality=QUALITY, method=6)
        total += path.stat().st_size
    print(f'rendered {len(refs)} plates into {OUT.relative_to(ROOT)}')
    print(f'{total / 1024 / 1024:.1f} MB total, avg {total / len(refs) / 1024:.0f} KB')
    return 0


if __name__ == '__main__':
    sys.exit(main())
