#!/usr/bin/env python3
"""Rebuild index.html and the Anki deck from the card sources.

    python3 build/build.py

Standard library only — no venv needed.

Pipeline:
    build/cards/{fsi,afm,ace}_cards.json  +  build/cards/gfs_sessions.json
    +  build/trainer.template.html
        -> index.html            (cards at __CARDS_DATA__, GFS at __GFS_DATA__)
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


def load_gfs(cards):
    """Load the GFS session plans, and prove every card reference resolves.

    A typo'd card id would render as a chip that drills nothing, so it is worth
    failing the build over rather than discovering it in the device.
    """
    path = BUILD / 'cards' / 'gfs_sessions.json'
    sessions = json.loads(path.read_text())
    known = {c['id'] for c in cards}
    keys = [s['key'] for s in sessions]
    dupes = {k for k in keys if keys.count(k) > 1}
    if dupes:
        raise SystemExit(f'duplicate GFS session keys: {sorted(dupes)}')

    blocks = items = minutes = 0
    for s in sessions:
        for field in ('key', 'day', 'phase', 'title', 'focus', 'blocks'):
            if not s.get(field):
                raise SystemExit(f'GFS {s.get("key")} missing field: {field}')
        for b in s['blocks']:
            for field in ('title', 'min', 'items'):
                if not b.get(field):
                    raise SystemExit(f'GFS {s["key"]} block missing field: {field}')
            missing = sorted(set(b.get('cards') or []) - known)
            if missing:
                raise SystemExit(
                    f'GFS {s["key"]} / "{b["title"]}" references unknown cards: {missing}')
            blocks += 1
            items += len(b['items'])
            minutes += b['min']
    print(f'  {"gfs_sessions.json":20} {len(sessions):>4} sessions, '
          f'{blocks} blocks, {items} items, {minutes} min')
    return sessions


def build_index(cards, gfs):
    template = (BUILD / 'trainer.template.html').read_text()
    for placeholder in ('__CARDS_DATA__', '__GFS_DATA__'):
        if placeholder not in template:
            raise SystemExit(f'template is missing the {placeholder} placeholder')
    out = template
    for placeholder, data in (('__CARDS_DATA__', cards), ('__GFS_DATA__', gfs)):
        payload = json.dumps(data, ensure_ascii=False).replace('</', '<\\/')
        out = out.replace(placeholder, payload)
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
    gfs = load_gfs(cards)

    (ROOT / 'flashcards_data.json').write_text(
        json.dumps(cards, ensure_ascii=False, indent=1))

    size = build_index(cards, gfs)
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
