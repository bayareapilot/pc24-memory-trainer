"""Build the ACE avionics card set (ACE-1 ... ACE-n).

Source: Pilatus ACE(TM) (Advanced Cockpit Environment, powered by Honeywell) for
the PC-24 Avionics System Pilot's Guide, Honeywell Pub. No. D201912000296-R002,
Revision 2, September 2022.

Scope choice: alerting, annunciation, mode logic, protections, display reversion
and data-integrity thresholds — the things a pilot must recall in the seat.
Menu navigation and page-by-page procedures are deliberately excluded; those are
lookup material, not recall material.
"""
import json

C = []
n = 0


def card(title, front, back, ref, topic):
    global n
    n += 1
    C.append({'id': f'ACE-{n}', 'title': title, 'front': front,
              'back': back, 'reference': ref, 'topic': topic})


T_ALERT = 'Alerting & aurals'
T_AFCS = 'AFCS & modes'
T_PROT = 'Automation protections'
T_DISP = 'Display failure & reversion'
T_DATA = 'Data integrity'
T_TCAS = 'TCAS'
T_TAWS = 'EGPWS / TAWS'

# ----------------------------------------------------- Alerting & aurals
card('CAS Message Levels — Colour, Light and Chime',
     'For each CAS level state the colour, whether a master light illuminates, '
     'and the aural:\n1. Warning — ?\n2. Caution — ?\n3. Advisory — ?\n4. Status — ?',
     '1. WARNING — RED · master WARNING button lights · TRIPLE CHIME · posted in red '
     'reverse video until a master warning button is pushed, then red text on black\n'
     '2. CAUTION — AMBER · master CAUTION button lights · SINGLE CHIME · amber reverse '
     'video until acknowledged, then amber text on black\n'
     '3. ADVISORY — CYAN · no light, no chime · cyan reverse video for 5 seconds, then '
     'automatically to cyan on black\n'
     '4. STATUS — WHITE · no light, no chime · white reverse video for 5 seconds, then '
     'automatically to white on black\n'
     'Pushing a master button silences the chime and drops the reverse video — that is '
     'what "acknowledged" means.',
     'ACE Pilot\'s Guide 8-6 to 8-8', T_ALERT)

card('CAS Window — Sort Order and Capacity',
     '1. In what order are CAS messages sorted — ?\n'
     '2. How are messages ordered within a colour group — ?\n'
     '3. How many messages display at once — ?\n'
     '4. Can the pilot clear a message — ?',
     '1. RED at the top, then AMBER, then CYAN, then WHITE\n'
     '2. Newest at the top of each colour group, oldest at the bottom\n'
     '3. As many as 12 at one time. With 12 or fewer, no manipulation is needed\n'
     '4. NO — the pilot cannot directly remove a message from the CAS stack. A message '
     'stays until the condition clears (or the CAS system removes it on a configuration '
     'change)\n'
     'When no messages are active, "CAS" is displayed on the top line. The CAS window is '
     'a high-priority window and is ALWAYS visible — on a composite PFD it moves to the '
     'bottom of the display, below the HSI.',
     'ACE Pilot\'s Guide 8-2 to 8-8', T_ALERT)

card('Aural Warning Priority — How Conflicts Resolve',
     'Two or more aural warnings are active at once. How does the system decide what '
     'you hear, and what is always first?',
     'Aurals are assigned to GROUPS by importance and urgency, and given a PRIORITY '
     'NUMBER within the group. ALL warnings from the most important group are presented '
     'first, in priority order. Warnings from the next group are not presented until no '
     'warnings from the more important group remain active.\n'
     'STALL is group 1, priority 1 — it outranks everything and is NOT mutable. It '
     'persists until the stall condition is corrected.\n'
     'Worked example from the guide: with stall, speed and fire warnings all active, you '
     'hear STALL first (and only STALL) until the stall is resolved, then the speed '
     'warning, then the fire warning.',
     'ACE Pilot\'s Guide 8-36, Table 8-5', T_ALERT)

card('Aural Priority Order — The Top of the List',
     'State the aural message and relative priority for: stall, gear, overspeed, '
     'takeoff configuration, speed brake, cabin pressurization, and a red CAS warning.',
     'Priority 1  — STALL (continuous, not mutable)\n'
     'Priority 5  — "GEAR" (continuous, not mutable)\n'
     'Priority 6  — "SPEED" — overspeed (continuous, not mutable)\n'
     'Priority 7  — "CAT 2 FAIL" (single)\n'
     'Priority 8  — "NO TAKEOFF" — takeoff configuration (continuous, not mutable)\n'
     'Priority 9  — "SPEED BRAKE" (continuous, not mutable)\n'
     'Priority 10 — "CABIN" — cabin pressurized (continuous, not mutable)\n'
     'Priority 11 — TRIPLE CHIME — CAS warning (continuous, mutable)\n'
     'Note the pattern: the un-mutable, continuous aurals are the ones tied to an '
     'immediate flight-path or configuration hazard.',
     'ACE Pilot\'s Guide Table 8-5 (8-37)', T_ALERT)

