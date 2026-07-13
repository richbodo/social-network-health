# SNH Check-in Protocol — Design Note
### "Proactive Peer Check-ins"

**Status:** v0.2 (2026-07-09) — grilled and promoted. Proposed by Rich out of the
project's memoriams postvention practice; drafted with corpus evidence by the snhdb
research agent (v0.1, 2026-07-08); anonymized, staged, and extended with the phone-tree
design same day (v0.1.1); all ten open design questions resolved in the 2026-07-08/09
grill (log: `brainstorms/20260708-checkin-protocol-grill.md`, gitignored). Remaining open
questions below are implementation-stage, not design-stage.
Companion notes: `notification-protocol.md` (this protocol is the outbound complement to
that note's inbound help-seeking, a humane implementation of its deferred
"analysis-initiated triggers" class, and shares its coordinator);
`../research_library/memoriams.md` (the anonymized postvention study behind the origin);
`../measurement/egocentric_to_community_network_health_research_note.md` (the consented
metrics substrate for Tier-C triggers).

---

## Origin

As part of our postvention practice, project members have studied and discussed suicides
attributed among open-source software contributors. The anonymized public summary of that
work is [`../research_library/memoriams.md`](../research_library/memoriams.md); the named
case records behind it are deliberately private. Two facts recur across the discussed
cases and shape this design:

1. **Radio silence was the warning signal that existed.** The member had gone quiet —
   stopped contributing, stopped answering messages — and the silence was raised by
   another community member only after it was too late to act on.
2. **The last contacts were purely technical.** The communities had structural bandwidth
   for code review and none for human review.

Community writing that followed one such loss proposed a practice, not a system: check in
on each other regularly, as people, and value the person maintaining the code above the
code. This note formalizes that practice into a protocol a community can actually run.

## Purpose & thesis

The notification protocol's thesis is one-button **help-seeking**: reduce the friction of
*asking*. But the people at highest risk often don't ask — they withdraw (threat catalog
RF1/K1 framing: those who most need help have the weakest ego networks, and withdrawal is
itself the symptom). A help-seeking button cannot reach someone who has stopped reaching.

**Thesis:** *regular, normalized, low-friction peer check-ins (a) strengthen the bonds
that are themselves protective, and (b) create routine occasions where deterioration and
withdrawal get noticed while there is still time to act.* Check-ins are not surveillance
and not diagnosis; they are scheduled human contact with a light escalation path.

## Scope (decided)

**v1 targets open-source and volunteer communities**; remote teams are v2. Four reasons:
the origin evidence is OSS-shaped; OSS activity signals are already public, shrinking the
Stage-2 surveillance surface to reading what is visible; power asymmetry is opt-in rather
than structural (no reporting lines by default); and deploying a suicide-adjacent
practice inside an employer raises HR/duty-of-care/liability questions on day one — the
worst environment in which to learn Stage 1. Remote teams inherit the protocol at v2 with
employer-context gates (Tier-B signals, Stage-3 legal review).

## Actors & roles

- **Member** — anyone participating in the community (contributor, teammate).
- **Checker** — a member who has agreed to do check-ins **and been chosen by the member
  they check on** (the phone tree below). Accepting a nomination means accepting the
  checker guidelines and the negotiated cadence — a two-party commitment.
- **Mentor** — a trained helper **elected by aggregate secret nomination** (votes never
  visible, so nobody is rejected), with declared capacity, serving members who did not
  nominate them; mentors staff the starter-checker pool. The second helper layer.
- **Operator (Stage 2)** — the technical host of the coordinator. Holds pairings and
  timestamps; has **no escalation authority** and no visibility into anything else. Not
  the steward.
- **Steward (Stage 3)** — accountable human: escalation rung, crisis-resource list,
  liability review. **Stages 1–2 run stewardless by design**; there may be communities
  that never add one.
- **Coordinator (Stage 2, software)** — schedules rotation and nudges checkers; holds the
  minimum state (who checks whom, when last checked — never content). Shared with the
  notification protocol (below).

