#!/usr/bin/env python3
"""Build the consolidated two-column study PDF from the verified card data.

    /tmp/pdfvenv/bin/python build/make_study_pdf.py

Needs reportlab (not stdlib), so it is a separate step from build.py:

    python3 -m venv /tmp/pdfvenv && /tmp/pdfvenv/bin/pip install reportlab

Output: PC-24 Study Reference.pdf at the repo root.

Left column is the question, right column is the answer, grouped by section in the
same divisions the app uses. Includes all 198 cards plus the gouge lines that
verified clean; the gouge lines that did not verify are deliberately excluded --
this document is meant to be trustworthy without cross-checking, so anything not
confirmed against the AFM or PTM does not belong in it.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'PC-24 Study Reference.pdf'

# Helvetica is WinAnsi; these four are outside it. Substituting beats silently
# dropping a glyph in a limitations document.
SUBS = {'→': ' -> ', '≤': '<=', '≥': '>=', '−': '-'}
WINANSI_EXTRA = set('§°±²³·×–—'
                    '“”•™')


def esc(text):
    """Normalize, escape for reportlab's mini-markup, keep line breaks."""
    for a, b in SUBS.items():
        text = text.replace(a, b)
    bad = {c for c in text if ord(c) > 126 and c not in WINANSI_EXTRA}
    if bad:
        raise SystemExit(f'un-encodable glyph(s) {bad!r} in: {text[:60]!r}')
    text = (text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))
    return text.replace('\n', '<br/>')