card('Aural Priority Order — Fire, Cabin and Trim',
     'State the aural and priority for: pitch/yaw trim runaway, pitch trim in motion, '
     'left and right engine fire, cabin altitude, emergency descent, battery hot.',
     'Priority 12 — "Trim Runaway" — pitch trim runaway (continuous, mutable)\n'
     'Priority 13 — "Trim Runaway" — yaw trim runaway (continuous, mutable)\n'
     'Priority 14 — CLACKER — pitch trim in motion (continuous, mutable)\n'
     'Priority 15 — "LEFT ENGINE FIRE" (continuous, mutable)\n'
     'Priority 16 — "RIGHT ENGINE FIRE" (continuous, mutable)\n'
     'Priority 17 — "CABIN ALTITUDE" (continuous, mutable)\n'
     'Priority 18 — "EMERGENCY DESCENT" (single, not mutable)\n'
     'Priority 19 — "Battery Hot" (continuous, mutable)',
     'ACE Pilot\'s Guide Table 8-5 (8-37, 8-38)', T_ALERT)

card('Aural Priority Order — Automation and Advisory',
     'State the aural and priority for: AT engaged, CAS caution, AP uncommanded '
     'disconnect, minimums, AP commanded disconnect, altitude alert, autothrottle '
     'disconnect, ice mode.',
     'Priority 23 — "AT ENGAGED" (single)\n'
     'Priority 24 — SINGLE CHIME — CAS caution (continuous, mutable)\n'
     'Priority 25 — CAVALRY CHARGE — AP UNCOMMANDED disconnect (CONTINUOUS)\n'
     'Priority 26 — "MINIMUMS" (single)\n'
     'Priority 27 — CAVALRY CHARGE — AP COMMANDED disconnect (SINGLE)\n'
     'Priority 28 — C CHORD — altitude alert (single)\n'
     'Priority 29 — C CHORD — vertical track alert (single)\n'
     'Priority 30 — "AUTOTHROTTLE" — AT abnormal disconnect (continuous, mutable)\n'
     'Priority 31 — "AUTOTHROTTLE" — AT normal disconnect (single)\n'
     'Priority 32 — "ICE" — ice mode alert (single)\n'
     'The commanded/uncommanded distinction is the one that matters: same cavalry '
     'charge, but CONTINUOUS means the aircraft dropped the autopilot, not you.',
     'ACE Pilot\'s Guide Table 8-5 (8-38)', T_ALERT)

card('Silencing the Cavalry Charge',
     'An uncommanded AP disconnect is sounding. How is that specific tone muted, and '
     'what will NOT mute it?',
     'The AP uncommanded disconnect tone is mutable ONLY via:\n'
     '• an AP QUICK DISCONNECT button (either yoke), or\n'
     '• the AP button on the Flight Controller\n'
     'Pushing Master Caution or Master Warning will NOT silence it — those mute other '
     'aurals, not this one.\n'
     'This is why the QRH AFCS Abnormal Disconnect procedure has you grasp the wheel and '
     'then press the AP disengage switch: that press is what stops the noise.',
     'ACE Pilot\'s Guide Table 8-5 Note 3 (8-39)', T_ALERT)

card('Aural Routing — EGPWS and TCAS vs CAS',
     '1. How do EGPWS and TCAS aurals reach you, relative to CAS aurals — ?\n'
     '2. What happens when a TAWS alert and a TCAS alert coincide — ?\n'
     '3. Which datalink aurals are inhibited, and when — ?',
     '1. EGPWS and TCAS aurals are input DIRECTLY to the Audio Panel and come straight '
     'to the headset, so they are heard SIMULTANEOUSLY with CAS-generated aurals.\n'
     '2. All TAWS alerts MUTE the TAS/TCAS alerts — terrain wins over traffic.\n'
     '3. ATC datalink aurals are inhibited during engine start, takeoff and landing; any '
     'alert received is annunciated at the completion of that phase. The SATCOM aural is '
     'inhibited during engine start, takeoff, approach and landing roll.',
     'ACE Pilot\'s Guide Table 8-5 Notes 1, 2, 4, 5 (8-39)', T_ALERT)

# ----------------------------------------------------- AFCS & modes
card('Flight Mode Annunciator — Layout and Colour Logic',
     '1. Where are lateral vs vertical FD modes displayed — ?\n'
     '2. What colour is an ACTIVE mode? An ARMED mode — ?\n'
     '3. What happens visually when an armed mode captures — ?',
     '1. Lateral modes are displayed to the LEFT of the AP engage annunciator; vertical '
     'modes to the RIGHT of the YD annunciator. The FMA sits in the upper-middle of the '
     'PFD.\n'
     '2. ACTIVE = GREEN. ARMED = WHITE.\n'
     '3. On capture the armed mode transitions to active and FLASHES GREEN REVERSE VIDEO '
     'for approximately 5 seconds, then remains steady green.\n'
     'FD modes are removed when the AP is not engaged and the FD has been deactivated.',
     'ACE Pilot\'s Guide 6-17, 6-18', T_AFCS)

card('Autopilot Status Annunciator',
     'State the meaning of each AP annunciator:\n1. Green AP — ?\n2. Amber TCS — ?\n'
     '3. Red AP flashing 5 seconds — ?\n4. Red AP flashing continuously — ?',
     '1. Green AP — autopilot engaged\n'
     '2. Amber TCS — the TCS button is pushed\n'
     '3. Red AP flashing for 5 seconds, then out — NORMAL disengagement. No pilot '
     'acknowledgment required.\n'
     '4. Red AP flashing CONTINUOUSLY until acknowledged with the Quick Disconnect — a '
     'FAILURE occurred while engaged. An "AP X Fail" advisory is displayed while the '
     'failure is present.\n'
     'Only one AP annunciator can be displayed at a time. Continuous = the aircraft '
     'dropped it; brief = you commanded it.',
     'ACE Pilot\'s Guide Table 4-25 (4-57)', T_AFCS)