## Protocol

### The phone tree — chosen checkers

Each member picks the people — **one or more, ideally three or more** — from whom they
would *like* to receive a check-in and have a real conversation from time to time. A
nomination is an invitation: the nominee accepts (becoming one of that member's checkers)
or lets it lapse. **Members name their checkers; nobody is assigned one.** The evidence
(end of note): the protective association in the flagship prevention programs runs
through *named* connections, and top-down assignment overlaps only 13–23% with
network-optimal selection while sitting farther from the at-risk.

Decided mechanics:

- **Capacity negotiation at acceptance.** Checker willingness is a quantity ("I can do
  quarterly"). A member wanting monthly coverage from quarterly-capacity checkers needs
  about three; the tree's math is visible to the member, who recruits accordingly. A sole
  checker carries the floor minimum alone.
- **Rotation.** One checker is nudged per cadence tick, rotating through the member's
  accepted checkers — the member gets one genuine contact per tick (not an alarm chorus),
  each bond refreshes at its own rhythm, and a lapsed checker costs a month, not the tree.
  Stewardless Stage 1 form: "you take January."
- **Mutual visibility: default OFF, double-consent.** A member's checkers learn of each
  other only if: each checker consents to being visible → only consenting checkers enter
  the visibility group → and the group exists at all only if the member also consents.
  Members who decline visibility accept weaker non-response detection (no
  "did-you-get-through-either" channel).
- **No structural reciprocity.** Member (receives) and checker (gives) are separate
  opt-ins; requiring symmetry would price out exactly the people in rough patches who
  most need checkers. Reciprocity is a norm to encourage, never a rule.
- **Declines are quiet lapses.** An unaccepted nomination expires after a fixed window;
  an explicit decline is indistinguishable from a lapse, and no reason is recorded or
  requested. The nominator's actionable information is identical either way: invite
  someone else. (A nominee who wants to explain can, personally, outside the protocol.)
- **In-community checkers for v1.** Shared context is the detection mechanism — you
  cannot notice project withdrawal from outside the project. Outside arrangements
  (family, old friends) are blessed as private practice the protocol never sees.
- **Spokes are the primitive; pods are emergent.** The check-in act is 1:1 (candor falls
  with audience size; the format literature is honestly mixed — see evidence). When
  three people all nominate each other a pod exists de facto; the protocol needs no pod
  object.

### Roster gaps — three-tier visibility (stewardless)

The members with no accepted checker are the highest-risk cell (the "adult-isolated"
analog), and noticing them must not stigmatize them:

1. **Tree health → visible to the tree.** "You asked monthly; your accepted checkers
   cover quarterly" is visible to the member and their accepted checkers only.
2. **Roster health → community aggregate, counts only.** N members, M% with ≥1 accepted
   checker, capacity shortfall yes/no — never names. This replaces the steward's gap duty
   for Stages 1–2 and drives open-call recruitment ("we need more checker volunteers").
3. **Individual gaps → member-actionable only.** A member with no one to nominate may
   request a **starter checker** from the mentor pool — self-initiated, so the contact
   carries no "we noticed nobody chose you" payload. Recruitment is never targeted at the
   unchosen; a targeted approach *is* the roster-gap-stigma threat firing.

Residual, stated honestly: a member who nominates no one, requests nothing, and opts out
is unreachable by this protocol at Stage 1. That is the right-to-silence boundary; the
notification protocol's one-button ask and community norms are the complement. A Stage-3
confidential steward gap view remains an open cost/benefit question.

### Cadence (decided)

**Member-chosen, monthly default, quarterly floor, checker-agreed at acceptance.**
Monthly catches a one-month drift while it is still a drift (the memoriams silences ran
months) and keeps checker load near one check-in sent per week in a balanced tree. The
floor exists because "I set mine to yearly" is opt-out-by-neglect — invisible in a way
explicit opt-out (which remains a right) is not. Release-cycle alignment is a project
skin, not protocol semantics. No steward involvement in cadence. (No direct corpus
evidence on frequency — monthly is a judgment call, flagged as such.)

### Trigger classes

Same state machine, three ways in:

1. **Cadence check-ins** — the default and Stage 1's entirety; normalization is the
   point. A check-in that only arrives when someone seems off is an alarm, not a
   relationship.
2. **Absence-triggered (Stage 2)** — the recurring memoriams pattern. Consented signal
   goes quiet beyond the member's own declared baseline → the coordinator nudges the
   rotation's current checker: "it's been a while — reach out." The nudge carries no
   inference, only elapsed time.
3. **Event-triggered** — after known acute stressors: heated conflict/fork, brutal
   release crunch, public failure, a nearby departure or loss. May be fired manually by
   anyone in the tree from Stage 1.

### Absence signals (decided)

- **Tier A — v1:** public project activity, **timestamps only** — commits, PR/issue
  activity, public chat/forum posts; the member selects which count. The activity is
  already public: consent adds aggregation-into-a-clock, not new access. Presence, never
  content.
- **Tier B — v2 (remote teams):** attendance/private presence data. Same *kind* of signal
  as Tier A (shared non-output presence); deferred because it is employer-shaped and
  often absent for OSS developers — an availability distinction, not a danger class.
- **Tier C — external trigger sources only.** The check-in protocol computes nothing
  content-derived, ever. Where the egocentric→community measurement protocol runs, its
  consented encrypted metrics may fire a trigger into this protocol via the
  release-only-to-chosen-checkers path (below). Communities running only check-ins never
  build content-analysis machinery at all.
- **Member controls:** the baseline is member-declared ("nudge my checkers at six weeks
  dark"), and members may **pause the clock** ("away until September") with no reason
  required — the pathologizing-absence mitigation.

**Invariant:** *the only signal this protocol ever computes is elapsed time since last
consented-visible activity, and the only thing it ever emits is "it's been a while."*

### The check-in itself

Deliberately unstructured minimum: a private, 1:1, off-task message from a human ("no
agenda — how are you doing?"). Anti-requirements: not a form, not a survey, not logged in
content, never framed as performance contact.

### Escalation (decided)

**Principle: escalation carries contact-facts, never content.** A checker may pass on
exactly two things — reachability facts ("no response in five weeks; Dana couldn't reach
them either") and their own concern flag. What a member *said* in a check-in is never
relayed to anyone, at any rung, at any stage.

- **Stage 1, rung 1 — the tree itself.** Concern or repeated non-response goes to the
  member's mutual-visibility group *where the member consented to one*. Without one, the
  lone checker's rung 1 is more direct human effort — that is what the member's consent
  structure permits.
- **Stage 1, rung 2 — acute danger: institutional crisis resources, immediately.** Anyone
  sensing acute danger escalates to crisis services (US: call/text **988**, the Suicide &
  Crisis Lifeline; elsewhere https://findahelpline.com) — no steward required. The
  checker tells the member what they did.
- **Stage 3 adds the steward rung:** concern flag + reachability facts only; steward
  function is logistics (fresh contact attempts, resources), not case management.
- **Member transparency, default-on.** The member is told what was shared and with whom.
  Notification may be **delayed, never skipped**, when telling them first would raise
  imminent risk — and judging that delay is a *required* checker-guidelines topic.
- **No escalation logs.** Escalations live in human memory; beyond the coordinator's
  timestamps nothing is written down, because an escalation log is a shadow mental-health
  record — the thing the hard constraints prohibit.

### Privacy & safety constraints (hard)

- Opt-in for members, checkers, and mentors; per-member consent for which absence signals
  count; double-consent for checker mutual visibility.
- No content logging; coordinator state is pairings + timestamps only.
- No mental-health inference, scoring, or risk ranking of members — ever. (The
  measurement layer may study the *practice* in aggregate — never individuals' states.)
- Right to silence: a member may decline contact without triggering escalation, may pause
  without reasons, and may leave the roster without explanation.

## The curriculum (decided)

The protocol ships coupled to an educational component — the evidence-based core of the
flagship programs (Sources of Strength and Wingman-Connect are, at heart, community-wide
strengths-and-connection trainings wrapped around naming/contact primitives):

1. **Community starter curriculum (everyone, recommended).** How to seek help, give help,
   listen, and talk about strengths — others' and your own. **Minimum-bar by design**:
   deliverable with free digital tools and self-serve online material, because
   professional trainers working with research teams are scarce, expensive, and
   surrounded by snake oil. Most communities will not get the optimal program; we do our
   best with free tools, and we still have to try. Communities with time and treasure
   should reserve **the best trainer available who works with the best research team
   available, over the longest span possible** — that is the honest optimum.
2. **Checker guidelines (required, lightweight).** A read-and-accept page that accepting
   a nomination *means* accepting: open, listen, don't fix, don't diagnose, know the
   crisis card, know what you may pass on (contact-facts only), and **when notification
   to the member may be delayed** (imminent risk only; delay, never skip). We cannot vet
   hearts; we can make the norms explicit and agreed to.
3. **Mentor training (full program, mentors only).** The real educational complexity
   loads onto the handful of people with declared capacity — never onto every checker,
   which would kill Stage 1's deployability.

## Staged development (decided)

Least risky and easiest first; each stage is a working practice alone and the gate to the
next:

- **Stage 1 — human-human cadence check-ins.** The phone tree + cadence + guidelines +
  starter curriculum. **No coordinator** — norms plus, at most, a shared calendar or
  pinned rotation doc. Stewardless. Deployable in any community immediately; this is
  where the protective bonds actually form.
- **Stage 2 — triggered check-ins.** Absence- and event-triggers over a *living* cadence
  practice, Tier-A signals, member baselines and pauses. The coordinator earns its place
  (elapsed-time detection is what humans reliably fail at) and brings the **operator**
  role. Still stewardless.
- **Stage 3 — escalation formalized.** Steward role, crisis-resource routing, the
  liability/duty-of-care review, and (if ever justified) the confidential gap view. Last
  because it is riskiest to get wrong and least useful without living Stages 1–2 beneath
  it.

## Coordinator substrate (decided)

- **Stage 1: none.**
- **Stage 2: reuse the notification protocol's coordinator** — same abstraction, same
  pluggable substrate spectrum (plain group chat ↔ private repo + operated agent ↔
  encrypted/ZK spaces), same guarantee-degradation table. One state machine, one trust
  surface, shared pairings/timestamps. The operator hosts it; the operator is not a
  steward.
- **Top of the spectrum:** where the egocentric→community machinery is deployed, **the
  encrypted space is the coordinator** — it holds pairings, baselines, and timestamps,
  computes elapsed-time conditions inside the privacy boundary, unlocks Tier-C triggers,
  and emits nothing but "it's been a while — reach out" **only to the member's chosen
  checkers** — never to stewards, operators, aggregates, or dashboards. Communities that
  never get there still have the middle rungs, with degraded guarantees honestly tabled.

## Relationship to the notification protocol

Same substrate, opposite direction, one coordinator. The notification note defers
"analysis-initiated triggers — 'someone should reach out to X'"; this protocol is that
class made humane: the "analysis" is a calendar or consented absence detection, the
"reach out" is a bonded human the member chose. A community running both gets members who
can ask with one button, and members who get asked without having to.

## Measurement (decided)

Five aggregate metric families, three guardrails, one honesty clause. All practice-level;
no individual is ever scored.

1. **Coverage** — % of members with ≥1 accepted checker; % whose tree meets their chosen
   cadence (doubles as the roster-health aggregate).
2. **Cadence adherence** — % of scheduled ticks completed (timestamps only).
3. **Member-rated value** — periodic anonymous pulse: *genuine vs performative* (the
   direct sensor for cadence theater), plus a brief validated support/belonging scale
   (e.g. UCLA-3) in aggregate.
4. **Tree dynamics** — mean checkers per member, lapse rate, **new nominations per
   quarter** (the Wingman sub-study's own bond-formation instrument).
5. **Retention** — roster churn; community contributor retention as a cautious distal
   signal.

**Guardrails:** no individual dashboards, ever; k-anonymity floor on every reported slice
(nothing for groups under ~5); no adherence leaderboards (competition incentivizes
cadence theater).

**Honesty clause:** crisis-outcome validation is beyond any single community's
statistical power — base rates are mercifully low. What a community can validate are the
mediators: bonds formed, support perceived, drift noticed. That is the same mediation
logic the Wingman-Connect trial published through.

## Threats / failure modes (to map against `../threat_modelling/threat_catalog.md`)

- **Surveillance creep** — mitigated by the Tier system, the timestamps-only invariant,
  and consented-signal allowlists; still needs a threat-catalog entry.
- **Pathologizing absence** — mitigated by member-declared baselines and no-reason
  pauses.
- **Checker load and burnout** — capacity negotiation + rotation spread load; the phone
  tree covers *who checks the checkers*; mentor layer absorbs overflow.
- **False reassurance / cadence theater** — watched by the genuineness pulse metric;
  leaderboards banned.
- **Power asymmetry** — member choice mitigates; OSS scope removes structural reporting
  lines; v2 must revisit for employers.
- **Roster-gap stigma** — mitigated by three-tier visibility and the
  self-initiated-only starter path; the aggregate view names no one.
- **Rejection pain** — mitigated by quiet-lapse declines and the mentor layer's
  secret-vote election (nobody is visibly unchosen or visibly declined).
- **Liability & duty-of-care** — Stage-3 gate; explicit non-clinical framing throughout;
  legal review before any org adoption.

## Open questions (implementation-stage)

1. **Guidelines drafting:** the actual checker-guidelines page and starter curriculum
   need writing (with the delay-notification judgment given real treatment).
2. **Mentor election mechanics:** ballot cadence, capacity declaration format, minimum
   votes, term length.
3. **Degradation table:** extend the notification protocol's substrate × guarantee table
   with the check-in semantics (rotation state, visibility groups, pause flags).
4. **The pods research question:** does check-in disclosure candor / drift detection
   differ 1:1 vs small-group? (Format literature is mixed and treatment-focused; this is
   an open empirical question we could eventually study through the measurement layer.)
5. **Pilot selection:** which OSS community runs Stage 1 first, and what does the
   retrospective look like?

## Evidence base (snhdb corpus; DOIs verified except where noted)

### Bond-building and proactive contact

- **Strengthening group bonds causally reduces suicidal ideation and depression.**
  Wingman-Connect cluster-RCT (n=1,485 Airmen, 215 classes): reduced suicidal ideation
  (ES −0.23) and depression at 1 month, depression sustained at 6 months; the effect was
  *statistically mediated by class-level cohesion, morale, and bonds* — direct support for
  bond-building as upstream prevention. Wyman et al. 2020, JAMA Network Open,
  doi:10.1001/jamanetworkopen.2020.22532.
- **Peer-leader network interventions change help-related norms at population scale.**
  Sources of Strength (peer leaders named trusted adults and normed help-seeking
  school-wide). Wyman et al. 2010, Am J Public Health, doi:10.2105/ajph.2009.190025.
- **Network position predicts risk: isolation from adults/mentors marks the vulnerable.**
  In 38 high schools (n=10,291), suicide attempts concentrated where youth-adult
  connectedness was low; "adult-isolated" members are the analog of the contributor no
  maintainer personally knows. Wyman et al. 2019, J Child Psychol Psychiatry,
  doi:10.1111/jcpp.13102.
- **Loneliness and isolation are mortality-grade risks, justifying proactive contact.**
  Holt-Lunstad et al. 2015 meta-analysis: social isolation, loneliness, and living alone
  associated with 26–32% increased mortality odds. doi:10.1177/1745691614568352.
- **Loneliness is intervenable.** Meta-analysis of psychological interventions for
  loneliness shows significant reductions (28 RCTs, g=0.43). Hickin et al. 2021, Clin
  Psychol Rev, doi:10.1016/j.cpr.2021.102066. Note for the pods question: Hickin's
  introduction reports prior moderator findings on *group vs individual delivery* as
  "mixed and inconclusive" — the format question is genuinely unsettled in the treatment
  literature, and untested for contact/monitoring practices like this one.
- **Context prevalence:** maintainer burnout/isolation is endemic (Articles topic:
  Linux Foundation maintainer reports, Tidelift surveys, first-person burnout accounts) —
  the population where quiet withdrawal is normalized as "life got busy."

### Withdrawal / silence as a risk signal

- **Elevated-risk members drift toward disconnection absent intervention.** The
  Wingman-Connect social-network sub-study (Social Science & Medicine, 2022; reported in
  the corpus evidence brief "14 points — the evidence"; DOI unverified in corpus copy)
  found the status-quo trajectory for Airmen at elevated suicide risk was one of
  *worsening disconnection* — declining valued-connection nominations in the control
  condition — and that the program offset it (at-risk Airmen made ~3× more new
  valued-connection nominations). Declining connection is the observable trajectory of
  risk; it is exactly what absence-triggers watch for.
- **Isolation as a network-position risk marker.** Wyman et al. 2019 (above): attempts
  concentrate where trusted-adult connectedness is low.
- **Belongingness deprivation is pathology-grade (theory).** Baumeister & Leary's
  need-to-belong review links belongingness deprivation to outcomes up to and including
  suicide; belonging requires *both* frequent positive interaction *and* a stable caring
  bond — which is why cadence contact from a chosen person, not either alone, is the
  design target. doi:10.4324/9781351153683-3 (corpus copy is the 2017 reprint).
- **Remote-work mechanism.** Unaddressed isolation is linked to declining contribution
  and participation as disengaged members further withdraw (systematic reviews, Remote
  Workers topic), and depleted social resources drive the disengagement arm of burnout
  in the job demands–resources model (Demerouti et al. 2001, corpus: Remote Workers
  topic) — withdrawal compounds itself.
- **Honest gap.** The corpus contains no psychological-autopsy-style study of behavior
  in the weeks preceding suicide. "Radio silence preceded the loss" is corroborated by
  our memoriams case records (private) and consistent with the drift finding above, but
  is *practice knowledge, not corpus-demonstrated fact* — treat proximal silence as a
  moderate-confidence warning sign, and the protocol's absence triggers as precautionary
  rather than predictive.

### Checker selection — why members choose

- **Naming trusted people is the program primitive.** Sources of Strength has students
  *name* their trusted adults (Wyman 2010, above), and the protective association runs
  through those named connections — students sharing trusted adults with friends sat in
  the low-attempt-rate networks (Wyman 2019, above).
- **Top-down assignment measurably misses.** Comparing staff-selected peer leaders
  against network-informed alternatives across 20 schools (n=5,746): adult-selected sets
  overlapped only 13.3–22.7% with network-optimal sets; network-informed sets sat
  systematically closer to at-risk students (suicidal ideation/attempt,
  network-peripheral, no trusted adult); and schools whose selections better matched the
  network saw greater program diffusion (+0.82pp peer communication per 1pp concordance).
  Pickering, Wyman, Valente et al. 2022, BMC Public Health,
  doi:10.1186/s12889-022-13372-w. *Limitation:* the network-informed sets were never
  implemented — correlational, 20 school-level observations.
- **Mentor election grounding.** The mentor layer's aggregate secret nomination is the
  "peer opinion leader in-degree" selection method from the same study — a
  network-informed method, of the family that sat closer to the at-risk than staff
  selection. SoS peer leaders receive a ~5-hour strengths-and-connection training and
  serve their whole school, including students who never nominated them (Pickering 2022
  full text) — the shape the mentor layer copies.
- **Implication for the phone tree:** member nomination puts the selection where the
  network knowledge actually is; the mentor pool catches those the tree cannot reach —
  and only when they ask (open question: the triple-opt-out member remains unreachable;
  see the notification protocol).
