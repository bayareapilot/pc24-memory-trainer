# GFS Session Plan — after GND Day 1

**Session:** evening of course Day 1 · two pilots, swap seats halfway
**Built:** 2026-07-30 · card IDs refer to the PC-24 Memory Trainer deck
**Aircraft:** MSN 631 (MSN 501-up column for every serial-dependent value)

---

## What the GFS is for, and what it isn't

The Graphical Flight Simulator earns its keep on **switch geography, flow sequence,
checklist discipline, and avionics button-pushing**. Those are exactly the things that
eat sim time later if you arrive not knowing them.

It is **not** worth spending tonight on handling, hand-flying, crosswinds, or emergency
memory items "to standard." No motion, no real control feel, and the emergency gate is
GND 8 — tonight is too early to be drilling E-1..E-15 for score. Locate the switches
those drills use, then stop.

**Rule for the night: nobody hunts for a switch twice.** If either of you has to search
for something, stop, both of you touch it, name it out loud, and move on.

---

## Pre-brief with your partner — 5 min

Agree these before you power anything up, or you'll drift into two people
independently pushing buttons:

1. **Roles.** One flying, one monitoring and reading the checklist. Not "both poking."
2. **Swap point.** Halfway. Whoever starts in the right seat gets the left seat for the
   second pass — the start flow (E-16/E-17/E-18) is asymmetric and you both need it
   from both seats.
3. **Challenge-and-response out loud, every time.** Silent button-pushing builds a habit
   you'll have to unlearn at the GND 6 SIT.
4. **Call the trap, don't just avoid it.** When one of you catches the other's error,
   say what the trap was. That's the part that sticks.

---

## Block 1 · Cockpit geography — 25 min

No procedures yet. Pure "where is it," partner calling items at random.