card('Autopilot Engagement and Disengagement',
     '1. What are the three normal means to manually disengage the AP — ?\n'
     '2. What does engaging the AP also engage — ?\n'
     '3. What happens if you engage the AP with the FD off — ?',
     '1. • the AP button on the Flight Controller\n  • an AP quick-disconnect button\n'
     '  • activation of manual stabilizer trim\n'
     '2. Selecting AP also activates the PITCH AUTOTRIM function and the YAW DAMPER '
     '(when not already active). Manual deselection of the AP does NOT deselect the YD.\n'
     '3. The FD automatically turns ON, with PITCH HOLD as the active vertical mode and '
     'ROLL HOLD as the active lateral mode.\n'
     'The AP can also be disengaged with the TCS or QD buttons. A yaw damper failure due '
     'to YD-only faults does NOT disengage the autopilot.',
     'ACE Pilot\'s Guide 4-56, 4-58', T_AFCS)

card('Yaw Damper — Interlocks You Must Know',
     '1. What happens to the AP when you disengage the YD — ?\n'
     '2. Above 30,000 ft, how must the YD be disengaged — ?\n'
     '3. When does the YD disengage automatically — ?\n'
     '4. Green vs amber YD — ?',
     '1. Disengaging the YD ALSO disconnects the AP. (The reverse is not true: '
     'deselecting the AP with the AP button or manual electric trim does not disengage '
     'the YD.)\n'
     '2. The YD is INHIBITED from disengaging above 30,000 ft using the QD button — it '
     'must be disengaged with the YD button on the Flight Controller.\n'
     '3. Automatically when radio altitude is valid and the aircraft transitions below '
     '30 FEET.\n'
     '4. Green YD = engaged. Amber YD = engaged, then a failure occurred.\n'
     'Pushing either the YD button or the QD button gives a red AP flashing for 2.5 sec '
     'plus the AP disconnect tone; no acknowledgment required.',
     'ACE Pilot\'s Guide 4-63, Tables 4-28, 4-29', T_AFCS)

card('Autopilot Control and Overpower Limits',
     '1. AP roll and pitch control limits — ?\n'
     '2. Maximum momentary overpower force at the column, pitch and roll — ?\n'
     '3. Roll and pitch acceleration limits — ?',
     '1. Roll ±35 degrees · Pitch ±20 degrees\n'
     '2. Not more than 50 POUNDS in pitch and 30 POUNDS in roll, measured at the '
     'control column\n'
     '3. Roll acceleration limited to +6 deg/s² · pitch acceleration limited to '
     '+3.0 deg/s²\n'
     'If the AP is engaged while outside the pitch or roll limits, it follows FD '
     'commands to bring the aircraft back within limits.',
     'ACE Pilot\'s Guide 4-55, 4-58', T_AFCS)

card('Touch Control Steering (TCS)',
     'What does pressing and releasing TCS do with the autopilot engaged?',
     'PRESSING TCS: the AFCS neutralizes the autopilot by RELEASING the aileron and '
     'elevator servo CLUTCHES, letting you hand-fly. An amber TCS is annunciated.\n'
     'RELEASING TCS: the autopilot clutches re-engage. The flight director modes react '
     'as if the autopilot had just been engaged — targets are SYNCHRONIZED with the '
     'current flight conditions.\n'
     'So TCS is the tool for a quick manual correction without dropping the autopilot — '
     'but be aware your targets resync on release.',
     'ACE Pilot\'s Guide 4-56', T_AFCS)

card('Thrust Rating Selection — Auto-Rating Types',
     'In auto-rating mode, what are the rating types, and how many can be active at '
     'once?',
     'Four auto-rating types: TAKEOFF (TO) · MAX CONTINUOUS THRUST (MCT) · CLIMB (CLB) · '
     'CRUISE (CRZ). Rating types are MUTUALLY EXCLUSIVE — only ONE engine data rating '
     'type is active at a time. (IDL and ATR are also rating types.)\n'
     'The TRS picks the rating from the phase of flight and communicates the active '
     'rating to the displays and to the autothrottle for scheduling engine response.\n'
     'Transitions back to TAKEOFF require: FD mode PIT, (V)FLC, VS, (V)ASEL, (V)ALT or '
     'VPATH, both engines on, and landing gear NOT extended. Any of flaps in takeoff '
     'config, gear extended, or FD mode GA drives it out of CLB/CRZ.',
     'ACE Pilot\'s Guide 4-81, Table 4-32', T_AFCS)

# ----------------------------------------------------- Protections
card('Emergency Descent Mode — Activation',
     'What three conditions must all be present for EDM to activate?',
     'ALL of:\n'
     '1. A cabin DEPRESSURIZATION is detected\n'
     '2. Aircraft altitude is greater than 30,000 FEET\n'
     '3. The AUTOPILOT is ON\n'
     'EDM is an OPTION and must be enabled via APM to operate.\n'
     'Both the lateral AND vertical fields of the FMA display an amber EDM to tell you '
     'the system is active.',
     'ACE Pilot\'s Guide 4-69', T_PROT)

card('Emergency Descent Mode — What the Aircraft Does',
     'EDM has activated. Describe the full sequence the aircraft flies.',
     '1. Performs a 90° LEFT turn\n'
     '2. ENGAGES the autothrottle\n'
     '3. Commands thrust to IDLE\n'
     '4. Descends at VMO to 15,000 FEET\n'
     '5. At 15,000 ft: altitude capture, then the AP transitions to HEADING mode and '
     '175-KNOT SPEED HOLD mode\n'
     'Know the left turn and the 15,000 ft / 175 kt end state — that is what you will be '
     'asked to predict and to monitor.',
     'ACE Pilot\'s Guide 4-69', T_PROT)

