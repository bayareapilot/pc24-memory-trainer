# Handoff — PC-24 Memory Trainer

Written 2026-07-30, substantially extended 2026-08-02. Point a new session at this file plus the repo.

## Who and what

Derek Evans is a contract pilot in **FlightSafety Pilatus PC-24 Pilot Initial (FAA)** training. Class started **Thu 30 Jul 2026** (that day was GND 1). Their aircraft is **MSN 631**, which puts every serial-dependent AFM value in the **MSN 501-up** column.

**Course position as of Sun 2 Aug 2026: GND 2 complete** (finished Fri 31 Jul; the course does not run weekends, so GND 3 is Mon 3 Aug). Do not re-derive this from file dates or from this document's own header — the app now stores it in `state.courseDay` and that is the thing to trust. Ask Derek if it looks stale.

The deliverable is a flashcard trainer plus a study schedule aligned to the FSI syllabus.

## Current state

- **198 cards** — 87 FSI + 65 AFM Extended + 46 ACE Avionics
- **16 GFS sessions** — 99 blocks, 397 checkable items, 1,445 min (see GFS sessions, below)
- **13 completion standards** on every item, plus 19 item criteria and 10 block exit gates
- **63 panel plates** from the FSI Pilot Training Manual, 5.6 MB (see Panel plates, below)
- App version **v2.6.0**, service worker **CACHE_VERSION v10**
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
| `Pilot Training Manual.pdf` | FSI PILATUS PC-24 Pilot Training Manual Rev 0.7, Apr 2026 — 781 pp, source of the 63 panel plates |

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

## GFS sessions

Added 2026-08-02. The **GFS tab** holds one Graphical Flight Simulator session per course
day — 9 ground-school evenings and 7 simulator pre-briefs — because the device is where
switch geography, flows and avionics button-pushing get learned, not the full-motion sim.

Each session is time-boxed blocks. A block carries its duration, a cumulative clock window,
a checkbox per item, and the card ids that back it with a Drill button. Session progress
and per-item checks persist in the same `localStorage` record as the SRS state
(`state.gfs`, `state.gfsPick`). Program-view day rows gained a **GFS** button that jumps to
the matching session.

Three things worth not re-deriving:

1. **Check state is keyed to a 32-bit hash of the item TEXT**, not its index
   (`itemKey()` / `hash32()`). Reordering a session preserves progress; editing an item's
   wording resets that one item, which is the correct behaviour. Do not "simplify" this to
   an array index — that silently mismatches every check below an inserted item.
2. **`build.py` fails the build if any GFS block references a card id that doesn't exist.**
   A typo would otherwise render as a chip that drills nothing. Keep that check.
3. **The tab bar needed a `max-width: 430px` rule to fit five tabs.** It already overflowed
   at 375 px with four; a fifth pushed Reference off-screen. Adding a sixth tab means
   revisiting that media query.

Content standard: items are actions and checks, and values live in the cards rather than
being restated in the item text. That keeps the deck the single source of truth for every
safety-critical number. Follow it when editing `build/cards/gfs_sessions.json`.

`GFS Session Plan.md` at the repo root is the standalone prose version of the GND 1 session,
written before the in-app feature. Keep or drop it; the app is the live artifact.

## Course-day pointer

Added 2026-08-02, after I spent a session giving advice based on this file's own
write date and telling Derek to run the GND 1 session when he had already finished
GND 2. The schedule is deliberately keyed to course **day numbers**, not calendar
dates, so the app cannot infer where he is — and neither can you. It now asks.

`state.courseDay` holds a GFS session key (`'gnd2'`), not an index, so it survives
reordering. A select at the top of the GFS tab sets it. Effects:

- the GFS tab opens on that session by default (`state.gfsPick` still wins if set,
  so browsing away is not overridden)
- a hint line names the session to run and the next class day, and correctly says
  "That was the last one" at SIM 7 rather than inventing a next day
- the matching Program-view row gets a green **You are here** chip

**If a future session needs to know where Derek is in the course, read
`state.courseDay` or ask him. Do not infer it from dates in this file.**

## Global search

Added 2026-08-02, because Derek asked for a card search that already existed and he had
never found it. The Reference tab's box only appears once you are in that tab and only
narrows that one list, so it was effectively invisible. The fix was discoverability, not
new matching.

A **Search** button sits in the header on every tab (plus `/` on a keyboard). It opens a
full-screen overlay over one flat index of **658 entries** — 198 cards, 397 GFS items, 63
panel plates — built once at load from the same data the views use, so it cannot drift.

Every result does something rather than just reporting a match: a card offers **Drill**,
a GFS item **Open** (switches session, scrolls to the block, flashes it), a plate **View**
(opens the lightbox). Matching is multi-term AND over id, title, body, reference, block
and session titles, standard labels and panel chapters.