def main():
    try:
        from reportlab.lib import colors
        from reportlab.lib.enums import TA_LEFT
        from reportlab.lib.pagesizes import letter
        from reportlab.lib.styles import ParagraphStyle
        from reportlab.lib.units import inch
        from reportlab.platypus import (BaseDocTemplate, Frame, KeepTogether, PageTemplate,
                                        Paragraph, Spacer, Table, TableStyle)
    except ImportError:
        sys.exit('reportlab not installed -- see the docstring')

    cards = {}
    order = []
    for f in ('fsi', 'afm', 'ace'):
        for c in json.loads((ROOT / 'build' / 'cards' / f'{f}_cards.json').read_text()):
            cards[c['id']] = c
            order.append(c['id'])
    gouge = json.loads((ROOT / 'build' / 'cards' / 'gouge.json').read_text())

    INK = colors.HexColor('#17202e')
    MUTED = colors.HexColor('#5c6b80')
    ACCENT = colors.HexColor('#0b6f8a')
    LINE = colors.HexColor('#c8d2df')
    ZEBRA = colors.HexColor('#f4f6fa')
    RULE = colors.HexColor('#8d9db4')

    def st(name, **kw):
        base = dict(fontName='Helvetica', fontSize=8.4, leading=10.4, textColor=INK,
                    alignment=TA_LEFT, spaceBefore=0, spaceAfter=0)
        base.update(kw)
        return ParagraphStyle(name, **base)

    S_Q = st('q')
    S_A = st('a')
    S_HEAD = st('head', fontName='Helvetica-Bold', fontSize=7.0, leading=8.4,
                textColor=colors.white)
    S_ID = st('cid', fontName='Helvetica-Bold', fontSize=7.4, leading=9.2, textColor=ACCENT)
    S_SEC = st('sec', fontName='Helvetica-Bold', fontSize=13.5, leading=15.5, textColor=INK,
               spaceBefore=13, spaceAfter=2)
    S_SUB = st('sub', fontName='Helvetica-Bold', fontSize=9.2, leading=11, textColor=ACCENT,
               spaceBefore=9, spaceAfter=3)
    S_NOTE = st('note', fontSize=7.8, leading=9.6, textColor=MUTED, spaceAfter=5)
    S_REF = st('ref', fontSize=6.5, leading=8, textColor=MUTED)
    S_TITLE = st('title', fontName='Helvetica-Bold', fontSize=20, leading=23, textColor=INK)
    S_SUBTITLE = st('subtitle', fontSize=9.2, leading=12.4, textColor=MUTED, spaceBefore=4)

    LEFT_W, RIGHT_W = 3.15 * inch, 4.25 * inch

    def row_cells(cid, title, question, answer, reference):
        left = [Paragraph(f'{esc(cid)} &nbsp;&nbsp;{esc(title).upper()}', S_ID),
                Spacer(1, 2.2), Paragraph(esc(question), S_Q)]
        if reference:
            left += [Spacer(1, 2.6), Paragraph(esc(reference), S_REF)]
        return [left, Paragraph(esc(answer), S_A)]

    def make_table(rows):
        data = [[Paragraph('QUESTION', S_HEAD), Paragraph('ANSWER', S_HEAD)]] + rows
        t = Table(data, colWidths=[LEFT_W, RIGHT_W], repeatRows=1)
        style = [
            ('BACKGROUND', (0, 0), (-1, 0), RULE),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('TOPPADDING', (0, 0), (-1, -1), 4.5),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 4.5),
            ('LEFTPADDING', (0, 0), (-1, -1), 6),
            ('RIGHTPADDING', (0, 0), (-1, -1), 6),
            ('GRID', (0, 0), (-1, -1), 0.4, LINE),
        ]
        for i in range(1, len(data)):
            if i % 2 == 0:
                style.append(('BACKGROUND', (0, i), (-1, i), ZEBRA))
        t.setStyle(TableStyle(style))
        return t

    ok_secs = [(s['name'], [i for i in s['items'] if i['status'] == 'ok'])
               for s in gouge['sections']]
    ok_secs = [(n, items) for n, items in ok_secs if items]
    n_ok = sum(len(i) for _, i in ok_secs)

    story = []
    story.append(Paragraph('PC-24 Study Reference', S_TITLE))
    story.append(Paragraph(
        'Consolidated verified data &mdash; MSN 631 (MSN 501-UP column throughout).<br/>'
        '198 cards from the FSI Memory Flash Cards, the Pilatus AFM (Report 02371, Issue 003 '
        'Rev 08) and the ACE Avionics Pilot&rsquo;s Guide, plus ' + str(n_ok) +
        ' independently verified lines from a student gouge.<br/>'
        'Every value in this document was checked against its source. Items that could not be '
        'verified are excluded.', S_SUBTITLE))

    # ---- card sections, in the app's divisions ----
    MEM = [f'E-{n}' for n in range(1, 16)] + ['E-20']
    FLOW = [f'E-{n}' for n in range(16, 20)] + ['E-21']
    L_IDS = [i for i in order if i.startswith('L-')]
    AGI_IDS = [i for i in order if i.startswith('AGI')]

    def topic_groups(prefix):
        seen = []
        for i in order:
            if i.startswith(prefix):
                tp = cards[i].get('topic') or 'General'
                if tp not in seen:
                    seen.append(tp)
        return [(tp, [i for i in order if i.startswith(prefix)
                      and (cards[i].get('topic') or 'General') == tp]) for tp in seen]

    def card_section(heading, note, ids, subgroups=None):
        story.append(Paragraph(esc(heading), S_SEC))
        if note:
            story.append(Paragraph(note, S_NOTE))
        if subgroups:
            for tp, tids in subgroups:
                story.append(Paragraph(esc(tp), S_SUB))
                story.append(make_table([row_cells(cards[i]['id'], cards[i]['title'],
                                                   cards[i]['front'], cards[i]['back'],
                                                   cards[i]['reference']) for i in tids]))
        else:
            story.append(make_table([row_cells(cards[i]['id'], cards[i]['title'],
                                               cards[i]['front'], cards[i]['back'],
                                               cards[i]['reference']) for i in ids]))

    card_section('Emergency memory items',
                 'Standard: <b>verbatim, in order, out loud</b>. These 16 are the procedures '
                 'the AFM encloses in a solid red box.', MEM)
    card_section('Normal procedure flows',
                 'Standard: fluent &mdash; sequence and every confirmation correct. These share '
                 'the E- numbering but are <b>not</b> memory items.', FLOW)
    card_section('Limitations',
                 'Standard: <b>exact number, exact unit</b>. &ldquo;About&rdquo; is a bust.', L_IDS)
    card_section('Aircraft general', 'Standard: fluent.', AGI_IDS)
    card_section('AFM extended', 'Working knowledge. Built from the AFM to close gaps in the '
                 'issued deck &mdash; mostly limitations.', None, topic_groups('AFM'))
    card_section('ACE avionics', 'Working knowledge &mdash; alerting, mode logic, reversion.',
                 None, topic_groups('ACE'))

    # ---- verified gouge lines ----
    story.append(Paragraph('Verified gouge values', S_SEC))
    story.append(Paragraph(
        f'{n_ok} lines from a classmate&rsquo;s gouge that were confirmed against the AFM or the '
        'FSI Pilot Training Manual. The gouge&rsquo;s wrong, conflicting and unconfirmed lines are '
        '<b>not</b> reproduced here &mdash; see the Gouge tab in the app for those.', S_NOTE))
    for name, items in ok_secs:
        story.append(Paragraph(esc(name), S_SUB))
        rows = []
        for it in items:
            left = [Paragraph(esc(it['label']).upper(), S_ID)]
            if it.get('src'):
                left += [Spacer(1, 2.6), Paragraph('Verified: ' + esc(it['src']), S_REF)]
            ans = esc(it['gouge'])
            if it.get('correct'):
                ans += '<br/><br/>' + esc(it['correct'])
            rows.append([left, Paragraph(ans, S_A)])
        story.append(make_table(rows))

    # ---- page furniture ----
    PW, PH = letter
    ML = MR = 0.55 * inch
    MT, MB = 0.52 * inch, 0.62 * inch

    class Doc(BaseDocTemplate):
        def afterFlowable(self, flowable):
            pass

    def furniture(canvas, doc):
        canvas.saveState()
        canvas.setFont('Helvetica', 6.8)
        canvas.setFillColor(MUTED)
        canvas.drawString(ML, 0.34 * inch,
                          'PC-24 Study Reference · MSN 631 · '
                          'For training purposes only, and not for sale.')
        canvas.drawRightString(PW - MR, 0.34 * inch, 'Page %d' % doc.page)
        if doc.page > 1:
            canvas.drawRightString(PW - MR, PH - 0.36 * inch, 'PC-24 Study Reference')
        canvas.setStrokeColor(LINE)
        canvas.setLineWidth(0.4)
        canvas.line(ML, 0.46 * inch, PW - MR, 0.46 * inch)
        canvas.restoreState()

    doc = Doc(str(OUT), pagesize=letter, leftMargin=ML, rightMargin=MR,
              topMargin=MT, bottomMargin=MB,
              title='PC-24 Study Reference', author='PC-24 Memory Trainer',
              subject='Consolidated verified limitations and memory items, MSN 631')
    frame = Frame(ML, MB, PW - ML - MR, PH - MT - MB, id='body',
                  leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id='all', frames=[frame], onPage=furniture)])
    doc.build(story)

    kb = OUT.stat().st_size / 1024
    print(f'wrote {OUT.name}  ({kb:.0f} KB)')
    print(f'  198 cards + {n_ok} verified gouge lines')
    return 0


if __name__ == '__main__':
    sys.exit(main())