card('Emergency Descent Mode — Cancelling It',
     '1. What four actions cancel EDM — ?\n'
     '2. What do the other Flight Controller buttons do — ?\n'
     '3. Does the AP QD button disconnect the autothrottle — ?',
     '1. • the AP QD button on the control wheels\n  • activation of MANUAL TRIM\n'
     '  • the AP button on the Flight Controller\n  • the TCS button\n'
     '2. ALL other Flight Controller buttons are IGNORED and have no effect while EDM '
     'is active.\n'
     '3. NO. Pushing the AP QD button during EDM does NOT disconnect the AT. The AT must '
     'be disconnected with the AT button on the Flight Controller or the AT QD button on '
     'the thrust lever.\n'
     'On releasing TCS, the AFCS reverts to basic PIT and ROL modes.',
     'ACE Pilot\'s Guide 4-70', T_PROT)

card('SWPS — Warning, Pusher, and How to Stop It',
     '1. How does the stall warning present — ?\n'
     '2. What does the stall warning function do to the autopilot — ?\n'
     '3. How is an active stick pusher disconnected — ?',
     '1. STALL / STALL* annunciation on the PFD, the aural "STALL", and STICK SHAKER '
     'activation.\n'
     '2. The stall warning function DISENGAGES THE AUTOPILOT before reaching the stick '
     'pusher condition.\n'
     '3. By HOLDING the QD button on the pilot\'s yoke. (The pusher activates when the '
     'pilot does not respond to the stall warning — it engages the pitch servo and noses '
     'the aircraft down until the stall condition has passed.)\n'
     'The SWPS computes from TWO AOA VANES, one each side, plus FLAPS and ICE MODE '
     'inputs. Left shaker/left AOA drives the pilot-side LSA; right drives the '
     'copilot-side LSA.',
     'ACE Pilot\'s Guide 4-70, 4-71', T_PROT)

card('SWPS CAS Messages and Their Level',
     'State the alert level for: Pusher Fail, Shaker Fail, and L/R LSA Fail.',
     'Pusher Fail — CAUTION. At least one instance of the pusher is not available for '
     'engagement.\n'
     'Shaker Fail — CAUTION. At least one instance of the shaker is not available.\n'
     'L LSA Fail / R LSA Fail / L+R LSA Fail — ADVISORY. The low speed awareness '
     '"thermometer" on that PFD has failed and will not be displayed.\n'
     'Remember the AFM warning that pairs with Pusher Fail: natural stalls are NOT '
     'prevented with the pusher inoperative — stalls must be avoided.',
     'ACE Pilot\'s Guide Table 4-31 (4-71)', T_PROT)

card('Tactile Feedback System — Bank and Overspeed',
     '1. When is TFS active — ?\n2. At what bank does it engage, and until what — ?\n'
     '3. How do those numbers change in an overspeed condition — ?',
     '1. TFS is active when the aircraft is IN THE AIR and the AUTOPILOT IS OFF. (Option.)\n'
     '2. If the aircraft banks through 51°, the roll servo engages and opposes the pilot. '
     'The opposing force continues until bank is reduced to 31°.\n'
     '3. When TFS is activated for an OVERSPEED condition, bank protection activates at '
     '31° instead of 51°, and opposes until bank is reduced to 11°.\n'
     'BNK and TF are displayed in the FMA; TF flashes reverse video until disengaged. '
     'Overspeed protection targets VMO/MMO — NOT placard speeds.',
     'ACE Pilot\'s Guide 4-68, 4-69', T_PROT)

card('Tactile Feedback System — Overriding It',
     'How do you override or disconnect the TFS, and what is the difference between the '
     'two methods?',
     'AP QD button (either yoke): DEACTIVATES the TFS and INHIBITS it from reactivating '
     'until conditions are met where TFS would again be active.\n'
     'TCS button: overrides the opposing force TEMPORARILY. When TCS is released, the '
     'TFS RE-ENGAGES if the aircraft is still within the conditions where TFS would be '
     'active.\n'
     'So QD is the "make it stop" action; TCS is the "hold it off while I maneuver" '
     'action.',
     'ACE Pilot\'s Guide 4-68', T_PROT)

card('Rudder Bias',
     '1. When is the rudder bias system active — ?\n'
     '2. What two conditions engage it — ?\n3. Which way does it push, and how far — ?\n'
     '4. What annunciates — ?',
     '1. During the TAKEOFF and GO-AROUND phases, with the YAW DAMPER OFF, up to '
     '2,500 FEET AGL.\n'
     '2. • the yaw damper is not active, AND\n  • the thrust (N1) difference between the '
     'two engines exceeds a defined threshold\n'
     '3. It commands the rudder TOWARD THE SIDE OF THE HIGHER-THRUST ENGINE at a '
     'predefined torque. It is NOT full authority — it supplies only a percentage of the '
     'required rudder input through the yaw servo.\n'
     '4. The RB annunciator REPLACES the yaw damper annunciator in the FMA field. Amber '
     'RB means rudder bias is NOT AVAILABLE.',
     'ACE Pilot\'s Guide 4-67', T_PROT)

