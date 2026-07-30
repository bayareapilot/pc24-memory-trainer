#!/usr/bin/env python3
"""Rebuild index.html and the Anki deck from the card sources.

    python3 build/build.py

Standard library only — no venv needed.

Pipeline:
    build/cards/{fsi,afm,ace}_cards.json  +  build/trainer.template.html
        -> index.html            (cards inlined at the __CARDS_DATA__ placeholder)
        -> flashcards_data.json  (all cards merged, for reference/rebuild)
        -> PC24_FSI_Flashcards_Anki.txt

After a card change you MUST also bump CACHE_VERSION in sw.js, or installed
phones keep serving the old cache. --bump does it for you.
"""
import argparse
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / 'build'
SOURCES = ['fsi_cards.json', 'afm_cards.json', 'ace_cards.json']

SECTION_OF = [
    ('E-', 'Emergency'),
    ('AGI', 'AircraftGeneral'),
    ('AFM', 'AFM_Extended'),
    ('ACE', 'ACE_Avionics'),
    ('L-', 'Limitations'),
]


def section(card_id):
    for prefix, name in SECTION_OF:
        if card_id.startswith(prefix):
            return name
    raise SystemExit(f'unrecognised card id prefix: {card_id}')


def load_cards():
    cards = []
    for name in SOURCES:
        path = BUILD / 'cards' / name
        batch = json.loads(path.read_text())
        print(f'  {name:20} {len(batch):>4} cards')
        cards += batch
    ids = [c['id'] for c in cards]
    dupes = {i for i in ids if ids.count(i) > 1}
    if dupes:
        raise SystemExit(f'duplicate card ids: {sorted(dupes)}')
    for c in cards:
        for field in ('id', 'title', 'front', 'back', 'reference'):
            if not c.get(field):
                raise SystemExit(f'{c.get("id")} missing field: {field}')
    return cards


def build_index(cards):
    template = (BUILD / 'trainer.template.html').read_text()
    if '__CARDS_DATA__' not in template:
        raise SystemExit('template is missing the __CARDS_DATA__ placeholder')
    payload = json.dumps(cards, ensure_ascii=False).replace('</', '<\\/')
    out = template.replace('__CARDS_DATA__', payload)
    (ROOT / 'index.html').write_text(out)
    return len(out)


def build_anki(cards):
    def br(text):
        return html.escape(text).replace('\n', '<br>')

    rows = []
    for c in cards:
        tag = 'PC24::' + section(c['id'])
        if c.get('topic'):
            tag += ' PC24::' + re.sub(r'[^A-Za-z0-9]+', '_', c['topic']).strip('_')
        front = f"<b>{html.escape(c['id'])} — {html.escape(c['title'])}</b><br><br>{br(c['front'])}"
        back = f"{br(c['back'])}<br><br><i>{html.escape(c['reference'])}</i>"
        rows.append(f'{front}\t{back}\t{tag}')
    text = '#separator:tab\n#html:true\n#tags column:3\n' + '\n'.join(rows) + '\n'
    (ROOT / 'PC24_FSI_Flashcards_Anki.txt').write_text(text)
    return len(rows)


def bump_cache_version():
    sw = ROOT / 'sw.js'
    text = sw.read_text()
    match = re.search(r"const CACHE_VERSION = 'v(\d+)';", text)
    if not match:
        raise SystemExit('could not find CACHE_VERSION in sw.js')
    nxt = int(match.group(1)) + 1
    sw.write_text(text.replace(match.group(0), f"const CACHE_VERSION = 'v{nxt}';", 1))
    return nxt


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--bump', action='store_true',
                    help='bump CACHE_VERSION in sw.js (required for any card change)')
    args = ap.parse_args()

    print('loading card sources:')
    cards = load_cards()
    print(f'  {"TOTAL":20} {len(cards):>4} cards')

    (ROOT / 'flashcards_data.json').write_text(
        json.dumps(cards, ensure_ascii=False, indent=1))

    size = build_index(cards)
    rows = build_anki(cards)
    print(f'\nindex.html               {size:>7} bytes')
    print(f'PC24_FSI_Flashcards_Anki {rows:>7} rows')
    print('flashcards_data.json     written')

    if args.bump:
        print(f'sw.js CACHE_VERSION      -> v{bump_cache_version()}')
    else:
        print('\nNOTE: CACHE_VERSION not bumped. Re-run with --bump if cards changed,')
        print('      otherwise installed devices will keep serving the old cache.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
