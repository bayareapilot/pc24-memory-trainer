"""Build the AFM-sourced supplementary card set (AFM-1 ... AFM-n).

Source: PC-24 EASA AFM Report 02371, Issue 003 Rev 08 (01 May 2025), Volume 1.
Aircraft-specific values resolved for MSN 631 (i.e. the MSN 501-up column).
Every value below was read from the AFM text extracted in this session.
"""
import json

C = []


def card(id_, title, front, back, ref, topic):
    C.append({'id': id_, 'title': title, 'front': front, 'back': back,
              'reference': ref, 'topic': topic})


n = 0
def nid():
    global n
    n += 1
    return f'AFM-{n}'


# ---------------------------------------------------------------- MSN 631
card(nid(), 'Weight Limits — Our Aircraft (MSN 631)',
     'For MSN 631, state all five weight limits:\n1. Max Ramp Weight — ?\n'
     '2. Max Takeoff Weight — ?\n3. Max Landing Weight — ?\n'
     '4. Max Zero Fuel Weight — ?\n5. Max Cargo Weight — ?',
     'MSN 631 is in the MSN 501-up column:\n'
     '1. Max Ramp Weight — 18,840 lb (8,545 kg)\n'
     '2. Max Takeoff Weight — 18,740 lb (8,500 kg)\n'
     '3. Max Landing Weight — 17,340 lb (7,865 kg)\n'
     '4. Max Zero Fuel Weight — 14,660 lb (6,650 kg)\n'
     '5. Max Cargo Weight — 2,940 lb (1,334 kg)\n'
     'NOTE: These are the higher values. The 101-500 figures are each 440 lb lower '
     '(except baggage/floor limits, which are common to all serials).',
     'AFM Table 2-1-15 (p 2-1-23)', 'MSN 631')

card(nid(), 'CG Limits — Our Aircraft (MSN 631)',
     'For MSN 631, state the forward and aft CG limits (% MAC) at:\n'
     '1. 18,840 lb (Max Ramp Weight) — ?\n2. 18,740 lb (MTOW) — ?\n'
     '3. 13,560 lb — aft limit ?\n4. 11,510 lb — forward limit ?',
     '1. 18,840 lb (MRW) — fwd 25.0% / aft 39.8% MAC\n'
     '2. 18,740 lb (MTOW) — fwd 25.0% / aft 40.0% MAC\n'
     '3. 13,560 lb (6,150 kg) — aft limit 47.6% MAC\n'
     '4. 11,510 lb (5,221 kg) — fwd limit 37.0% MAC\n'
     'NOTE: Straight-line variation between points. Datum is 146.1 in (3,711 mm) '
     'forward of the forward jacking point.',
     'AFM Table 2-1-16 (p 2-1-24)', 'MSN 631')

# ---------------------------------------------------------------- Airspeeds
card(nid(), 'VO — Maximum Operating Maneuvering Speed',
     'Do not make full or abrupt control movements above VO.\n'
     'State VO for MSN 501-up MTOW, and the schedule down to minimum weight.',
     '18,740 lb (8,500 kg) MTOW MSN 501-up — 170 KIAS\n'
     '18,300 lb (8,300 kg) MTOW MSN 101-500 — 170 KIAS\n'
     '17,650 lb (8,005 kg) — 165 KIAS\n'
     '17,000 lb (7,711 kg) — 160 KIAS\n'
     '16,000 lb (7,258 kg) — 155 KIAS\n'
     '15,000 lb (6,804 kg) — 150 KIAS\n'
     '14,000 lb (6,350 kg) — 145 KIAS\n'
     '13,000 lb (5,897 kg) — 140 KIAS\n'
     '12,000 lb (5,443 kg) — 135 KIAS\n'
     '11,440 lb (5,190 kg) — 120 KIAS\n'
     'NOTE: Avoid rapid, large alternating control inputs — especially combined with '
     'large pitch/roll/yaw changes — as these may cause structural failure at ANY '
     'speed, including below VO.',
     'AFM Table 2-1-5 (p 2-1-9), 19.3 (p 2-1-24)', 'Airspeeds')

card(nid(), 'VO RUDDER — Rudder Maneuvering Limits',
     '1. Full/abrupt rudder input limit up to 20,000 ft — ?\n'
     '2. Full/abrupt rudder input limit above 20,000 ft — ?\n'
     '3. Speed above which pedal travel is limited to 1/3 — ?\n'
     '4. Speed above which pedal travel is limited to 1/10 — ?',
     '1. Up to 20,000 ft (6,096 m) — 130 KIAS\n'
     '2. Above 20,000 ft (6,096 m) — 125 KIAS\n'
     '3. 185 KIAS (SL to 45,000 ft) — do not exceed 1/3 of pedal travel\n'
     '4. 290 KIAS (SL to 45,000 ft) — do not exceed 1/10 of pedal travel',
     'AFM Table 2-1-6 (p 2-1-9)', 'Airspeeds')

card(nid(), 'VMCG — Minimum Control Speed on Ground',
     'VMCG (flaps 8° / 15°) — ?',
     'VMCG — 87 KIAS (flaps 8° / 15°)',
     'AFM Table 2-1-10 (p 2-1-10)', 'Airspeeds')

card(nid(), 'VMC — Minimum Control Speed for Takeoff',
     'State VMC by weight for flaps 15° and flaps 8°.',
     'Flaps 15°:\n  ≥13,228 lb (6,000 kg) — 77 KIAS\n  >12,125 lb (5,500 kg) — 81 KIAS\n'
     '  >11,023 lb (5,000 kg) — 84 KIAS\n'
     'Flaps 8°:\n  ≥13,669 lb (6,200 kg) — 82 KIAS\n  >12,125 lb (5,500 kg) — 87 KIAS\n'
     '  >11,023 lb (5,000 kg) — 90 KIAS\n'
     'NOTE: Flight testing determined the PC-24 has NO critical engine for VMC purposes.',
     'AFM Table 2-1-11 (p 2-1-10)', 'Airspeeds')

