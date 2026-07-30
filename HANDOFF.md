# Handoff — PC-24 Memory Trainer

Written 2026-07-30. Point a new session at this file plus the repo.

## Who and what

Derek Evans is a contract pilot in **FlightSafety Pilatus PC-24 Pilot Initial (FAA)** training. Class started **Thu 30 Jul 2026**; that day was ground school Day 1. Their aircraft is **MSN 631**, which puts every serial-dependent AFM value in the **MSN 501-up** column.

The deliverable is a flashcard trainer plus a study schedule aligned to the FSI syllabus.

## Current state

- **198 cards** — 87 FSI + 65 AFM Extended + 46 ACE Avionics
- App version **v2.0.0**, service worker **CACHE_VERSION v4**
- Live: **https://bayareapilot.github.io/pc24-memory-trainer/**
- Repo: **https://github.com/bayareapilot/pc24-memory-trainer** (public, GitHub Pages from `main` at root)
- `gh` CLI is installed and authenticated as `bayareapilot`
- Derek has it installed on his iPhone home screen; updates reach him via the in-app "A newer card set is available" banner

## Source documents

All in `/Users/derekevans/Documents/AI Code/Pilatus PC24/` and **git-ignored** (`*.pdf`):

| File | What it is |
|---|---|
| `FSI Memory Flashcards.pdf` | FSI PC-24 Memory Flash Cards Rev 1.0, Mar 2026 — 180 pp, source of the 87 FSI cards |
| `PC-24 AFM.pdf` | Pilatus EASA AFM Report 02371, Issue 003 Rev 08, 01 May 2025 — 1,074 pp Vol 1 |
| `Pc24 ACE.pdf` | Honeywell ACE Pilot's Guide D201912000296-R002 Rev 2, Sep 2022 — 2,131 pp |
| `PC24 Client Schedule.pdf` | FSI Pilot Client Guide Rev 1.0 — the course syllabus |

Derek confirmed with his FSI instructor on 2026-07-30 that posting this content publicly is permitted. That is why the repo is public. Attribution and "for training purposes only" notices are in the README, the app footer, and the study program.

## Card sections and standards

| Prefix | Count | Source | Recall standard |
|---|---|---|---|
| `E-1..E-21` | 21 | FSI | Emergency memory items: **verbatim, in order, out loud**. E-16..E-19 and E-21 are normal-procedure *flows*, not memory items |
| `L-1..L-57` | 57 | FSI | Exact number, exact unit |
| `AGI-1..AGI-9` | 9 | FSI | Fluent |
| `AFM-1..AFM-65` | 65 | AFM | Working knowledge |
| `ACE-1..ACE-46` | 46 | ACE guide | Working knowledge |

Two findings worth not re-deriving:

1. **The AFM contains exactly 16 red-boxed memory items and all 16 were already covered by FSI cards E-1..E-15 and E-20.** No memory items were missing. `3-ENG-01` (dual engine failure) genuinely has no memory box.
2. **AGI-1..AGI-7 (display unit colours) are ACE-derived** but were deliberately left in the FSI section so the checkride deck numbering matches what FSI issued. Do not "tidy" them into the ACE section.

## Schedule model

Keyed to **course day numbers, not calendar dates** — ground school may or may not run weekends, and this is deliberate. Do not reintroduce dated rows.

- **Phase 1 · GND 1–9** — each block holds the cards for the systems taught that day. All 198 cards map to exactly one ground day. SIT falls on Days 6 and 8.
- **Phase 2 · SIM 1–7** — prep blocks from each session's listed maneuvers. SIM 7 is the LOS.
- **Phase 3 · six gates** — `gate-normal` (before GND 6 SIT, 90%), `gate-emer` (before GND 8 SIT, **100% verbatim** — the real memory-item deadline), `gate-written` (before the written test, 100%), `gate-sim3`, `gate-sim4`, `gate-los` (95%).
- **Phases 4–5** — AFM and ACE topic blocks for targeted review.

The FSI written standard is 80% (FAA) corrected to 100%; the card standard is deliberately stricter.

The guide does **not** itemize a separate FAA checking event after SIM 7 (EASA gets 8 sims). If Derek's practical test is scheduled as its own session, add a final gate for it.

## Build pipeline

Standard library Python only — **no venv needed** for rebuilds.

