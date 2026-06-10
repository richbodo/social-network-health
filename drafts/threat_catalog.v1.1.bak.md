# Threat Catalog — Social Network Health Interventions for Remote-Worker Communities

**Status:** Working catalog (v1.1, 2026-06-09 — completeness pass integrated; see the Completeness Addendum appended at the end of this file). Living document — we add, revise, and
"consider further" as the grill continues.
**Provenance:** Distilled from the `snh-harm-research` multi-agent study (12 research seams
→ 92 raw → 38 consolidated → adversarially verified → synthesized; 52 agents, ~1.5M tokens).
Full verbose synthesis with all citation corrections: `brainstorms/20260609-snh-threat-catalog.md`
(gitignored). Grill log: `brainstorms/20260609-102346-snh-session.md`.

---

## Purpose & how this fits

This is the **"where the mines are"** document. Before designing *any* social-network-health
(SNH) intervention for remote workers — and long before building the experimental
notification/response protocol — we need a documented, citable understanding of the credible
ways such interventions harm people.

It is the **first of two paired research datasets**:

1. **Threat model (this document)** — credible failure modes of SNH interventions for remote
   workers.
2. **Success model (forthcoming)** — design features and practices empirically linked to
   *better* outcomes in the remote-worker context (the "what works" counterpart; the content
   that will seed the toolkit's remote-teams Practice section).

Together these become a reusable evidence base we draw on repeatedly. They feed, in dependency
order: **safety guardrails + design methodology** ("where we land" — nothing past it, including
experiments, is legitimate until it exists) → **the community guide** (a partly-assisted
meta-process for a community to build, *by and with itself*, a communications system that
improves its social network health, with stepwise safe experiment/evaluate/pivot) → **(long
term) the protocol experiment** (a privacy-preserving notification/response protocol + community
metrics — known to face hard challenges; deferred).

**Scale & evidence stance.** We do **not** optimize for any scale. Remote-teams research spans
every size, so we follow the *strongest available evidence* for each threat (and, later, each
success case) wherever it sits — n=1 or n=1,000,000 — and report each study's **own scale and
context** in its evidence line, so the reader knows exactly what was shown and where. The `scale`
tag below is only a light "where this is most acute" applicability aid; it is **never** a filter
on which evidence counts. (Detailed mitigations lean toward small home-cooked communities,
N≈10–50, because that is the immediate build context — but the catalog is meant to serve mid-size
orgs, platform-scale networks, and academic ideation equally.)

**Design stance.** Most harm here is *iatrogenic by design*, not the work of a bad actor. The
fight is for harm avoidance, maximal use of current evidence, and a well-informed design
process. Leaders are part of a system, not the sole point of failure.

---

## How to use this catalog

Each threat has a **stable ID** (e.g., `B1`) so the success model, guardrails doc, and future
research can reference it permanently. The "Mitigation seed" line is the bridge to the success
model; the "Consider further" line is an open question for the ongoing grill.

**Severity** (harm to a preventive remote-worker SNH intervention): `high` = serious individual
harm or silent corruption of the whole intervention · `medium` = meaningful but recoverable ·
`low` = friction/quality risk.
**Confidence** = verifier confidence in the evidence as characterized: `high` / `med`; `exp` =
expert-asserted (Category K), citation pending the completeness sweep.
**Scale** = a light applicability aid — where the threat is *most acute* (`team` N≈10–50 ·
`org` 100s–1000s · `platform` very large). It is **not** a filter on which evidence counts: we
follow the strongest evidence at *any* scale and report each study's own N/scale/context in its
evidence line.
**Layers** it threatens: **APP** (personal network app) · **PROTO** (notification/response
protocol) · **METRICS** (community health metrics) · **FACIL** (facilitation process) ·
**LEAD** (leadership/governance).
**Citations** are kept precise and *quotable* (specific source + the passage that grounds the
claim) so they can later become **deep links** on the toolkit MediaWiki: Anton Krom's PDF
highlight extension opens the source, finds the passage by text string, and highlights it —
letting a reader see exactly what the research said and at what scale (whether n=1 or n=1,000,000).

---

## Threat register

| ID | Threat | Sev | Conf | Scale | Layers |
|----|--------|-----|------|-------|--------|
| **A. Iatrogenic design** |
| A1 | Single-session emotional-processing backfire (debriefing harm) | high | high | team·org | PROTO·FACIL |
| A2 | Universal prevention worsening a vulnerable subgroup | high | high | org·platform·team | APP·METRICS·FACIL |
| A3 | Scared-Straight / fear-arousal deterrence backfire | med | high | all | FACIL·METRICS |
| A4 | Symptom-surveillance anxiety amplification ("worry engines") | med | med | all | APP·METRICS |
| **B. Labeling / medical model** |
| B1 | **Labeling / at-risk identification (master threat)** | high | high | all·acute team | APP·PROTO·METRICS·FACIL |
| B2 | False-positive "at-risk" designation harms non-converters | high | med | team·org | METRICS·APP |
| B3 | Responder/facilitator bias from diagnostic frame | med | high | all | PROTO·FACIL·LEAD |
| B4 | Self-stigma / prevalence inflation from medicalized framing | med | med | all | FACIL·METRICS |
| **C. Contagion** |
| C1 | Peer contagion / deviancy training in aggregated support | high | high | team·org | PROTO·FACIL |
| C2 | Suicide/crisis contagion via distress visibility (Werther) | high | high | all·acute platform+team | PROTO·METRICS·FACIL |
| C3 | Co-rumination, emotional contagion & cyberostracism in text | high | high | team·org | PROTO·METRICS |
| C4 | Digital bystander effect: broadcast → diffusion → no response | high | med | org·platform | PROTO |
| **D. Surveillance / metrics** |
| D1 | Employer-adjacency: surveillance perception + disclosure retaliation | high | med | all | all (esp. PROTO) |
| D2 | Goodhart/Campbell metric collapse + impression mgmt + selection | high | high | all·acute org | METRICS·FACIL |
| D3 | Engagement-ranked / silent curation amplification of distress | high | high | platform·(any feed) | APP·PROTO·METRICS |
| D4 | Emotion-AI / biometric metrics mislabel healthy workers | med | med | all | METRICS |
| D5 | Homophily–contagion confound: phantom "spread" misleads facilitators | med | high | all | METRICS·FACIL |
| **E. Privacy / re-identification** |
| E1 | Cumulative-release attacks (reconstruction / membership / composition) | high | high | acute team·org | METRICS |
| E2 | ZKP proves correct computation, **not** non-identifying output | high | high | all | METRICS |
| E3 | Behavioral-trace re-identification of pseudonymous signals | high | high | acute team | APP·PROTO |
| **F. Consent / governance** |
| F1 | Coerced/bundled consent at the moment of distress | high | high | all | APP·PROTO·FACIL |
| F2 | Coercive financial incentives → compelled disclosure | high | high | org | PROTO·FACIL |
| F3 | Non-consensual crisis escalation → harmful welfare/police checks | high | high | all·acute team | PROTO |
| **G. Help-seeking suppression & stepped-care** |
| G1 | Chilling effect on help-seeking (stigma + reactance + coercion) | high | med | all | entire intervention |
| G2 | Gatekeeper training: confidence without behavior change; repels high-risk | high | med | all | PROTO·FACIL |
| G3 | Stepped-care evaporation: preventive layer fails to step up | high | med | all | PROTO·FACIL |
| G4 | False reassurance: quick response masks unmet clinical need | med | med | all | PROTO·FACIL |
| **H. Communication-medium (CMC)** |
| H1 | Text-only misattribution, dehumanization, toxic disinhibition | high | high | all | PROTO·METRICS·FACIL |
| H2 | Remote-network atrophy: weak-tie loss, video fatigue, onboarding failure | high | high | all (remote) | community·FACIL·APP |
| **I. Community / leadership** |
| I1 | Peer enforcement of harmful norms + polarization + call-out dynamics | high | med | all·acute team | FACIL·LEAD·PROTO |
| I2 | Leadership inaction / inadequate response to a first-time signal | high | med | all·acute team | LEAD·PROTO |
| **J. Transfer / fidelity** |
| J1 | Voltage drop, model drift, surface-only cultural adaptation | high | med | org·platform·(team transfer) | FACIL·LEAD |
| J2 | Successor-facilitator competency decay + satisfaction-masks-harm | high | med | all | FACIL·PROTO·METRICS |
| **K. Baseline risk environment & operating constraints** *(K1–K4 cited — Addendum §3; K5/K6 thin)* |
| K1 | Chronic isolation & weak belonging (baseline) | high | high | all | substrate |
| K2 | Timezone dispersion, interruption, sleep/circadian disruption | high | high | all | substrate·FACIL |
| K3 | Tech displacement / underemployment / job insecurity → depression | high | high | all | substrate·METRICS |
| K4 | Declining in-person contact (post-COVID inflection) | med | high | all | substrate·FACIL |
| K5 | "Degraded mode": loss of embodied/experiential co-present learning | high | low | all | substrate·FACIL |
| K6 | Hard-to-corral / unreachable-in-bulk → selection bias & coverage gaps | high | exp | all | METRICS·PROTO·FACIL·LEAD |

**Completeness-pass additions (v1.1; full detail in the appended Addendum §2):**

| ID | Threat | Sev | Conf | Scale | Layers |
|----|--------|-----|------|-------|--------|
| A5 | Subgroup-masking — harm + averaged eval both hide the at-risk stratum | high\* | med | org·platform·team | APP·PROTO·METRICS |
| D6 | Invisible facilitation / emotional-labor blind spot | med | high | all | METRICS·FACIL·LEAD |
| D7 | Public-performance-audit impostor (AI-amplified) | med | med | all | METRICS·FACIL |
| G5 | Platform-distrust silencing (techno-insecurity mutes signals) | high | high | all | PROTO·all |
| H3 | AI-mediated interaction displaces human bonds | med | med | all | substrate·PROTO |
| H4 | Capable-contributor blind spot (risk indicators anti-predictive) | high | med | all | FACIL·LEAD·METRICS |
| I3 | Entitled-user demand escalation → suppresses disclosure + trust vacuum | high | high | all | FACIL·LEAD·PROTO |
| I4 | Consensus-governance overload → facilitator burnout | med | med | all | FACIL·LEAD |
| J3 | Single-maintainer "lottery factor" (knowledge concentration) | med | high | all | FACIL·LEAD |
| K7 | Professional/career isolation (distinct from social loneliness) | med | high | all | substrate |
| K8 | Reciprocal distress↔isolation feedback loop | high | high | all | substrate·METRICS |
| K9 | Silent dropout / invisible attrition as a distress signal | high | med | all | substrate·METRICS·PROTO |
| K10 | Telepressure / always-on → rumination, sleep loss, burnout | high | high | all | substrate·FACIL |
| K11 | Inverted-U work-mode dose curve (fully-remote deficit vs hybrid) | high | med | all | substrate |
| K12 | Long-term full-remote suppresses the need to belong | high | med | all | substrate |
| K3a | Anticipatory AI-threat distress (harms employed workers) | med | med | all | substrate |
| K3b | Reputation-premium collapse for high-skill freelancers | high | med | all | substrate |
| K3c | GenAI productivity-expectations ratchet | high | med | all | substrate·FACIL |

\*A5 severity may be overstated (single cross-sectional study) — see Addendum §6. J4 folds into J2;
K13 is a cross-reference to H3/K3/K4 (no new ID).

**Confirmed — formerly quarantined (now verified, high confidence; detail in Addendum §4):**
**Q-a** third-party SDK/tracking-pixel leakage + data-broker sale (FTC v. BetterHelp; Cerebral pixel
breach 3.1M; Duke Sanford brokers); **Q-b** commercial pivot of help-seeking data (FTC v. Cerebral;
23andMe bankruptcy → ~15M people); **Q-c** small-N re-identification from "aggregate" metrics
(Sweeney: 3 quasi-identifiers → 87% of US population) — **CONFIRMED; this GATES the metrics layer.**

---

## Detailed catalog

> Each entry: **Mechanism** (causal chain) · **Evidence** (with citations) · **Bites** (layers)
> · **Scale** (how it changes with community size) · **Mitigation seed** (→ success model) ·
> **Consider further** (open grill question).

### A. Iatrogenic design — the intervention itself causes harm

**A1 — Single-session emotional-processing backfire** · `high` · conf high · team·org
- **Mechanism:** A mandatory structured session forcing articulation of distress right after an
  event interferes with natural habituation and appears to re-consolidate the trauma memory
  before the nervous system stabilizes → elevated PTSD.
- **Evidence:** Rose, Bisson, Churchill & Wessely (2002), *Cochrane* CD000560 (15 RCTs; single-
  session debriefing "equivalent to, or worse than" no intervention). Bisson et al. (1997),
  *Br J Psychiatry* 171 — OR 2.51 (95% CI 1.24–5.09) at 1yr. Mayou, Ehlers & Hobbs (2000),
  *BJP* 176:589–93 (3yr adverse). Lilienfeld (2007), *Perspectives on Psych Science* 2(1).
- **Bites:** PROTO, FACIL.
- **Scale:** Universal to any facilitated response; the harm is per-person, not size-dependent.
- **Mitigation seed:** No mandatory single-session emotional processing; responses are low-demand
  check-ins; watchful waiting + peer support; structured trauma work referred to professionals
  only after time elapses.
- **Consider further:** What is the minimum, *non-iatrogenic* shape of a "response"? Where is the
  line between a supportive check-in and a harmful debrief?

**A2 — Universal prevention worsening a vulnerable subgroup** · `high` · conf high · org·platform·team
- **Mechanism:** Content pushed to everyone raises symptom salience without coping scaffolding,
  primes misattribution (nocebo), becomes ruminative for some → a minority deteriorates while the
  mean improves.
- **Evidence:** MYRIAD RCT (Kuyken et al. 2022; n≈8,376, 84 schools) — no overall benefit, at-risk
  students worse at post & 1yr (PMC9340028/PMC9340034). Venturo-Conerly et al. (2023, PMC10764854)
  — 12.42% reliable worsening (depression), 11.78% (anxiety). Guzman Holst et al. (2025), *CAMH*
  doi:10.1111/camh.12760. Werch & Owen (2002), *J Stud Alcohol* 63(5) — 43 harmful outcomes/17 RCTs.
- **Bites:** APP, METRICS, FACIL.
- **Scale:** Worse the more *uniform* the rollout — acute at org/platform "push to everyone," but
  present at team scale too.
- **Mitigation seed:** Coping resources at every touchpoint; no standalone awareness content;
  pilot with **subgroup-worsening** monitoring (not just averages); opt-out / reduced-intensity track.
- **Consider further:** Can an *ecologically self-built* program even do subgroup analysis at N≈30,
  or is the safeguard only available at larger N?

**A3 — Scared-Straight / fear-arousal deterrence backfire** · `med` · conf high · all
- **Mechanism:** Vivid worst-case framing as a deterrent triggers reactance, social learning, and
  identity rebound → increases the warned-against behavior.
- **Evidence:** Petrosino et al. (2022), *Cochrane* CD002796 — 9 RCTs, N=946, OR 1.68 (1.20–2.36)
  for reoffending vs nothing. NIJ CrimeSolutions "Ineffective." Witte & Allen (2000) fear-appeal lit.
- **Bites:** FACIL, METRICS (communication copy).
- **Scale:** Universal; matters wherever messaging is authored.
- **Mitigation seed:** "Papageno orientation" — model coping success, not crisis. Ban urgency/alarm
  framing ("your community health is declining — act now"). Stories show recovery and effective help.
- **Consider further:** What is the catalog of *safe* framings? (Seeds a success-model entry.)

**A4 — Symptom-surveillance anxiety amplification ("worry engines")** · `med` · conf med · all
- **Mechanism:** Repeated prompts to self-monitor train hypervigilance to normal fluctuation;
  streaks/badges/red-dots manufacture micro-crises; the most conscientious (often most at-risk)
  over-engage with their own distress data.
- **Evidence:** APA (2023) *Healthy Workplaces* (n=2,515): monitored vs unmonitored 56%/40% stress,
  45%/29% negative MH impact. Astill Wright et al. (2025), *npj Digital Medicine*
  doi:10.1038/s41746-025-02118-8 (11/14 studies negative; authors note the link is *inferred*).
  Klintman (2025), *The Conversation*. *(Verifier downgraded some causal framing; mechanism real.)*
- **Bites:** APP, METRICS.
- **Scale:** Universal (app/UX level).
- **Mitigation seed:** Minimum effective check-in cadence; never display personal negative-trend
  data saliently; prohibit streaks/urgency badges/red-dots/scored mood dashboards; batch
  notifications; clinician-reviewed copy; frictionless permanent opt-out.
- **Consider further:** Is *any* individual self-tracking safe, or should tracking be community-level
  only by default?

### B. Labeling / medical-model trap

**B1 — Labeling / at-risk identification (THE MASTER THREAT)** · `high` · conf high · all (acute team)
- **Mechanism:** Selection into an "at-risk/treatment" population → self-perception of needing
  treatment → anticipated devaluation → withdrawal/secrecy/lowered hope → network contraction →
  worse outcomes. A transient stressor crystallizes into a stable "career" as the group's troubled
  person; the label becomes a master status. **Identification itself is the harm** — no adversary
  needed, and it operates even via well-meaning facilitators or self-application.
- **Evidence:** Link et al. (1989), *ASR* 54(3) (modified labeling: withdrawal, secrecy, network
  shrinkage). McCord (1978), *Am Psychologist* 33(3) — 42% treatment vs 32% control undesirable
  outcomes (30yr). Glass et al. (2014), PMC3980578 — ~39%/49% mediated via reduced social support.
  Goffman (1963) spoiled identity / courtesy stigma (taint extends to responders). Link (1987),
  *ASR* 52 (earnings impact).
- **Bites:** APP, PROTO, METRICS, FACIL.
- **Scale:** Universal, but **acute at team scale** — at N≈10–50 any "at-risk" signal is de facto
  individual identification.
- **Mitigation seed:** Never expose individual signal frequency/history to anyone, incl.
  facilitators; ephemeral/unlinkable signals; asset-based non-deficit framing; treat *post-signal
  withdrawal by a previously-visible member* as a **sentinel event** (confidential follow-up), not
  positive variance.
- **Consider further:** This is the crux of the deferred protocol question — can a protocol *connect*
  someone without *identifying* them? (Parked: user has "a lot to say" here.)

**B2 — False-positive "at-risk" designation harms non-converters** · `high` · conf med · team·org
- **Mechanism:** Any "at-risk" flag mislabels a large fraction who'd never have had the problem; the
  label itself triggers anticipatory stigma, altered colleague behavior, self-stigma, secrecy. In a
  10–50-person group, probabilistic flagging *is* individual identification.
- **Evidence:** Yang, Link et al. (2015), *Schizophrenia Research* 168, PMC4751087 — ~65% of
  clinical-high-risk cases never convert yet experience labeling shame/anxiety. Nocebo RCT (Sandra
  et al. 2025, *Psych Medicine*, n=215) — awareness exposure increased false self-diagnosis. Foulkes
  & Stringaris (2023), *BJPsych Bulletin* doi:10.1192/bjb.2022.96.
- **Bites:** METRICS, APP.
- **Scale:** Acute at team scale (small N → flag = identification); present at org.
- **Mitigation seed:** No individual-level risk scoring/flagging; metrics community-level only; any
  metric-triggered outreach delivered **universally** to remove its marking value.
- **Consider further:** Is there any acceptable false-positive rate, or is individual flagging simply
  off the table?

**B3 — Responder/facilitator bias from diagnostic frame** · `med` · conf high · all
- **Mechanism:** A diagnostic/at-risk frame makes responders reinterpret ordinary behavior
  symptomatically and deliver lower-quality/patronizing/avoidant support — even when trained and
  well-intentioned. Managers with signal history apply biased performance assessments.
- **Evidence:** Lam, Salkovskis & Hogg (2016), *Br J Clinical Psych* 55(3) — identical video rated
  worse with a diagnostic label than a behavioral description. (Rosenhan 1973 as illustrative
  background given later methodological criticism.)
- **Bites:** PROTO, FACIL, LEAD.
- **Mitigation seed:** Responders get a *connection* request without diagnostic framing; train on
  label bias; informationally isolate facilitators from individual signal histories.
- **Consider further:** How do you brief a responder enough to help, without handing them a frame
  that biases them?

**B4 — Self-stigma / prevalence inflation from medicalized framing** · `med` · conf med · all
- **Mechanism:** Accepting a MH label → internalizing stereotypes → lowered self-efficacy →
  avoidant coping → worsening. Macro: awareness leads some to re-categorize normal distress
  (loneliness, timezone fatigue) as disorder, adopt the script, and produce genuine new pathology.
- **Evidence:** Corrigan & Watson (2002), *Clin Psych S&P* 9 (self-stigma model; developed for
  already-diagnosed). Foulkes & Andrews (2023/2024) prevalence-inflation hypothesis (explicitly a
  "call to test"). *(Severity downgraded high→med: plausible, partial clinical support, undemonstrated
  in remote-work contexts.)*
- **Bites:** FACIL, METRICS.
- **Mitigation seed:** Strengths-based, non-diagnostic language ("I could use connection," not "I'm
  struggling with my mental health"); problem-normalization ("common for distributed teams"); track
  positive indicators (connection, engagement) not deficit counts.
- **Consider further:** Untested at our scale/context — candidate for the first pilot's measurement.

### C. Contagion

**C1 — Peer contagion / deviancy training in aggregated support** · `high` · conf high · team·org
- **Mechanism:** Aggregating people with shared vulnerabilities lets peers reinforce the targeted
  states; distress/rule-breaking talk met with attention/empathy/laughter escalates. Worst with a
  predominantly high-risk group, unstructured time, thin facilitation.
- **Evidence:** Dishion, McCord & Poulin (1999), *Am Psychologist* 54(9), PMID 10510665. McCord
  (1978) 42%/32%. Cho, Hallfors & Sanchez (2005), *J Abnormal Child Psych* (n=1,218). Ang & Hughes
  meta-analysis (homogeneous high-risk d=0.55 vs mixed/individual d=0.70).
- **Bites:** PROTO, FACIL.
- **Scale:** Group-composition dependent (team/org); the *protocol* design controls exposure.
- **Mitigation seed:** Don't structure groups around distress-sharing; heterogeneous composition
  (mix struggling + thriving); trained facilitation; anti-rumination norms; route peer responses to
  **individual private channels first**, not broadcast; auto-rebalance if responder-pool distress
  concentrates.
- **Consider further:** In a 30-person community, is heterogeneous composition even achievable, or
  does small N force high-risk concentration?

**C2 — Suicide/crisis contagion via distress visibility (Werther)** · `high` · conf high · all (acute platform+team)
- **Mechanism:** Surfacing distress/crisis detail lets vulnerable members identify with and model
  the state via imitation, norm-shift ("crisis is the normal response"), and identification
  (amplified for a known peer). The protocol surfaces distress to peers — contagion's exact pathway.
- **Evidence:** Fink et al. (2018), *PLOS One* PMC5802858 — 1,841 excess US suicides (+9.85%) after
  Robin Williams; suffocation +32.3%. Bridge et al. (2019), *JAACAP* (13 Reasons Why; causal
  attribution *disputed* — Romer 2020). Calvo et al. (2024), *Spanish J Psych & Mental Health* PMID
  38848950 (25-study review). WHO/AFSP safe-messaging; Papageno effect.
- **Bites:** PROTO, METRICS, FACIL.
- **Scale:** Platform (broadcast reach) **and** team (identified peers raise identification).
- **Mitigation seed:** Distress routes to **designated responders only — never a community feed**;
  severity tiers with **no free-text crisis narrative** to the group; validator strips
  method/location specifics + attaches resources; metrics never show raw distress counts; warm-handoff
  acute risk to crisis resources, not peers; Papageno design (every distress narrative carries a
  coping arc).
- **Consider further:** What's the visibility threshold at which peer-identified distress flips from
  supportive to contagious at N≈30? (Research gap.)

**C3 — Co-rumination, emotional contagion & cyberostracism in text** · `high` · conf high · team·org
- **Mechanism:** Text support can (a) loop into co-rumination; (b) spread emotional contagion to
  responders/observers; (c) inflict **cyberostracism** when a signal gets *no* response — in text-
  only CMC, silence reads as active rejection. The harm is *inaction*, so moderation can't detect it;
  in a small community the same few people signal and respond, closing the loop.
- **Evidence:** Mackenzie et al. (2023), *Frontiers in Psychiatry* 14:1040636, PMC10027699 (online
  support-seeking +depression β=0.28, +anxiety β=0.23; in-person negative). Easton et al. (2017),
  *JMIR Mental Health* PMC5684514 — emotional contagion 23.4%, social exclusion 25.4% of adverse
  events. Williams et al. (2000), *JPSP* 79(5) + Hartgerink et al. (2015) Cyberball meta (d>1.4).
- **Bites:** PROTO, METRICS.
- **Mitigation seed:** **Timed-acknowledgment gate** — every signal gets ≥1 ack within a window;
  absence-of-response surfaced to designated responders, never hidden. Structured responder scripts
  with coping/closure; bounded routing not broadcast; track responder burden; professional off-ramps.
- **Consider further:** The acknowledgment gate seems essential — but does an automated ack itself
  become hollow/harmful? What's the minimum *human* guarantee?

**C4 — Digital bystander effect: broadcast → diffusion → no response** · `high` · conf med · org·platform
- **Mechanism:** Broadcasting a help-signal to a visible group diffuses responsibility; response rate
  falls; the signaler reads silence as rejection; stigma + severity-uncertainty add inhibition.
- **Evidence:** Scaffidi Abbate et al. (2022), *Frontiers in Psychology* PMC9413050 — response
  dropped 78.3% (sole recipient) → 21.7% (14 recipients); prosocial priming eliminated it. Barron &
  Yechiam (2002); Latané & Darley (1968). *(Scenario low-stakes; MH-signal inhibition is inference.)*
- **Bites:** PROTO.
- **Scale:** Worse as recipient set grows (org/platform), but present whenever >1 recipient.
- **Mitigation seed:** Route to a **specific named responder** with explicit responsibility + SLA,
  escalate if unacknowledged; prosocial-priming language; **prohibit open-broadcast distress signals**.
- **Consider further:** Named-responder routing collides with B1's "never identify" — the core tension.

### D. Surveillance / metrics harm

**D1 — Employer-adjacency: surveillance perception + disclosure retaliation** · `high` · conf med · all
- **Mechanism:** When perceived as employer-adjacent (company benefit/device/shared infra), two harms
  compound: (1) anticipated surveillance → the highest-risk self-censor, skewing participation and
  corrupting metrics; (2) disclosure retaliation → a signal seen/inferred by anyone with employment
  authority enters supervisor discretion (scrutiny, exclusion, documented "gaps") — plausibly deniable.
- **Evidence:** APA (2023) *Work in America* (n=2,515) — monitored vs unmonitored worse on MH
  (32%/24%), work-harms-MH (45%/29%), exhaustion (39%/22%), intent-to-leave (42%/23%). Dewa et al.
  (2021), *Frontiers in Psychiatry* PMC8032877 — of disclosers with negative experiences, 46.7% lost
  jobs. EEOC v. Ranew's Management ($250K). *(Several secondary stats corrected/removed by verifier.)*
- **Bites:** all layers, acutely PROTO + governance.
- **Scale:** Any employer context, any size.
- **Mitigation seed:** Run on **technically + visibly separate** infrastructure from any monitoring;
  route only to peers with **no employment authority** over the sender; make employer/manager access
  to individual data **technically impossible** (not policy-only); publish an auditable data-flow
  diagram; run a trust/legibility audit with real members; ideally worker-governed/independent
  ownership.
- **Consider further:** Your communities are *not* employer-run — does that neutralize D1, or does
  "any infra someone controls" reintroduce it?

**D2 — Goodhart/Campbell collapse + impression-management + selection bias** · `high` · conf high · all (acute org)
- **Mechanism:** (1) Once aggregate scores become targets, people perform the metric (respond to
  boost rates, avoid honest distress signals) → dashboard green while help-seeking collapses; (2) fear
  of consequences inflates positive surveys (a floor, not a reading); (3) volunteers are already
  healthier → overstated benefit; the most isolated are invisible. **Leaders declare success and
  defund at the point of failure.**
- **Evidence:** Campbell (1979). Keiser & Payne (2019), *Safety Science* 118 — impression management
  28–35% of variance even with anonymity. Jones, Molitor & Reif (2019), *QJE* 134(4) — workplace-
  wellness RCT null; 2020 *JAMA Int Med* confirms. CISD/D.A.R.E. sustained for decades on satisfaction.
- **Bites:** METRICS, FACIL (evaluation).
- **Scale:** Universal; acute wherever metrics become KPIs (org).
- **Mitigation seed:** **Never make aggregate metrics a success criterion** tied to continuation or
  leadership evaluation — strictly diagnostic + lagging; track the *full* community incl. non-
  participants + exits; independent qualitative triangulation; pre-committed stopping rule; **treat a
  suspiciously positive trend as a gaming signal, not a win.**
- **Consider further:** If metrics can never be a success target, what *is* the legitimate success
  signal for the guide? (Bridges to the success model + the metrics-feasibility question.)

**D3 — Engagement-ranked / silent curation amplification of distress** · `high` · conf high · platform
- **Mechanism:** Any ranking/filtering of the signal feed alters the emotional climate; engagement
  ranking over-weights negative content → a doom-loop. *Any* silent curation that shifts emotional
  state without users' knowledge is manipulation.
- **Evidence:** Kramer, Guillory & Hancock (2014), *PNAS* 111(24) — 689,003 feeds manipulated without
  consent; PNAS Expression of Concern. Haugen "Facebook Files" (2021); 32% of teen girls said
  Instagram worsened body image.
- **Bites:** APP, PROTO, METRICS.
- **Scale:** Platform-defining, but applies to any algorithmic feed.
- **Mitigation seed:** **Chronological or severity-tiered routing, never engagement-ranked**; no
  reaction/upvote counts on help signals; disclose all curation logic in consent; **no emotional-
  state-affecting algorithm operates silently.**
- **Consider further:** Mostly a large-scale lesson — what's the minimal-curation default for a small
  community feed?

**D4 — Emotion-AI / biometric metrics mislabel healthy workers** · `med` · conf med · all
- **Mechanism:** "Objective" biometric stress signals carry systematic error that mislabels certain
  populations (post-COVID autonomic dysfunction, chronic conditions, non-Western baselines) →
  aggregate elevates → outreach targets the non-distressed, experienced as surveillance.
- **Evidence:** McLachlan & Truong (2023), *JCDD* 10(4):141, PMC10142541 (5 commercial HRV platforms,
  no clinical definitions). Roemmich, Schaub & Andalibi (2023), *CHI '23* doi:10.1145/3544548.3580950.
- **Bites:** METRICS.
- **Mitigation seed:** **Exclude biometric/AI-inferred emotional signals** from metrics absent
  population-specific peer-reviewed validation; if used, disclose error rates + get explicit consent;
  default to self-report with genuine anonymity.
- **Consider further:** Simplest stance: ban inferred-emotion metrics outright in the guide?

**D5 — Homophily–contagion confound misleads facilitators** · `med` · conf high · all
- **Mechanism:** Observational network metrics can't distinguish contagion (A caused B) from homophily
  (A,B distressed for the same environmental reason). A "wellbeing diffusion index" can be an artifact;
  facilitators then apply social interventions while the real stressor (overwork, isolation) goes
  untouched.
- **Evidence:** Shalizi & Thomas (2011), *Soc Methods & Research* 40(2), PMC3328971. Cohen-Cole &
  Fletcher (2008), *BMJ* 337:a2533 — "contagion" of acne (62%) and headaches (47%) via the same methods.
- **Bites:** METRICS, FACIL.
- **Mitigation seed:** Any graph-based "spread" metric needs an explicit confound-control plan +
  statistician sign-off; give facilitators a checklist of shared-environment explanations to rule out.
- **Consider further:** Does the guide simply prohibit network "spread" metrics for lay facilitators?

### E. Privacy / re-identification

**E1 — Cumulative-release attacks (reconstruction / membership / composition)** · `high` · conf high · acute team·org
- **Mechanism:** A preventive SNH system is **longitudinal** — repeated aggregates about the *same
  small group* — the exact threat model that defeats naive per-release noise. Reconstruction
  (Dinur–Nissim), membership inference/differencing (with side knowledge), and composition (DP epsilon
  accumulates additively) all apply.
- **Evidence:** Dinur & Nissim (2003), *ACM PODS* doi:10.1145/773153.773173. Abowd et al. (2025),
  *HDSR* arXiv:2312.11283 — reconstructed 97M Census records, re-identified 3.4M at 95%. Jacobs et al.
  (2009), *Nature Genetics* 41 (membership from aggregate frequencies). Von Thenen et al. (2019),
  *Bioinformatics* 35(3) — membership at 95% with 5 queries in a 65-person beacon (a 30-person
  community is *more* vulnerable). Ganta et al. (2008) composition attacks.
- **Bites:** METRICS (over time); also cumulative session notes/trend reports.
- **Scale:** **Acute at team scale** — small N is the worst case, not the safe case.
- **Mitigation seed:** Formal **differential privacy with a GLOBAL lifetime privacy budget**
  (sequential-composition / Rényi accounting), not per-release noise; release only DP-noised outputs;
  fixed pre-registered breakdowns (no differencing); retention limits; **"we add noise per release" =
  red flag.**
- **Consider further:** Bombshell — may make useful longitudinal metrics *infeasible* at N=10–50.
  (Becomes the metrics-feasibility question.)

**E2 — ZKP proves correct computation, NOT non-identifying output** · `high` · conf high · all
- **Mechanism:** ZKPs prove a computation ran correctly on private inputs — but say **nothing** about
  whether the output is identifying. A ZKP over a differencing query proves the count is correct yet
  doesn't protect the person. DP and ZKPs are orthogonal; conflating them produces false confidence.
- **Evidence:** Garrido, Babel & Sedlmeir (2022), "Towards Verifiable Differentially-Private Polling,"
  arXiv:2206.07220 (ZKP verifies the DP mechanism was applied; DP must still be designed in). Biswas &
  Cormode (2022), arXiv:2208.09011 (both layers must coexist).
- **Bites:** METRICS (design).
- **Mitigation seed:** Separation of concerns — **ZKP = verifiability, DP = output privacy; require
  BOTH**; "ZKP is our privacy protection" = escalate to a cryptographer.
- **Consider further:** Directly corrects the project's stated ZKP plan — metrics need DP *and* ZKP,
  not ZKP alone.

**E3 — Behavioral-trace re-identification of pseudonymous signals** · `high` · conf high · acute team
- **Mechanism:** Even with no identifiers, behavioral patterns (timestamps, response latency,
  frequency, device/network metadata) are unique enough to re-identify. A curious admin matches a
  pseudonymous trace to a known person ("Alice always logs on at 6am Pacific"). Distinctiveness is
  highest in small teams.
- **Evidence:** Narayanan & Shmatikov (2008), *IEEE S&P* (Netflix de-anon). De Montjoye et al. (2013),
  *Sci Reports* 3:1376 — 4 points uniquely identify 95% in mobility data. AOL search-log re-ID (2006).
- **Bites:** APP, PROTO.
- **Scale:** Acute at team scale (behavioral uniqueness highest at small N).
- **Mitigation seed:** Strip/bucket timestamps before storage; don't log device IDs/IPs/latency with
  signals; k-anonymize log exports; **separate metrics-access (aggregates) from admin-access (raw
  logs)** with audit trails.
- **Consider further:** Even a benevolent builder *inside* the community is a re-identification vector —
  how does the architecture bind the builder's own hands?

### F. Consent / governance

**F1 — Coerced/bundled consent at the moment of distress** · `high` · conf high · all
- **Mechanism:** Broad data-sharing consent presented in ToS at acute distress, or as a precondition
  of help, when capacity is impaired and refusal is unrealistic; data later used for ads/AI-training/sale.
- **Evidence:** FTC v. BetterHelp (Mar 2023, $7.8M) — required MH intake then shared answers with
  ad platforms despite confidentiality promises. Crisis Text Line / Loris.ai (danah boyd, Jan 2022:
  "A ToS is not consent"). Brookings (2023) on MH-app policy readability.
- **Bites:** APP, PROTO, FACIL.
- **Mitigation seed:** **Separate consent from help-seeking** — governance disclosures accepted during
  a calm onboarding, never at distress; ~6th-grade reading level; granular consent; withdrawable
  without losing access; review with a community advocate before launch.
- **Consider further:** Onboarding-time consent vs B1 (you can't fully understand consent before
  you've used the system) — how to keep consent live and re-affirmed?

**F2 — Coercive financial incentives → compelled disclosure** · `high` · conf high · org
- **Mechanism:** Penalties for non-participation make refusal economically irrational, converting a
  "voluntary" program into a de facto mandatory medical exam + data-sharing requirement.
- **Evidence:** AARP Foundation v. Yale (2022, $1.29M settlement) — $25/wk opt-out fee + biometric
  screening; AARP v. EEOC (D.D.C. 2017) vacated 30%-surcharge rules as involuntary.
- **Bites:** PROTO, FACIL.
- **Scale:** Employer-program (org) specific.
- **Mitigation seed:** Structurally independent of any employer incentive/penalty/participation
  tracking; binding rule that utilization/signals never inform employment decisions.
- **Consider further:** Mostly out-of-scope for your volunteer communities — keep as a large-scale
  warning.

**F3 — Non-consensual crisis escalation → harmful welfare/police checks** · `high` · conf high · all (acute team)
- **Mechanism:** Automated crisis detection (keyword/sentiment/NLP) flags high-severity and escalates
  to emergency services/security/HR without consent; responders arrive in a way that outs MH status,
  creates a legal record/debt, or — with police — physical danger. Others learn and stop using it.
- **Evidence:** Calou & Zeavin (2022), Slate. Forced psychiatric hospitalization ~30× baseline suicide
  rate at 5–10yr (2017 *JAMA Psychiatry* meta, 100 studies). Pendse et al. (2024), "Consent-Forward
  Paradigm," arXiv:2404.14548 / *Nature Mental Health*. Crisis Text Line ~28 non-consensual rescues/day.
- **Bites:** PROTO.
- **Scale:** Universal; **acute for remote workers** — the employer/system knows the home address, so
  an automated wellness check *is* a disclosure of MH status.
- **Mitigation seed:** **Prohibit automated escalation to third parties by default**; any escalation
  beyond peers needs explicit, revocable, **advance** consent + a clear "do not escalate" option;
  surface crisis resources as **information, not triggered actions**; discuss scenarios before go-live.
- **Consider further:** This is the sharpest "well-intentioned automation kills trust" case — should the
  guide ban automated escalation entirely?

### G. Help-seeking suppression & stepped-care failure

**G1 — Chilling effect on help-seeking (stigma + reactance + coercion)** · `high` · conf med · all
- **Mechanism:** A formal help-signal channel can *suppress* help-seeking among those who most need
  it (label avoidance, self-stigma); coercive/collective participation makes the not-ready conceal
  → false negatives. Remote workers lack ambient informal help-seeking, so a stigmatized formal channel
  blocks all routes.
- **Evidence:** Corrigan, Druss & Perlick (2014), *PSPI* 15(2). Clement et al. (2015), *Psych Medicine*
  45(1) (144 studies; stigma 4th-highest barrier; d≈−0.27). Kisely, Campbell & Preston (2011), *Cochrane*
  (no consistent benefit of compulsory community treatment).
- **Bites:** entire intervention.
- **Mitigation seed:** Frame **entirely outside clinical language** — universal peer connection
  (everyone sends *and* responds), not a help-system for the distressed; explicitly voluntary,
  individually anonymous, never tied to performance or visible to management; leadership models
  help-seeking without enforcing it.
- **Consider further:** "Everyone sends and responds" is the leading candidate resolution to B1/C4 —
  does it dissolve the chilling effect, or just hide need?

**G2 — Gatekeeper training: confidence without behavior change; repels high-risk** · `high` · conf med · all
- **Mechanism:** (1) Gatekeeper programs raise knowledge/confidence but show no reliable improvement in
  observable helping behavior — a false "it's working" signal; (2) training the people *around*
  high-risk individuals can turn them into perceived *reporting nodes* rather than safe confidants.
- **Evidence:** Forthal et al. (2022), *Psychiatric Services* 73(4), PMC8814050 (MHFA: 6/9 high-quality
  studies no behavior change). 2025 gatekeeper RCT meta (PMC11956478) — no significant skill
  improvement. Wyman et al. (2008) — *the 17.8/37.8% figure is a baseline difference, not a
  training-caused decline.* (Part 2 plausible but not demonstrated as training-caused.)
- **Bites:** PROTO, FACIL.
- **Mitigation seed:** Don't treat training completion/confidence as readiness — require **observed
  role-play** before certifying responders + periodic behavioral follow-up; separate "trained" from
  "able"; keep responders free of evaluative/managerial authority.
- **Consider further:** Feeds the responder-readiness gate — what's the minimum *demonstrated*
  competency bar?

**G3 — Stepped-care evaporation: preventive layer fails to step up** · `high` · conf med · all
- **Mechanism:** The prevention→crisis continuum only works if people can escalate when they deteriorate;
  in practice step-up fails (clinical judgment over instruments, no formal agreements to the next level,
  patients lose contact with referrals). Someone stays trapped in the preventive layer as they worsen.
- **Evidence:** Hermens et al. (2014), *BMC Family Practice* 15:5, PMC3893377. (Telehealth engagement
  ~56.6% initial; corrected figures.)
- **Bites:** PROTO, FACIL.
- **Mitigation seed:** **Pre-connect explicit step-up pathways** (EAP, crisis line, clinician) before
  deployment, verified across time zones; severity/frequency threshold surfaces a **direct clinical
  resource**; **never let the preventive layer be the only layer.**
- **Consider further:** Directly operationalizes your "preventive AND emergency, not emergency-only"
  point — what's the minimum viable step-up for a small volunteer community without a budget?

**G4 — False reassurance: quick response masks unmet clinical need** · `med` · conf med · all
- **Mechanism:** A peer/automated response felt as "heard and helped" reduces urgency about
  professional care without any severity screen; the person disengages from professional pathways;
  conditions worsen; dashboards show high engagement mistaken for good outcomes.
- **Evidence:** Linardon et al. (2024), *npj Digital Medicine* PMC11655657 — only 32%/171 MH-app trials
  reported adverse events; deterioration 6.7% *but not different from controls*. Babu & Joseph (2025),
  *Frontiers in Psychiatry* PMC12003299 (commentary). (Direct causal evidence sparse.)
- **Bites:** PROTO, FACIL.
- **Mitigation seed:** Distinguish **"acknowledged" from "adequately supported"**; 24–48h follow-up;
  train peers *not* to position as clinical substitutes; make referral a standard output; track
  follow-through-to-referral, not just response rate.
- **Consider further:** How does a peer system know when *not* to reassure?

### H. Communication-medium harm (CMC)

**H1 — Text-only misattribution, dehumanization, toxic disinhibition** · `high` · conf high · all
- **Mechanism:** Text strips cues that activate empathy and self-regulation: (1) senders overestimate
  how legibly tone transfers → real distress read as "fine," benign messages read as alarming; (2)
  voice humanizes, text conceals → a help signal may read as aggression/weakness; (3) lack of eye
  contact drives flaming → a single mocking reply poisons the well community-wide.
- **Evidence:** Kruger, Epley, Parker & Ng (2005), *JPSP* 89(6) — senders predicted ~78% tone-decode,
  actual ~56% (≈chance). Schroeder, Kardas & Epley (2017), *Psych Science* 28(12). Lapidot-Lefler &
  Barak (2012), *Computers in Human Behavior* 28(2) (eye-contact > anonymity for disinhibition). Suler
  (2004).
- **Bites:** PROTO, METRICS, FACIL.
- **Mitigation seed:** Specify **richer-channel response (voice/async voice notes)** as standard; text
  only for initial ack; treat text signals as **imprecise triggers for richer follow-up, not
  diagnostic data**; templates that name uncertainty ("I read this as X — is that right?");
  **discount text-derived sentiment in metrics.**
- **Consider further:** Your IT background covers comms *effectiveness* — this is the *psychological*
  layer; a big seam for the success model (channel-by-type effects).

**H2 — Remote-network atrophy: weak-tie loss, video fatigue, onboarding failure** · `high` · conf high · all (remote)
- **Mechanism:** Remote-only work degrades the social substrate the intervention runs on: weak/bridging
  ties atrophy (siloed strong-tie clusters; signals may never reach the best responder); videoconference
  fatigue makes the "rich" channel least accessible to the exhausted (selection toward the well-rested);
  remote-onboarded members form almost no bridging ties → the highest-need are least reachable.
- **Evidence:** Yang et al. (2022), *Nature Human Behaviour* 6(1) (n=61,182 Microsoft) — WFH −32% weak-tie
  time, −9% bridging ties, −41% bridging collaboration. Fauville et al. (2021) Zoom Exhaustion scale
  (N=2,724). Bailenson (2021), *Tech, Mind & Behavior* 2(1). Smite et al. (2025), arXiv:2510.05878
  (remote-onboarded resign more within 3yr).
- **Bites:** underlying community layer, FACIL, APP (onboarding).
- **Mitigation seed:** **Network-mapping gate before launch** (find siloed clusters/missing bridges);
  track weak-tie density + new-member centrality as leading indicators; route **cross-cluster pairings**;
  structured weak-tie onboarding for ~8 weeks; **audit aggregate video-load; default to audio for the
  richer-medium step.**
- **Consider further:** The intervention assumes a social substrate that remote work has already
  eroded — does the guide need a "build the substrate first" pre-phase?

### I. Community / leadership

**I1 — Peer enforcement of harmful norms + polarization + call-out dynamics** · `high` · conf med · all (acute team)
- **Mechanism:** An ecologically-built program can encode and amplify existing maladaptive norms: (1)
  destructive conformity (stoicism/overwork → peer-shunning of help-signalers); (2) group polarization
  (homogeneous online deliberation → more extreme shame toward disclosure); (3) call-out dynamics (a
  named responder who "fails" becomes a target → "safety through silence").
- **Evidence:** Abbink et al. (2017), *Nature Communications* 8:609, PMC5607004 — peer punishment drove
  participation in *destructive* behavior. Sunstein (2002), *J Political Philosophy* 10(2) (group
  polarization, worse online/homogeneous). Aguiar (2025) call-out chilling (FIRE/YouGov: ~62% self-censor).
- **Bites:** FACIL, LEAD, PROTO.
- **Scale:** Universal; acute in tight (team) communities.
- **Mitigation seed:** **Norm-mapping phase** to surface maladaptive norms *before* protocol design;
  facilitators empowered to **challenge a destructive consensus**, not just mirror it; add a
  **help-seeking-suppression metric** (low signal in high-stress env = RED); structured dissent
  mechanisms; privacy-preserve responders (no public logging/grading); no naming-and-shaming.
- **Consider further:** "By and with the community" can *encode* the very norms that harm — how much
  authority does the facilitator/guide get to override community consensus?

**I2 — Leadership inaction / inadequate response to a first-time signal** · `high` · conf med · all (acute team)
- **Mechanism:** A leader receives a distress signal and fails to act (lack of training, boundary
  uncertainty, liability fear, avoidance). No response to a clear crisis, or a delayed/shaming response,
  confirms to the member *and the watching community* that signaling is unsafe — especially damaging on
  a first-time signal. Because reporting is low, leaders mistake silence for health.
- **Evidence:** Grotto-de-Souza et al. (2023), PMC10124815 (harm underestimated due to low reporting).
  Miyake et al. (2022), PMC9425057 (n=13,468) — telework loneliness AOR 2.49.
- **Bites:** LEAD, PROTO.
- **Mitigation seed:** Escalation chain with **response-time SLAs** + auto-escalation fallback if no human
  ack; **leadership training a deployment prerequisite, not optional**; a **leader-readiness gate** (skills
  *and* institutional authority to respond); measure leadership response rate as a primary process metric.
- **Consider further:** You named leadership ignorance the greatest threat — but reframed leaders as part
  of a system. Does the gate test the *leader*, the *system*, or both?

### J. Transfer / fidelity — the "build-it-yourself ecological guide" failure cluster

**J1 — Voltage drop, model drift, surface-only cultural adaptation** · `high` · conf med · org·platform·(team transfer)
- **Mechanism:** A meta-process rebuilt by each community is exactly the transfer condition where EBPs
  decay: voltage drop (expert pilot → ordinary practitioners), model drift (each layer reinterprets
  components until only the name remains, while leadership believes it runs the validated model), and
  surface-only adaptation (language changes but not the deep-structure assumptions the program depends on).
- **Evidence:** McKay et al. (2023), *PLOS ONE* 18(5):e0268164 — median 52.6% voltage drop. Al-Ubaydli,
  List & Suskind (2019), NBER WP 25848. Markström (2014), *IJERPH* 11(10), PMC4211004 (model drift).
  Schloemer & Schröder-Bäck (2018), *Implementation Science* 13(1):88. MYRIAD (83% form-fidelity, null-to-harmful).
- **Bites:** FACIL, LEAD.
- **Scale:** Acute at scale-up (org/platform), but any community-to-community transfer applies.
- **Mitigation seed:** Publish a **core-components inventory** (non-negotiable "active ingredients" vs
  adaptable periphery) communities map against at intake + 6-month review; **minimum-dose spec** + 30/90-day
  fidelity self-assessment ("voltage monitor"); **deep-structure diagnostic gate** before adoption
  (help-seeking norms, psychological safety, power, disclosure attitudes — block until prerequisites built);
  a **"model steward"** role (separate from the community) to flag drift.
- **Consider further:** This is *the* risk for a self-propagating guide — how do you keep "active
  ingredients" intact while honoring genuine ecological adaptation?

**J2 — Successor-facilitator competency decay + satisfaction-masks-harm** · `high` · conf med · all
- **Mechanism:** (1) Generational decay — each cohort of facilitators is trained more briefly; successors
  master surface mechanics but not judgment calls (when to escalate, unsafe disclosures, harmful dynamics)
  — invisible in async remote settings until a crisis; (2) measurement substitution — participants report
  satisfaction even when the process is null/harmful, so facilitators expand a harmful program (worsened by
  the community having *designed* it).
- **Evidence:** Shahmalak et al. (2019), PMC6790996 (lay health workers want more supervision). Kagee
  (2002), *Critical Care* 6(2), PMC137400 (CISD satisfaction = gratitude, not symptom reduction). West &
  O'Neal (2004), *AJPH* 94(6), PMC1448384 (D.A.R.E. satisfaction with null/negative effects).
- **Bites:** FACIL, PROTO, METRICS.
- **Mitigation seed:** **Minimum competency standard** (not curriculum completion) with **observed
  role-play at each training generation**; supervision chain back to clinical/facilitation expertise;
  **cap train-the-trainer chains** (≤2 hops without re-certification); objective leading indicators
  *alongside* satisfaction; pre-committed stopping trigger; **independent outcome monitor** outside the
  facilitation team.
- **Consider further:** A "partly-assisted" guide could make AI the consistency-keeper across generations —
  is that a safe use of AI, or does it reintroduce voltage drop of a different kind?

### K. Remote-worker baseline risk environment & operating constraints

> **A different *kind* of threat from A–J.** A–J are *iatrogenic failure modes* (how an
> intervention harms). **K is the terrain** — the baseline stressors and constraints that (i)
> define what the intervention must address (→ success model), (ii) make the population more
> vulnerable, *amplifying* the A–J harms, and (iii) limit which interventions are even possible
> remotely. **Source:** domain expert (Rich), 2026-06-09. **Citations now supplied by the completeness
> pass (Addendum §3): K1–K4 strongly cited (conf high); K5 thin; K6 still under-cited (gap).** The
> number of these risk factors is *increasing*.

**K1 — Chronic isolation & weak belonging (baseline)** · `high` · conf exp · all
- **Mechanism:** Remote work makes isolation the daily default and weakens belonging to the
  remote community; ambient/informal contact is scarce. This *lowers the protective factors the
  intervention depends on* and raises baseline vulnerability.
- **Evidence:** *pending* — connects to Miyake et al. (2022) telework loneliness AOR 2.49 (cited
  in I2); Buffer State of Remote Work; needs current sources.
- **Bites:** the whole substrate; amplifies B-cluster, C3/C4, G1, H2.
- **Note:** the *problem the intervention targets*, not a failure mode.
- **Consider further (success model):** what reliably builds belonging remotely?

**K2 — Timezone dispersion, interruption, sleep/circadian disruption → health** · `high` · conf exp · all
- **Mechanism:** Cross-timezone work + frequent interruption → fragmented schedules, sleep
  disturbance, circadian misalignment → physical & mental-health decline; also makes synchronous
  connection (and synchronous interventions) hard to schedule.
- **Evidence:** *pending.*
- **Bites:** operating constraint on any synchronous intervention (H2); amplifies vulnerability.
- **Consider further:** async-first design; respect-the-clock norms.

**K3 — Technological displacement / underemployment / job insecurity → depression** · `high` · conf exp · all *(current, worsening)*
- **Mechanism:** AI/automation is displacing remote knowledge workers (acutely software
  developers; gig/freelance work such as Fiverr that supported livelihoods, e.g. in India) →
  unemployment/underemployment/insecurity → elevated depression. A *rising* macro stressor; the
  population is increasingly precarious.
- **Evidence:** *pending — explicitly needs current 2025–2026 research.*
- **Bites:** raises baseline depression (amplifies every help-seeking, contagion, and labeling
  threat); a **confound for metrics** (D2/D5 — distress driven by the external labor market, not
  the community).
- **Consider further:** an intervention can't fix the labor market — what is the honest scope, and
  how do you avoid blaming the community for macro-driven distress?

**K4 — Declining in-person contact (post-COVID inflection)** · `med` · conf exp · all
- **Mechanism:** Since COVID, remote communities meet in person far less (travel cost/time); the
  periodic co-presence that built trust has thinned, and the trend is ongoing (observed in the
  decentralized-web-dev community).
- **Evidence:** *pending.*
- **Bites:** erodes the trust substrate the intervention assumes (H2; J1 deep-structure
  prerequisites).
- **Consider further:** should the guide recommend periodic co-presence as an active ingredient?

**K5 — "Degraded mode": loss of embodied / experiential co-present learning** · `high` · conf exp · all
- **Mechanism:** Experiential learning involving the body and the physical presence of others is
  uniquely valuable for building community comfort and help-seeking. Remote operates in a *degraded
  mode* where some connection/help-seeking affordances simply aren't available — not a normal
  evolutionary state for humans.
- **Evidence:** *pending — experiential-learning / embodiment / co-presence literature.*
- **Bites:** caps the ceiling of any remote intervention; some school/military protective
  mechanisms may not transfer (J1 surface-vs-deep adaptation).
- **Consider further (key success-model question):** which protective factors *require* embodiment,
  and which have viable remote analogs?

**K6 — Hard-to-corral / unreachable-in-bulk → selection bias & coverage gaps** · `high` · conf exp · all
- **Mechanism:** Remote workers are notoriously hard to get onto one channel at one time; you reach
  — and gather SNH data from — only the reachable subset, so the least-reachable (often
  highest-need) are invisible. Interventions are simply harder to run remotely.
- **Evidence:** *pending; connects to D2 healthy-worker selection.*
- **Bites:** METRICS (selection bias), PROTO/FACIL (coverage), LEAD (mistaking the reachable
  sample's health for the community's).
- **Consider further:** channel-agnostic "meet them where they are" design (a stated PRM goal) and
  phone-tree fan-out (see design ideas in the session log) as partial coverage mitigations.

---

## Confirmed threats — formerly quarantined (RESOLVED by the completeness pass)

All three were re-run through adversarial verification and **CONFIRMED (high confidence)** — promoted
out of quarantine. Full citations: **Addendum §4**.

- **Q-a — Third-party SDK / tracking-pixel leakage + onward data-broker sale. CONFIRMED (high).**
  FTC v. BetterHelp ($7.8M); Cerebral pixel breach (3.1M users); Duke Sanford report (brokers selling
  mental-health-identified records from $0.20). Consistent with F1.
- **Q-b — Commercial pivot of help-seeking data without meaningful consent. CONFIRMED (high).**
  FTC v. Cerebral ($7.1M); 23andMe 2025 bankruptcy → potential data-transfer of ~15M people (27 states
  sued to require re-consent). Consistent with F1.
- **Q-c — Small-community re-identification from "aggregate" metrics. CONFIRMED (high). GATES THE
  METRICS LAYER.** Sweeney (2002): 3 quasi-identifiers (ZIP + gender + DOB) uniquely identify 87% of
  the US population; k-anonymity collapses at small N. **Governing rule:** in a community of ~10–200,
  {role + timezone + tenure} routinely yields equivalence classes of k=1 — **no per-subgroup metric
  breakdown is safe by default**; it requires a hard minimum-cell threshold (n≥5, often higher),
  complementary-cell suppression to block differencing, and differential privacy over a multi-year
  release budget (which may render useful longitudinal small-N metrics infeasible — Research Gap #3).
  Consistent with E1–E3.

---

## Research gaps (what to study next)

1. Empirical test of these mechanisms in **non-clinical, remote-worker** populations (most citations are
   clinical/school/justice/general-CMC). Prevalence inflation (B4), async deviancy training (C1), and the
   gatekeeper "repelling" effect (G2.2) are explicitly *undemonstrated* in this context.
2. The "repelling the highest-risk" mechanism (G2.2) is theorized but unproven — needs a controlled study.
3. **Small-N DP utility/privacy tradeoff at N=10–50 over a multi-year budget** — defensive parameterization
   is unworked; may show useful longitudinal metrics are infeasible at this N (a possibility the methodology
   must be prepared to accept).
4. Whether **any** community health metric survives Goodhart + suppression + selection simultaneously in a
   small voluntary remote community (plausibly: qualitative + process measures must be primary).
5. Re-verify the three quarantined privacy threats (Q-a/b/c) before designing metrics.
6. Werther/contagion **visibility threshold** for a tight identified community (C2) — when does
   peer-identified distress flip from supportive to contagious at small N?
7. **Facilitator-competency decay rate** for a self-propagating model (J2) — how many train-the-trainer hops
   before judgment falls below a safety floor, and whether async remote delivery accelerates it.

---

## Next: from threats to a success model

Every **Mitigation seed** above is a hypothesis about what *works*. The forthcoming **success model** will
research the positive evidence — design features and practices empirically linked to better remote-worker SNH
outcomes — and link each one back to the threat IDs it addresses, so the two datasets form a single queryable
evidence base for the guide and (eventually) the guardrails + methodology.


---

# Completeness Addendum to the Threat Catalog — Social Network Health Interventions for Remote-Worker Communities

**Status:** Completeness pass (addendum to v1, 2026-06-09). Living document.
**Provenance:** Completeness sweep over the verified catalog — targeted at MISSING threats, MISSING citations (esp. K1–K6), and quarantine re-verification. Every finding below carries the study's own scale/context and a verbatim quotable passage so each citation can later become a deep link. All verifier corrections are applied inline. Strongest evidence wins regardless of n.

> **How to read IDs here.** New threats *extend* existing letter categories where the mechanism fits the cluster, and use **K7+** for remote-baseline *terrain* (K is explicitly "the terrain," not an iatrogenic failure mode). The brainstorm's working "L#" labels are mapped to stable catalog IDs and noted in each header as `(was L#)`.

---

## 1. Summary — what the completeness pass changed

- **17 new threats verified and added.** IDs assigned by extending existing categories (A5, D6, D7, G5, H3, H4, I3, I4, J3, J4) and the baseline-terrain category (K7–K13). Three are materially-different *angles* on K3 (anticipatory AI threat, top-performer reputation collapse, employed-but-trapped productivity ratchet) and are added as **K3a/K3b/K3c** sub-entries rather than new IDs, to keep K3 as the single "labor-market macro stressor" anchor.
- **K1–K6 citations lifted out of "pending."** K1, K2, K3, K4 are now strongly cited with scale + quote (multiple sources each, including 2024–2026 large-N work the original corpus lacked). K5 has one practitioner source (remains thin). **K6 remains under-cited** — only adjacent evidence found; flagged as a remaining gap.
- **Additional citations supplied for previously-thin existing IDs:** A2, B2, B4, C3, D1, D2, G1, G2, G3, H1, H2, I1, I2, J1, J2.
- **Quarantine fully resolved — all three confirmed.** Q-a (SDK/pixel leakage + broker sale), Q-b (commercial pivot of help-seeking data), and **Q-c (small-N re-identification from "aggregate" metrics) — CONFIRMED, high confidence.** Q-c gates the metrics layer: per-subgroup breakdowns in a small community are **not** safe by default; the addendum states the governing rule.
- **34 success-model leads captured** for the next phase, each tagged to the threat IDs it may mitigate.
- **Single-source / low-confidence flags** are called out explicitly in §2 and §6. The most theoretically contested new claim (belonging-need *irreversibility*) was downgraded per verifier and re-scoped.

---

## 2. New threats to add

> Each entry: **PROPOSED ID** · severity · confidence · scale — **Mechanism** · **Evidence** · **Source / scale-context / quote** · **Bites** · **Mitigation seed** · **Distinct from**. Verifier corrections applied inline; residual weaknesses flagged.

### A. Iatrogenic design (extension)

**A5 — Subgroup-masking: harm + averaged intervention BOTH hide the at-risk stratum (defeats null-result evaluation)** · `high` (see caveat) · conf med · org·platform·team
- **Mechanism:** Remote work does not uniformly reduce engagement/wellbeing — it *selectively* harms high/moderate-loneliness workers while leaving low-loneliness workers unaffected. A universal intervention evaluated on population averages can show a **null** result while masking severe harm to the loneliest subgroup. This is a different angle from A2: not "universal prevention worsens a subgroup," but that **the underlying harm *and* an averaged-out evaluation both hide the same stratum** — so a clean-looking null is not evidence of safety.
- **Evidence:** Moderated mediation: for high-loneliness workers, remote work significantly negatively predicted job engagement (b=−0.08, β=−0.23, p<.001); for low-loneliness workers, no effect (b=−0.001, p=.96). Authors explicitly warn that interventions averaging across employees miss the most-harmed subgroup.
- **Source:** Bareket-Bojmel, Chernyak-Hai & Margalit (2023), *"Out of sight but not out of mind: The role of loneliness and hope in remote work and in job engagement,"* **Personality and Individual Differences** 202:111955, doi:10.1016/j.paid.2022.111955. **Scale/context:** n=349 US/UK employees, Prolific, cross-sectional, 2022. **Quote:** *"Remote work predicted decreased job engagement only for employees with high and moderate levels of loneliness. These results challenge the widespread assumption that remote work impairs employee engagement."*
- **Bites:** APP, PROTO, METRICS.
- **Mitigation seed:** Risk-stratify (screen for high-loneliness, solo-living, junior/freelance subgroups); track **individual-level outcomes**, never group averages alone, to catch non-responders and harmed subgroups early; route the lonely subgroup to more intensive contact (step-care logic).
- **Distinct from:** A2 (worsening) — here the hazard is *evaluation blindness*.
- **⚠ Verifier caveat:** Cross-sectional Prolific sample → cannot establish causation (loneliness may precede both remote-work preference and disengagement). A representative Norwegian longitudinal study (n=1,511) found remote work *positively* associated with engagement overall, so the population-level harm claim is not settled, and **severity=high may be overstated** for a population where lonely workers are *targeted* rather than averaged. Single unreplicated moderated-mediation study. **Convergent (not replication) support:** Becker et al. (2022), *"Surviving remotely,"* **Human Resource Management** (Wiley) — loneliness as a key mediator of remote-work harm.

---

### D. Surveillance / metrics (extension)

**D6 — Invisible facilitation / emotional-labor blind spot: care work is untracked → hidden facilitator burnout + biased health metrics** · `medium` · conf high · all *(was L6)*
- **Mechanism:** Maintainers/facilitators perform complex, invisible interpersonal and organizational work (conflict mediation, donation/labor management, onboarding diplomacy, code-of-conduct enforcement). Because workload metrics capture only technical/visible output, any community-health metric layer systematically **underestimates the load on the very people SNH depends on** — burning them out and biasing the metrics simultaneously.
- **Evidence:** Geiger, Howard & Irani (2021): F/OSS maintainers perform "complex and often-invisible interpersonal and organizational work." Intel survey: maintainer burnout the **top** challenge at **45%** (self-selected sample, n=666). A 2024 quantitative anchor (arXiv 2401.06889) finds **~50% of OSS activities are invisible** and half of that work is uncompensated.
- **Source:** Geiger, Howard & Irani (2021), *"The Labor of Maintaining and Scaling Free and Open-Source Software Projects,"* **Proc. ACM CSCW** 5(CSCW1):175, doi:10.1145/3449249; Intel **2023 Open Source Community Survey** (ran Dec 2023–Jan 2024, n=666); OpenSauced (2024) *"The Hidden Cost of Free."* **Scale/context:** Geiger qualitative interviews across many F/OSS projects (UCSD); Intel n=666 self-selected; OpenSauced industry analysis. **Quote (confirmed verbatim abstract language):** *"F/OSS maintainers also perform complex and often-invisible interpersonal and organizational work to keep their projects operating as active communities of users and contributors."*
- **Bites:** FACIL, METRICS, LEAD.
- **Mitigation seed:** Make invisible facilitation labor visible, rotate it, and recognize it in acknowledgment systems; community-health metrics must include facilitation/social labor alongside technical contribution; distribute care labor explicitly before the community grows.
- **Distinct from:** J2 (successor competency decay) and K3 (economic precarity) — here the harm is the **measurement invisibility of care labor itself**.
- **Correction applied:** The "more difficult and draining aspects" line is a paraphrase of paper body, not a verbatim abstract pull — the verbatim abstract sentence is used above instead. Intel 45% is "of survey respondents," not a population estimate. Stronger quantitative anchor: arXiv 2401.06889 (142 respondents).

**D7 — Public-performance-audit impostor phenomenon: output visibility drives anxiety, self-silencing, productivity suppression (AI-amplified)** · `medium` · conf med · all *(was L13)*
- **Mechanism:** Public code review, open contribution histories (commit graphs/leaderboards), and constant output visibility create a persistent performance-audit environment. Members chronically compare worth against visible metrics → impostor phenomenon, anxiety, self-silencing that suppress help-seeking and perceived productivity, progressing to depression/burnout. Remote/async removes the normalizing peer feedback that would attenuate it; AI adds a second layer (feeling inadequate vs. AI output speed).
- **Evidence:** n=624 software engineers across 26 countries — **52.7%** experience frequent-to-intense impostor phenomenon (women 60.6%, men 48.8%); statistically significant negative effect on perceived productivity across **all** SPACE constructs; may progress to depression/burnout. First-person Babel-maintainer account on commit-as-worth.
- **Source:** Guenes, Tomaz, Kalinowski, Baldassarre & Storey (2023), *"Impostor Phenomenon in Software Engineers,"* arXiv:2312.03966 (published ICSE-SEIS 2024); Zhu, Henry (2019), *"(Open) Source of Anxiety,"* **Increment** Issue 9. **Scale/context:** Guenes n=624, 26 countries; Zhu n=1 Babel maintainer. **Quote:** *"The presence of IP showed a statistically significant negative effect on the perceived productivity for all SPACE framework constructs."*
- **Bites:** APP, FACIL, METRICS.
- **Mitigation seed:** De-prioritize individual-output leaderboards in community metrics; normalize struggle and surface routine peer vulnerability; onboarding/facilitator training names impostor phenomenon and its AI-augmented form; validate non-code contributions.
- **Distinct from:** B4 (self-stigma from labeling) and K1 — here the driver is the **visibility/audit architecture** of public contribution; concrete design lever = de-emphasize output dashboards.
- **Correction applied:** **DROP the "Devsu 2025: 40% AI-induced impostor" statistic — unverifiable, likely fabricated.** For the AI-amplification layer use instead: Stack Overflow **2025 Developer Survey** (n=49,009) — 20% of developers report declining confidence in personal problem-solving from AI over-reliance — plus the SO blog (Jul 31 2025) qualitative coverage. Backbone (Guenes 2023, Zhu 2019) is solid.

---

### G. Help-seeking suppression (extension)

**G5 — Platform-distrust silencing: perceived techno-insecurity/complexity/invasion suppresses psychological safety → mutes the signals the platform seeks** · `high` · conf high · all *(was L10)*
- **Mechanism:** When members perceive technology as unreliable, insecure, complex, or boundary-invading, they conserve cognitive resources by **staying silent** rather than voicing concerns/suggestions — with reduced psychological safety as the mediator. For a small SNH community this is self-defeating: distress signals and early warnings are never surfaced because the platform meant to detect them is itself distrusted.
- **Evidence:** n=361 Hungarian remote/hybrid employees — techno-insecurity (β=−0.32), techno-complexity (β=−0.23), techno-invasion (β=−0.27) all reduced psychological safety; techno-insecurity (β=−0.19) and techno-complexity (β=−0.16) directly reduced promotive voice; techno-insecurity reduced intrinsic motivation and affective commitment. Systematic review (10 studies, 2015–2025): technostress fosters social isolation by replacing deep interaction with superficial digital exchange.
- **Source:** Frontiers in Psychology (2025), *"Navigating the digital landscape: …technostress on employee voice behavior,"* doi:10.3389/fpsyg.2025.1434275; **American Journal of Applied Scientific Research** (2025), *"Mapping the Impact: A Systematic Review of the Psychological and Social Repercussions of Technostress,"* Vol. 11(4). **Scale/context:** n=361 Hungarian remote/hybrid (collected Mar–Apr 2022); review of 10 studies. **Quote:** *"Technostress arises from the perception that information technology is unreliable, insecure, and uncertain, ultimately decreasing employees' belief that it is safe to take risks."*
- **Bites:** G1, H1, PROTO.
- **Mitigation seed:** Make the SNH platform demonstrably low-insecurity, low-complexity, non-invasive (participatory design, transparent data practices, radically simple UX); audit every added feature/notification channel for techno-invasion. **A distrusted platform will silence the very signals it seeks to detect.**
- **Distinct from:** G1 (general help-seeking chilling) and H1 (CMC disinhibition) — the causal lever is the **perceived insecurity/complexity/invasiveness of the tooling itself**, independent of social stigma.
- **Note:** COVID-era Hungarian cross-sectional sample may overestimate magnitude for a voluntary purpose-built platform — weakens magnitude, not existence. Mechanism multiply replicated in the broader technostress literature. ("paradoxically" in the review gloss is the threat author's addition, not a direct quote.)

---

### H. Communication-medium / CMC (extension)

**H3 — AI-mediated interaction displaces human-to-human bonds: bot-filed issues/PRs/reviews erode belonging and mutual trust** · `medium` · conf med · all *(was L12)*
- **Mechanism:** As GenAI bots increasingly file issues, submit PRs, and perform code review, transactional AI-mediated exchanges displace human-to-human interaction, reducing mentorship, informal learning, and interpersonal trust — the social capital that sustains participation. Members never receive genuine **human** acknowledgment of their contribution, diminishing belonging and relatedness. Structurally distinct from H1: the counterpart is **non-human**, so the relational return that text normally still provides is absent.
- **Evidence:** Peer-reviewed roadmap (now in ACM TOSEM): "loss of community interaction emerges when generic AI comments may make reviews transactional, reducing human engagement and community bonds"; grounded in self-determination theory.
- **Source:** Feng, Milewicz, Murphy-Hill, Menezes, Serebrenik, Steinmacher & Sarma (2024), *"Charting Uncertain Waters: A Socio-Technical Roadmap for Sustaining Open Source Communities in the Age of GenAI,"* arXiv:2508.04921v2, **published ACM TOSEM** doi:10.1145/3789210. **Scale/context:** conceptual/vision paper, multidisciplinary team + 2 external expert validators (no empirical effect sizes yet). **Quote:** *"loss of interpersonal connection and mutual trust may diminish contributors' sense of belonging and relatedness."*
- **Bites:** APP, PROTO, FACIL.
- **Mitigation seed:** Track the ratio of human-to-human vs. bot-mediated interactions at key touchpoints (code review, issue triage); create explicitly **human-only** spaces (synchronous rituals, mentorship pairings) that AI tools are not invited into.
- **Distinct from:** H1 (human↔human text CMC).
- **Correction applied:** The "94% of OSS orgs use GenAI" figure is **unverified** against the primary Linux Foundation 2024 report, which states **84% moderate-to-high GenAI adoption** (Lawson et al. 2024) — use 84% (or flag 94% as unverified). Threat is prospective/theoretical (no measured belonging/trust degradation yet); industry pattern may be augmentation rather than pure displacement. Emerging empirical literature is forming (Vaccargiu et al., BoatSE '26).

**H4 — Capable-contributor blind spot: visible high competence/output masks rapid deterioration; risk indicators are anti-predictive** · `high` · conf med · all *(was L4)*
- **Mechanism:** High-achieving / neurodivergent contributors maintain visible productivity and apparent normalcy until a sudden discontinuity; members and gatekeepers calibrate risk on recent output and **systematically miss the deterioration underneath**. The "capable contributor" profile is *anti-predictive* of safety — defeating any output- or distress-cue-based detection.
- **Evidence:** Reflective project-lead account after a prolific 18-year-old contributor's suicide: "How could such a prolific contributor… feel that death was preferable to life? This was a person who was boundlessly competent." Independent peer-reviewed corroboration of the high-capability/elevated-risk inversion: autistic individuals with exceptional cognitive ability show *elevated* suicidal ideation (the usual protective effect of high IQ inverts).
- **Source:** jackpot51 (2021), *"Open Source and Mental Health,"* **Redox OS Blog**, June 12 2021; corroboration — Cassidy et al. (2022/2023), *"The combination of autism and exceptional cognitive ability is associated with suicidal ideation,"* PMC10088461; prevalence anchor — **OSMI Mental Health in Tech Survey 2016** (osmihelp.org/research, n≈1,400): 51% diagnosed vs ~19% US adults. **Scale/context:** n=1 fatality reflective account; Cassidy peer-reviewed empirical; OSMI self-selected survey. **Quote:** *"To succeed [at suicide] is to overcome extreme subconscious desires. This means that, for suicide, often the smartest and most capable people are able to succeed. This anti-selection of capable people is a terrifying epidemic."*
- **Bites:** APP, FACIL, LEAD.
- **Mitigation seed:** Do **not** rely on visible distress cues or productivity drops as primary risk indicators; build check-in/belonging infrastructure for high-performers; gatekeeper/peer training must explicitly name the capable-contributor blind spot and the misleading nature of competence-as-safety.
- **Distinct from:** G2 (gatekeeper false confidence) and B3 (responder diagnostic bias) — here visible competence is itself an actively-misleading safety cue. (Definitional overlap with G2/B3 is acknowledged.)
- **Correction applied:** **Replace the "Chan, Business Insider 2020" secondary citation — not verifiable.** Cite OSMI data directly (osmihelp.org/research, n≈1,400, self-selected). "Anti-selection" rests on a single n=1 essay (compelling, not a validated predictive model); Cassidy provides the peer-reviewed mechanism support.

---

### I. Community / leadership (extension)

**I3 — Entitled-user demand escalation suppresses distress disclosure and opens a trust vacuum for bad actors** · `high` · conf high · all *(was L5)*
- **Mechanism:** In publicly visible communities, when a maintainer/facilitator signals distress or capacity limits, **entitled consumers respond with escalating demands rather than support**. This asymmetric pressure (few maintainers, many demanders) suppresses honest help-seeking (one cannot signal need without receiving *more* demands), accelerates crisis, drives chronic emotional-labor burnout, **and opens a trust vacuum a malicious actor can exploit.**
- **Evidence:** xz/liblzma: the sole maintainer disclosed "my ability to care has been fairly limited mostly due to longterm mental health issues," following a coordinated sock-puppet pressure campaign — and the **only** actor who responded with "help" was the attacker who later inserted the backdoor. Industry: "Consumers make demands (some polite, some not-so-polite) of one maintainer (rarely two) that does everything." Survey trend: severe interpersonal challenges (stalking, doxxing, harassment) rose 2017→2024 and drive contributor dropout.
- **Source:** Mensching, Rob (2024), *"A Microcosm of the Interactions in Open Source Projects"* (Mar 30 2024); Speed, Richard (2025), *"Open Source Maintainers Are Really Feeling the Squeeze,"* **The Register** (Feb 16 2025); Sapegin, Artem, *"Why I quit open source,"* sapegin.me (Sep 2023, updated Feb 2024); *"Shifting Sands of Toxicity"* (2025), **IEEE Xplore** 11323252. **Scale/context:** xz n=1 case (Lasse Collin; critical Linux infra, millions of systems); The Register industry reporting; Shifting Sands n=5,495 (2017) vs n=8,452 (2024) GitHub surveys. **Quote:** *"I haven't lost interest but my ability to care has been fairly limited mostly due to longterm mental health issues but also due to some other things."* (Collin)
- **Bites:** APP, FACIL, LEAD.
- **Mitigation seed:** Train members to recognize distress-coded language in public channels and respond with **offers of help, not demands**; create a "signal amplification" norm prioritizing wellbeing disclosures over issue queues; give facilitators low-friction deflection tools + moderator authority over hostile interactions; surface asymmetric workload via visibility dashboards.
- **Distinct from:** I1 (peer enforcement of *in-group* norms) — here the harmful pressure comes from **external consumers/free-riders**, and the documented consequence includes a **security/safety exploit**, not just polarization.
- **Correction applied (minor dates only — no fabrication):** Collin's quote originates June 2022 (xz-devel list); the 2024 date refers to the Mensching article citing it. Sapegin originally published Sep 2023 (edited Feb 2024). Mensching's own verbatim line ("Consumers make demands…") is distinct from the Collin quote.

**I4 — Consensus-governance overload: open all-decisions consensus amplifies conflict + political labor → facilitator burnout** · `medium` · conf med · all *(was L8)*
- **Mechanism:** Communities relying on consensus for *all* decisions generate disproportionate coordination burden; conflict-averse members' attempts to "be nice" create ambiguity and stalemate; the resulting frustration and political labor burn out leaders and drive exodus. The **structure of decision-making itself** is the harm vector — and it has a documented fix (modular governance).
- **Evidence:** Jupyter (1,500+ contributors, 100+ repos) could not sustain consensus governance; community-wide frustration contributed to leader burnout; restructuring to an Executive Committee + Working Groups reduced it.
- **Source:** Salkever, Alex (2023), *"Open Source Maintainers,"* **Linux Foundation Research** (32 interviews with maintainers of top-200 critical OSS projects). **Scale/context:** 32 qualitative interviews; Jupyter case 1,500+ contributors, 100+ repos. **Quote:** *"the ambiguity that exists and the difficulty of really balancing a consensus model with a lot of people who tend to be conflict diverse or just want to be nice all the time results in patterns that are likely to burn folks out."*
- **Bites:** APP, FACIL, LEAD.
- **Mitigation seed:** Allocate explicit decision rights and conflict-resolution pathways before growth; avoid pure consensus above ~15–20 active participants; adopt modular governance (steering council + working groups).
- **Distinct from:** I-series (norm enforcement / leadership inaction) and J-series (fidelity decay).
- **⚠ Correction applied:** **Re-attribute the quote.** The Jupyter interviewee in the LF 2023 report is **Brian Granger** (Jupyter co-creator), **not Myles Borins** (who has no documented Jupyter-governance connection). The Jupyter restructuring is independently confirmed (jupyter.org/governance). Cite as Salkever (2023) — Jupyter case, **Granger**; re-verify the exact quote against the full PDF and attribute to Granger.

---

### J. Transfer / fidelity (extension)

**J3 — Single-maintainer "lottery factor": knowledge concentration makes one person's burnout a whole-community crisis** · `medium` · conf high · all *(was L7)*
- **Mechanism:** In small distributed communities one person holds disproportionate technical **and social** knowledge; their burnout/departure/crisis leaves no continuity, and the resulting collapse or trust vacuum is itself a community-health crisis for everyone remaining. A "trust paradox" compounds it: incumbents hesitate to delegate for fear of quality loss, perpetuating the single point of failure.
- **Evidence:** Lottery factor: "If 50% of the PR contributions come from two or fewer contributors, the lottery factor is high." **61% of unpaid maintainers work entirely alone**; **>18M of ~28M npm package releases have a single maintainer**; node-pre-gyp departure left the ecosystem scrambling 2+ years; xz-utils and Kubernetes Ingress NGINX retirement (Nov 11 2025) as exemplars.
- **Source:** OpenSauced (2024), *"The Silent Crisis in Open Source: When Maintainers Walk Away"*; Socket.dev (2025), *"The Unpaid Backbone of Open Source"*; **Tidelift 2024 State of the Open Source Maintainer Report** (n=437). **Scale/context:** node-pre-gyp n=1; Tidelift n=437; ecosystem ~1.4M maintainers (Ecosyste.ms; current est. ~1.7M). **Quote:** *"This current unsustainable model is a ticking time bomb. When key maintainers leave, projects can quickly become outdated, insecure, or completely non-functional."*
- **Bites:** APP, LEAD, FACIL.
- **Mitigation seed:** Track community-wide lottery/bus factor as a health metric; build succession protocols and graduated-trust delegation (review access before merge rights); distribute institutional knowledge via documentation **before** crisis.
- **Distinct from:** I2 (leadership inaction on a signal) and J2 (successor competency decay) — here the hazard is the **structural concentration** of knowledge/dependency and the **irreversibility of sudden loss**.
- **Correction applied:** npm stat understated — real figure is **>18M of ~28M single-maintainer releases (>64%)**, not 16M (i.e., worse). Ecosyste.ms 1.4M is slightly dated (~1.7M now). "Ticking time bomb" / "trust paradox" quotes are approximate paraphrases of the OpenSauced article — treat as such.

**J4 — Successor onboarding decay via undocumented-knowledge loss** *(reinforces J2; not a separate ID — fold into J2 evidence)*
- **Note:** The Intel 2023 finding — maintainer burnout 45% **and** documentation/onboarding challenges 41% as paired top concerns — supplies the missing causal link for J2: *burnout degrades documentation → impairs successor onboarding → competency decay.* Added to J2's citation set in §3 rather than as a new ID.

---

### K. Remote-worker baseline risk environment (terrain extension, K7–K13)

**K7 — Professional/career isolation as a distinct harm from social loneliness (lost mentoring, visibility, promotion penalty)** · `medium` · conf high · all *(was L1)*
- **Mechanism:** Remote workers lose informal mentoring, casual problem-solving, organizational visibility, and informal learning ("out of sight, out of mind"). This is empirically **distinct from social loneliness**: it produces missed-career-opportunity perceptions, reduced self-efficacy, a degraded wellbeing→performance link, and measurable career harm (e.g., promotion at ~half the rate despite higher productivity).
- **Evidence:** Professional isolation moderated the wellbeing–performance relationship (3-way interaction p=0.010; performance lowest at high PI + low boundary control, 2.85 vs 4.05). Grounded theory: telecommuting reduces networking, informal learning, mentoring (stronger in public sector). RCT: home workers 13% more productive but **promoted at half the rate**. Definition: professional isolation as "a state of mind or belief that one is out of touch with others in the workplace."
- **Source:** Jaiswal & Prabhakaran (2024), **Employee Relations** 46(1):115–132, doi:10.1108/ER-08-2022-0384; Cooper & Kurland (2002), *"Telecommuting, Professional Isolation, and Employee Development…"* **J. Organizational Behavior** 23:511–532, doi:10.1002/job.145; Bloom, Liang, Roberts & Ying (2015), *"Does Working from Home Work?"* **QJE** 130(1):165–218; Golden, Veiga & Dino (2008), **J. Applied Psychology** 93(6):1412–1421. **Scale/context:** Jaiswal n=218 Indian IT (2022–23); Cooper & Kurland n=93 grounded theory; Bloom Ctrip RCT. **Quote:** *"there was a sudden void felt by employees with regard to informal mentoring, casual discussions for problem-solving, and the occasional exchange of pleasantries that contributed to employee's sense of belongingness with the organisation."*
- **Bites:** substrate, APP.
- **Mitigation seed:** Distinguish social- vs professional-isolation interventions; add lightweight visibility rituals (async show-and-tell, shared work logs, explicit mentoring pairings) that rebuild professional presence without surveillance; advocate promotion-criteria transparency to counter the remote advancement penalty.
- **Distinct from:** K1 (social belonging), K3 (job insecurity/displacement), H2 (weak-tie atrophy).
- **Note:** Jaiswal interaction stats (p=0.010; 2.85 vs 4.05) are paywalled — confirmed design/direction, treat exact values as unverified detail (not fabrication). Multi-decade, multi-method support.

**K8 — Reciprocal distress↔isolation feedback loop: distress independently increases perceived isolation; detection itself can feed the loop** · `high` · conf high · all *(was L2)*
- **Mechanism:** Isolation causes distress **and** distress independently increases perceived isolation — a bidirectional reinforcing loop. Critically, a wellness platform that **surfaces or amplifies distress signals** (e.g., highlighting who didn't engage) can worsen isolation perception; interventions targeting only one direction will fail.
- **Evidence:** 3-wave cross-lagged SEM: both isolation→distress and distress→isolation paths significant; authors describe a reciprocal effect.
- **Source:** Van Zoonen & Sivunen (2022), *"The impact of remote work and mediated communication frequency on isolation and psychological distress,"* **EJWOP** 31(4):610–621, doi:10.1080/1359432X.2021.2002299. **Scale/context:** n=1,164 Finnish workers; 3-wave longitudinal Mar–Sep 2020; 77.2% remote 5 days/week. **Quote:** *"The findings highlight a reciprocal effect between psychological distress and isolation, suggesting that strain may both increase perceptions of isolation and be a result of being isolated."*
- **Bites:** APP, PROTO, METRICS.
- **Mitigation seed:** **Do not surface distress signals or non-engagement** in ways that heighten perceived isolation; break the loop with low-stakes positive touchpoints that reduce distress first; monitor distress **and** isolation as co-evolving indicators with early triggers before the loop self-sustains.
- **Distinct from:** K1 (isolation as upstream cause) and C2/C3 (visibility→contagion) — here the mechanism is the **self-sustaining loop** and the risk that **detection feeds it**.
- **Correction applied:** The "reverse path (distress→isolation) is *often stronger*" / "meta-analytic hints" framing **could not be verified** — the confirmed finding is **symmetric reciprocity** (both directions significant), with no confirmed directional ranking. Drop the "stronger reverse path" claim; the loop + both-directions-matter + detection-can-feed-it core is fully supported.

**K9 — Silent dropout / invisible attrition as a distress signal in distributed communities** · `high` · conf med · all *(was L3)*
- **Mechanism:** In remote/OSS communities there is **no visible absence**: distressed members simply stop contributing/communicating without signaling distress. Unlike physical workplaces where absence triggers concern, digital absence is normalized and unnoticed until total attrition — producing survivorship/selection bias where only resilient members stay visible, masking population-level distress. The missing signal is the member's **own silence/exit**, the very thing a preventive system must detect.
- **Evidence:** "burnout often goes unnoticed in the open-source community, as contributors silently drop out and disengage." Onion-model health indicators: low active-user participation + leadership-succession failure. n=1 fatality: the last contact before a contributor's death was purely technical, indistinguishable from routine work.
- **Source:** Raghunathan (2024), *"Cultivating Community Health and Well-being in Open Source,"* **J. Technology & Systems** 6(2):1–8, doi:10.47941/jts.1791; Crowston & Howison (2006), *"Assessing the Health of Open Source Communities,"* **IEEE Computer** 39(5):89–91; jackpot51 (2021), *"Open Source and Mental Health,"* **Redox OS Blog**. **Scale/context:** Raghunathan mixed-methods whitepaper; Crowston & Howison observational over the 100,000+ SourceForge population; Redox OS n=1. **Quote:** *"burnout often goes unnoticed in the open-source community, as contributors silently drop out and disengage."*
- **Bites:** APP, METRICS, FACIL.
- **Mitigation seed:** Treat sudden activity/contact drop as a signal requiring **human follow-up (with consent)**; establish non-technical touchpoints decoupled from work output; design outreach for members who go silent; use onion-model contribution mapping + lottery-factor as leading indicators.
- **Distinct from:** K6 (hard-to-corral selection bias *at recruitment*) and C4 (broadcast→no response).
- **⚠ Correction applied:** Raghunathan is a **self-described whitepaper in a low-tier open-access journal (CARI Journals) — downgrade evidential weight**; the verbatim quote could not be confirmed against full text (likely close paraphrase). **Prefer higher-rigor citations:** Raman et al. (2020), *"Stress and Burnout in Open Source,"* **ICSE-NIER 2020** (CMU, peer-reviewed, empirical); Guizani et al. (2021), emoji/dropout study, arXiv:2102.05737. Phenomenon itself is well-supported (also Science 2023 aec7671).

**K10 — Telepressure / always-on availability drives rumination, sleep loss, burnout (modifiable upstream of K2)** · `high` · conf high · all *(was, in part, the K2 deep-dive)*
- **Mechanism:** Telepressure (perceived expectation to respond quickly) extends cognitive engagement into non-work hours → work-related rumination that blocks detachment/recovery; combined with actual after-hours work it **nearly quadruples sleep-disturbance odds.** The operative mechanism is the **social-availability norm itself** — directly modifiable by community design.
- **Evidence:** Telepressure → burnout (β=0.19, p<0.001), mediated by work-related rumination, worse when organizational support low (n=323). WFH alone OR 1.71 for sleep disturbance; work-during-nonwork-time OR 3.04; **combined OR 3.93 (men 5.08)** (n=27,473). Blurred boundaries OR 2.67 and >45 hrs/week OR 2.11 as strongest independent predictors of emotional exhaustion (63.1% prevalence; n=247).
- **Source:** Qin, Yu, Cai, Jiang & Chung (2025), *"How Workplace Telepressure Fuels Job Burnout Among Educators,"* **Behavioral Sciences** (MDPI) 15(8):1109, doi:10.3390/bs15081109, PMC12383041; *"Combined effect of work from home and work during nonwork time on sleep disturbance,"* PMC10493373 (**Sixth Korean Working Condition Survey 2020**); **J. Health & Rehabilitation Research** (2025), *"Prevalence of Burnout and Emotional Exhaustion in Remote or Hybrid Workers."* **Scale/context:** n=323 Chinese teachers; n=27,473 Korean workers; n=247 remote/hybrid (Jan–Apr 2025). **Quote:** *"Workplace telepressure increases employees' workload and extends their cognitive engagement into non-working hours."*
- **Bites:** K2, H1, APP.
- **Mitigation seed:** Build explicit off-hours messaging norms + socially-enforced quiet windows; default the platform to silencing notifications outside working windows; model facilitator disconnection; use right-to-disconnect-style **collective rituals**, not individual willpower.
- **Distinct from:** K2 (timezone/interruption→circadian) and H1 (CMC misattribution) — the lever is the **availability norm**.
- **Correction applied:** Journal name fix — PMC12383041 is **Behavioral Sciences (MDPI)**, not Frontiers. All statistics verified exactly.

**K11 — Inverted-U / non-monotonic work-mode dose curve: fully-remote shows a persistent mental-health/thriving deficit vs hybrid (with a hybrid sleep counter-twist)** · `high` (scoped) · conf med · all *(was L9)*
- **Mechanism:** Work-mode outcomes are non-monotonic. **Fully-remote carries a persistent mental-health/thriving deficit vs hybrid** in both COVID-era and post-COVID data, implying a purely-remote community has a structural disadvantage that better belonging design *reduces but may not fully erase*. Counter-twist: hybrid's **irregular cadence** produces the worst circadian/sleep disruption (instability of both modes without the regularity of either).
- **Evidence:** Both exclusive-remote and exclusive-in-person had higher odds of poorer self-rated mental health vs hybrid (aOR=2.79). Fully-remote: highest engagement but lowest thriving (36% vs 42% hybrid). Hybrid "least beneficial" for sleep due to irregular cadence.
- **Source:** Bodner, Ruhl, Barr, Shridhar, Skakoon-Sparling & Card (2022), *"The Impact of Working from Home on Mental Health… Third Wave,"* **IJERPH**, PMC9517068; **Gallup 2025** *"The Remote Work Paradox"*; **Polish National Health Programme 2021–2025** (Nofer Institute of Occupational Medicine, Łódź) via Science in Poland (2024). **Scale/context:** Bodner n=1,576 Canadian workers (Apr–Jun 2021); Gallup global tracking 2025; Polish N>1,000. **Quote:** *"hybrid work associates with better mental health outcomes, while exclusive remote or exclusive in-person work both correlate with poorer self-rated mental health."*
- **Bites:** substrate, LEAD, APP.
- **Mitigation seed:** Design at least some in-person/synchronous touchpoints into nominally-remote communities to capture the hybrid mood benefit; **anchor hybrid cadence to a predictable rhythm** to avoid the circadian penalty of irregular switching.
- **Distinct from:** K1/K4 (isolation, declining in-person contact) and K2 (circadian) — the variable is the **work-mode configuration** and its non-monotonic dose-response.
- **⚠ Correction applied (framing downgrade):** **The clean "both extremes worse" inverted-U is overstated.** Bodner is a **COVID-era artifact** (skewed sample: 77.2% hybrid, only 6.6% in-person-only; cross-sectional; in-person disadvantage likely reflects COVID safety anxiety). **Gallup does NOT show a clean inverted-U:** on thriving, on-site **ties** hybrid (both 42%) and on-site has **lower** stress than both hybrid and remote. Correct reading: *fully-remote is worse than hybrid AND on-site on thriving; hybrid and remote are similarly stressed; on-site is not clearly worse than hybrid post-COVID.* Cite Bodner as a pandemic-context finding, not a structural law. The Polish sleep finding is accurately cited and adds genuine nuance. Re-scope severity to the **fully-remote deficit** specifically (well-supported), not the symmetric U.

**K12 — Long-term full-remote work suppresses the *need to belong* itself (engagement-resistance risk)** · `high` (re-scoped) · conf med · all *(was L11)*
- **Mechanism:** Prolonged remote work appears to reduce not just the *fulfillment* of the belonging need but **the need itself**, lowering motivation to seek social re-integration and producing a self-reinforcing withdrawal tendency that **resists later interventions**. Members fully remote for an extended period may not engage with the very programs designed to help them — a **timing-critical** hazard.
- **Evidence:** Three-wave longitudinal study (n=876): heavy remote work "not only reduced employees' sense of community but also their need to belong to one," described as **unexpected**. Corroborating withdrawal arm: professional isolation → social withdrawal and reluctance to seek support.
- **Source:** Finnish Institute of Occupational Health (Kaltiainen J, Suutala S) (2024/2025), *"Engagement and Social Connections in Multi-location Work"* / *"Remote work can weaken the need for belonging"* (Finnish Work Environment Fund 230152); Figueiredo, Margaça & Sánchez-García (2025), **Healthcare** 13(16):1943, doi:10.3390/healthcare13161943, PMC12385570. **Scale/context:** FIOH **n=876**, three survey waves 2023–2024 + six weekly surveys (City of Kuopio + OP Financial Group), **observational/longitudinal (not causal)**; Figueiredo bibliometric review of 65 articles, 40 countries (underlying studies cross-sectional). **Quote:** *"Remote work is not just either a good or a bad thing. It can increase flexibility, but also weaken the sense of community."*
- **Bites:** APP, PROTO, FACIL.
- **Mitigation seed:** Initiate preventive SNH interventions **EARLY** (before prolonged isolation sets in); do not rely on opt-in community spaces or assume stable belonging motivation; onboard members into community structures at entry; use proactive, facilitated connection rather than passive availability.
- **Distinct from:** K1 (weak belonging) and H2 (network atrophy) — here the **motivational substrate for community-building decays**.
- **⚠ Correction applied (important — most contested claim downgraded):** **Remove "irreversibility," "down-regulation," and "withdrawal-spiral / motivational-substrate decay" language** — the FIOH source describes a **self-reinforcing tendency**, *not* irreversibility, and uses none of those terms; the ">6–12 months" threshold has **no empirical basis** in either source. This collides with foundational theory (Baumeister & Leary 1995), where deprivation **intensifies** the belonging need rather than suppressing it — making irreversibility the most theoretically contested claim. **Re-label as "belonging-need suppression / engagement-resistance," not "irreversibility."** Cite FIOH accurately (n=876, three-wave, observational, self-reinforcing dynamics noted but irreversibility *not* established). Mitigation (early proactive intervention) remains well-grounded after the downgrade.

**K13 — AI-mediated displacement (terrain twin of H3 / K3)** *(cross-reference, no new ID)* — the *baseline-terrain* face of bot displacement (declining human contact as ambient condition) is covered by H3 (mechanism) + K4 (declining in-person contact) + K3 (labor-market macro stressor). No separate K ID; cross-linked.

---

### K3 — labor-market macro stressor (three new materially-different angles, added as sub-entries)

> These extend K3 without creating new IDs; K3 remains the single "external labor market drives distress" anchor. Each is a **different angle**: anticipatory threat (K3a), top-performer inversion (K3b), employed-but-trapped (K3c).

**K3a — Anticipatory AI/automation-threat distress: fear of obsolescence harms even employed, non-displaced workers (incl. clinical construct AIRD)** · `medium` · conf med
- **Mechanism:** *Mere awareness* of AI in the workplace — without any actual job loss — predicts job insecurity, emotional exhaustion, anxiety, insomnia, identity loss, via AI-awareness → job-insecurity / work-family-interference → exhaustion. Clinicians propose a distinct syndrome ("AI Replacement Dysfunction") that impairs workers **before** displacement.
- **Evidence:** AI awareness → emotional exhaustion (β=0.648, p<0.001); job insecurity carried 34.4% of the effect, work-family interference 24.2%, serial path 16.8% (n=303). Automatable-job workers had **+4 percentage-point** probability of severe mental disorder (corrected — see below), mediated by fear of job loss/skill obsolescence. APA: 54% say job insecurity significantly affects stress.
- **Source:** Zheng & Zhang (2025), **Behavioral Sciences**, PMC12024253; Blasco, Rochut & Rouland (2025), **Industrial Relations**, doi:10.1111/irel.12356 (IZA DP15434); McNamara & Thornton (2025), *"AIRD,"* PMC12459875 / Cureus doi:10.7759/cureus.93026; **APA 2025 Work in America Survey** (n=2,017, Mar–Apr 2025). **Scale/context:** Zheng n=303 China (cross-sectional); Blasco nationally-representative French PSM; AIRD conceptual/clinical framework. **Quote:** *"AI awareness positively predicts job insecurity, which in turn positively predicts emotional exhaustion."*
- **Bites:** substrate, APP, PROTO.
- **Mitigation seed:** Track **subjective AI-threat perception** (not just actual job loss) as an early-warning signal; flag AIRD-type symptom clusters and high-automation-exposure occupations as priority subgroups; gatekeeper training should include AI job-loss as an explicit stressor category.
- **⚠ Corrections applied:** (1) Blasco effect is **+4 pp** (IZA DP15434), not +3. (2) The APA ~2× exhaustion/demotivation finding applies to firms hit by **government-policy changes broadly** (tariffs, federal cuts), **not AI-specific firms** — the APA report does not isolate AI-exposed firms; reframe as "~1.7–1.9× at policy-disrupted organizations, with AI obsolescence fears noted separately but without a dedicated effect size." Core phenomenon strongly supported across all four sources with corrections.

**K3b — Reputation-premium collapse for high-skill freelancers: expertise no longer buffers AI displacement (identity double-bind)** · `high` · conf med
- **Mechanism:** Generative AI compresses the historic reputational/earnings premium of top-tier freelancers (comparable output at negligible cost); the highest-skill, highest-reputation workers experience the steepest **relative** declines. This **inverts** the usual K3 framing — experienced experts who believed expertise was protective face an unexpected identity threat compounded by economic harm, a double-bind that "competence-as-protection" peer framing actively worsens.
- **Evidence:** ~2% decline in monthly contracts and ~5% earnings drop after GenAI releases; writing/editing/translation posts fell **20–50%**. Firms substituted ~$1 freelance spend for $0.03 AI; >50% of 2022 freelance buyers exited by Q3 2025.
- **Source:** Hui, Reshef & Zhou (2024), *"The Short-Term Effects of Generative AI on Employment: Evidence from an Online Labor Market,"* **Organization Science** (Upwork, millions of contracts); *"Winners and losers of generative AI,"* **JEBO** Jan 2025, doi:10.1016/j.jebo.2024.106845 (3M+ postings); Kharazian, A. (2026), *"AI's First Substitution: Freelancers,"* **Ramp**. **Scale/context:** Upwork millions of contracts; JEBO 3M+ postings; Ramp firm-level Q4 2021–Q3 2025. **Quote:** *"Skilled freelancers, who have traditionally relied on their expertise and reputation, are now competing against advanced algorithms that perform tasks faster and cheaper."*
- **Bites:** substrate, APP.
- **Mitigation seed:** Do **not** assume experienced/high-skill freelancers are psychologically resilient; peer support must acknowledge the reputational-premium collapse and identity threat; facilitators avoid framing competence as protection, and instead support AI-complementary reframing + income-volatility normalization.
- **⚠ Corrections applied:** (1) The JEBO paper authors are **Teutloff, Einsiedler, Kässi, Braesemann, Mishkin & del Rio-Chanona** — **not Hui/Reshef**. (2) Ramp/Kharazian published **Feb 2026** (not 2025); exit data runs to **Q3 2025** (not Q2). (3) The "top-earner harmed most" finding is real but **labeled "suggestive"** by the authors (secondary heterogeneity result) — do not present as definitive; the specific interaction coefficients (0.5%/1.7% per 1% prior earnings) are **unverified** paywalled regression estimates. (4) The "identity double-bind" is an editorial inference, not a direct claim of the papers.

**K3c — GenAI productivity-expectations ratchet: more output expected while hidden validation/debug burden rises → burnout for the still-employed** · `high` · conf med
- **Mechanism:** GenAI adoption inflates organizational throughput expectations while increasing **hidden** demands (validating, debugging, security-remediating AI output). Developers who can't sustain the accelerated pace face elevated burnout even as visible output grows — **employed but locked into an escalating output contract.** Demand amplification + invisible work under continued employment, plus a forecasting illusion (devs expect AI to save time but it costs time).
- **Evidence:** Job demands → burnout (β=0.398, p<0.001) (n=442); qualitative: "I move fast with AI and move mountains of work, but I am losing my passion." RCT: experienced devs forecast AI would cut completion time 24% but it **increased** completion time **19%**.
- **Source:** Feng, Afroz & Sarma (2025/2026), *"From Gains to Strains: Modeling Developer Burnout with GenAI Adoption,"* arXiv:2510.07435v2 (accepted ICSE-SEIS 2026); Becker et al. (2025), *"Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity,"* arXiv:2507.09089 (METR). **Scale/context:** Feng n=442 across 56 OSS communities + multinationals, PLS-SEM mixed-methods; Becker **n=16 developers, 246 tasks**, RCT (confidence intervals not fully reported; authors caution against over-generalization; scoped to early-2025 frontier tools). **Quote:** *"I move fast with AI and move mountains of work, but I am losing my passion."*
- **Bites:** APP, PROTO, LEAD.
- **Mitigation seed:** Track invisible-work load (review burden, AI-output remediation hours) **separately** from commit velocity; facilitators name the expectations-ratchet in onboarding; help-seeking norms must affirm that "keeping up" is not a moral failure; protect autonomy over AI tool use and provide learning resources.
- **⚠ Corrections applied:** **The "~10 more PRs/year per core contributor" sub-claim appears in neither paper — flag/remove (unverified).** Note Becker n=16 with wide CIs in scale-context. "Non-renegotiable output contract" is an interpretive framing beyond what either paper directly demonstrates.

---

## 3. Citations for K1–K6 and other previously-thin entries

> "Citations pending" can now be lifted for **K1, K2, K3, K4** (strongly cited). **K5** has one practitioner source (thin). **K6 remains under-cited** — see §6.

### K1 — Chronic isolation & weak belonging (conf now **high**)
- **Holt-Lunstad, Smith, Baker, Harris & Stephenson (2015)**, *"Loneliness and Social Isolation as Risk Factors for Mortality,"* **Perspectives on Psychological Science** 10(2):227–237, doi:10.1177/1745691614568352. *70 prospective studies, combined N in the hundreds of thousands; effects stronger for samples mean age <65 (working-age).* Quote: *"The weighted average effect sizes were as follows: social isolation odds ratio (OR) = 1.29, loneliness OR = 1.26, and living alone OR = 1.32…"*
- **Emanuel, Harrington & Pallais (2026)**, *"Home alone: Remote work, isolation, and mental health,"* **Science**, doi:10.1126/science.aec7671. *N=588,322 employed US adults; five nationally representative surveys 2011–2024; remote work explains ~1/3 of the post-pandemic rise in distress; effect ~10× for those living alone.* Quote: *"The shift in work location to the home carries measurable costs at the population level."*
- **He, Wei, Goodman, Pagan, Cuevas & Bather (2026)**, **J. Affective Disorders** 393(Pt B):120456. *N=87,317 (weighted ~33M employed US adults), 2024 Household Pulse.* Quote: *"A high frequency of remote work (>3 days per week) appears to increase the likelihood of loneliness…"*
- **Miyake et al. (2021)**, medRxiv doi:10.1101/2021.05.31.21258062. *n=4,052 Japanese desk workers, Dec 2020.* Quote: *"Frequency of remote work was moderately associated with loneliness (adjusted odds ratio [AOR] = 1.60, 95% CI: 1.04–2.46, P = 0.033)."*
- **Gallup (2025)**, *"The Remote Work Paradox"* (State of the Global Workplace). Quote: *"Fully remote workers are the most likely to be engaged at work (31%) [yet] only 36% of fully remote workers report thriving overall, versus 42% of hybrid workers."*
- **Murthy VH (2023)**, US Surgeon General Advisory. Quote: *"The mortality impact of being socially disconnected is similar to that caused by smoking up to 15 cigarettes a day…"*
- *Supporting:* Van Orden et al. (2010), **Psychological Review** 117(2):575–600 (interpersonal theory of suicide — thwarted belongingness); Wyman et al. (2022), **Soc Sci Med** 296:114737 (Airmen — declining valued connections in the control arm); Toscano & Zappalà (2020), **Sustainability** 12:9804; Trinkenreich et al. (developer burnout SEM, n=3,281, 17 countries); Almeida et al. (2023), arXiv:2309.17140 (n=500, 35 countries).

### K2 — Timezone dispersion, interruption, sleep/circadian (conf now **high**)
- **Combined-effect study (2023)**, *"Combined effect of work from home and work during nonwork time on sleep disturbance,"* PMC10493373 (Sixth Korean Working Condition Survey 2020). *n=27,473.* Quote: combined exposure **OR 3.93 (men 5.08)** for sleep disturbance.
- **Polish National Health Programme 2021–2025** (Nofer Institute, Łódź) via Science in Poland (2024). *N>1,000.* Quote: *"Remote and hybrid work are more often associated with sleep and circadian rhythm disorders than in-office work… the body had no chance to adjust to the lifestyle. And this is where the most severe sleep disorders occurred."*
- **Otsuka et al. (2026)**, **J. Sleep Research**, doi:10.1111/jsr.70101. *n=824 Japanese workers, FY2021–FY2023, longitudinal (U-shaped: worst at <20% remote).*
- **Qin et al. (2025)** (telepressure), **Behavioral Sciences** 15(8):1109, PMC12383041 (n=323). Quote: *"Workplace telepressure increases employees' workload and extends their cognitive engagement into non-working hours."*
- **Gao et al. (2025)**, **BMC Psychiatry** PMC12218947 (social jetlag → depression, n=148,410): high social jetlag (≥2h) OR 1.44.
- *Supporting:* Consiglio et al. (2023), **IJERPH** 20:7051 (technostress→burnout→mood, n=225); Jaiswal & Prabhakaran (2024) (24×7 availability technostress); Emerald Internet Research (2026) (hybrid technostress→detachment, n=405); sedentary-behavior meta-analysis PMC12621373 (n=282,264; sitting +31 min/day, ≥8h sitting OR 2.10); burnout-circadian review PMC12651070.

### K3 — Tech displacement / job insecurity → depression (conf now **high**; current 2025–2026 evidence supplied)
- **Brynjolfsson, Chandar & Chen (2025)**, *"Canaries in the Coal Mine?,"* **Stanford Digital Economy Lab** (ADP payroll, 25M+ US workers). Quote: *"employment for workers in less exposed fields and more experienced workers in the same occupations has remained stable or continued to grow"* — while 22–25yo developer employment fell **−16%** since late 2022.
- **Blasco, Rochut & Rouland (2025)**, **Industrial Relations**, doi:10.1111/irel.12356 (IZA DP15434), nationally representative French PSM. Quote: *"working in an automatable job is associated with a [4] percentage point increase in the probability of suffering from mental disorders"* (corrected to +4 pp).
- **Sharma et al. (2025)**, **Int. J. Qualitative Studies on Health & Well-being**, PMC12409910 (n=24 IT professionals + 20 Delphi experts, India, 2024). Quote: *"I had just received a project excellence award a month before. Then I was told, 'Your role is no longer needed.' It felt surreal—like the ground just vanished."*
- **Zheng & Zhang (2025)**, **Behavioral Sciences**, PMC12024253 (n=303). Quote: *"AI awareness positively predicts job insecurity, which in turn positively predicts emotional exhaustion."*
- **Kharazian A (2026)**, Ramp/EconLab (thousands of firms, Q4 2021–Q3 2025). Quote: *"Firms most exposed to AI… substituted at a rate of about $1 in reduced freelance spend for $0.03 in AI spend."*
- *Supporting:* Almeida et al. (2023) arXiv:2309.17140 (freelancer status positively correlated with MH-disorder history p=0.03; organizational employment inversely p=0.02); APA 2025 Work in America (n=2,017; 54% job-insecurity stress); Posel et al. (NIDS-CRAM, South Africa); Speed/The Register (2025) (Tidelift: 60% quit-or-considering).

### K4 — Declining in-person contact (post-COVID) (conf now **high**)
- **Murthy VH (2023)** US Surgeon General Advisory (ATUS 2003–2020). Quote: *"time Americans spent with friends declined by nearly 70% over almost two decades, from roughly 150 minutes per day in 2003 to 40 minutes per day in 2020."* And: *"almost half of Americans (49%) in 2021 reported having three or fewer close friends — only about a quarter (27%) reported the same in 1990."*
- **Emanuel et al. (2026)**, **Science**, doi:10.1126/science.aec7671. *84% of remote workers spend entire workdays alone vs 23% onsite; 7% have zero human contact on a given day.* Quote: *"workers may not realize the costs of remote work for their well-being."*
- **Gallup (2025)**, *"Fully Remote Work Least Popular With Gen Z"* (n=19,043, May 2025). Quote: Gen Z *"almost twice as likely as Gen X, and nearly three times as likely as baby boomers, to say they experienced loneliness a lot of the day yesterday."*
- *Supporting:* Lyzwinski (2022/2024), **J Occ Health** 66:uiae005 (scoping review, 62 studies); Wells et al. (2022) (systematic review, 34 studies).

### K5 — "Degraded mode" loss of embodied/experiential co-present learning (conf **exp/low — thin, single practitioner source**)
- **Coates, Tim (2024)**, *"Mental Health of Developers in the Open Source Landscape"* (citing Rob Mensching). *Qualitative practitioner synthesis.* Quote: *"This mismatch can lead to frustration for both the developer struggling with unfamiliar code and the maintainer reviewing potentially flawed contributions."*
- **⚠ Remains thin.** Recommend targeted sourcing in the experiential-learning / embodiment / co-presence literature (see §6).

### K6 — Hard-to-corral / unreachable → selection bias (conf **exp — UNDER-CITED; gap remains**)
- **No strong direct source found.** Closest adjacent: Raghunathan (2024), **J. Technology & Systems** 6(2):1–8 — *"burnout often goes unnoticed in the open-source community, as contributors silently drop out and disengage"* (members become unreachable, biasing who stays visible; but this is the **silent-attrition** angle, K9, not recruitment-coverage). **K6 still needs a dedicated citation** on survey non-response / hard-to-reach population selection bias → see §6.

### Additional citations for other previously-thin existing IDs
- **A2** — McFillin (2023), citing the **WISE Teens RCT** (Johnstone et al., *Behaviour Research & Therapy*; n=1,071 Australian teens, school RCT 2017–18). Quote: *"one out of every eight participants in WISE Teens showed signs of clinical depression post-program, as opposed to one out of every 13 participants in the regular health classes."* Also Jibunoh et al. (2024) (n=5,000; location a significant predictor → universal approaches miss subgroups).
- **B2** — McFillin (2023), citing Shaffer/Columbia **TeenScreen**. Quote: *"Dr. David Shaffer of Columbia University… admits it has a potential 84 percent chance of wrongly identifying teens to be at risk of suicide."*
- **B4** — McFillin (2023) (medicalization → medication-seeking); McDonald, *"Why Your ACEs Score Doesn't Mean As Much As You Might Think"* (reductionist events-based approach risks pathologizing).
- **C3** — Zhu, Henry (2019), **Increment** Issue 9 (n=1 Babel maintainer): public-performance reactive/validation loop — *"constantly reactive, feeling exposed and lacking control."*
- **D1** — Collins, Hislop & Cartwright (2016), **New Technology Work & Employment** 31:161 (UK public-sector teleworking). Quote: *"supervisors in this study appeared to know a great deal about the personal lives of the teleworkers."*
- **D2** — Loon, Otaye-Ebede & Stewart (2019), **Int. J. HRM** 30(1):156–187 (integrative review, 30+ studies) — *"many HR practices aimed at increasing employees' psychological wellbeing… conflict and even contradict one another."* Plus Gallup 2025 (engagement-without-thriving warns against engagement-as-wellbeing-proxy).
- **G1** — Fukita, Kawasaki & Yorozuya (2025), **Cureus** 17(4):e82935 (10 RCTs): *"Avoiding the disclosure of mental health problems was a default position of workers because of the fear of being stigmatized in the workplace."* Plus Almeida et al. (2023); Figueiredo et al. (2025) **Healthcare** 13(16):1943.
- **G2** — Wyman, Brown, LoMurray et al. (2010), **Am J Public Health** 100(9):1653–1661 (18 high schools, 453 peer leaders): gatekeeper training for adult staff found minimal change in adult–student communication about suicide.
- **G3** — Wyman PA (2014), **Am J Prev Med** 47(3S2):S251–S256 (citing Luoma et al.): *"strategies limited to already identified high-risk individuals will not capture most youth who will die by suicide, the majority of whom are not seen by a mental health professional in the months prior to death."*
- **H1** — jackpot51 (2021), Redox OS Blog (n=1 fatality): *"This communication was purely technical, regarding the aarch64 port of the Redox kernel. I can't help but think, that perhaps this was a factor in his decision to choose death."*
- **H2** — Yang, Holtz, Jaffe, Suri, Sinha et al. (2022), **Nature Human Behaviour** 6(1):43–54, doi:10.1038/s41562-021-01196-4 (n=61,182 Microsoft employees, natural experiment): *"the shift to firm-wide remote work caused business groups within Microsoft to become less interconnected… reduced the number of ties bridging structural holes."* Plus Kraut et al. (1998) Internet Paradox; Morrison-Smith & Ruiz (2020) (255 studies); Bennett et al. (videoconference fatigue, n=55/279 VCs); Speakwise (2026) remote-onboarding (74% rate it a failure).
- **I1** — Murthy VH (2023) Advisory Ch.3: *"among highly cohesive groups, there are also strong pressures to conform to the group norms—often with high costs like rejection or ostracization if one doesn't comply."* Plus Sapegin (2023/2024) (user entitlement, low-quality contributions).
- **I2** — Crowston & Howison (2006), **IEEE Computer** 39(5):89–91: *"change at the center of FLOSS projects is uncommon… the founders' word still carries inordinate weight."* Plus Geiger et al. (2021) (BDFL veto bottleneck).
- **J1** — Wyman, Cero, Brown et al. (2023), **Injury Prevention** 29:442–445 (78 high schools, 39,960 students, 3 pooled RCTs): *"Sources of Strength delivered with low implementation fidelity may have limited or even adverse impact on suicidal behaviour among younger cohorts."* Plus List (2022), MIT Tech Review (voltage drop).
- **J2** — **Intel 2023 Open Source Community Survey** (n=666): maintainer burnout 45% **and** documentation/onboarding 41% as paired top concerns → burnout degrades documentation → impairs successor onboarding.

---

## 4. Quarantine resolution

| ID | Threat | Verdict | Confidence |
|----|--------|---------|------------|
| Q-a | Third-party SDK / tracking-pixel leakage + data-broker sale | **CONFIRMED** | high |
| Q-b | Commercial pivot of help-seeking data without meaningful consent | **CONFIRMED** | high |
| Q-c | Small-community re-identification from "aggregate" metrics | **CONFIRMED** | high |

**Q-a — CONFIRMED (high).** Promote out of quarantine. Empirically established across enforcement actions, academic research, and journalism. Canonical citations: (1) **FTC v. BetterHelp (2023, case 2023169)** — shared mental-health questionnaire answers, emails, IPs with Facebook/Snapchat/Criteo/Pinterest; $7.8M settlement, refunds began May 2024. (2) **Cerebral telehealth pixel breach (2023)** — Google/Meta/TikTok pixels collected self-assessment data, names, phone, DOB, IP for **3.1 million** users (Oct 2019–Jan 2023). (3) **Duke Sanford report (Feb 2023)** — 11 of 37 data brokers willing to sell people identified by mental-health diagnosis, prices as low as **$0.20/record**. (4) **UC Irvine/UCR (arXiv:2605.02016, May 2026)** — every one of 25 sampled Android mental-health apps embeds ≥1 undisclosed tracker SDK; 68% fail to disclose >half. *Relevance:* a remote worker's mood check-ins / stress self-assessments / therapy-initiation signals are exactly the help-seeking traces at risk. **Consistent with F1.**

**Q-b — CONFIRMED (high).** Promote out of quarantine. (1) **FTC v. BetterHelp (2023, $7.8M)** — sharing beyond stated purposes. (2) **FTC v. Cerebral (2024, $7.1M)** — shared sensitive MH/prescription data with LinkedIn/Snapchat/TikTok; ~3.2M consumers. (3) **23andMe 2025 bankruptcy** — corporate insolvency triggered potential transfer of health/genetic data on ~15M people to a new owner with different incentives; a coalition of **27 states** sued to require re-consent; scholars noted original ToS consent was insufficient for changed ownership (Lawfare 2025; NPR 2025). The acquisition/pivot/new-ToS vector is empirically established, not theoretical. **Consistent with F1** (and the Crisis Text Line/Loris.ai pattern noted in the original quarantine).

**Q-c — CONFIRMED (high). This gates the metrics layer.** Promote out of quarantine. The mechanism (quasi-identifier combinations collapse k-anonymity in small populations) is among the most thoroughly documented results in data-privacy research.
- **Sweeney, L. (2002)**, *"k-Anonymity: A Model for Protecting Privacy,"* **IJUFKS** 10(5), doi:10.1142/S0218488502001648 — *three quasi-identifiers (5-digit ZIP, gender, DOB) uniquely identified **87%** of the US population.* Companion: *"Simple Demographics Often Identify People Uniquely"* (CMU Data Privacy Lab, 2000) — small-population specifics (ZIPs with only 2 Black women / 4 Asian families).
- **Machanavajjhala et al. (2007)**, *"l-Diversity,"* **ACM TKDD** — k-anonymity alone is insufficient even when formally satisfied.
- **Applied corroboration:** HR-analytics tools (Lattice, CultureMonkey, CheckMarket) uniformly enforce minimum-threshold rules (typically **n ≥ 5**) precisely because role/shift/tenure/location breakdowns re-identify individuals; Statistical Disclosure Control literature (OpenSAFELY, UK Data Service SDC Handbook) sets thresholds of 5–10 and flags secondary disclosure via differencing across tables.
- **Curse of dimensionality** (Aggarwal): each added quasi-identifier multiplies unique combinations.

> **Governing rule for the metrics layer (now established):** In a small remote-worker community (≈10–200), the combination of **role + timezone + tenure** is a quasi-identifier set whose intersection routinely yields equivalence classes of **k=1**. **No per-subgroup metric breakdown is safe by default.** Per-subgroup reporting requires, at minimum, a hard **minimum-cell threshold (n ≥ 5, often higher at small N)**, suppression of complementary cells to block differencing, and consideration of differential privacy over a multi-year release budget (which, per the catalog's own Research Gap #3, may render useful longitudinal small-N metrics infeasible — a possibility the methodology must accept). **Consistent with E1–E3.**

---

## 5. Success-model leads (for the next phase)

> Tagged with the threat IDs each may mitigate. Captured for the forthcoming success model; not yet adversarially weighted against each other.

**Network / cohesion programs**
- **Wingman-Connect (US Air Force)** — universal cohesion training of *intact units* produces **differential benefit for the most vulnerable** (no at-risk targeting). Cluster RCT, n≈1,485, 2017–19; reduced ideation/depression/occupational impairment (~50% fewer corrective-training events). *Wyman et al., JAMA Network Open Oct 2020; Soc Sci Med 296:114737 (2022).* → mitigates **A5, B1, K1, K8, G2/G3**.
- **Sources of Strength** — train network-selected **opinion leaders**, not "at-risk" individuals; peer leaders 4× more likely to refer suicidal friends; 0 suicides in intervention vs 4 in control across 3 pooled RCTs (78 schools, 39,960 students). → mitigates **B1, B2, G2, A5, K1**.
- **Cobbler 2 Cobbler (Rapid City)** — year-round peer mentoring + scenario-based **role-limitation** training + structured freshman integration; zero teen suicides since Sep 2011 (vs 14 in prior 30 months). → mitigates **G2, G4, K1, K9**.
- **Youth-adult network integration** — sharing a common trusted adult lowered attempt rates (n=10,291, 38 schools). → mitigates **I2, K1, G3**.
- **Diverse social-network size** (range of distinct contacts) buffers stress/worry/fatigue (n=902 representative Austrian). → mitigates **K1, H2, K8**.

**Remote-specific connection**
- **Co-worker (horizontal) peer support** the dominant buffer (AOR 4.06 > supervisor 2.49 > remote-frequency) (Miyake n=4,052). → mitigates **K1, K7, I3**.
- **Higher mediated-communication frequency** reduces isolation longitudinally — buffer, not substitute (Van Zoonen & Sivunen, n=1,164). → mitigates **K1, K8, H2**.
- **Hybrid / minimum in-person threshold** (42% vs 36% thriving) (Bodner; Gallup; Emanuel). → mitigates **K11, K1, K4, H2**.
- **Buddy/peer-pairing at onboarding** seeds weak ties before withdrawal (retention ~+52%, time-to-productivity ~−60%). → mitigates **H2, K1, K7, K12**.
- **Coworking / virtual co-presence** generates weak ties structurally, no networking event needed. → mitigates **H2, K1, K4**.
- **Group belongingness** = top protective factor against videoconference fatigue (n=55/279 VCs). → mitigates **K1, K2, H2**.

**Circadian / boundary**
- **Schedule/location autonomy** buffers technostress→detachment→burnout (Emerald n=405; Jaiswal n=218). → mitigates **K2, K10, K7**.
- **Chronotype-aligned flexibility** dissolves the social-jetlag→depression cascade for evening types (Gorgoni n=875; Otsuka n=824). → mitigates **K2, K10**.
- **Right-to-disconnect / collective off-hours norms** — employee health *and* firm ROA/EBITDA (~+0.8%); collective enforcement > individual willpower (n=136,429 firm-obs, 28 OECD countries). → mitigates **K2, K10, A4**.
- **Light therapy + behavioral sleep intervention** normalizes circadian profile, reduces burnout (n=43 night-shift nurses). → timezone-dispersed analog; mitigates **K2** without surveillance.
- **E-work self-efficacy training** buffers technostress→burnout→mood (Consiglio n=225). → mitigates **K2, G5, K10**.

**Organizational / governance**
- **Visible, responsive support (not passive availability)** moderates wellbeing/productivity declines (Ralph n=2,225/53 countries; Bentley n=804; Mindshare: 2× "no burnout" at supportive firms). → mitigates **I2, K1, G3, D6**.
- **Climate for learning + belonging + inclusiveness** reduce burnout via satisfaction, esp. for non-leaders (Trinkenreich n=3,281). → mitigates **K1, I1, B4, D6**.
- **Modular governance** (Executive Committee + Working Groups) cures consensus-overload burnout (Jupyter). → mitigates **I4, I2, J3**.
- **Active-user buffer layer** insulates core contributors from support load (Crowston & Howison). → mitigates **I3, J3, D6**.
- **Human infrastructure for maintainers** (funded co-maintainership, knowledge distribution, CoC enforcement, episodic-contributor acceptance) (Linaker et al. ESEM 2024, n=10). → mitigates **J3, D6, I3, K3**.
- **Funded/paid maintainership** as a wellbeing (+security) lever — paid maintainers 55% more likely to implement critical security practices (Tidelift n=437). → mitigates **K3, J3, D6, I3**.

**Help-seeking / norms**
- **Navigator-assisted help-seeking** (human-guided) — the **only** durable behavioral uptake (OR 1.84–1.90; 98.6% utilization at 12 mo); passive info failed; adult gatekeeper-only training did not work (Fukita systematic review, 10 RCTs). → mitigates **G1, G2, G3, G4**.
- **Personal 1:1 contributor outreach** converts anonymous users into members (Storybook: 200+ meetings/yr, ~20% repeat). → mitigates **K1, K9, H3, B1**.
- **Structured peer-support workshops** naming chronic stressors ("personal ecology," GitHub n=40). → mitigates **K1, D6, I3**.
- **Peer storytelling by credible peers** (OSMI) breaks stigma, triggers disclosure. → mitigates **G1, B4, H4, K1**.
- **Public norm-change after tragedy** ("we will no longer value contributors by the code they crank out," Redox OS) — durable artifact subordinating output to wellbeing. → mitigates **D7, H4, D2, D6**.
- **Flexible/low-expectation contribution norms** (no weekend-work expectation) reduce burnout/silent dropout (Raghunathan; GitHub). → mitigates **K9, K10, I3**.

**AI-era**
- **Hope-activation micro-interventions** for lonely remote workers (hope mediated remote→engagement for high-loneliness; loneliness interventions g=0.43) (Bareket-Bojmel n=349; Hickin meta-analysis). → mitigates **A5, K1, K12**.
- **Job resources (AI-use autonomy + reskilling)** buffer GenAI burnout (β=−0.360) (Feng n=442). → mitigates **K3c, K3a, J3**.
- **CSR** buffers AI-adoption→insecurity→depression (3-wave, n=403/287 orgs) (Kim & Lee 2025). → mitigates **K3a, K3, B4**.
- **AI-complementary skill acquisition / reframing** reverses freelancer income decline (+~40%/hr) (Kharazian/Ramp). → mitigates **K3b, K3, K3c**.

---

## 6. Remaining gaps

**Threats that are single-source or low-confidence (flag for re-sourcing before they drive design):**
- **A5** — single unreplicated cross-sectional study (Bareket-Bojmel 2023); causation unestablished; one large longitudinal study (Norwegian, n=1,511) points the *other* way at the population level. **Severity=high may be overstated.** Needs a longitudinal/experimental test of subgroup masking under an *actively targeted* (not averaged) design.
- **H4 (capable-contributor blind spot)** — the "anti-selection" core rests on a **single n=1 reflective essay**; only indirectly corroborated (Cassidy 2022/2023 high-IQ-autism). Definitional overlap with G2/B3 unresolved. Needs a controlled study; treat as low-confidence.
- **K9 (silent attrition)** — strongest cited source (Raghunathan) is a **low-tier whitepaper**; re-anchor on Raman et al. (ICSE-NIER 2020) + Guizani et al. (arXiv:2102.05737).
- **K12 (belonging-need suppression)** — **irreversibility downgraded/removed** (theoretically contested vs Baumeister & Leary); rests on one observational Finnish study (n=876). Needs longitudinal causal work on whether suppressed belonging motivation recovers, and on the engagement-resistance timing window.
- **H3 (AI-mediated displacement)** — entirely prospective; **no measured belonging/trust degradation yet**; "94%" adoption figure corrected to 84%. Watch emerging empirical work (Vaccargiu et al., BoatSE '26).
- **K3b/K3c** — top-earner finding is "suggestive" (authors' own label); some cited regression coefficients/sub-claims unverifiable (paywalled) or **not found in source** (the "~10 PRs/year" claim — remove); Becker RCT n=16 with wide CIs.
- **K5 ("degraded mode")** — **still thin**: one practitioner source. Target the experiential-learning / embodiment / co-presence literature for a primary citation.
- **D7 AI-amplification layer** — fabricated Devsu stat removed; the AI-amplified-impostor angle lacks a rigorous quantitative source (qualitative SO-blog coverage only).
- **I4 quote attribution** — re-verify against the LF 2023 full PDF and re-attribute to **Brian Granger** (not Myles Borins).

**Catalog-level gaps still open:**
- **K6 (hard-to-corral/unreachable → selection bias) remains genuinely under-cited.** No dedicated source found in this sweep. Recommend targeted sourcing in **survey non-response / hard-to-reach-population methodology** (e.g., respondent-driven sampling literature; non-response bias in occupational-health surveys) to lift K6 out of "exp."
- **Mechanism tests in non-clinical remote-worker populations** are still mostly absent — most A–J citations are clinical/school/justice/general-CMC; the OSS literature is the closest proxy for distributed-community dynamics but is dev-specific (generalization caveat applies to D6/D7/H3/H4/I3/I4/J3/K9).
- **Small-N DP utility/privacy tradeoff at N=10–50 over a multi-year budget** (catalog Research Gap #3) is now *more* pressing given Q-c confirmation — it may show that useful longitudinal per-subgroup metrics are infeasible at this scale. This is the highest-leverage open question for the metrics layer.
- **Werther/contagion visibility threshold at small N** (C2) and **facilitator-competency decay rate** (J1/J2) remain unmeasured for tightly-identified small remote communities.

---

*End of Completeness Addendum. Source files referenced: `/Users/rsb/src/host-happily-hub/threat_catalog.md` (catalog to be amended with the IDs above). All new IDs (A5, D6, D7, G5, H3, H4, I3, I4, J3, K7–K12, K3a–K3c) and lifted citations (K1–K4 strong; K5 thin; K6 still pending) are ready to merge into the register table and detailed catalog.*
