# PC-24 Memory Items & Limitations Study Program

**Sources:** FlightSafety International PC-24 Memory Flash Cards, Rev 1.0 (Mar 2026) · Pilatus PC-24 EASA AFM Report 02371, Issue 003 Rev 08 (01 May 2025)
**Aircraft:** MSN 631 — all serial-dependent values resolved to the **MSN 501-up** column
**Scope:** 152 cards — 87 FSI (21 Emergency E-1–E-21, 57 Limitations L-1–L-57, 9 Aircraft General AGI-1–AGI-9) plus 65 AFM Extended (AFM-1–AFM-65)
**Program length:** 7-day compressed track (active) + AFM Extended topic blocks, drilled any time

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

## Phase 1 — Limitations foundation: the hard numbers (Days 1–6)

The goal this week is the numeric backbone of the airplane. These respond best to *clustering* — learn the pattern, not 57 isolated facts.

### Day 1 — Speeds (L-1, L-28, L-29, L-30)
Build the speed ladder top-down:
- **290 KIAS / 0.74 M** — VMO/MMO (crossover 28,230 ft)
- **250 KIAS or 0.74 M (lower)** — VLE and VLO extend
- **200 KIAS** — VLO retract, VFE 8° and 15°
- **175 KIAS** — VFE 33°
- **180 KIAS** — VLO extend with EGES (*QRH emergency extension procedure itself wants ≤160*)
- **165 kt GS** — max tire speed

### Day 2 — Weights, loading, load factors (L-2, L-3, L-4, L-5, L-6)
Master pattern: **every MSN 501-up weight = the MSN 101–500 weight + 440 lb.**
- MZFW 14,220 → 14,660 · Ramp 18,400 → 18,840 · MTOW 18,300 → 18,740 · MLW 16,900 → 17,340 · Max cargo 2,500 → 2,940
- Baggage nets: small **400 lb** / large **530 lb**. Floor: **100 lb/ft²** panels, **670 lb/ft** seat rails.
- Load factors: **+3.0/−1.2 g** flaps up; **+2.0/0.0 g** flaps down.

### Day 3 — Envelope & airport (L-7, L-8, L-9, L-10, L-11) · review Days 1–2
- **45,000 ft** max operating altitude · OAT at sea level **−54 °C to +50 °C**
- **8 passengers** max (Executive interior, incl. two optional infant fits)
- Runway slope **±2%** · dry/wet paved (contaminated & unpaved per AFM supplements) · tailwind **10 kt** · pressure altitude **−1,000 ft** to **10,000 ft** landing field elevation

### Day 4 — Engine & starter (L-12 through L-22) · review Day 3
Biggest single block — 11 cards. Sub-clusters:
- **Identity:** 2 × Williams FJ44-4A QPM · takeoff thrust **3,420 lb**, ATR **3,600 lb** · oil not below **ADD** mark
- **Starter duty cycle:** 50 s ON / 1 min OFF (attempt 1 and dry motor) → attempt 2: 50 s ON / **30 min OFF**. Abort if N1 hasn't risen by **25% N2**.
- **Start limits:** tailwind **20 kt** / crosswind **25 kt** · **60 s** between starts · light-off within **12 s** · Ni-Cad **22.0 V** (BAT 1) / **23.5 V** (BAT 2), Li-Ion both SOC green · min oil temp **−40 °C**
- **The two-minute engine:** post-start oil temp **+10 °C** before N2 > 80% or QPM · QPM only after **2 min** stabilized ground idle, and **2 min** ground idle after QPM before shutdown/thrust · cooldown **2 min** idle before shutdown
- **QPM box:** stationary + park brake ON, thrust lever IDLE, gen load ≤ **250 A**

### Day 5 — Fuel & oxygen (L-23–L-27, L-49) · review Day 4
- Total **895 gal / 5,999.8 lb** · usable **890 gal / 5,964 lb** · max imbalance **49 gal / 330 lb**
- Fuel temp **−40 °C to +80 °C** · pressure refuel max **60 PSI** · booster pumps + crossfeed must be **operative** · grades: **Jet A, Jet A-1, JP-8, TS-1**
- Oxygen: **680 L** min dispatch · **10 min** per occupant above FL250

### Day 6 — **Checkpoint 1.** Full pass of Days 1–5 (31 cards). Standard: **≥ 90%**, misses re-drilled to 100% before stopping.

---

## Phase 2 — Systems & operational limitations (Days 7–12)

### Day 7 — Electrical (L-34, L-35, L-36, L-37, L-38)
Cluster by ceiling: **29.5 VDC is the max everywhere** (GPU supply, battery charge, generator).
- GPU: > battery voltage to connect · 25.0–29.5 VDC · **1,200 A** surge / **450 A** continuous · min 24.0 V for start · 28.0–29.5 V to charge batteries · min OAT −54 °C
- Generator: **400 A** (ground idle & flight), **250 A** in QPM
- Battery: min temp for flight **0 °C** · Ni-Cd min **−20 °C**, Li-Ion min **−5 °C** · start volts same as Day 4 · charge rate before takeoff: BAT 1+2 **< 50 A and decreasing**