- Overhead / IPS rotary · engine start switches · START buttons · booster pumps
- Fuel crossfeed · GEN 1 / GEN 2 · battery master · GPU
- Flight Controller buttons (you'll need these cold for EDM — ACE-18)
- AP / YD engage, **AP Disengage switch on both wheels** (E-20 step 2), TCS
- Flap lever and detents · airbrake · gear lever
- Guarded/emergency handles: emergency brake, engine fire handles, evacuation
- Transponder panel (ACE-39 — why never STBY on the ground)

**Drill it as a quiz, not a tour.** Partner reads a switch name, you put a finger on it
without narrating the search. Then reverse. Do the list twice — the second pass is where
the time savings actually come from.

While you're here, verify the **DU colour conventions against the real screens**
(AGI-1..AGI-7). Seeing red/amber/magenta/cyan/green/white/grey on an actual display
locks those in far better than the card does.

Also worth eyeballing now, since it's a Day 1 topic: doors, exits, and the internal
emergency exit security pins (L-33) — and the engine danger areas (AGI-9), which you
can't see in a GFS but should say out loud while you're thinking about the airplane.

---

## Block 2 · Displays and CAS — 25 min

This is the single best use of a GFS and most people skip it.

**Display architecture and reversion** — ACE-27 through ACE-33:
- Which AGM drives which DUs; how many unique images one AGM can produce (ACE-27)
- **Tell a DU failure from an AGM failure** (ACE-28) — the guide calls this essential
- Single DU failed → corrective action (ACE-29)
- DU 1 *and* 2 both showing a large X → actions **in order** (ACE-30)
- Two DUs failed and off → what appears where, for each pair (ACE-31)
- "Check Pilot PFD" / "Check Copilot PFD" / "Check Engine Display" (ACE-33)

Actually *do* the reversion selections if the GFS supports failures. Reading ACE-30 and
performing ACE-30 are different skills.

**CAS system** — ACE-1 through ACE-8:
- Warning / Caution / Advisory / Status: colour, master light, aural (ACE-1)
- Sort order, ordering within a colour group, how many messages display (ACE-2)
- Aural priority when two fire at once, and what's **always first** (ACE-3)
- Walk the priority ladder aloud (ACE-4, ACE-5, ACE-6)
- **Mute an uncommanded AP disconnect** — and what will *not* mute it (ACE-7)
- How EGPWS/TCAS aurals interleave with CAS; TAWS + TCAS together (ACE-8)

**Miscompares** (ACE-34, ACE-35, ACE-36): thresholds for IAS?/ROLL?/PITCH?, how RAD? is
computed and how long it must persist, and how the PFD shows *invalid* data versus a
miscompare. Trigger them in the GFS if you can.

---

## Block 3 · Power-up → start → ground idle — 30 min

Run it as a real flow, checklist in hand, challenge-and-response.

**Cockpit prep and power-up.** GPU voltage check before connecting (L-34), GPU limits
(L-35), battery minimums for start (L-18, L-36), battery temperature limits (L-38).

**RH engine start — E-16, then E-17:**
1. R Engine switch → RUN
2. Confirm R booster pump running, **no FUEL PRESSURE CAS messages**
3. R START — press
4. "START" appears ON on the PFD
5. ~10% N2 — START and IGN in inverse video; **check N1 increasing**
6. Observe light-up and parameters to IDL
7. START and IGN extinguish ~45–50% N2 (ambient dependent)

**Ground idle values — E-19.** Say the targets before you look at the gauges, then
compare: N1 25%, ITT 400 °C, N2 min 53.4%, FF 160–180 lb. **Confirm GEN 2 takes over and
is supplying the aircraft.** And the note that bites people: TAT or reported OAT below
10 °C with visible moisture → IPS rotary to AUTO/NAI.

**LH engine start — E-18. This is tonight's sequencing trap:** the right engine must
**exit QPM and be set to Ground Idle before** you start the left. Have your partner try
to walk you into starting the left engine with the right still in QPM, and catch it.

**QPM gates while you're here** — L-19, L-20, L-21, L-22. Remember the *2-minute engine*
anchor: QPM entry, QPM exit, and shutdown cooldown are all 2 minutes at ground idle.
State each from memory, then confirm.

Start limits worth reciting in the seat: start attempt / dry motor run / second attempt
(L-15), tailwind and crosswind for start (L-16), minimum time between starts and max time
to light-off (L-17).

---

## Block 4 · Taxi, takeoff, climb flow — 20 min

- **Taxi:** you taxi by outside reference, not by chart symbol (L-50, L-51, L-52). Say it
  out loud in the seat — it's an easy written-test item and a real-world trap.
- **Transponder:** not STBY on the ground; what to select instead (ACE-39). TCAS test and
  arm, and what it does while still on the ground (ACE-40).
- **Thrust:** normal takeoff thrust vs Automatic Thrust Reserve (L-14); auto-rating types
  and how many can be active at once (ACE-15). AT takeoff monitor protection band (ACE-25).

**CLIMB flow — E-21, run it clean:**
1. **Gear — UP** · confirm lever up and lights out on the System Summary Page
2. **Yaw Damper — ON** · confirm on the FMA
3. **Flaps — UP** · confirm lever at 0 and indication on the System Summary Page
4. **Thrust — MCT** · levers back to the MCT gate **within five minutes** of setting T/O;
   verify MCT on **both** engine PFD indications

Note how much of that flow is *confirm on a specific display page*. That's the half people
lose under load, and it's the half a GFS can actually teach you.

Speed and config limits to call while flying it: VMO/MMO (L-1), flap speeds (L-6),
VLO/VLE (L-28), max tire speed (L-29).

---

## Block 5 · Autopilot, FMA, and the abnormal disconnect — 15 min

- Where lateral vs vertical FD modes live; ACTIVE vs ARMED colours (ACE-9)
- AP annunciator meanings — green AP, amber TCS, red flashing AP (ACE-10)
- **Three normal ways to manually disengage the AP**, and what engaging AP also engages
  (ACE-11)
- Disengaging the YD and what it does to the AP; above 30,000 ft (ACE-12); YD prohibition
  altitude (L-42)
- Press-and-release TCS with AP engaged (ACE-14) — do it, don't just read it
- AP operational limits: crew seated and belted (L-39), AP/YD off for takeoff and landing
  (L-40), minimum disengage altitudes by approach type (L-41)

**Then E-20, AFCS Abnormal Disconnect.** This one *is* worth running tonight, because it's
the memory item most about hands and switch location:
1. Control wheel — grasp firmly, regain control
2. AP Disengage switch — press to cancel the aural (either wheel)
3. Aircraft — retrim manually as necessary
4. If no AFCS-associated CAS messages: attempt to re-engage **once**

Flashing red AP plus continuous Cavalry Charge. Have your partner fire it while you're
mid-sentence on something else.

---

## Block 6 · Locate-only pass on emergency controls — 10 min

**Touch, name, move on. Do not run these to standard tonight.**

Engine fire handles (E-5) · emergency brake (E-1) · crew oxygen masks — all three of
Cabin Altitude, Emergency Descent and Smoke start with masks (E-2, E-12, E-13) ·
evacuation controls (E-14) · Flight Controller buttons for EDM and the four ways to
cancel it (ACE-16, ACE-17, ACE-18).

Goal is only that at the GND 8 SIT your hands already know where these live, so you can
spend that session on the words instead of the geography.

---

## Swap seats, then second pass — abbreviated

Other pilot flies. Cut to: power-up → both starts → ground idle → taxi → climb flow →
one E-20. Skip the Block 1 quiz if the first pass went clean.

---

## Debrief — 5 min

Three lists, written down:

1. **Switches either of you hunted for.** Straight into tomorrow's review.
2. **Flow steps that came out wrong or out of order.** Those are card drills tonight.
3. **Questions for your instructor tomorrow.** GFS behaviour that didn't match the cards
   is worth asking about — the GFS is a training device and is not always faithful.

---

## If you only get an hour

Blocks 1, 2, and 3. Cockpit geography, displays/CAS, and the start sequence. Those three
have the highest payoff per minute and the least overlap with what the sim will teach you
anyway.

---

## Card blocks to drill after, while it's fresh

| Cards | Why tonight |
|---|---|
| AGI-1..AGI-7 | You just saw the colours on real screens |
| E-16, E-17, E-18, E-19 | Start flow, in the seat, both seats |
| E-21 | Climb flow |
| E-20 | Ran it live |
| ACE-1..ACE-8 | CAS and aural priority |
| ACE-27..ACE-36 | Displays, reversion, miscompares |
| L-15..L-22 | Start and QPM gates |
| L-34..L-38 | Ground power and battery |

Reminder on the real deadlines: **gate-normal before the GND 6 SIT (90%)**, and
**gate-emer before the GND 8 SIT (100% verbatim)** — that second one is the memory-item
deadline, not Day 3.

---

*For training purposes only. Derived from FlightSafety International PC-24 Memory Flash
Cards Rev 1.0, Pilatus PC-24 AFM Report 02371, and the Pilatus ACE™ Avionics Pilot's
Guide. Not a substitute for approved manuals or checklists.*
