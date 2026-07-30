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


def load_standards():
    """Completion standards — what the partner must observe, and what advances you.

    Items name a standard by key rather than restating it, so every item of the
    same kind is judged identically. That consistency is the point: a training
    standard that drifts item to item is not a standard.
    """
    path = BUILD / 'cards' / 'standards.json'
    standards = json.loads(path.read_text())
    for key, s in standards.items():
        for field in ('label', 'demo', 'gate', 'who'):
            if not s.get(field):
                raise SystemExit(f'standard "{key}" missing field: {field}')
        if s['who'] not in ('flying', 'monitoring', 'both'):
            raise SystemExit(f'standard "{key}" has a bad "who": {s["who"]}')
    print(f'  {"standards.json":20} {len(standards):>4} completion standards')
    return standards


def load_gfs(cards, standards):
    """Load the GFS session plans, and prove every reference resolves.

    A typo'd card id would render as a chip that drills nothing, and an unknown
    standard key would render an item with no completion criteria at all. Both
    are worth failing the build over rather than discovering in the device.
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
            for it in b['items']:
                if not isinstance(it, dict) or not it.get('do') or not it.get('std'):
                    raise SystemExit(
                        f'GFS {s["key"]} / "{b["title"]}": item needs both "do" and "std": {it!r}')
                if it['std'] not in standards:
                    raise SystemExit(
                        f'GFS {s["key"]} / "{b["title"]}": unknown standard "{it["std"]}" '
                        f'on item {it["do"][:48]!r}')
            blocks += 1
            items += len(b['items'])
            minutes += b['min']
    crits = sum(1 for s in sessions for b in s['blocks'] for i in b['items'] if i.get('crit'))
    exits = sum(1 for s in sessions for b in s['blocks'] if b.get('exit'))
    print(f'  {"gfs_sessions.json":20} {len(sessions):>4} sessions, '
          f'{blocks} blocks, {items} items, {minutes} min')
    print(f'  {"":20} {crits:>4} item criteria, {exits} block exit gates')
    return sessions


def load_panels(cards):
    """Load the panel-plate references and prove each one resolves.

    Two failure modes worth failing the build over: a card id that does not
    exist (the plate would never surface), and a missing rendered image (the app
    would show a broken thumbnail offline, with no way to tell why). Rendering is
    a separate step — build/render_panels.py — because it needs the source PDF,
    which is not in this repo.
    """
    path = BUILD / 'cards' / 'panel_refs.json'
    refs = json.loads(path.read_text())
    known = {c['id'] for c in cards}
    pages = [r['page'] for r in refs]
    dupes = {p for p in pages if pages.count(p) > 1}
    if dupes:
        raise SystemExit(f'duplicate panel pages: {sorted(dupes)}')

    missing_img, total = [], 0
    for r in refs:
        for field in ('page', 'folio', 'chapter', 'title', 'cards'):
            if not r.get(field):
                raise SystemExit(f'panel p{r.get("page")} missing field: {field}')
        bad = sorted(set(r['cards']) - known)
        if bad:
            raise SystemExit(f'panel p{r["page"]} references unknown cards: {bad}')
        img = ROOT / 'images' / 'panels' / f'ptm-{r["page"]}.webp'
        if not img.exists():
            missing_img.append(img.name)
        else:
            total += img.stat().st_size
        r['img'] = f'images/panels/ptm-{r["page"]}.webp'
    if missing_img:
        raise SystemExit(
            f'missing rendered panels: {missing_img}\n'
            'run build/render_panels.py (needs the source PDF + a pypdfium2 venv)')

    # The service worker warms this list in the background so the plates are
    # available with no signal, not just after you have viewed each one.
    names = sorted(f'ptm-{r["page"]}.webp' for r in refs)
    (ROOT / 'images' / 'panels' / 'index.json').write_text(
        json.dumps(names, indent=0))

    covered = {c for r in refs for c in r['cards']}
    print(f'  {"panel_refs.json":20} {len(refs):>4} plates, {len(covered)} cards covered, '
          f'{total / 1024 / 1024:.1f} MB')
    return refs


def build_index(cards, gfs, panels, standards):
    template = (BUILD / 'trainer.template.html').read_text()
    for placeholder in ('__CARDS_DATA__', '__GFS_DATA__', '__PANELS_DATA__',
                        '__STANDARDS_DATA__'):
        if placeholder not in template:
            raise SystemExit(f'template is missing the {placeholder} placeholder')
    out = template
    for placeholder, data in (('__CARDS_DATA__', cards), ('__GFS_DATA__', gfs),
                              ('__PANELS_DATA__', panels),
                              ('__STANDARDS_DATA__', standards)):
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
    standards = load_standards()
    gfs = load_gfs(cards, standards)
    panels = load_panels(cards)

    (ROOT / 'flashcards_data.json').write_text(
        json.dumps(cards, ensure_ascii=False, indent=1))

    size = build_index(cards, gfs, panels, standards)
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