card(nid(), 'VMCL — Minimum Control Speed for Landing',
     'State VMCL by weight for flaps 15° and flaps 33°.',
     'Flaps 15°:\n  ≥13,007 lb (5,900 kg) — 78 KIAS\n  >12,125 lb (5,500 kg) — 81 KIAS\n'
     '  >11,023 lb (5,000 kg) — 84 KIAS\n'
     'Flaps 33°:\n  ≥13,228 lb (6,000 kg) — 73 KIAS\n  >12,125 lb (5,500 kg) — 77 KIAS\n'
     '  >11,023 lb (5,000 kg) — 80 KIAS\n'
     'NOTE: No critical engine for VMC purposes.',
     'AFM Table 2-1-12 (p 2-1-10)', 'Airspeeds')

card(nid(), 'Airspeed Tape Markings (PFD / ESIS)',
     'Identify each airspeed tape marking and its value:\n'
     '1. Red/white barber pole — ?\n2. Placard "G" — ?\n3. Placard "Gr" — ?\n'
     '4. Placards "08" / "15" — ?\n5. Placard "33" — ?\n6. Red low-speed tape — ?',
     '1. Barber pole (across and upward, right side of tape) — the lower of 290 KIAS '
     'or 0.74 M (VMO / MMO)\n'
     '2. "G" — 250 KIAS, VLO Extend (max landing gear operating speed, extend)\n'
     '3. "Gr" — 200 KIAS, VLO Retract\n'
     '4. "08" / "15" — 200 KIAS, VFE at flaps 8° / 15°\n'
     '5. "33" — 175 KIAS, VFE at flaps 33°\n'
     '6. Red low speed awareness tape — extends up from the bottom of the tape to '
     'shaker speed\n'
     'NOTE: The red high-speed strip extends down from VMO/MMO to the valid VLO or VFE; '
     'it is not shown in clean configuration or with gear extended only.',
     'AFM Table 2-1-13 (p 2-1-11)', 'Airspeeds')

card(nid(), 'Minimum Airspeed — Flaps Retracted in Icing',
     'The minimum airspeed with flaps retracted in icing conditions — ?',
     'Minimum airspeed, flaps retracted, in icing conditions — 150 KIAS',
     'AFM 16.3 (p 2-1-21)', 'Icing')

card(nid(), 'Dual Engine Failure — Glide Speed',
     'Both engines have failed. Per the AFM WARNING, what speed is recommended '
     'with flaps up, and what protection is lost?',
     'WARNING: AVOID STALL — SHAKER AND PUSHER ARE UNAVAILABLE. WITH FLAPS UP, '
     '150 KIAS IS RECOMMENDED AS A SAFE SPEED WITH GOOD GLIDE PERFORMANCE.\n'
     'Procedure order (3-ENG-01): 1. Airspeed — As required · 2. Cabin Altitude — '
     'Monitor · 3. Emergency Descent 3-NAE-02 — Accomplish · at or below 25,000 ft: '
     '4. Engine Airstart 3-NAE-03 — Accomplish · if no airstart successful: '
     '5. Forced Landing 3-NAE-15\n'
     'CAUTION: Start with the engine deemed most likely to relight successfully.\n'
     'NOTE: 3-ENG-01 has NO red memory-item box — step 1 is not a boxed memory item.',
     'AFM 3-ENG-01 (p 3-13-1)', 'Emergency knowledge')

# ---------------------------------------------------------------- AFCS
card(nid(), 'AFCS — Minimum Engagement Heights After Takeoff',
     '1. Minimum autopilot engagement height after takeoff — ?\n'
     '2. Minimum yaw damper engagement height after takeoff — ?\n'
     '3. What must be done before YD engagement — ?',
     '1. Autopilot — 400 ft AGL\n'
     '2. Yaw damper — 50 ft AGL\n'
     '3. The landing gear must be selected UP prior to YD engagement',
     'AFM 4.2.2 (p 2-1-3)', 'AFCS')

card(nid(), 'AFCS — General Prohibitions and Overrides',
     'State the AFCS general limitations: override, tactile feedback, quick '
     'disconnect, TCS, and the yaw-damper altitude limit.',
     '• Do NOT override the autopilot or yaw damper\n'
     '• Do NOT engage the autopilot while the tactile feedback system is active\n'
     '• The pilot-side quick disconnect button must be operable before departure\n'
     '• Servos may be temporarily disengaged without disengaging the AP by pushing '
     'and holding the TCS switch on the control wheel for the desired duration\n'
     '• Flight above 30,000 ft MSL with the yaw damper disengaged is PROHIBITED\n'
     '• During AP operation a qualified pilot must be seated in a pilot position with '
     'seat belt fastened',
     'AFM 4.2.1 (p 2-1-3)', 'AFCS')

card(nid(), 'Autothrottle — Override and Approved Phases',
     '1. How is the autothrottle intentionally overridden — ?\n'
     '2. In which phases of flight may the autothrottle be used — ?',
     '1. Reposition and HOLD the thrust lever for a minimum of 3 seconds. This causes '
     'an AT disconnect and aural warning, cancelled with the AT quick disconnect '
     'button on the power control lever.\n'
     '2. Takeoff, climb, cruise, descent and approach.',
     'AFM 4.2.1 (p 2-1-3)', 'AFCS')

card(nid(), 'TCAS II — Aural Inhibit and OEI',
     '1. RA and TA aural messages are inhibited below what radio altitude during '
     'ascent — ?\n2. ...and during descent — ?\n'
     '3. With one engine inoperative, which TCAS mode is selected — ?\n'
     '4. May the pilot deviate from an ATC clearance to comply with an RA — ?',
     '1. Ascent — inhibited below 1,100 ft radio altitude\n'
     '2. Descent — inhibited below 900 ft radio altitude\n'
     '3. One engine inoperative — select TA ONLY\n'
     '4. Yes — the pilot is authorized to deviate from ATC to the extent necessary to '
     'comply with an RA. Prompt return to the ATC cleared altitude when "CLEAR OF '
     'CONFLICT" is announced.\n'
     'NOTE: Do not maneuver on a TA alone — TA information is only an aid to visual '
     'acquisition.',
     'AFM 4.5 (p 2-1-7)', 'AFCS')