```bash
cd "/Users/derekevans/Documents/AI Code/Pilatus PC24/Study Program"
python3 build/build.py --bump
```

| Path | Role |
|---|---|
| `build/cards/{fsi,afm,ace}_cards.json` | **Card sources — edit these, not index.html** |
| `build/trainer.template.html` | App template; cards are injected at the `__CARDS_DATA__` placeholder |
| `build/build.py` | Merges sources → `index.html`, `flashcards_data.json`, Anki deck. `--bump` increments `CACHE_VERSION` |
| `build/generate_{afm,ace}_cards.py` | The scripts that authored those card sets; keep for provenance and value citations |
| `index.html` | **Generated. Never hand-edit** — the next build overwrites it |

Verified 2026-07-30: `build.py` reproduces the deployed `index.html` byte-for-byte.

To change the schedule, gates, styling or UI, edit `build/trainer.template.html`, then rebuild.

**Every card or template change needs `--bump`.** Skip it and installed phones keep serving the stale cache indefinitely.

Ship it:

```bash
git add -A && git commit -m "..." && git push origin main
```

Pages takes 30–60 s. Poll the live URL for the new version string rather than assuming.

## Gotchas that cost real time here

1. **The service worker will serve you a stale page during local testing.** It is cache-first by design. A `?v=N` query does *not* bust it — the SW matches with `ignoreSearch: true`. Before trusting any local test, run:
   ```js
   for (const r of await navigator.serviceWorker.getRegistrations()) await r.unregister();
   for (const k of await caches.keys()) await caches.delete(k);
   ```
   then reload. This wasted two rounds of "my fix didn't work" — the fix had worked.

2. **The browser-pane viewport can silently collapse to `clientWidth === 0`** after a resize or navigate. Text then wraps one character per line and you get nonsense card heights (4,770 px) and phantom horizontal overflow. **Assert `document.documentElement.clientWidth` before trusting any layout measurement.**

3. **Prefix collision: `AFM`, `AGI`, `ACE` all begin with "A".** `sec()` in the template tests AFM, then AGI, then ACE, then falls back to `id[0]`. Order matters; adding another `A*` section means updating it.

4. **The browser pane blocks bare localhost.** Serving a local copy requires a `.claude/launch.json` entry in the *working* directory plus `preview_start`. Clean up that file afterwards — it is scratch, not project config.

## Verification discipline used here

These are safety-critical numbers, so every value was checked two ways. Keep this up for any new cards:

1. **Numeric presence** — regex every number-with-unit token out of the card backs and confirm each appears in the extracted source text.
2. **Context pairing** — a list of `(description, regex)` pairs asserting the *label and value adjacent* in the source, because a number existing somewhere in a 1,000-page manual proves nothing.

Results so far: AFM 258 tokens + 55 pairings, ACE 52 tokens + 70 pairings, all passing. Also sweep every card at 375 px for clipping and horizontal overflow after any card or CSS change.

Technique worth reusing: **AFM memory items are detectable programmatically** as red-stroked lines at `linewidth 2.0` via pdfplumber `page.lines` (Note/Caution borders use 0.75). Pair the horizontal lines and crop between them to read the boxed text. PDF extraction needs `pypdf`, `pdfplumber`, `pypdfium2`, `Pillow` in a throwaway venv.

## Known non-issues

- `flashcards_data.json` is a generated convenience copy. The sources of truth are under `build/cards/`.
- One source typo is deliberately corrected: FSI card E-21A prints "PDF" where it means "PFD".
- Probe scripts have twice reported false negatives from casing/spacing (`Dual Chine` vs `DUAL CHINE`, `90 ° left` vs `90° LEFT`). Confirm against the card text before treating a failed probe as a missing value.

## Possible next steps

Nothing is outstanding or broken. Ideas, in rough order of likely value:

- Add a gate for the practical test if it gets scheduled as its own session.
- Adjust GND blocks if Derek's actual class order differs from the guide (instructors reorder; the guide notes SIT timing can move).
- Mine AFM Section 5 performance or Section 6 weight-and-balance if he wants those as cards — both were deliberately skipped as lookup material.
- ACE page-by-page operation (flight-plan entry, charts, datalink, radios, SATCOM) was skipped for the same reason.
- The AFM placard pages (115–194) are images and were never OCR'd.