Three implementation notes:

1. **Highlighting stages marks as `\u0001`/`\u0002`, then swaps them for tags last.**
   Escape first, wrap after. Wrapping in real `<mark>` tags inside the per-term loop lets
   a later term match the letters of an earlier tag and corrupt the markup. Do not
   "simplify" this back to a direct tag replace.
2. **Results cap at 60 per group with a visible "N more" line.** A one-letter query
   matches most of the index; silent truncation would read as "that is all there is".
3. The Reference filter was left in place but relabelled to "Filter these 198 cards" so
   the two boxes are not mistaken for each other.

## Card divisions

Added 2026-08-02. `DIVISIONS` in the template splits the deck by provenance:

- **FSI Memory Flash Cards (87)** — what FSI actually issued, subdivided into
  **memory items (16)**, **normal procedure flows (5)**, **limitations (57)** and
  **aircraft general (9)**.
- **Supplementary (111)** — AFM Extended (65) and ACE Avionics (46), built here.

The memory-item / flow split inside the E- range is the one that matters: the AFM
red-boxes exactly 16 procedures (E-1..E-15 and E-20), and only those carry the verbatim
standard. E-16..E-19 and E-21 share the E- numbering because that is how FSI issued them,
not because they are memory items — see the E-16..E-21 note under Card sections.
`AGI-1..AGI-7` stay in the issued deck even though the content is ACE-derived, for the
same reason: FSI issued them there.

Surfaces in three places: Drill scope (optgrouped), Exam scope (each subdivision has its
own pass standard — 100% for memory items and limitations, 90% for flows and general),
and Program view as two phases at the bottom. Reference groups are relabelled
`FSI deck — …` and `Supplementary · …` so provenance is visible while browsing.

Three things worth not re-deriving:

1. **`DIVISIONS` must be declared before `EXAM_SCOPES`, `REF_GROUPS` and
   `renderScopeOptions`.** `EXAM_SCOPES` spreads it at module-evaluation time, so
   declaring it lower down throws a temporal-dead-zone error that kills the entire
   script — the page renders the tab bar and nothing else, with no console error to
   find. This happened once; the layout assert caught it.
2. **Exam scope keys `fsi`, `afm` and `ace` were kept** rather than renamed, so exam
   history recorded before the divisions existed still resolves to a label.
3. The old Drill scope label read `Full deck (87)` — a stale count from before the AFM
   and ACE cards existed. It now reads from `CARDS.length`.

## Completion standards

Added 2026-08-02. Every GFS item carries a **standard** — what the partner must observe,
and what advances you to the next item. Items are `{do, std[, crit]}`; `std` names one of
13 keys in `build/cards/standards.json`, each with `label`, `demo`, `gate` and `who`.

**The design decision worth defending: 13 shared standards, not 397 bespoke ones.** A
training standard that is worded differently for every item is not a standard — it drifts,
and two items of the same kind end up judged differently. Naming a shared standard means
every recall item is graded identically, and the standard can be improved in one place.
Item-specific criteria go in `crit` (19 of them, only where there is a hard number — the
five-minute MCT gate, the two-minute QPM gates, mask-donning times).

The 13: `brief`, `locate`, `recall`, `verbatim`, `flow`, `operate`, `identify`, `explain`,
`repeat`, `trap`, `swap`, `note`, `log`. `note` exists for lines that set how a block is
run and have nothing to demonstrate; `swap` for the other-seat repeats. Without those two,
those items get a standard they cannot meet.