card('Mach Trim and Automatic Pitch Trim',
     '1. What does the Mach Trim function do, and when — ?\n'
     '2. What does automatic pitch trim do, and which motor does it use — ?',
     '1. Mach Trim automatically compensates for MACH TUCK by commanding the pitch trim '
     'actuator at high Mach numbers WHEN THE AUTOPILOT IS OFF.\n'
     '2. Automatic pitch trim commands the ALTERNATE STABILIZER TRIM MOTOR to offload '
     'steady-state loads on the AP elevator servo — keeping the elevator near neutral, '
     'improving cruise performance, and minimizing transients at AP disengagement.\n'
     'Note the split: Mach Trim works with the AP OFF; automatic pitch trim works with '
     'the AP ON (it is enabled by AP engagement).',
     'ACE Pilot\'s Guide 4-66, 4-67', T_PROT)

card('Autothrottle — Takeoff Window Protection',
     '1. Between what limits does the AT takeoff monitor protect against inadvertent '
     'thrust reduction — ?\n2. Which lane performs it — ?\n'
     '3. How does the AT engage into takeoff thrust mode — ?',
     '1. From 60 KNOTS to 400 FEET AGL — the "takeoff window".\n'
     '2. LANE B of the autothrottle performs the takeoff monitor function and controls '
     'power to the TQA servos, and can disable AT control of the TQA so the system can '
     'reliably be disconnected and inhibited. (The AT function requires two AIOPs — '
     'lanes A and B. AT is hosted in MAU1 only.)\n'
     '3. With the AT armed for takeoff, ADVANCING the TLA of BOTH thrust levers while '
     'airspeed is LESS THAN 60 KNOTS engages the takeoff thrust control mode.',
     'ACE Pilot\'s Guide 4-73, 4-74', T_PROT)

card('Autothrottle — Modes, Protections and Limits',
     '1. What are the primary AT modes — ?\n'
     '2. Does the AT protect against engine overspeed or over-temperature — ?\n'
     '3. When does the AT engage automatically — ?',
     '1. SPEED, THRUST, LIM and EDM.\n'
     '2. NO. Engine overspeed and over-temperature protection are FADEC functions, not '
     'AT functions. However, the AT ALWAYS HONORS the active engine thrust rating.\n'
     '3. Automatically when EMERGENCY DESCENT MODE or AUTOTHROTTLE SPEED PROTECTION mode '
     'becomes active.\n'
     'The AT mode is synchronous with the active FD pitch mode: thrust mode when speed is '
     'being controlled by the FD mode or the FD mode is TO/GA, otherwise speed mode. '
     'Disengagement sounds the "AUTOTHROTTLE" aural.',
     'ACE Pilot\'s Guide 4-73, 4-74', T_PROT)

# ----------------------------------------------------- Display reversion
card('Which AGM Drives Which Display',
     'State the display architecture: which AGM drives which DUs, and how many unique '
     'images can one AGM produce?',
     'AGM 1 drives DU 1 and DU 2. AGM 2 drives DU 3 and DU 4.\n'
     'DU 1 = pilot PFD · DU 2 and DU 3 = the two middle MFDs · DU 4 = copilot PFD.\n'
     'An individual AGM can generate only TWO different screen images at any one time. '
     'That is why, after an AGM failure, the copilot PFD shows an EXACT DUPLICATE of the '
     'pilot PFD rather than its own independent image — the images are identical, not '
     'symmetrical.',
     'ACE Pilot\'s Guide 5-48, 5-49', T_DISP)

card('DU Failure vs AGM Failure — The Critical Distinction',
     'The guide says distinguishing a DU failure from an AGM failure is essential. How '
     'do you tell them apart?',
     'DU FAILURE — that DU goes BLANK (dark, no image), shows a GROSSLY DISTORTED image, '
     'or is physically damaged (cracked/shattered). The other three DUs keep working '
     'normally; both AGMs are healthy.\n'
     'AGM FAILURE — the two DUs driven by that AGM each display a LARGE "X". A large X '
     'means the DU is OPERATING but is NOT RECEIVING IMAGE DATA from the selected AGM.\n'
     'So: X on both DU 1 and DU 2 (or both DU 3 and DU 4) is almost certainly ONE AGM '
     'failure — NOT two failed displays. Concluding "two DUs failed" would be wrong, '
     'precisely because they are displaying the X.',
     'ACE Pilot\'s Guide 5-47, 5-49, 5-50', T_DISP)

card('Single DU Failure — Action',
     'A single DU has failed. What is the corrective action?',
     'Turn that DU\'s DIMMER CONTROL past the detent to the OFF / REV position. This '
     'tells the ACE system the display is no longer of any use so it can redistribute '
     'the images.\n'
     'The remaining three DUs continue to present all information. Nothing is wrong with '
     'either AGM or any other avionics — only that one KDU-1200 display has failed.',
     'ACE Pilot\'s Guide 5-47, 5-49', T_DISP)

card('AGM Failure — Action',
     'DUs 1 and 2 are both displaying a large X. State the corrective actions in order.',
     '1. Turn the CIRCULAR COLLAR surrounding the PFD DIMMER on the AFFECTED SIDE to '
     'select the ALTERNATE (non-normal) AGM to drive the displays. For DUs 1 and 2 '
     'showing X, move the collar around the AGM2 dimmer to PILOTS PFD.\n'
     '2. Then indicate that DU 2 is still showing an X and is of no use: turn the DU 2 '
     'dimmer PAST THE DETENT to OFF / REV.\n'
     '3. Use the TSC MFD SWAP button to alternate between the Situational Awareness and '
     'Systems displays on DU 3.\n'
     'What you lose: the copilot no longer has an independently configurable PFD (it is '
     'a slave image of the pilot\'s), and you can no longer show Situational and Systems '
     'at the same time.',
     'ACE Pilot\'s Guide 5-49', T_DISP)

