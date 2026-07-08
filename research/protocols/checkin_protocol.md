# SNH Check-in Protocol — Design Note
### "Proactive Peer Check-ins"

**Status:** v0.1 (2026-07-08) — proposed protocol, idea-stage. Proposed by Rich after the
Redox OS post below; drafted with corpus evidence by the snhdb research agent. Open
questions at the bottom are unresolved — grill before promoting to v0.2.
Companion note: `notification-protocol.md` (this protocol is the outbound complement to
that note's inbound help-seeking, and a candidate implementation of its deferred
"analysis-initiated triggers" class).

---

## Origin

Jeremy Soller's Redox OS post *"Open Source and Mental Health"* (June 2021), written after
the death — believed suicide — of jD91mZM2, an 18-year-old prolific Redox contributor.
The post's proposal is not a system but a practice:

> "I feel compelled to check in on the many people I have lost in the years, and I hope
> you do too. … the more we check in with each-other, the better we will do."
> "I will no longer value contributors by the code they crank out. … the person writing
> the code needs even more maintenance than the 'open source' itself."

Two facts from that account shape the design. First, the warning signal that existed —
jD91mZM2 had gone quiet and stopped answering emails — was only acted on *after* another
contributor raised it, too late. Second, the last contact the author had with him was
"purely technical." The community had bandwidth for code review and none, structurally,
for human review.

Corpus copy: `Articles/MD/Open Source and Mental Health Redox OS` (snhdb; no DOI, blog
post, June 2021).

## Purpose & thesis

The notification protocol's thesis is one-button **help-seeking**: reduce the friction of
*asking*. But the people at highest risk often don't ask — they withdraw (threat catalog
RF1/K1 framing: those who most need help have the weakest ego networks, and withdrawal is
itself the symptom). A help-seeking button cannot reach someone who has stopped reaching.

**Thesis:** *regular, normalized, low-friction peer check-ins (a) strengthen the bonds
that are themselves protective, and (b) create routine occasions where deterioration and
withdrawal get noticed while there is still time to act.* Check-ins are not surveillance
and not diagnosis; they are scheduled human contact with a light escalation path.

## Evidence base (snhdb corpus, DOIs verified)

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

## Actors & roles

- **Member** — anyone participating in the community (contributor, teammate).
- **Checker** — a member who has agreed to do check-ins. Not a clinician, not a manager
  by default (power asymmetry changes the conversation — see open questions).
- **Steward** — accountable human (same role as notification protocol): maintains the
  checker roster, receives escalations, owns the crisis-resource list, audits that the
  practice is alive without reading its contents.
- **Coordinator (optional, software)** — schedules pairings and nudges checkers; holds
  the minimum state (who checks whom, when last checked — never content).

## Protocol sketch

**Trigger classes** (same state machine, three ways in):

1. **Cadence check-ins** — default: every member is checked in on by a human at some
   floor cadence (e.g. monthly), rotated so pairs vary but repeat enough to build real
   bonds. The point of cadence is *normalization*: a check-in that only arrives when
   someone seems off is an alarm, not a relationship.
2. **Absence-triggered** — the jD91mZM2 case. If a member's ordinary visible activity
   (commits, chat, meetings — signals the member consented to in advance) goes quiet
   beyond their own stated baseline, the coordinator nudges that member's checker:
   "it's been a while — reach out." The nudge carries no inference, only elapsed time.
3. **Event-triggered** — after known acute stressors: a heated conflict/fork, a brutal
   release crunch, a public failure, a departure or layoff nearby. Named in Soller's
   post as acute triggers; maintainers may fire these manually.

**The check-in itself.** Deliberately unstructured minimum: a private, 1:1, off-task
message from a human ("no agenda — how are you doing?"). Anti-requirements: it is not a
form, not a survey, not logged in content, and never framed as performance contact.
A short optional script for checkers (open, listen, don't fix, know the escalation path)
plus the crisis-resource card is the entire training surface for v0.1.

**Escalation path.** Checker judgment, two rungs: (a) concerning response or repeated
non-response → tell the steward (fact of concern only, minimum detail); (b) acute danger
signals → crisis resources immediately (e.g. 988 in the US), steward informed. Checkers
are explicitly *not* responsible for outcomes — the protocol's promise is contact, not
rescue. jD91mZM2's community acted correctly with what it had; it just had no structure
that acted earlier.

**Privacy & safety constraints (hard):**

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
absence detection, the "reach out" is a bonded human, and the coordinator/steward roles
are shared. A community running both gets: members who can ask with one button, and
members who get asked without having to.

## Threats / failure modes (to map against `../threat_modelling/threat_catalog.md`)

- **Surveillance creep** — absence detection quietly widening into activity monitoring;
  mitigated by consented-signal allowlist and no-inference rule, but needs a threat entry.
- **Pathologizing absence** — people take breaks; a nudge must never read as "explain
  yourself." Baseline is member-defined.
- **Checker load and burnout** — the caring labor problem; checkers need small rosters,
  rotation, and their own checkers (who checks the checkers is an open question).
- **False reassurance** — a checked box is not a relationship; cadence theater could
  *lower* vigilance. Aggregate measurement should watch for this.
- **Power asymmetry** — manager/maintainer-as-checker converts care into evaluation.
- **Liability & duty-of-care** — once a community institutionalizes check-ins, what does
  it owe when one is missed? Needs explicit non-clinical framing and legal review before
  any org adoption.

## Open questions (for the next grill)

1. **Scope of v1:** open-source projects (Soller's context) or remote teams (SNH's core
   population) first? The trust structures and available signals differ a lot.
2. **Cadence default:** monthly? aligned to release cycles? member-chosen with a floor?
3. **Pairing policy:** stable buddies (deep bonds, single point of failure) vs rotation
   (coverage, shallower)? Wingman-Connect argues group-level bonds matter — is the unit a
   pair or a small pod?
4. **Absence signals:** which are acceptable inputs even with consent? (commit activity
   feels different from chat presence; both feel different from calendar data.)
5. **Checker eligibility:** any volunteer? vetted by steward? excluded if in a reporting
   line? What minimal training is required before first check-in?
6. **Escalation specifics:** what exactly may a checker tell a steward, and what must the
   member be told about what was shared?
7. **Measurement:** which aggregate metrics validate the thesis without touching
   individual states — coverage %, cadence adherence, member-rated value, retention?
8. **Coordinator substrate:** does this ride the notification protocol's coordinator, a
   plain shared calendar, or nothing (pure norm) for v1?
