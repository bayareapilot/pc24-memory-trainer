# PC-24 Memory Items & Limitations Study Program

**Sources:** FlightSafety International PC-24 Memory Flash Cards, Rev 1.0 (Mar 2026) · Pilatus PC-24 EASA AFM Report 02371, Issue 003 Rev 08 (01 May 2025) · Pilatus ACE™ (powered by Honeywell) PC-24 Avionics System Pilot's Guide, D201912000296-R002 Rev 2 (Sep 2022)
**Aircraft:** MSN 631 — all serial-dependent values resolved to the **MSN 501-up** column
**Scope:** 198 cards — 87 FSI (21 Emergency E-1–E-21, 57 Limitations L-1–L-57, 9 Aircraft General AGI-1–AGI-9), 65 AFM Extended (AFM-1–AFM-65), 46 ACE Avionics (ACE-1–ACE-46)
**Course:** FSI Pilot Initial (FAA) — 9 ground school days (SIT on Days 6 and 8) then 7 simulator sessions, SIM 7 being the LOS. Class started 30 Jul 2026.
**Schedule basis:** keyed to **course day numbers**, not calendar dates

---

## How this program works

Three kinds of material live in this deck, and each needs a different standard of recall:

| Material | Cards | Standard |
|---|---|---|
| **Limitations** | L-1–L-57 | Exact number + exact unit, every time. "About 290" is a bust. |
| **Emergency memory items** | E-1–E-15, E-20 | **Verbatim, in order.** Say the step and the action, out loud, no hesitation. |
| **Flows & general** | E-16–E-19, E-21, AGI-1–9 | Fluent recall — sequence and meaning correct; wording can flex. |

**Daily cadence (35–45 min total):**
- **AM session (25–35 min):** New cards for the day. For each card: read the answer side once → cover it → recall out loud → check → repeat misses. For Emergency cards, also **write the flow out by hand** once — writing forces verbatim encoding.
- **PM session (10 min):** Review cards due today under the spacing schedule below.

**Spaced repetition schedule:** every new card comes back at **+1 day, +3 days, +7 days**, then weekly. The interactive trainer (see Tools, below) tracks this automatically; on paper, just re-drill each day's block on those offsets.

**Checkpoint rule:** don't advance past a checkpoint day until you hit its standard. Slipping one day is fine; slipping the standard isn't.

---

## The course, and where the deadlines actually fall

From the FSI Pilot Client Guide (Rev 1.0), Pilot Initial — FAA: **9 ground school days, then 7 simulator sessions.** SIT sessions fall on ground Days 6 and 8. The written test follows ground school (FSI standard 80% FAA, corrected to 100% — our card standard stays stricter: exact values).

That reshapes the plan. The schedule is now keyed to **course day numbers, not calendar dates**, because ground school may or may not run weekends — map GND 1–9 onto your own dates.

### Ground school — drill each evening what class covered that day

| Day | Syllabus topics | Your drill block |
|---|---|---|
| **GND 1** | Aircraft General · AFM/AOM | AGI-1–9, documents, kinds of operation, doors & exits, pax seating |
| **GND 2** | Avionics · **Master Warning** · Electrical | CAS levels + full aural priority order, display reversion, electrical limits |
| **GND 3** | Lighting · Flight Controls · Fuel | AFCS/FMA logic, SWPS/TFS/rudder bias, flap & airbrake limits, fuel system |
| **GND 4** | Gear & Brakes · Powerplant · Fire · Pneumatics · A/C · Pressurization | Biggest day — engine limit tables, QPM gates, fire drills, pressurization |
| **GND 5** | Oxygen · Ice & Rain · Waste · Pitot-Static | Oxygen limits, the 10 °C ice line, miscompare thresholds |
| **GND 6** | **SIT** — cockpit prep → shutdown | Start flows, ground idle gates, climb flow, QPM |
| **GND 7** | Performance · Avionics | Speed ladder, VO/VMCG/VMC/VMCL, TOLD advisory status, EGPWS modes |
| **GND 8** | **SIT** — normal / abnormal / **emergency** | All 21 emergency cards + emergency knowledge |
| **GND 9** | CRM/SRM · W&B · Flight planning · Windshear · Stalls (incl. UPRT) | Weights & CG for MSN 631, avionics limitations, TCAS, stall/SWPS |

### Simulator prep — drill the night before each session

| Session | What it introduces | Drill focus |
|---|---|---|
| **SIM 1** | Normal ops, steep turns, stalls, precision approach | Normal flows, speed limits, AP/FD basics |
| **SIM 2** | Engine failure incl. shutdown/restart, OEI, holding | Engine fail/start, fuel, electrical, AFCS abnormals, VMC/VMCL |
| **SIM 3** | **Fire drills, smoke, evacuation**, airframe icing, RTO | Fire and smoke memory items, icing limits, pitot-static |
| **SIM 4** | **Decompression, emergency descent max rate**, windshear, high-altitude stalls, GPWS | Cabin/pressurization, EDM, flight controls, gear, GPWS/TCAS |
| **SIM 5** | Fire and smoke to standard, powerplant failure on takeoff, OEI precision | Repeat fire/smoke/evac, full powerplant limits |
| **SIM 6** | Circling, no-flap landing, backup instrumentation | Flap limits, AFCS modes, FMS approach conditions |
| **SIM 7** | **LOS** — one simple correctable problem + one complex problem for the whole flight | Everything |