# ---------------------------------------------------------------- Powerplant
card(nid(), 'Engine Operating Limits — Thrust, N1, N2, ITT',
     'State thrust, N1, N2 and ITT limits with time limits for:\n'
     '1. Normal Takeoff — ?\n2. ATR — ?\n3. Max Continuous / Climb — ?',
     '1. Normal Takeoff — 3,420 lb · N1 104.7% · N2 100.8% · ITT 855 °C · max 5 min\n'
     '2. ATR — 3,600 lb · N1 104.7% · N2 100.8% · ITT 855 °C · max 10 min with OEI, '
     'otherwise 5 min\n'
     '3. Max Continuous / Climb — N1 104.7% · N2 100.8% · ITT 835 °C\n'
     'Oil for all three: PRESS 40-120 psi · TEMP 10-135 °C\n'
     'Except in an emergency, selecting thrust greater than NTO is PROHIBITED.\n'
     'If ATR Disarm CAS is shown, do not attempt takeoff if performance was '
     'calculated with ATR available.',
     'AFM Table 2-1-18 (p 2-1-29), 24.1 (p 2-1-28)', 'Powerplant')

card(nid(), 'Engine Transient Limits',
     'State the transient (short-duration) limits:\n1. N1 — ?\n2. N2 — ?\n'
     '3. ITT — ?\n4. Oil pressure high / low — ?\n5. Oil temperature — ?',
     '1. N1 — 105.7% (2 min)\n2. N2 — 101.5% (2 min)\n3. ITT — 855 °C (0 sec)\n'
     '4. Oil pressure — 130 psi high (max 5 min); 23 psi transient low\n'
     '5. Oil temperature — 149 °C (when operating below 80% N2 for up to 5 min)',
     'AFM Table 2-1-18 (p 2-1-29)', 'Powerplant')

card(nid(), 'Oil Pressure and Temperature Limits',
     '1. Minimum oil pressure at or above 80% N2 — ?\n'
     '2. Minimum oil pressure below 80% N2 — ?\n'
     '3. Maximum allowable oil pressure — ?\n'
     '4. Oil temp range at ground/flight idle — ?\n5. QPM oil pressure range — ?',
     '1. At or above 80% N2 — 40 psig minimum\n'
     '2. Below 80% N2 — 30 psig minimum\n'
     '3. 130 psig maximum, for 5 minutes maximum\n'
     '4. Ground or Flight Idle (continuous) — oil temp -40 to 135 °C; '
     'oil press 30 min / 120 max\n'
     '5. QPM — oil press 30-120 psi, oil temp 10-135 °C, N1 45.4%\n'
     'NOTE: Elevated oil pressure is typically observed when oil temperature is cold.',
     'AFM Table 2-1-18 (p 2-1-29)', 'Powerplant')

card(nid(), 'Zero and Negative G Limit',
     'The engine is limited to how long at zero and/or negative G, and what '
     'indication is acceptable during that time?',
     '10 seconds of continuous flight at zero and/or negative G.\n'
     'During this time it is acceptable for engine OIL PRESSURE to indicate ZERO.\n'
     'Exceeding the limit may cause engine damage from oil starvation.',
     'AFM 24.1 (p 2-1-28)', 'Powerplant')

card(nid(), 'Oil Quantity and Consumption',
     '1. Oil tank total volume — ?\n2. Oil tank fill volume — ?\n'
     '3. Oil tank usable volume — ?\n4. Maximum permissible oil consumption rate — ?\n'
     '5. Minimum level before flight — ?',
     '1. Total volume — 5.85 qt\n2. Fill volume — 5.65 qt\n3. Usable volume — 4.32 qt\n'
     '4. Max consumption — 0.032 gal/hr (0.128 qt/hr)\n'
     '5. Oil level must not be below the ADD indicator mark on the sight glass\n'
     'Approved oils: Mobil Jet II (preferred) and Mobil 254, both MIL-L-23699. '
     'Mixing approved oils when topping off is permitted.',
     'AFM 20.1, 20.2 (p 2-1-25, 2-1-26)', 'Powerplant')

card(nid(), 'High Tailwind — N1 Restriction',
     'When the tailwind component is greater than 10 kt, what N1 restriction applies?',
     'CAUTION: When the tailwind component is greater than 10 kt, do NOT exceed 60% N1 '
     'until the aircraft rolling speed is greater than the tailwind component.\n'
     'NOTE: Higher minimum throttle-up speeds up to 60% N1 may be required if the '
     'tailwind component exceeds 10 kt.',
     'AFM 24.1 (p 2-1-28), Table 2-1-19 footnote (p 2-1-31)', 'Powerplant')

card(nid(), 'Dry Motor Run — Duty Cycle Exception',
     'An engine emergency or abnormal procedure calls for a Dry Motor Run. Do the '
     '1-minute and 30-minute starter cooling waits apply?',
     'CAUTION: If any engine related emergency or abnormal procedure requires a Dry '
     'Motor Run, the Dry Motor Run may be performed WITHOUT DELAY.\n'
     'There is NO requirement to wait 1 minute (after the first start attempt) or '
     '30 minutes (after the second start attempt) before initiating the Dry Motor Run.\n'
     'Abort engine start where N1 fails to increase by 25% N2.\n'
     'Provided the table wait times are met, an indefinite number of start attempts '
     'is permitted.',
     'AFM 24.2.2, Table 2-1-19 (p 2-1-31, 2-1-32)', 'Powerplant')

card(nid(), 'Before Left Engine Start — Doors',
     'What must be confirmed about the doors before left engine start?',
     'The main passenger door and the cargo door must be CLOSED and SECURED before '
     'left engine start.',
     'AFM 24.2.1 (p 2-1-31)', 'Powerplant')

card(nid(), 'Freezing Fog — Engine Limitation',
     'Engine operation in freezing fog is prohibited below what temperature?',
     'Do NOT operate the engines in freezing fog conditions below -15 °C.',
     'AFM 24.7.2 (p 2-1-37)', 'Powerplant')