card('Two DUs Failed — Reversion Logic',
     'Two DUs have failed and been turned off. What appears where, for each pair?',
     'DU 2 + DU 3 (both middle) — COMPOSITE display on DU 1; normal PFD continues on '
     'DU 4\n'
     'DU 1 + DU 2 — left PFD on DU 3; single MFD on DU 4\n'
     'DU 3 + DU 4 — normal left PFD continues on DU 1; single MFD on DU 2\n'
     'DU 1 + DU 4 (both outboard) — left PFD on DU 2; single MFD on DU 3\n'
     'In every case the single MFD toggles between Situational Awareness and Systems with '
     'the TSC MFD Swap button.\n'
     'The logic is optimized for SINGLE-PILOT operations: the composite display — the '
     'hardest to work with — only appears if BOTH MIDDLE displays are gone. In two-crew '
     'ops the copilot (full PFD on DU 4) should take pilot-flying duties.',
     'ACE Pilot\'s Guide 5-50, 5-51, 5-52', T_DISP)

card('Display Integrity Monitors',
     'Name the two display monitors and what each one checks.',
     'DU CRC MONITOR — constantly evaluates the display integrity of each DU '
     'individually, verifying that image data generated by the AGM is properly rendered '
     'on that DU. If tripped, a "Check DU X" CAUTION is posted; that DU is considered '
     'UNRELIABLE and should be reverted off (dimming knob to OFF / REV). Inhibited for a '
     'DU that is not powered.\n'
     'CRITICAL SYMBOL MONITOR — compares AGM-generated image data against the raw data '
     'for critical items, confirming the graphics processor is not outputting corrupt '
     'image data. Critical items: airspeed, baro altitude, baro correction, pitch, roll, '
     'zero-pitch reference line and flight path symbol on each PFD; N1 fan speed (and '
     'status) and ITT (and status) in the engine windows.',
     'ACE Pilot\'s Guide 5-45, 5-46, Table 5-1', T_DISP)

card('Critical Symbol Monitor CAS Messages — Actions',
     'State the required action for: "Check Pilot PFD", "Check Copilot PFD", and '
     '"Check Engine Display".',
     'Check Pilot PFD — cross-check critical data on the pilot PFD against the STANDBY '
     'attitude indicator or the copilot PFD. If the data does not reasonably agree, '
     'REVERT THE PILOT PFD TO AGM2.\n'
     'Check Copilot PFD — cross-check against the standby AI or the pilot PFD. If it does '
     'not reasonably agree, REVERT THE COPILOT PFD TO AGM1.\n'
     'Check Engine Display — cross-check ITT and N2 fan speed against another display. If '
     'they do not reasonably agree, revert the affected PFD to an alternate AGM.\n'
     'In every case the drill is the same: CROSS-CHECK FIRST, revert only if the data '
     'disagrees.',
     'ACE Pilot\'s Guide Table 5-2 (5-46)', T_DISP)

# ----------------------------------------------------- Data integrity
card('PFD Miscompare Thresholds',
     'State the difference between left and right PFD that triggers each miscompare:\n'
     '1. IAS? — ?\n2. ROLL? — ?\n3. PITCH? — ?\n4. ALT? — ?\n5. BARO? — ?',
     '1. IAS? — 10 KNOTS or more (upper-left of both airspeed indicators)\n'
     '2. ROLL? — 6 DEGREES or more (upper-left of both PFDs)\n'
     '3. PITCH? — 5 DEGREES or more (upper-right of both PFDs)\n'
     '4. ALT? — 200 FEET or more (upper-right of both altitude displays)\n'
     '5. BARO? — 0.02 inHg or more (or 1 hPa), when the altimeters are set up for '
     'synchronization (lower-right of both altitude displays)\n'
     'All are displayed in AMBER REVERSE VIDEO. Mnemonic for the attitude pair: roll '
     'tolerance is the larger number (6), pitch the smaller (5).',
     'ACE Pilot\'s Guide 6-10, 6-26, 6-71', T_DATA)

card('Radio Altitude and Vertical Deviation Miscompare',
     '1. How is the RAD? miscompare threshold computed, and how long must it persist — ?\n'
     '2. What triggers a VDEV? miscompare — ?',
     '1. RAD? appears when the difference between radio altitude indications exceeds a '
     'predefined threshold for MORE THAN 1 SECOND. The threshold is computed as:\n'
     '   10 + 0.0625 × [ABS(Pilot RadAlt) + ABS(Copilot RadAlt)]\n'
     '   — i.e. the allowable difference GROWS with height, so it is tightest near the '
     'ground where it matters.\n'
     '2. VDEV? appears below the vertical deviation scale when the pilot side and copilot '
     'side have selected TWO DIFFERENT FMSs as navigation source, the FMS vertical '
     'deviation type is VPATH, and the difference between left and right vertical '
     'deviation exceeds 50% OF FULL SCALE.',
     'ACE Pilot\'s Guide 6-46, 6-56', T_DATA)

card('Invalid Data Presentation',
     'How does the PFD present invalid airspeed, altitude, or attitude data — and how '
     'does that differ from a miscompare?',
     'INVALID data is REMOVED and replaced with a large X over the affected area:\n'
     '• Invalid airspeed — the airspeed tape is removed and replaced with an X; the '
     'rolling digits are removed\n'
     '• Invalid altitude — all altitude data removed, X over the entire altitude tape\n'
     'A MISCOMPARE (amber "?" annunciator) means both sides are producing data but they '
     'DISAGREE — you must decide which to trust, typically by cross-checking the standby '
     'instrument. An X means that data is GONE.\n'
     'Different problem, different action: miscompare → cross-check and choose; X → use '
     'the other source.',
     'ACE Pilot\'s Guide 6-10, 6-71', T_DATA)

