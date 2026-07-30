# PC-24 Memory Trainer

A flashcard trainer and study schedule for the **Pilatus PC-24** — memory items, limitations, and aircraft general knowledge.

**198 cards** from three sources:

| Section | Cards | Source |
|---|---|---|
| Emergency · Limitations · Aircraft General | 87 | FlightSafety PC-24 Memory Flash Cards, Rev 1.0 (Mar 2026) |
| AFM Extended | 65 | Pilatus PC-24 EASA AFM, Report 02371, Issue 003 Rev 08 |
| ACE Avionics | 46 | Pilatus ACE™ (powered by Honeywell) PC-24 Avionics System Pilot's Guide, D201912000296-R002 Rev 2 |

Serial-dependent values are resolved for **MSN 631** (the MSN 501-up column).

## Use it

Open the site, then on iPhone tap **Share → Add to Home Screen**. It installs as a standalone app, works with no signal, and updates itself when a new card set is published.

Four tabs:

- **Program** — the FSI Pilot Initial syllabus: ground Days 1–9 matched to the topics taught each day, SIM 1–7 prep blocks, six gates, plus AFM and ACE topic blocks. Every row has a Drill button that loads exactly those cards
- **Drill** — flip cards with grading; misses re-queue immediately and return on a 1/3/7-day spaced-repetition schedule
- **Exam** — six syllabus gates (before GND 6 SIT, GND 8 SIT, the written test, SIM 3, SIM 4, SIM 7 LOS), plus FSI-deck, AFM-only, ACE-only, mock oral and whole-deck scopes — each with a pass standard and attempt history
- **Reference** — all 198 cards, searchable

Progress is stored in your browser's `localStorage`, so it stays on the device and never leaves it. Each install keeps its own record — drill in one place so your due-card schedule doesn't fragment.

## Study standards

Three kinds of material, three standards of recall:

| Material | Cards | Standard |
|---|---|---|
| Limitations | L-1–L-57 | Exact number and exact unit, every time |
| Emergency memory items | E-1–E-15, E-20 | Verbatim, in order, out loud |
| Flows & general | E-16–E-19, E-21, AGI-1–9 | Fluent — sequence and meaning correct |
| AFM Extended | AFM-1–AFM-65 | Working knowledge; not part of the memory-item standard |
| ACE Avionics | ACE-1–ACE-46 | Working knowledge — alerts, mode logic, reversion |

The AFM marks true memory items with a solid red box. There are exactly **16** in the manual and all 16 are already covered by the FSI Emergency cards — the AFM Extended set exists because the gap was in *limitations*, not memory items. E-16 to E-19 and E-21 are normal-procedure flows, not memory items.

## Files

| Path | What it is |
|---|---|
| `index.html` | The trainer — one self-contained file, all 198 cards inline |
| `PC-24 Memory Items Study Program.md` | Written study program: schedule, standards, memory anchors |
| `PC24_FSI_Flashcards_Anki.txt` | Anki import (tab-separated, tagged `PC24::Section`) |
| `flashcards_data.json` | Structured card data — the source for rebuilding `index.html` |
| `sw.js` | Service worker: offline caching and update prompts |
| `manifest.webmanifest` | Web app manifest for installation |

## Publishing an update

1. Edit the cards (`flashcards_data.json` and the `CARDS` array in `index.html`) or the schedule.
2. Bump `CACHE_VERSION` in `sw.js` — this is required. Without it, installed devices keep serving the old cache.
3. Bump the version stamp in `index.html` (the `#ver` span in the header) so you can confirm on-device which set you're running.
4. Commit and push. Installed apps show an "A newer card set is available" banner on next launch.

## Accuracy

Every card was transcribed from the source PDF and independently verified against it, field by field, with attention to numbers and units. One known source quirk: card E-21A prints "PDF" where it means "PFD" — corrected here.

**For training purposes only.** The AFM, current revisions, Service Bulletins, and applicable AFM Supplements are the authoritative source. Card content is FlightSafety International material, reproduced with instructor permission for training use.