card(nid(), 'QPM — Complete Prerequisite Gate List',
     'List every condition that must be satisfied before activating Quiet Power Mode.',
     'ALL of the following must be true:\n'
     '1. Aircraft stationary with PARK BRAKE ON\n'
     '2. Ground icing conditions are NOT present\n'
     '3. NOT (visible moisture present AND TAT less than 10 °C)\n'
     '4. Crosswind / tailwind less than 20 kt (average)\n'
     '5. Only the RIGHT engine is to be operated in QPM\n'
     '6. A flight crew member seated at the controls with lap belt fastened\n'
     '7. Aircraft at Ground Idle N2, stabilized, for at least 2 min\n'
     'During QPM: thrust lever at IDLE · generator load ≤250 A · NAI must NOT be '
     'operated · right engine must exit QPM and be set to Ground Idle before left '
     'engine start.\n'
     'After QPM termination: acceleration or shutdown only after ≥2 min at Ground Idle.',
     'AFM 24.6, Fig. 2-1-8 (p 2-1-36)', 'Powerplant')

card(nid(), 'Engine Fire Protection — Dispatch',
     'May the aircraft be operated with one engine fire protection system inoperative?',
     'No. Do NOT operate the aircraft system if the left or right fire protection '
     'system is inoperative.',
     'AFM 24.4 (p 2-1-36)', 'Powerplant')

card(nid(), 'Engine Airstart — Starter Assist Limits',
     'For a starter-assisted airstart:\n1. Battery voltage to confirm — ?\n'
     '2. Airspeed limit if only battery power is available — ?\n'
     '3. N2 required before selecting RUN — ?\n4. When must you not airstart at all — ?',
     '1. BAT 2 — Confirm ON / above 23.0 V. If <23.0 V, consider a windmill airstart.\n'
     '2. CAUTION: If ONLY battery power is available (after loss of all generated '
     'power), only a starter-assisted airstart is permitted, and airspeed must be '
     '≤150 KIAS (ensuring N2 <10%). Attempting a starter-assisted airstart above '
     '150 KIAS may cause loss of BOTH FADEC channels.\n'
     '3. ENG switch — check N2 below 24%, then select RUN.\n'
     '4. Do NOT airstart if engine integrity is in question or after an engine fire.',
     'AFM 3-NAE-03 (p 3-3-3)', 'Emergency knowledge')

card(nid(), 'Engine Fire — Second Extinguisher',
     'After firing the first extinguisher bottle and the fire CAS message remains:\n'
     '1. What confirms the second bottle is available — ?\n'
     '2. May the engine be restarted after a confirmed fire — ?',
     '1. CONFIRM green "2" illuminated approximately 30 sec after firing the first '
     'extinguisher, then push the associated EXTINGUISHER push button.\n'
     '2. CAUTION: Do NOT restart the engine after a confirmed engine fire.\n'
     'Also: BLEED Rotary Selector — select operating engine side; FUEL — monitor '
     'balance; FUEL X-FEED should be closed prior to landing; Aircraft — land as soon '
     'as possible.',
     'AFM 3-FIRE-01 (p 3-15-1)', 'Emergency knowledge')

# ---------------------------------------------------------------- Icing
card(nid(), 'Wing Anti-Ice (WAI) — Inhibit and Limits',
     '1. WAI is inhibited under what two conditions — ?\n'
     '2. Above what TAT must WAI not be operated — ?',
     '1. WAI is inhibited when: TAT >15 °C, or the aircraft is on the ground.\n'
     '2. Do NOT operate WAI with a TAT of more than 10 °C, unless required by the '
     'presence of icing conditions.',
     'AFM 15.2 (p 2-1-20)', 'Icing')

card(nid(), 'Windshield Emergency Heat — Limits',
     'When must windshield emergency heating not be operated?',
     'Do NOT operate windshield EMERGENCY heating on the ground, or when TAT is '
     '>10 °C.',
     'AFM 15.3 (p 2-1-20)', 'Icing')

card(nid(), 'Flaps in Icing Conditions',
     '1. Maximum flap extension in icing — ?\n'
     '2. Flap setting for approach and landing in active icing — ?\n'
     '3. Retraction limit with ice on the lifting surfaces — ?',
     '1. Do NOT extend the flaps beyond 15° in icing conditions.\n'
     '2. Use FLAPS 15 for approach and landing in current icing conditions (ice '
     'detectors indicating ICE or pilot assessment). Do NOT use Flaps 33 for landing '
     'in current, active icing conditions.\n'
     '3. Do NOT retract the flaps below 8° if signs of ice are present on the lifting '
     'surfaces.\n'
     'Minimum airspeed with flaps retracted in icing — 150 KIAS.',
     'AFM 16.3 (p 2-1-21)', 'Icing')

card(nid(), 'Severe Icing — Visual Cues and Autopilot',
     '1. Name the two visual cues that require you to immediately exit icing.\n'
     '2. What is the autopilot limitation in severe icing — ?',
     '1. Immediately exit icing conditions if either cue exists:\n'
     '  • Unusual, extensive ice accumulation on the airframe or on the cockpit SIDE '
     'WINDOWS\n'
     '  • Excessive accumulation of ice BEYOND the wing protected leading edge\n'
     '2. Do NOT engage the autopilot in severe icing conditions. When the AP is used '
     'in icing, periodically disengage it to check for abnormal forces — tactile cues '
     'such as increased aileron force can be masked by the autopilot.',
     'AFM 16.4, 16.5 (p 2-1-21)', 'Icing')

card(nid(), 'Icing — Wing Check, Holding, and SWPS Override',
     '1. What must the pilot periodically check while flying in icing — ?\n'
     '2. What holding restriction applies in icing — ?\n'
     '3. When must the SWPS ICE OVRD not be used — ?',
     '1. WARNING: THE PILOT SHALL PERIODICALLY CHECK THE LEFT WING UPPER SURFACE ON A '
     'REGULAR BASIS WHILE FLYING IN ICING CONDITIONS TO ENSURE THERE IS NO UNUSUAL ICE '
     'ACCUMULATION.\n'
     '2. Extended holding in icing conditions on a SINGLE BLEED SOURCE is not allowed.\n'
     '3. Do NOT operate the SWPS ICE OVRD push button / SWPS ICE MODE rotary selector '
     'if there are signs of ice on the wings.',
     'AFM 16, 16.2, 16.6 (p 2-1-20, 2-1-21)', 'Icing')