# ----------------------------------------------------- TCAS
card('TCAS Aural Notifications',
     'State the aural for: a new traffic advisory, a further TA while one is active, an '
     'RA that has cleared, and the self-test result.',
     'New traffic advisory — "TRAFFIC, TRAFFIC"\n'
     'When a previous TA is already active — "TRAFFIC"\n'
     'RA cleared (TCAS II only) — "CLEAR OF CONFLICT"\n'
     'Self-test passed — "TCAS SYSTEM TEST OK"\n'
     'Self-test failed — "TCAS SYSTEM TEST FAIL"',
     'ACE Pilot\'s Guide Table 15-2 (15-51)', T_TCAS)

card('Resolution Advisories — Corrective vs Preventive',
     'What is the aural difference between a CORRECTIVE and a PREVENTIVE RA?',
     'CORRECTIVE RA — tells you to CHANGE the flight path:\n'
     '  Climb — "CLIMB, CLIMB, CLIMB"\n'
     '  Descent — "DESCEND, DESCEND, DESCEND"\n'
     '  Crossover climb — "CLIMB, CROSSING CLIMB, CLIMB"\n'
     'PREVENTIVE RA — tells you NOT to change what you are doing:\n'
     '  "MONITOR VERTICAL SPEED, MONITOR VERTICAL SPEED"\n'
     'A preventive RA requires you to keep out of a vertical band — it does not require a '
     'maneuver. RAs are TCAS II installations only.',
     'ACE Pilot\'s Guide Table 15-3 (15-52)', T_TCAS)

card('Transponder — Never Select STBY on the Ground',
     'Why must the transponder not be set to STBY on the ground, and what should be '
     'selected instead?',
     'The ACE transponder supplies AUTOMATIC air-to-ground (GND) switching, so the old '
     'practice of selecting STBY on the ground does NOT apply. The pilot must NEVER set '
     'the active mode to STBY while on the ground.\n'
     'Instead select the mode you want IN FLIGHT — normally TA/RA for TCAS II (or TA for '
     'TCAS I). Transmissions begin automatically at takeoff and stop automatically on '
     'landing (except replies to specifically addressed interrogations).\n'
     'On the ground with GND displayed and not in STBY, the transponder still replies to '
     'interrogations addressed to the aircraft by name, and other traffic can be viewed '
     'with TA or TA/RA selected.',
     'ACE Pilot\'s Guide 15-57, 15-58', T_TCAS)

card('TCAS Before Takeoff',
     'How is TCAS tested and armed before flight, and what does it do while still on '
     'the ground?',
     'Test with the TCAS TEST softkey during cockpit preparation. After passing '
     'self-test, place TCAS in TA/RA (TCAS II) or TA (TCAS I) by selecting the '
     'transponder to TA/RA or TA.\n'
     'While the aircraft is on the ground (per air-ground logic) TCAS does NOT issue '
     'advisories — although threat traffic IS displayed in YELLOW.\n'
     'On transition to air mode the GND annunciator is removed, the transponder begins '
     'broadcast operation, and TCAS becomes active.',
     'ACE Pilot\'s Guide 15-58', T_TCAS)

card('TCAS Limitations — Why Traffic May Not Appear',
     'Name the situations in which an aircraft you can see is not shown by TCAS.',
     '• NO OPERATING TRANSPONDER — TCAS cannot detect it at all\n'
     '• NON-ALTITUDE REPORTING (NAR) intruder — range and bearing only; can produce a TA '
     'but never an RA; TCAS ASSUMES NAR traffic is CO-ALTITUDE with you\n'
     '• ANTENNA SHADING — most small aircraft have one transponder antenna on the '
     'belly; when you are above them the antenna can be shaded so interrogations or '
     'replies do not get through. Also happens when the other aircraft maneuvers and '
     'blocks line of sight\n'
     '• CONE OF CONFUSION — the upper directional antenna determines bearing only for '
     'intruders between -10° and +70° elevation; outside that they are tracked with NO '
     'bearing\n'
     '• LOWER MONOPOLE ANTENNA — no bearing available; the intruder is tracked but NOT '
     'DISPLAYED unless a TA is issued\n'
     '• A poor transponder on the other aircraft — ground stations have more gain, so ATC '
     'may call traffic your TCAS never sees\n'
     '• NO CLOSURE RATE — TCAS derives closest point of approach; co-speed same-direction '
     'traffic may never be a threat',
     'ACE Pilot\'s Guide 15-59, 15-60', T_TCAS)

# ----------------------------------------------------- EGPWS
card('EGPWS Mode 1 — Excessive Descent Rate',
     '1. When is Mode 1 active — ?\n2. Outer boundary alert — ?\n'
     '3. Inner boundary alert — ?',
     '1. Active regardless of flight phase whenever radio altitude is VALID and LESS '
     'THAN 2,450 FEET AGL. Lower cutoff at 10 ft RA during landing; re-enabled at 30 ft '
     'RA during takeoff. When barometric input is used, cut off at 30 ft and re-enabled '
     'at 65 ft.\n'
     '2. OUTER — GND PROX annunciator and "SINKRATE, SINKRATE". Repeated twice, then '
     'silent unless the condition degrades by about 20% (by computed time to impact), '
     'which gives two more and repeats the cycle.\n'
     '3. INNER — PULL UP annunciator and "PULL UP, PULL UP", or optionally a continuous '
     '"WHOOP-WHOOP PULL UP", repeating continuously until the inner boundary is exited.\n'
     'Steep approach selected desensitizes the outer curve by 500 FPM and the inner by '
     '200 FPM.',
     'ACE Pilot\'s Guide 16-31, 16-32', T_TAWS)