### Day 8 — Cabin & AFCS (L-31, L-32, L-33, L-39, L-40, L-41, L-42)
- Pressurization: **9.27 psid** max / **−0.3 psid** negative / **0.7 psid** takeoff & landing
- **1 person** on the airstair · emergency-exit security pins **removed and stowed**
- AP: pilot **seated, belt fastened** · AP & YD **OFF for takeoff and landing** · **no YD-off flight above 30,000 ft**
- Minimum AP altitudes: **1,000 ft AGL** general · **400 ft AGL** non-precision/circling/visual (<150 KIAS, VS <1,500 fpm) · **200 ft AGL** VGP and coupled ILS (GS < 4.5°)

### Day 9 — Icing (L-43, L-44, L-45, L-46, L-47, L-48)
- Severe icing: freezing rain/drizzle/mixed can exceed the **ice protection system** — recognize and exit
- AP in icing: **periodically disengage** to feel for abnormal forces
- **NAI ON — ground/takeoff/landing:** visible moisture + SAT/OAT < 10 °C, or ice adhering to engine inlet
- **NAI ON — climb/cruise/descent:** visible moisture TAT < 10 °C, ice crystals, or any airframe accretion
- NAI never when TAT > 10 °C or in QPM; ON **before setting takeoff power**
- HSDI: not recommended TAT < −40 °C unless needed; if used ≤ −40 °C → **boot inspection + functional test** before takeoff

### Day 10 — Avionics & displays (L-50 through L-57)
One idea covers five cards: **nothing on the MFD replaces primary navigation** (ACE charts, INAV map, Smart View, VSD — all "not primary"). Plus:
- Weather radar prohibited: in hangar, during fueling, personnel within safe distance ±60° of the nose
- FMS: **ILS, LOC, LOC-BC, LDA, SDF, MLS approaches prohibited** via FMS