card(nid(), 'Takeoff with Contamination / Freezing Precipitation',
     '1. What inspection is required before takeoff if contamination is suspected — ?\n'
     '2. What must you do on encountering freezing rain or freezing drizzle — ?\n'
     '3. May you operate into an airport reporting freezing rain — ?',
     '1. Do NOT take off if there are signs of ice, snow or frost on the lifting '
     'surfaces. A VISUAL AND TACTILE inspection of the wing leading edge and upper '
     'wing surface must be conducted.\n'
     '2. Immediately EXIT the freezing rain or freezing drizzle by changing altitude '
     'or course.\n'
     '3. No. Do NOT operate into airports reporting freezing rain or freezing drizzle.\n'
     'Approved fluids: AMS 1424/1 Type I and AMS 1428/1 Types II, III and IV.',
     'AFM 16, 16.1 (p 2-1-20)', 'Icing')

card(nid(), 'NAI — Minimum On Time',
     'Why is NAI recommended to remain on for a minimum period once activated, and '
     'how long?',
     'NOTE: Turning NAI on and off in quick succession in flight may cause a '
     '"No Dispatch" annunciation. It is recommended that NAI remains ON for a minimum '
     'of 2 MINUTES when activated, to let the Tt2 sensor heat stabilize and clear all '
     'moisture from the probe.\n'
     'Anticipate ice-crystal icing by operating NAI near unstable cumuliform '
     '(convective) and high-altitude stratiform clouds.',
     'AFM 24.7.1 (p 2-1-37)', 'Icing')

card(nid(), 'Ice Detection and Wing Inspection Light',
     '1. Is the PFID system operative on the ground — ?\n'
     '2. When must the wing inspection light be operational — ?',
     '1. No. The PFID system is not operative on the ground, as ice detector signals '
     'are not available on the ground. Signals become available as soon as the aircraft '
     'is in the air.\n'
     '2. The wing inspection light must be operational if flying into known icing '
     'conditions at night, or if known icing conditions are forecast at night.',
     'AFM 15.4, 15.5 (p 2-1-20)', 'Icing')

# ------------------------------------------------- Secondary flight controls
card(nid(), 'Airbrake Limitations',
     '1. May you land with the airbrake extended — ?\n'
     '2. By what height must the airbrake be stowed on approach — ?',
     '1. No. Do NOT attempt to land with the airbrake extended.\n'
     '2. Use of the airbrake on approach is permitted provided the aircraft is on a '
     'STABLE approach and the airbrake is stowed NO LATER THAN 50 ft AGL.',
     'AFM 26.1 (p 2-1-39)', 'Flight controls')

card(nid(), 'Flap and Stab Trim Limitations',
     '1. Above what altitude must flaps not be operated in flight — ?\n'
     '2. Is landing with Flaps 0° or 8° permitted — ?\n'
     '3. When may secondary stab trim be used — ?',
     '1. Do NOT operate the flaps in flight above 20,000 ft.\n'
     '2. Landing with Flaps 0° or 8° is PROHIBITED unless the flaps have failed.\n'
     '3. Do NOT use secondary stab trim unless the primary stab trim has failed.',
     'AFM 26.2, 26.3 (p 2-1-39)', 'Flight controls')

card(nid(), 'Maneuver Limits and Bank Angle',
     '1. Are acrobatic maneuvers or spins authorized — ?\n'
     '2. To what bank angle is operation limited — ?\n3. Load factor limits — ?',
     '1. No acrobatic maneuvers, including spins, are authorized.\n'
     '2. Operation is limited to maneuvers incident to normal flying, stalls (except '
     'whip stalls) and steep turns with bank angle NOT MORE THAN 60°.\n'
     '3. Flaps up +3.0 g / -1.2 g · Flaps down +2.0 g / -0.0 g',
     'AFM 19.3, 19.4 (p 2-1-24)', 'Flight controls')

card(nid(), 'Landing — Nose Landing Gear Unlocked',
     'Nose L/G indicates unlocked. State the key actions.',
     '1. L/G position — attempt to confirm by exterior means\n'
     '2. CPCS DUMP pushbutton — when below 10,000 ft AMSL, push to DUMP\n'
     '3. Landing configuration — FLAPS 33°\n'
     '4. Aircraft — touch down with normal landing attitude, gently lower the nose to '
     'the ground while the elevator remains effective; do NOT use the brakes until the '
     'nose gear is on the ground\n'
     'If L/G collapses during touchdown or if considered appropriate — accomplish '
     'Emergency Evacuation 3-EVAC-01.\n'
     'NOTE: Consider pressing AURAL DISABLE to suppress "Gear Gear" and TAWS callouts.',
     'AFM 3-NAE-18 (p 3-6-x)', 'Emergency knowledge')

# ---------------------------------------------------------------- Brakes/tires
card(nid(), 'Brake Cooling Requirement',
     'After which two events must the aircraft remain on the ground for a cooling '
     'period, and for how long?',
     'The aircraft must remain on the ground for at least 120 MINUTES following '
     'either of these events:\n'
     '• Rejected takeoff with brake-on speed greater than VR - 20 kt AND heavy brake '
     'usage\n'
     '• 0° flap full-stop landing AND heavy brake usage',
     'AFM 7.1 (p 2-1-15)', 'Brakes & gear')

card(nid(), 'Tire Limits and Towing',
     '1. Maximum permissible tire speed — ?\n2. What type must the nose tire be — ?\n'
     '3. Maximum weight of a towbar-less tug — ?',
     '1. 165 kt groundspeed\n'
     '2. The nose tire must be a "DUAL CHINE" tire\n'
     '3. 5,379 lb (2,440 kg)\n'
     'NOTE: Tug weight influences the force on the nose landing gear if the '
     'towbar-less tug needs to brake.',
     'AFM 7.2, 18 (p 2-1-15, 2-1-22)', 'Brakes & gear')

# ---------------------------------------------------------------- Fuel
card(nid(), 'Fuel Quantity — Full Table',
     '1. Total quantity — ?\n2. Usable quantity — ?\n3. Max permissible imbalance — ?\n'
     '4. Unusable fuel quantity — ?\n5. On what density are these based — ?',
     '1. Total — 895 gal (3,389 l) / 5,999.8 lb (2,721 kg)\n'
     '2. Usable — 890 gal (3,369 l) / 5,964 lb (2,705 kg)\n'
     '3. Max imbalance — 49 gal (189 l) / 330 lb (150 kg)\n'
     '4. Unusable — 5.3 gal (20 l) / 35 lb (16 kg)\n'
     '5. Based on fuel temp 59 °F (15 °C) and density 6.7 lb/gal (0.803 kg/l). '
     'The weight values are not limiting — higher fuel weights are permitted provided '
     'the aircraft stays within the weight limits.',
     'AFM Table 2-1-14 (p 2-1-18)', 'Fuel')