Ten blocks also carry an `exit` — a stricter gate than "all items met their standard",
used where the block is a rehearsal for a named gate (GND 8's verbatim block, GND 6's
profile runs, SIM 3's fire drills).

Two things to know before editing:

1. **Check state is keyed on the item's `do` text**, so the string→object migration
   preserved every existing check. Verified: all 397 hashes unchanged. Keep hashing `do`.
2. `build.py` fails on an item missing `do`/`std`, or naming a standard that does not
   exist. A bad key would otherwise render an item with no criteria at all.

Badge colour follows the standard: `verbatim` red, `recall` amber, `note` dimmed, so the
hard items are scannable without expanding anything. The `s-<key>` class drives it — a new
standard gets the default grey unless you add a rule.

The classifier that assigned these lives in the scratch work, not the repo; it was a
one-time migration with ~70 hand corrections after review. Re-running it is not a thing you
should need to do — edit `gfs_sessions.json` directly.

## Panel plates

Added 2026-08-02. Each GFS block shows thumbnails of the annotated flight-deck plates
from the FSI Pilot Training Manual that cover the switches in that block — tap for a
full-resolution view with a fit/natural zoom toggle.

**Licensing.** Derek's FSI instructor cleared this on 2026-08-02: reproduction is
permitted **for personal training purposes and not for sale**. That is a narrower grant
than the flashcard text, which is why the condition is stated in the app footer, the
lightbox caption, and the README. Keep those notices on any new image work. The manual's
own front matter (p2–3) carries an FSI copyright notice and a US export-control notice;
the plates also contain the FlightSafety logo and third-party photo credits. Do not
extend this to a commercial or unattributed use without a fresh, wider permission.

How it fits together:

- `build/cards/panel_refs.json` — page, printed folio, chapter, title, and the card ids
  each plate serves. **This is the only hand-maintained mapping.**
- `build/render_panels.py` — renders `images/panels/ptm-<page>.webp` from the PDF at
  scale 2.0 / quality 80 (~91 KB each, 1584×1224). Needs the source PDF and a
  `pypdfium2` venv, so it is **not** part of a normal build. Output is committed, so
  `build.py` needs neither.
- `build.py` fails if a plate names an unknown card **or** its rendered image is missing,
  and writes `images/panels/index.json` for the service worker.

Three decisions worth not re-deriving:

1. **Plates attach to blocks through cards, not a second mapping.** `platesFor()` scores
   plates by how many of the block's cards they cover, takes the top 4. Add a plate with
   good card ids and it appears in every relevant block automatically.
2. **The service worker warms the images after `activate`, not in `install`.** Precaching
   5.6 MB would stall the update the user just tapped; leaving it to the runtime cache
   means an unopened plate is missing with no signal. `warmPanels()` walks
   `index.json` sequentially and swallows failures.
3. **Resolution beats file size here.** These are line-art plates whose callout labels are
   small; at scale 1.5 the switch legends stop being readable. 2.0 was the floor.

The PTM has ~140 further diagram pages that were not mined — mostly per-control close-ups
and synoptic-page state variations. `plate_index.json`-style detection lives in
`render_panels.py`'s sibling scratch work; the detector that found these looked for pages
whose non-boilerplate text is short with 2+ short title-case label lines.

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
| `build/cards/gfs_sessions.json` | **GFS session sources** — same rule; card refs and standard keys validated at build time |
| `build/cards/standards.json` | **The 13 completion standards** — edit here, not per item |
| `build/cards/panel_refs.json` | **Panel plate mapping** — page → cards; refs and image presence validated at build time |
| `build/render_panels.py` | Renders `images/panels/*.webp` from the PDF. Separate step — needs the PDF + a venv |
| `images/panels/` | 63 rendered plates + `index.json` for the service worker. Generated, but **committed** |
| `build/trainer.template.html` | App template; injected at the `__CARDS_DATA__`, `__GFS_DATA__`, `__PANELS_DATA__` and `__STANDARDS_DATA__` placeholders |
| `build/build.py` | Merges sources → `index.html`, `flashcards_data.json`, Anki deck. `--bump` increments `CACHE_VERSION` |
| `build/generate_{afm,ace}_cards.py` | The scripts that authored those card sets; keep for provenance and value citations |
| `index.html` | **Generated. Never hand-edit** — the next build overwrites it |

Verified 2026-08-02: `build.py` reproduces the deployed `index.html` byte-for-byte.

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

4. **Serving a local copy for browser testing needs a `.claude/launch.json` entry in the
   *working* directory plus `preview_start`.** Clean up that file afterwards — it is
   scratch, not project config. Three sandbox traps bite in sequence (all diagnosed
   2026-07-30, cost ~5 attempts):
   - `python3 -m http.server` dies at import: its argparse default calls `os.getcwd()`,
     which is **denied** in the preview subprocess. `sh -c 'cd … && …'` fails the same way.
   - `SimpleHTTPRequestHandler` then calls `os.getcwd()` **per request**, so it dies on
     every connection instead. Pass `directory=` explicitly via `functools.partial`.
   - The preview subprocess **cannot read the `Pilatus PC24` tree at all**, and a denied
     read surfaces as a plain **404**, not a permission error. Copy `index.html` into the
     scratchpad and serve *that*.

   Working recipe: a small server script in the scratchpad with
   `functools.partial(SimpleHTTPRequestHandler, directory=SCRATCH_SITE)`, `index.html`
   copied in beside it, and `launch.json` pointing `python3` at that script. Bonus: the
   copy has no `sw.js`, so the service-worker staleness in gotcha 1 cannot bite either.
   Note `navigator.serviceWorker` is `undefined` in that pane context, so the unregister
   snippet above throws there — it is only needed against a real deployed origin.

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
