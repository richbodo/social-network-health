# SNH Check-in Protocol — Design Note
### "Proactive Peer Check-ins"

**Status:** v0.1.1 (2026-07-08) — proposed protocol, idea-stage. Proposed by Rich out of
the project's memoriams postvention practice; drafted with corpus evidence by the snhdb
research agent. Revised same-day: origin anonymized to match memoriams practice,
development staged (cadence → triggers → escalation), chosen-checker "phone-tree" design
added, evidence base moved to the end and extended with corpus findings on withdrawal and
checker selection. Open questions at the bottom are unresolved — grill before promoting
to v0.2.
Companion notes: `notification-protocol.md` (this protocol is the outbound complement to
that note's inbound help-seeking, and a candidate implementation of its deferred
"analysis-initiated triggers" class); `../research_library/memoriams.md` (the anonymized
postvention study behind the origin below);
`../measurement/egocentric_to_community_network_health_research_note.md` (the consented
metrics substrate that Stage 2's automatic triggers would ride).

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

## Actors & roles

- **Member** — anyone participating in the community (contributor, teammate).
- **Checker** — a member who has agreed to do check-ins **and been chosen by the member
  they check on** (see the phone tree below). Not a clinician, not a manager by default
  (power asymmetry changes the conversation — see open questions).
- **Steward** — accountable human (same role as notification protocol): maintains the
  roster, receives escalations, owns the crisis-resource list, audits that the practice
  is alive without reading its contents.
- **Coordinator (optional, software)** — schedules pairings and nudges checkers; holds
  the minimum state (who checks whom, when last checked — never content). In the Stage-2
  architecture below, the coordinator can be the measurement protocol's encrypted space.

## Protocol sketch

### Chosen checkers — the phone tree

Each member is asked to pick the people — **one or more, ideally three or more** — from
whom they would *like* to receive a check-in and have a real conversation from time to
time. A nomination is an invitation: the nominee accepts (becoming one of that member's
checkers) or declines privately. This mirrors the selection primitive in peer-to-peer
prevention programs, where members *name* their own trusted adults and the protective
association runs through the named-not-assigned connections; the corpus evidence (end of
note) additionally shows that top-down selection of peer agents overlaps only ~13–23%
with network-optimal choices and sits farther from the at-risk. **Members name their
checkers; nobody is assigned one.**

Three properties fall out of the tree shape:

- **Redundancy.** With three or more checkers, one person's lapse doesn't sever a
  member's coverage — a phone tree, not a single thread.
- **Who checks the checkers.** Everyone, checkers included, has their own chosen
  checkers; the tree covers its own operators.
- **The roster's gaps are the risk map.** Members who nominate no one, or whom no one
  accepts, are the analog of the "adult-isolated" students the school studies flag as
  highest-risk. Noticing that the roster has gaps is a steward duty and an *aggregate*
  observation — never an individual inference or score.

### Trigger classes

Same state machine, three ways in:

1. **Cadence check-ins** — default: every member is checked in on by a human at some
   floor cadence (e.g. monthly), rotated across their chosen checkers so contact repeats
   enough to build real bonds. The point of cadence is *normalization*: a check-in that
   only arrives when someone seems off is an alarm, not a relationship.
2. **Absence-triggered** — the recurring memoriams pattern. If a member's ordinary
   visible activity (commits, chat, meetings — signals the member consented to in
   advance) goes quiet beyond their own stated baseline, the coordinator nudges that
   member's checkers: "it's been a while — reach out." The nudge carries no inference,
   only elapsed time.
3. **Event-triggered** — after known acute stressors: a heated conflict/fork, a brutal
   release crunch, a public failure, a departure or layoff nearby. Community accounts of
   contributor loss name these as the acute moments; maintainers may fire these manually.

### Staged development

Build in three stages, **least risky and easiest to implement first**. Each stage is a
working practice on its own and the gate to the next:

- **Stage 1 — human-human cadence check-ins.** The phone tree plus a floor cadence plus
  the check-in norms below. No software beyond, at most, a shared calendar; no absence
  detection; escalation is informal ("talk to the steward"). Deployable in any community
  immediately — and it is where the bonds, the protective mechanism itself, actually form.
- **Stage 2 — triggered check-ins.** Add absence- and event-triggers on top of a *living*
  cadence practice, with per-member consented signals and the no-inference rule. Software
  earns its place here (the coordinator), because elapsed-time detection is exactly what
  humans reliably fail at. Where the egocentric→community measurement protocol is
  running, its consented communications metrics can fire these triggers automatically —
  released **only to the member's chosen checkers** (see below).
- **Stage 3 — escalation paths.** Formalize the two-rung escalation, steward duties,
  crisis-resource routing, and the liability/duty-of-care review. Last because it is the
  riskiest to get wrong and the least useful without living Stages 1–2 underneath it.

### The check-in itself

Deliberately unstructured minimum: a private, 1:1, off-task message from a human ("no
agenda — how are you doing?"). Anti-requirements: it is not a form, not a survey, not
logged in content, and never framed as performance contact. A short optional script for
checkers (open, listen, don't fix, know the escalation path) plus the crisis-resource
card is the entire training surface for Stage 1.

### Escalation path

Checker judgment, two rungs: (a) concerning response or repeated non-response → tell the
steward (fact of concern only, minimum detail); (b) acute danger signals → crisis
resources immediately (e.g. 988 in the US), steward informed. Checkers are explicitly
*not* responsible for outcomes — the protocol's promise is contact, not rescue. The
communities in our memoriams records acted correctly with what they had; they had no
structure that acted earlier.

### Privacy & safety constraints (hard)

- Opt-in for members and checkers; per-member consent for which absence signals count.
- No content logging; coordinator state is pairings + timestamps only.
- No mental-health inference, scoring, or risk ranking of members — ever. (The
  measurement layer may study the *practice* in aggregate — cadence adherence, coverage,
  member-reported value — never individuals' states.)
- Right to silence: a member may decline contact without triggering escalation, and may
  leave the roster without explanation.

## Relationship to the notification protocol

Same substrate, opposite direction. The notification note defers "analysis-initiated
triggers — 'someone should reach out to X'" over its state machine; the check-in protocol
is that trigger class made humane: the "analysis" is either a calendar or consented
absence detection, the "reach out" is a bonded human the member chose, and the
coordinator/steward roles are shared. A community running both gets: members who can ask
with one button, and members who get asked without having to.

## Relationship to the egocentric→community measurement protocol

The measurement note proposes estimating community-health indicators from opt-in
egocentric communications metrics inside zero-knowledge / secure-aggregation machinery.
This protocol is a natural *actuator* for that sensor layer. When consented metrics
exist, a member's deviation from **their own baseline** can fire a Stage-2 trigger
automatically, under two hard properties:

- the inference never leaves the encrypted space in any form except a nudge, and
- the nudge is released **only to that member's chosen checkers** — never to stewards,
  aggregates, or dashboards.

In that architecture **the encrypted space is the coordinator**: it holds the pairings,
baselines, and timestamps, computes elapsed-time conditions inside the privacy boundary,
and emits nothing but "it's been a while — reach out" to the right humans.

## Threats / failure modes (to map against `../threat_modelling/threat_catalog.md`)

- **Surveillance creep** — absence detection quietly widening into activity monitoring;
  mitigated by consented-signal allowlist and no-inference rule, but needs a threat entry.
- **Pathologizing absence** — people take breaks; a nudge must never read as "explain
  yourself." Baseline is member-defined.
- **Checker load and burnout** — the caring labor problem; checkers need small rosters
  and rotation. The phone tree covers *who checks the checkers*, but not the load itself.
- **False reassurance** — a checked box is not a relationship; cadence theater could
  *lower* vigilance. Aggregate measurement should watch for this.
- **Power asymmetry** — manager/maintainer-as-checker converts care into evaluation.
  Member choice mitigates but does not eliminate (members may feel obliged to nominate a
  lead).
- **Roster-gap stigma** — the "nobody chose them" observation is the protocol's most
  sensitive datum; handling it badly *creates* the isolation signal it detects.
- **Liability & duty-of-care** — once a community institutionalizes check-ins, what does
  it owe when one is missed? Needs explicit non-clinical framing and legal review before
  any org adoption (Stage 3 gate).

## Open questions (for the next grill)

1. **Scope of v1:** open-source projects (the memoriams context) or remote teams (SNH's
   core population) first? The trust structures and available signals differ a lot.
2. **Cadence default:** monthly? aligned to release cycles? member-chosen with a floor?
3. **Tree topology:** are a member's checkers rotated per cadence tick or all nudged?
   Do checkers of one member know about each other (coordination vs privacy)? Is the
   unit ever a pod rather than spokes (Wingman-Connect argues group-level bonds matter)?
4. **Nomination dynamics:** what happens for members who nominate no one, or whom no one
   accepts — the highest-risk cell? Who may see roster gaps, and what may they do?
5. **Reciprocity:** does choosing someone imply being choosable? May a nominee's decline
   be visible to the nominator, and how is that softened?
6. **Absence signals:** which are acceptable inputs even with consent? (commit activity
   feels different from chat presence; both feel different from calendar data.)
7. **Checker eligibility:** any chosen volunteer? vetted by steward? excluded if in a
   reporting line? What minimal training is required before first check-in?
8. **Escalation specifics:** what exactly may a checker tell a steward, and what must the
   member be told about what was shared?
9. **Measurement:** which aggregate metrics validate the thesis without touching
   individual states — coverage %, cadence adherence, member-rated value, retention?
10. **Coordinator substrate:** Stage 1 needs none; does Stage 2 ride the notification
    protocol's coordinator, a plain shared calendar, or the measurement protocol's
    encrypted space from day one?

## Evidence base (snhdb corpus; DOIs verified except where noted)

### Bond-building and proactive contact (v0.1 base)

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
  loneliness shows significant reductions. Hickin et al. 2021, Clin Psychol Rev,
  doi:10.1016/j.cpr.2021.102066.
- **Context prevalence:** maintainer burnout/isolation is endemic (Articles topic:
  Linux Foundation maintainer reports, Tidelift surveys, first-person burnout accounts) —
  the population where quiet withdrawal is normalized as "life got busy."

### Withdrawal / silence as a risk signal (added v0.1.1)

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

### Checker selection — why members choose (added v0.1.1)

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
- **Implication for the phone tree:** member nomination puts the selection where the
  network knowledge actually is. The at-risk cell this can't reach — members with no one
  to nominate — is open question 4, and the steward's aggregate roster-gap duty exists
  precisely for it.