card(nid(), 'Refueling and Defueling Limits',
     '1. Maximum refueling pressure — ?\n2. Maximum defueling suction pressure — ?\n'
     '3. What must be done with the refuel power switch before departure — ?',
     '1. Maximum refueling pressure — 60 psi\n'
     '2. Maximum defueling suction pressure — 10 psi\n'
     '3. The power switch (PWR - REFUEL / DEFUEL) must be OFF and GUARDED prior to '
     'departure',
     'AFM 13.8 (p 2-1-18)', 'Fuel')

card(nid(), 'Approved Fuel Grades — Full List',
     'List every approved fuel grade with its specification.',
     'Jet A — ASTM D1655\nJet A-1 — ASTM D1655\nJP-8 — MIL-DTL-83133\n'
     'TS-1 — GOST 10227\nChinese No. 3 — GB 6537-2018\n'
     'For Chinese No. 3, these additives are PROHIBITED on the PC-24: T1502 '
     '(antistatic), T1602 (antiwear), Ethylene Glycol Methyl Ether (anti-icing).\n'
     'NOTE: Fuel meeting ASTM D7566 (synthesized hydrocarbons), redesignated as '
     'ASTM D1655, is acceptable.\n'
     'The electric fuel booster pumps and the fuel crossfeed valve must be OPERATIVE. '
     'Fuel temp limits -40 °C to +80 °C.',
     'AFM 13.1, 13.2 (p 2-1-17)', 'Fuel')

# ---------------------------------------------------------------- Oxygen
card(nid(), 'Oxygen System — Additional Limits',
     '1. Minimum quantity for dispatch — ?\n'
     '2. Below what altitude may the oxygen saver function not be used — ?\n'
     '3. Maximum cabin altitude for passenger masks — ?\n'
     '4. PBE cockpit temperature limit — ?\n'
     '5. Crew mask press-to-test temperature limit after cold soak — ?',
     '1. 680 liters (and, above 25,000 ft MSL pressurized, 10 min supply per occupant)\n'
     '2. Do NOT use the oxygen saver function below 25,000 ft\n'
     '3. Passenger oxygen masks are limited to a maximum cabin altitude of 40,000 ft\n'
     '4. Do NOT operate the PBE when cockpit temperature is ≤-29 °C (≤-20 °F)\n'
     '5. After ground cold soak, do NOT operate the crew oxygen mask press-to-test / '
     'reset button when cockpit temperature is ≤-12 °C (≤10 °F)\n'
     'Cylinder must be filled with Aviators Oxygen per MIL-PRF-27210.',
     'AFM 23.1 (p 2-1-28)', 'Oxygen')

card(nid(), 'Oxygen — High Field Mode',
     'What oxygen requirement applies when High Field Mode is active?',
     'Single pilot operations — the pilot is required to use oxygen CONTINUOUSLY when '
     'High Field Mode is active.\n'
     'Multi pilot operations — at least ONE pilot is required to use oxygen '
     'continuously when High Field Mode is active.',
     'AFM 23.2 (p 2-1-28)', 'Oxygen')

# ---------------------------------------------------------------- Cabin/loading
card(nid(), 'Cabin Pressurization — Warning Range',
     'Between what values does the maximum cabin NEGATIVE pressure differential '
     'exceedance warning occur?',
     'The negative differential warning occurs between -0.3 and -0.6 psid.\n'
     'Limits: max positive differential 9.27 psid · max negative -0.3 psid · '
     'max differential for takeoff and landing 0.7 psid.',
     'AFM 8 (p 2-1-15)', 'Cabin & loading')

card(nid(), 'Baggage vs Cargo — Definitions and Securing',
     '1. What mass distinguishes baggage from cargo — ?\n'
     '2. How must each be secured — ?\n3. Minimum tie-down strap strength — ?\n'
     '4. What may be stowed unstrapped — ?',
     '1. Baggage is any item ≤66 lb (30 kg). Cargo is any item >66 lb (30 kg).\n'
     '2. Baggage must be stowed in the restraint system (baggage net). Cargo must be '
     'tied down to the seat rails and secured individually with an approved cargo '
     'tie down, against a retaining bar secured laterally to the seat rails.\n'
     '3. Tie-down straps with a breaking strength of at least 1,800 lb per strap.\n'
     '4. Items up to a total weight of 66 lb (30 kg) may be stowed in the cabin '
     'unstrapped, provided a cargo net is installed in front of them.\n'
     'No cargo on the seats; cargo must permit free access to the passenger door and '
     'the emergency overwing exits.',
     'AFM 6, 6.2 (p 2-1-12, 2-1-15)', 'Cabin & loading')

card(nid(), 'Baggage / Cargo Clearance and Cargo Door',
     '1. Clear area forward of the LARGE baggage restraint — ?\n'
     '2. Clear area forward of the SMALL baggage restraint — ?\n'
     '3. Clear area in front of cabin cargo — ?\n'
     '4. Crosswind limit for cargo door operation / loading — ?',
     '1. 9.1 in (250 mm) forward of the large baggage restraint system\n'
     '2. 7.5 in (190 mm) forward of the small baggage restraint system\n'
     '3. 4 in (100 mm) in front of the cargo in the cabin\n'
     '4. Do NOT open / close the cargo door or perform cargo loading operations in '
     'crosswinds exceeding 60 kt\n'
     'A life raft carried in the baggage area must be properly secured and, when '
     'required by operating regulations, accessible in flight.',
     'AFM 6, 6.1 (p 2-1-12, 2-1-13)', 'Cabin & loading')