### Day 11 — Aircraft General (AGI-1 through AGI-9)
- **DU colors** (these are the CAS logic you'll live with): Red = warning/limits · Amber = caution/invalid/miscompare · Magenta = FD-coupled/active plan · Cyan = advisory/crew-selected · Green = engaged/on · White = armed/standby/status · Gray = legends/structure
- Dimensions: length **55 ft 2 in** · height **17 ft 4 in** · wingspan **55 ft 9 in** (span > length!)
- Danger areas: **20 ft** forward radius · start **60 × 36.7 ft** aft · max thrust **286 × 125.7 ft** aft

### Day 12 — **Checkpoint 2.** All Limitations + AGI (66 cards). Standard: **≥ 90%**, then re-drill misses to 100%.

---

## Phase 3 — Emergency memory items (Days 13–18)

**Standard is different here: 100%, verbatim, out loud, in order.** Method for every card: read once → write the flow by hand → say it standing up (simulated cockpit scan helps anchor it) → drill until three clean consecutive recitations.

### Day 13 — Fire & rejected takeoff (E-5, E-9, E-10, E-11)
- **Engine Fire in flight (E-5):** Confirm → Thrust lever IDLE → Engine switch OFF/STOP → ISOL push (check ENGINE ISOLATED CAS after 5 s, green "1") → if fire persists, EXTINGUISHER push. Pitch/bank ±10° for extinguisher effectiveness.
- **Engine fire on ground / tailpipe (E-9):** Identify/IDLE → ENG switch OFF → ISOL push → FIRE XTING push
- **Fire/failure during takeoff (E-10):** below V1 → reject. At/above V1 → thrust fully forward (ATR), rotate 9° ANU, ≥ V2, gear up with positive rate
- **Rejected takeoff (E-11):** thrust IDLE → max braking. Caution: kill the autothrottle (AT DISC or hold idle 2–3 s).

### Day 14 — Pressurization & smoke: the "masks first" family (E-2, E-3, E-12, E-13)
Pattern: **crew masks are step 1** in Cabin Altitude, Emergency Descent, and Smoke/Fumes.
- **Cabin Altitude (E-2):** crew masks don/100%/comm → pax oxygen ON, don masks → if rapid/explosive decompression, Emergency Descent
- **Cabin Pressure (E-3):** excessive negative differential in flight → reduce descent rate
- **Emergency Descent (E-12):** masks → pax O₂ ON → belts ON → thrust IDLE → airbrakes OUT
- **Smoke/fire/fumes (E-13):** crew mask don / **EMGCY** / vent open → goggles → pax O₂ ON → **land ASAP / divert**

### Day 15 — Ground malfunctions (E-1, E-6, E-7, E-14)
- **Hung start (E-6):** fails to accelerate > 30 s → engine switch OFF
- **Hot start (E-7):** ITT racing toward 1,000 °C, or hanging 900–1,000 °C for 15 s → engine switch OFF
- **All brakes fail, taxi (E-1):** use wheel brakes and EMER brake if anything is left
- **Evacuation (E-14):** park brake set → notify ATC → both engines OFF

### Day 16 — Automation & flight controls (E-4, E-8, E-15, E-20)
- **Engine fail indication (E-4):** N1 drop 15% in 0.5 s (activates ATR on takeoff) → monitor/confirm engine instruments
- **SWPS inadvertent pusher (E-8):** hold against pusher → **press and hold AP disconnect continuously**. Warning: no natural stall protection with pusher inop — avoid stalls.
- **TCAS RA (E-15):** yoke quick-disconnect if AP on → comply immediately with RA on PFD → tell ATC → return to assigned altitude when clear
- **AFCS abnormal disconnect (E-20):** grasp wheel, regain control → press AP disengage to cancel cavalry charge → retrim → re-engage **once** if no AFCS CAS messages

### Day 17 — Flows (E-16, E-17, E-18, E-19, E-21)
- **RH engine start** (rotate RUN → booster pump, no FUEL PRESSURE CAS → START) and monitoring sequence (START on PFD → ~10% N2 START+IGN inverse video, N1 rising → light-up → IDL → START/IGN out ~45–50% N2)
- **LH start:** RH engine must exit QPM to ground idle first
- **Ground idle gates (E-19):** N1 ~25% · ITT ~400 °C · N2 min 53.4% · FF 160–180 lb · GEN 2 takes over. TAT/OAT < 10 °C + moisture → IPS to AUTO/NAI.
- **Climb flow (E-21):** gear up (lights out) → YD on (FMA) → flaps 0 (summary page) → MCT within 5 min of setting T/O
- PM: re-run Days 13–14 emergency cards.

### Day 18 — **Checkpoint 3.** All 21 Emergency cards, **100% verbatim**. Anything short of word-perfect gets re-written by hand and re-drilled same day.

---

## Phase 4 — Integration & overlearning (Days 19–21)

- **Day 19:** Full-deck shuffle drill, all 87 cards mixed. Flag every hesitation, not just every miss.
- **Day 20:** Weak-card intensive (flagged cards ×3 spaced through the day) + **mock oral**: have someone read card fronts cold — or use the trainer's Exam mode — covering ~30 cards across all sections.
- **Day 21:** Final check: Limitations **100%**, Emergency **100% verbatim**, AGI fluent. Then drop to maintenance.

**Maintenance until class:** 10 min/day on due cards; one full-deck pass the day before training starts. The last pre-class pass matters more than any single day in the program.

---

## Compressed 7-day schedule — **ACTIVE PLAN** (class starts Thu Jul 30, 2026)

With class starting tomorrow, the order flips: **emergency memory items come first** — instructors quiz memory items and limitations from day one, and the sim sessions arrive before the oral does. Limitations blitz lands on the weekend when there's more time.

| Day | Date | Material | Time |
|---|---|---|---|
| 1 | **Wed 7/29 — tonight** | Emergency core: fire & RTO (E-5, E-9, E-10, E-11) + masks-first family (E-2, E-3, E-12, E-13) + speed ladder (L-1, L-28, L-29, L-30). Write each emergency flow by hand once. | ~90 min |
| 2 | Thu 7/30 · class day 1 | Emergency remainder: ground malfunctions (E-1, E-6, E-7, E-14) + automation (E-4, E-8, E-15, E-20). Re-drill Day 1 misses first. | 45–60 min |
| 3 | Fri 7/31 | Start & climb flows (E-16–E-19, E-21) + weights (L-2–L-6, the +440 rule). Finish with **Checkpoint 3** (all 21 Emergency) — goal ≥90% tonight. | ~60 min |
| 4 | Sat 8/1 | **AM:** engine & starter (L-12–L-22) + envelope & airport (L-7–L-11). **PM:** fuel & oxygen (L-23–L-27, L-49) + electrical (L-34–L-38). Re-run Checkpoint 3 → **100% verbatim**. | 2 × 60–75 min |
| 5 | Sun 8/2 | **AM:** cabin & AFCS (L-31–L-33, L-39–L-42) + icing (L-43–L-48). **PM:** avionics (L-50–L-57) + AGI (AGI-1–9). Finish with **Checkpoint 1** (36 limitations). | 2 × 60–75 min |
| 6 | Mon 8/3 | No new cards. **Checkpoint 2** (all Limitations + AGI, 66 cards) ≥90%; drill every miss to clean; one emergency verbatim re-pass. | 45–60 min |
| 7 | Tue 8/4 | **Final check** (full 87) + mock oral. Limitations exact, emergency 100% verbatim. Then drill "Due today" to zero. | 45–60 min |

From Aug 5 on: 10 minutes of due-card review every evening for the rest of class. If class runs the weekend, split each Sat/Sun block into that evening + the next morning. Where possible, drill each system's limitation cards the same evening class covers that system — the numbers stick faster with the system fresh.

---

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

## What this program does *not* cover

Systems theory, non-memory QRH procedures, performance charts, and avionics operation. Pair it with the FSI PC-24 Pilot Training Manual and QRH review — the limitations anchor much faster once each number is attached to the system it protects.

*Values transcribed from the FSI card set Rev 1.0 and AFM Report 02371 Issue 003 Rev 08. For training purposes only — the AFM, current revisions, Service Bulletins, and applicable AFM Supplements remain the authoritative source. Card content is FlightSafety International and Pilatus material, reproduced with instructor permission for training use.*