card('EGPWS Mode 3 — Altitude Loss After Takeoff',
     '1. When is Mode 3 enabled — ?\n2. What is the alert — ?\n'
     '3. How does the aural repeat — ?',
     '1. Enabled after TAKEOFF or GO-AROUND when the landing gear or flaps are NOT in '
     'the landing configuration, and stays enabled until the EGPWS detects the aircraft '
     'has gained enough altitude to no longer be in the takeoff phase.\n'
     '2. A GND PROX caution on the right side of the attitude indicator and the aural '
     '"DON\'T SINK, DON\'T SINK".\n'
     '3. The aural is annunciated again only when a further 20% OF RADIO ALTITUDE is '
     'lost. If that additional altitude is lost, two more aurals are given and another '
     '20% is added into the calculation — ratcheting until the original altitude is '
     'recovered. The visual stays on the whole time the envelope is violated.',
     'ACE Pilot\'s Guide 16-40', T_TAWS)

card('EGPWS Mode 6 — Advisory Callouts',
     'List the Mode 6 callouts and the altitude each occurs at.',
     '"MINIMUMS" — at minimums\n'
     '"APPROACHING MINIMUMS" — DH/MDA bug setting PLUS 80 FEET\n'
     '"FIVE HUNDRED" — 500 ft AGL\n'
     '"ONE HUNDRED" — 100 ft AGL\n'
     '"FIFTY" — 50 · "FORTY" — 40 · "THIRTY" — 30 · "TWENTY" — 20 · "TEN" — 10 ft AGL\n'
     'Each selected callout is annunciated ONCE PER APPROACH. The system must transition '
     'to approach mode to RE-ARM the callouts for the next approach. Valid radio altitude '
     'above the highest selected callout must be present; minimums callouts additionally '
     'need the landing gear down (or alternate mode 4B select). No visual alerting '
     'accompanies Mode 6 callouts.',
     'ACE Pilot\'s Guide Table 16-3 (16-47)', T_TAWS)

card('Terrain and Obstacle Alerts — Caution vs Warning',
     'State the aural, colour and repeat behaviour for terrain/obstacle CAUTION and '
     'WARNING alerts.',
     'CAUTION — "CAUTION TERRAIN, CAUTION TERRAIN" (optionally "TERRAIN AHEAD, TERRAIN '
     'AHEAD"); for obstacles "CAUTION OBSTACLE, CAUTION OBSTACLE" (optionally "OBSTACLE '
     'AHEAD"). Repeated EVERY 10 SECONDS while inside the caution envelope. Threat '
     'terrain is coded AMBER; GND PROX caution on the attitude indicator.\n'
     'WARNING — "TERRAIN, TERRAIN, PULL UP" (optionally "TERRAIN AHEAD, PULL UP"); for '
     'obstacles "OBSTACLE, OBSTACLE, PULL UP". "PULL UP" repeats CONTINUOUSLY while '
     'inside the warning envelope. Threat terrain is coded RED; PULL UP warning on the '
     'attitude indicator.\n'
     'In both cases only terrain along the aircraft track and within ±90° OF TRACK is '
     'coded, and the threat image appears on the HSI.',
     'ACE Pilot\'s Guide 16-53, 16-54', T_TAWS)

card('EGPWS Class A-Only Modes',
     'Which EGPWS modes are unavailable when Class B TAWS is selected, and what does '
     'each do?',
     'MODE 2 — Excessive Closure to Terrain. Alerts on excessive terrain closure rate; '
     'the aircraft need NOT be descending — level flight or a climb toward rising terrain '
     'can trigger it. Sub-modes 2A and 2B by configuration. In a high-integrity terrain '
     'awareness state the maximum altitude is reduced from 2,450 ft to 950 ft to cut '
     'nuisance alerts.\n'
     'MODE 4 — Unsafe Terrain Clearance. 4A: cruise/approach, gear not in landing '
     'config. 4B: gear in landing config, flaps not. 4C: takeoff phase with either gear '
     'or flaps not in landing config.\n'
     'MODE 5 — Excessive Deviation Below Glideslope. Front-course ILS, or below the '
     'selected GPS vertical path on approaches to LPV minimums. Needs localizer within '
     '±2 dots, radio altitude valid and below 1,000 ft, and gear down; below 500 ft it is '
     'enabled without a valid localizer.\n'
     'Subsequent Mode 4 aurals occur only when envelope penetration increases by 20%.',
     'ACE Pilot\'s Guide 16-33, 16-34, 16-42, 16-49', T_TAWS)

data = [{'id': c['id'], 'title': c['title'], 'front': c['front'],
         'back': c['back'], 'reference': c['reference'], 'topic': c['topic']} for c in C]
json.dump(data, open('ace_cards.json', 'w'), ensure_ascii=False, indent=1)

topics = {}
for c in data:
    topics.setdefault(c['topic'], []).append(c['id'])
print(f'built {len(data)} ACE cards')
for t, ids in topics.items():
    print(f'  {t:30} {len(ids):>2}  {ids[0]}..{ids[-1]}')