card(nid(), 'Passenger Seating by Configuration',
     'State the maximum number of passengers for:\n1. Executive interiors — ?\n'
     '2. EX-5S-DIV-1 — ?\n3. EX-5S-COM-1S-DIV-1 and EX-6S-DIV-1 — ?\n'
     '4. Commuter interior — ?\n5. What restrictions apply to children and divans — ?',
     '1. Executive interiors — 8 passengers (one per seat); optional fit allows two '
     'additional infants at the first seating row, left and right\n'
     '2. EX-5S-DIV-1 — 7 passengers (one per seat, two on the divan)\n'
     '3. EX-5S-COM-1S-DIV-1 and EX-6S-DIV-1 — 8 passengers (one per seat, two on the '
     'divan)\n'
     '4. Commuter interior — 10 passengers (one per seat)\n'
     '5. Children only allowed in rows 1 and 2. During taxi, takeoff and landing: no '
     'occupant in the forward divan seat; no infants or children in the divan seats; '
     'no pregnant women in the divan seats (aft-facing executive seats recommended).\n'
     'In single pilot operation an additional passenger may occupy the RH cockpit seat.',
     'AFM 19.5 (p 2-1-25)', 'Cabin & loading')

# ---------------------------------------------------------------- Electrical / CB
card(nid(), 'Battery Charging Voltage Ceiling',
     'The voltage for charging the batteries must not exceed what value?',
     'The voltage for charging the batteries must not exceed 32 V.\n'
     'Related: generator max voltage 29.5 Vdc · GPU 25.0-29.5 Vdc · min voltage to '
     'charge batteries 28.0 Vdc · max voltage to charge batteries 29.5 Vdc.',
     'AFM 11.2 (p 2-1-16)', 'Electrical')

card(nid(), 'Circuit Breakers — Reset Rules',
     '1. May CBs be reset in flight — ?\n'
     '2. How many reset attempts on an Essential Bus CB, and under what conditions — ?\n'
     '3. What does "reset" mean procedurally — ?\n'
     '4. Where must extreme caution be exercised — ?',
     '1. Do NOT reset CBs in flight, EXCEPT when required by a procedural step in '
     'Section 3, 3A or 4, or if the PIC judges the reset necessary for safe completion '
     'of the flight.\n'
     '2. Only ONE attempt, if the PIC determines the system is needed for safe '
     'completion of that flight, after at least ONE MINUTE has elapsed since the trip, '
     'and only if there is no remaining smoke or burning smell.\n'
     '3. Reset = OPEN (pull out) the CB, wait approximately 2 seconds, then CLOSE '
     '(push in). If a CB is found already open, reset means simply close it.\n'
     '4. Fuel pumps and/or fuel quantity indication systems — arcing might ignite fuel '
     'or fuel vapors.',
     'AFM 9 (p 2-1-15), Section 3 General (p 3-1-1)', 'Electrical')

# ---------------------------------------------------------------- General ops
card(nid(), '"Land as Soon as Possible" vs "Practical"',
     'Define the two AFM landing urgency terms.',
     'LAND AS SOON AS POSSIBLE — land without delay at the nearest airport where a '
     'safe approach and landing is reasonably assured.\n'
     'LAND AS SOON AS PRACTICAL — the landing airport and duration of flight are at '
     'the discretion of the pilot. Extended flight beyond the nearest suitable airport '
     'is not recommended.',
     'AFM Section 3 General (p 3-1-1)', 'General ops')

card(nid(), 'Memory Items — Definition and Marking',
     'How does the AFM define a memory item, and how are memory items marked?',
     'A memory item is a check for an abnormal or emergency situation that requires '
     'IMMEDIATE action and is therefore carried out from memory, without prior '
     'reference to a checklist. Memory items are executed by heart without referring '
     'to a checklist. A specific checklist may be required to complete the action if '
     'the memory items cover only the initial actions.\n'
     'Memory items are denoted by a SOLID RED BOX around specific challenge and '
     'response items.',
     'AFM Section 3 General §3, Section 3A General §3', 'General ops')

card(nid(), 'Minimum Flight Crew and Kinds of Operation',
     '1. Minimum required flight crew — ?\n2. Certification category — ?\n'
     '3. Approved kinds of operation — ?',
     '1. One pilot in the LEFT HAND seat.\n'
     '2. Commuter Category (approved based on CS-23 through Amendment 3).\n'
     '3. VFR Day · VFR Night · IFR Day including automatic approaches to CAT I '
     'minimums, single pilot · IFR Night including automatic approaches to CAT I '
     'minimums, single pilot · Flight Into Known Icing (FIKI).\n'
     'All installed equipment shall be operative at dispatch (normally indicated by '
     'the absence of CAS messages) unless an approved (M)MEL is used.',
     'AFM 12, 17 (p 2-1-17, 2-1-22)', 'General ops')

card(nid(), 'Required Documentation On Board',
     'Which documents must be aboard in PAPER, and which may be electronic or paper?',
     'PAPER (hard copy), readily accessible to the pilot:\n'
     '• PC-24 Airplane Flight Manual (AFM) Report No. 02371, Cockpit Handbook '
     'Volumes 1 and 2\n'
     'ELECTRONIC (digital) OR PAPER, for reference:\n'
     '• PC-24 Quick Reference Handbook (QRH) Report No. 02382\n'
     '• Advanced Cockpit Environment (ACE) Avionics System Pilot\'s Guide applicable '
     'to that serial number\'s software/hardware configuration\n'
     '• PC-24 Flight Crew Operating Manual (Document No. 02383)\n'
     'The AFM must be carried in the airplane at all times.',
     'AFM 2 (p 2-1-1)', 'General ops')

card(nid(), 'Wet Runway — Definition',
     'How does the AFM define a wet runway?',
     'A runway whose surface is covered with a layer of water LESS THAN 1/8 in (3 mm) '
     'in depth, or the equivalent amount of a related substance, or has a sufficient '
     'level of moisture to give a REFLECTIVE APPEARANCE — but WITHOUT any significant '
     'area of standing water.\n'
     'Approved surfaces: dry and wet paved runways. Contaminated paved runways per AFM '
     'Supplement 02442. With the gravel kit (stone guard) installed: dry/wet prepared '
     'dirt-sand-gravel per Supplement 02444, dry/wet prepared grass per Supplement '
     '02473.',
     'AFM 3 (p 2-1-1)', 'General ops')