### The six gates

Each is an exam in the app, tied to the event that tests it:

| Gate | Standard | Why here |
|---|---|---|
| Before **GND 6 SIT** | 90% | Normal flows fluent before you fly the procedures walkthrough |
| Before **GND 8 SIT** | **100% verbatim** | First full emergency workout — this is the real memory-item deadline |
| Before the **written test** | 100% exact | Every limitation, FSI's own gate at end of ground school |
| Before **SIM 3** | 100% | Fire, smoke, evacuation, icing all get exercised |
| Before **SIM 4** | 100% | Decompression, emergency descent, flight controls |
| Before **SIM 7 LOS** | 95% | Whole deck, integrated |

### A correction to the earlier plan

The retired 7-day sprint front-loaded emergency memory items on my assumption that instructors quiz them from day one. The syllabus shows the real gate is **GND 8 SIT** — the first session that works normal, abnormal and emergency procedures together. Emergency items still matter early (each AST systems day covers that system's emergency procedures), but the hard 100%-verbatim deadline is Day 8, not Day 3.

That works in your favour: you already drilled the emergency core and remainder under the old plan, so you are ahead of the Day 8 gate rather than behind it.

## Memory anchors worth keeping

- **+440 lb rule** — every MSN 501-up weight limit is the early-serial value plus 440 lb.
- **The 2-minute engine** — QPM entry, QPM exit, and shutdown cooldown are all 2 minutes at ground idle.
- **29.5 VDC ceiling** — max voltage for GPU, generator, and battery charging alike.
- **10 °C is the ice line** — NAI required below it (with moisture), prohibited above it.
- **−40 °C cluster** — min fuel temp, min oil temp for start, HSDI caution threshold.
- **−54 °C cluster** — min OAT at sea level, min OAT for GPU start.
- **Masks first** — Cabin Altitude, Emergency Descent, and Smoke flows all begin with crew oxygen masks.
- **"Not primary"** — ACE charts, INAV map, Smart View, and VSD are all situational-awareness-only.
- **Span beats length** — 55'9" wingspan vs 55'2" length.

---

## AFM Extended — 65 additional cards (AFM-1 to AFM-65)

The AFM was cross-checked against the FSI deck. Two findings shaped this set:

**1. The FSI deck is complete on memory items.** The AFM marks true memory items with a solid red box around the challenge-and-response items. There are exactly **16** of them in the whole manual, and all 16 are already in your FSI Emergency cards:

| AFM procedure | FSI card |
|---|---|
| 3-BRKS-01 All Brakes Fail | E-1 |
| 3-ECS-01 Cabin Altitude | E-2 |
| 3-ECS-02 Cabin Pressure | E-3 |
| 3-ENG-02 L/R ENG Fail | E-4 |
| 3-FIRE-01 L/R Engine Fire | E-5 |
| 3A-NAA-08 Engine Hung Start | E-6 |
| 3A-NAA-07 Engine Hot Start | E-7 |
| 3A-NAA-18 SWPS Inadvertent Pusher | E-8 |
| 3-NAE-05 Engine Fire On-ground / Tail Pipe | E-9 |
| 3-NAE-06 Engine Fire or Failure During Takeoff | E-10 |
| 3-NAE-19 Rejected Takeoff | E-11 |
| 3-NAE-02 Emergency Descent | E-12 |
| 3-SMOKE-01 Smoke, Fire or Fumes | E-13 |
| 3-EVAC-01 Emergency Evacuation | E-14 |
| TCAS Resolution Advisory | E-15 |
| 3A-NAA-01 AFCS Abnormal Disconnect | E-20 |

The other five FSI Emergency cards (E-16 to E-19, E-21) are engine-start and climb **flows** from Section 4 Normal Procedures, not memory items. Worth knowing which is which: instructors expect the 16 verbatim, and the 5 flows fluently.

Note that **3-ENG-01 (dual engine failure) has no memory box** — its "Airspeed — As Required" step is deliberately not a memory item. Its 150 KIAS flaps-up glide speed is on card AFM-19 anyway, because you need that number.

**2. The real gap was limitations, not memory items.** AFM Section 2 carries far more than the 57 FSI limitation cards. The 65 new cards cover, by topic:

| Topic | Cards | Highlights |
|---|---|---|
| MSN 631 | 2 | Your weight and CG limits, no serial ambiguity |
| Airspeeds | 6 | **VO, VO RUDDER, VMCG, VMC, VMCL** — entirely absent from the FSI deck |
| AFCS | 4 | AP min 400 ft AGL / YD min 50 ft AGL after takeoff; AT override 3 sec; TCAS inhibit 1,100/900 ft |
| Powerplant | 11 | Full engine limit table, transients, oil pressure by N2, QPM's 7-gate list |
| Icing | 9 | WAI inhibits, flaps 15 in active icing, severe-icing visual cues |
| Flight controls | 3 | Airbrake stowed by 50 ft AGL; no flaps above 20,000 ft |
| Brakes & gear | 2 | 120-minute brake cooling rule |
| Fuel | 3 | Unusable quantity, defuel pressure, full grade list |
| Oxygen | 2 | Saver not below 25,000 ft; pax masks max 40,000 ft cabin |
| Cabin & loading | 4 | 66 lb baggage/cargo split, 1,800 lb straps, seating by config |
| Electrical | 2 | 32 V charge ceiling; CB reset rules |
| Emergency knowledge | 4 | Airstart ≤150 KIAS on battery; second extinguisher green "2" |
| General ops | 13 | Land ASAP vs practical, RVSM, FMS approach conditions, wet runway |

**How to use them:** these are *not* required for your checkride memory-item standard, so they don't touch the 7-day schedule. Drill them by topic from the Program tab's Extended section once the FSI deck is solid — or pull a topic the night after class covers that system. Exam has an "AFM Extended only" scope and an "Everything" scope (152 cards).

Every value was verified against the AFM: 258 numeric tokens checked for presence and 55 label-value pairings confirmed in context.

## ACE Avionics — 46 cards (ACE-1 to ACE-46)

The Honeywell ACE Pilot's Guide is 2,131 pages, almost all of it page-by-page operating detail that belongs in a lookup reference, not in memory. These cards deliberately cover only what you must recall **in the seat** — alerts, annunciations, mode logic, protections, and reversion. Menu navigation is excluded on purpose.

Why a separate section rather than folding into AFM Extended: different source and different authority. The AFM carries approved limitations; the Pilot's Guide describes system behaviour. Keeping them apart means an examiner's "what's the limit?" and "what will the box do?" stay distinct in your head.

| Topic | Cards | Why it earns a card |
|---|---|---|
| Alerting & aurals | 8 | CAS colour/chime/light logic, and the **aural priority order** — STALL is group 1 priority 1 and outranks everything |
| AFCS & modes | 7 | FMA green/white logic, AP and YD interlocks, AP control and overpower limits, TCS |
| Automation protections | 11 | **EDM**, SWPS, tactile feedback bank thresholds, rudder bias, autothrottle takeoff window |
| Display failure & reversion | 7 | **DU failure vs AGM failure** — the guide calls this distinction essential |
| Data integrity | 3 | Miscompare thresholds: IAS 10 kt, ROLL 6°, PITCH 5°, ALT 200 ft, BARO 0.02 inHg |
| TCAS | 5 | Aurals, corrective vs preventive RAs, why traffic you can see may not appear |
| EGPWS / TAWS | 5 | Mode 1/3/6 behaviour, the callout ladder, terrain caution vs warning |

**The three highest-value items in this set:**

1. **X on two displays is one AGM failure, not two dead screens.** AGM 1 drives DU 1 and 2; AGM 2 drives DU 3 and 4. A large X means the display works but is receiving no image data. Fix: rotate the circular collar around the affected side's PFD dimmer to the alternate AGM, then turn the still-useless DU past its detent to OFF/REV.
2. **EDM needs all three: depressurization, above 30,000 ft, autopilot on.** It then turns 90° **left**, engages the autothrottle, idles the thrust, and descends at VMO to 15,000 ft, ending in heading mode at 175 kt. The AP QD button cancels EDM but does **not** disconnect the autothrottle.
3. **The cavalry charge has exactly two mute buttons** — an AP quick-disconnect or the AP button on the Flight Controller. Master Caution and Master Warning will not silence it. Continuous cavalry charge means the aircraft dropped the autopilot; a single one means you did.

Note that AGI-1 to AGI-7 in the FSI deck (display unit colour conventions) are already ACE-derived — they came from the same Honeywell guide. I left them in the FSI section so your checkride deck numbering stays exactly as FlightSafety issued it.

Verification: 52 numeric tokens confirmed present in the Pilot's Guide text and 70 label-value pairings confirmed in context.

## What this program does *not* cover

Systems theory, non-memory QRH procedures, performance charts, and ACE page-by-page operation (flight planning entry, chart manipulation, datalink menus, radio tuning pages, SATCOM). Pair this with the FSI PC-24 Pilot Training Manual and QRH review — the limitations anchor much faster once each number is attached to the system it protects.

*Values transcribed from the FSI card set Rev 1.0, AFM Report 02371 Issue 003 Rev 08, and ACE Pilot's Guide D201912000296-R002 Rev 2. For training purposes only — the AFM, current revisions, Service Bulletins, and applicable AFM Supplements remain the authoritative source. Card content is FlightSafety International and Pilatus material, reproduced with instructor permission for training use.*