card(nid(), 'Extended Temperature Envelope — Minimum Mach',
     'For the extended operating temperature envelope (OAT < -65 °C), state the '
     'minimum operating speed for each temperature.',
     '-66 °C — 0.59 M\n-67 °C — 0.62 M\n-68 °C — 0.65 M\n-69 °C — 0.68 M\n'
     '-70 °C — 0.70 M\n-71 °C — 0.73 M\n'
     'The minimum operating speed provides adequate aerothermodynamic heating to '
     'maintain minimum skin and local ambient (zone) temperatures.\n'
     'Sea level limits: min OAT -54 °C (-65 °F) · max OAT +50 °C (122 °F). '
     'Max operating altitude 45,000 ft (13,716 m).',
     'AFM 22.2 (p 2-1-26)', 'General ops')

card(nid(), 'RVSM — Required Equipment and Critical Area',
     '1. What equipment must be operational to enter RVSM airspace — ?\n'
     '2. What are the dimensions of the RVSM critical area — ?\n'
     '3. May the ESIS be used for RVSM — ?',
     '1. Two primary Air Data Systems (ADS) · one flight controller KMC 9200A with '
     'altitude pre-selector · one automatic flight control system · one altitude '
     'reporting transponder KXP 2290A.\n'
     '2. An area 24 in (0.6 m) FORWARD, and 12 in (0.3 m) above, below and AFT of the '
     'pitot-static tube — must be free of paint ridges/flaking, dents, skin '
     'deformation/delamination, loose or missing rivets and fasteners, nicks, '
     'scoring/scratches and corrosion. Nose doors closed and latched, panel edges '
     'flush.\n'
     '3. No. The ESIS has not been demonstrated to meet RVSM performance requirements '
     'and shall only be used for emergency procedures.',
     'AFM 25 (p 2-1-37, 2-1-38)', 'General ops')

card(nid(), 'FMS — Conditions for Instrument Approaches',
     'Use of the FMS to conduct instrument approaches is permitted provided what five '
     'conditions are met?',
     '• The reference coordinate datum system for the approach is WGS-84, AND\n'
     '• The approach is an approved instrument approach procedure, AND\n'
     '• The approach is retrieved from the FMS database, AND\n'
     '• APP (approach active) mode is annunciated at the Final Approach Fix, AND\n'
     '• The approach is NOT any of these prohibited types: ILS, LOC, LOC-BC, LDA, '
     'SDF, MLS\n'
     'FMS use for IFR requires the most current database update cycle. The PIC must '
     'verify FMS-managed speeds do not violate published procedural speeds.',
     'AFM 4.3.1, 4.3.2 (p 2-1-4)', 'General ops')

card(nid(), 'VNAV / LNAV Approach Limitations',
     '1. What must remain the primary altitude reference when using VNAV — ?\n'
     '2. Which minimums are controlling — ?\n'
     '3. What is the CAUTION about the VNAV deviation indicator — ?',
     '1. The BAROMETRIC ALTIMETER must be used as the primary altitude reference at '
     'all times.\n'
     '2. The published LNAV/VNAV minimums on the approach chart are controlling; all '
     'operations below them must be conducted by outside visual reference. On an LNAV '
     'approach using FMS vertical guidance, never descend below the published LNAV MDA '
     'unless the required runway visibility exists.\n'
     '3. CAUTION: Due to the large tolerances of the Vertical Navigation system, the '
     'deviation indicator must NOT be relied on when operating below the applicable '
     'published minimum.',
     'AFM 4.3.3 (p 2-1-4)', 'General ops')

card(nid(), 'Water Waste System Limitation',
     'When must the water waste system not be operated or serviced?',
     'If installed, do NOT operate the Water Waste System in flight or on the ground '
     'if the cabin temperature is ≤2 °C (≤36 °F).\n'
     'Do NOT service the system in freezing conditions — if servicing is required, it '
     'must be done in a heated hangar.',
     'AFM 28 (p 2-1-41)', 'General ops')

card(nid(), 'Portable Electronic Devices',
     'What are the limitations on passenger electronic device and wireless use?',
     'Use of Portable Electronic Devices is permitted during ALL phases of flight.\n'
     'There are NO limitations on the use of wireless systems, including Wi-Fi, '
     'Bluetooth and cellular systems (GSM, UMTS/3G, LTE/4G).',
     'AFM 27.1 (p 2-1-40)', 'General ops')

card(nid(), 'Dynamic Speed Bug and Stall Warning — Advisory Only',
     'What is the status of the Dynamic Speed Bug, low speed awareness and stall '
     'warning systems, and what must you rely on instead?',
     'They are for ADVISORY USE ONLY. Maintain a safe stall margin based on the Stall '
     'Speed charts in Section 5 (Performance) of the AFM.\n'
     'NOTE: Use of "PITCH ATTITUDE HOLD" mode is recommended during operation in '
     'severe turbulence.',
     'AFM 4.1, 4.2.1 (p 2-1-2)', 'General ops')

card(nid(), 'TOLD — Advisory Status and Exclusions',
     '1. What is the status of TOLD calculations — ?\n'
     '2. Name the four Section 5 exceptions TOLD does not cover.\n'
     '3. Does TOLD consider terrain for climb performance — ?',
     '1. ADVISORY PURPOSES ONLY — it must always be cross-referenced against the AFM '
     'or other certified performance calculation software.\n'
     '2. (a) Acceleration and final segment for OEI climb procedure (b) consideration '
     'of turns in the OEI climb procedure for obstacle clearance (c) cold temperature '
     'compensation below standard temperatures (d) abnormal landing scenarios such as '
     'system failures and emergency landings.\n'
     '3. No — TOLD does not consider terrain data for climb performance. It is the '
     'operator\'s responsibility to determine the most limiting obstacle.\n'
     'TOLD does not support Supplements 02442, 02444, 02451, 02457 or 02473.',
     'AFM 4.4 (p 2-1-6)', 'General ops')

data = [{'id': c['id'], 'title': c['title'], 'front': c['front'],
         'back': c['back'], 'reference': c['reference'], 'topic': c['topic']}
        for c in C]
json.dump(data, open('afm_cards.json', 'w'), ensure_ascii=False, indent=1)

topics = {}
for c in data:
    topics.setdefault(c['topic'], []).append(c['id'])
print(f'built {len(data)} AFM cards')
for t, ids in topics.items():
    print(f"  {t:22} {len(ids):>2}  {ids[0]}..{ids[-1]}")
