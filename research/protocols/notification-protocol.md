# SNH Notification Protocol — Design Note
### "Connection Requests with Staged Disclosure"

**Status:** v0.2 (2026-07-04) — idea-stage design, workshopped for the DWeb Camp Berlin 2026
talk and aligned with the published talk description (where it appears as **Opportunity 2**).
Grill log: `brainstorms/20260704-notification-protocol-grill.md` (gitignored).
Threat references (`G1`, `Q-a`, `RF1`, …) resolve to `../threat_modelling/threat_catalog.md`.

---

## Purpose & thesis

**Thesis** (from the knowledge-base plan): *if help-seeking behaviors for remote workers become
one-button simple, friction to help-seeking drops and help-seeking increases.*

This note defines the protocol that makes the button work: **connection requests with staged
disclosure**. A user who needs to talk to someone — about taxes, a mental-health dip, a legal
question — asks their network for a one-on-one, and the system finds a willing, topical,
available human while disclosing as little as possible to as few as possible at every step.

The load-bearing case is the user whose own network *can't* answer. Threat catalog RF1/K1:
the people who most need help have the weakest ego networks. A protocol that only works for
people with rich, well-tagged contact lists solves the wrong problem. So the protocol must
reach **beyond** the egocentric network — into communities the user belongs to but has not
individually enumerated — without centralizing anyone's relationship data.

**Scope.** In scope now: user-initiated help requests (this note). Named but deferred:
**analysis-initiated triggers** — the SNH analysis layer (see
`../measurement/community-network-health-explainer.md`) emitting "someone should reach out
to X" prompts as a second trigger class over the *same* state machine. Out of scope: the
anonymized-statistics protocol (Choir) — *the statistics protocol measures; the notification
protocol acts.*

---

## Actors & roles

- **Requester** — the person seeking a one-on-one.
- **Responder** — an audience member who answers a ping.
- **Audience** — *any addressable set of potential helpers.* The protocol's central
  abstraction; see next section.
- **Coordinator** — the *function* that holds staged state and performs matching while both
  sides remain blinded. A role, not a fixed component: bound per-deployment (see substrate
  section).
- **Steward** — the human accountable for a community's participation: proposes the super
  contact, operates or designates the coordinator, curates topic vocabulary, receives abuse
  reports and aggregate audit.

## The audience abstraction: tag groups and super contacts

One protocol, one state machine, two ends of an audience spectrum:

- **Egocentric audience** — a tag group in the requester's own PRM ("finance people").
  Membership enumerated, contact data local, members pre-validated by the requester.
- **Super contact** — a whole community (a 100-person Signal group, of whom maybe two are PRM
  contacts) addressable *as a single contact*. Membership unknown to the requester; one known
  way to reach the whole.

Staged release is always structurally present; **disclosure policy is a per-audience knob.**
For a pre-trusted tag group the stages may collapse to a single direct ask; for a super
contact the full staged dance is the default.

**A super contact exists only by community consent — the opt-in ceremony.** (In the talk's
public framing: *opt-in access to broader communities*.) A steward
proposes; the group consents through its own mechanisms (vote, objection window); the
coordinator agent joins *visibly* (a bot account members can see and eject); individual
members can mute or opt out of pings. A member's PRM stores only the super-contact handle and
steward — never the roster. Nobody can unilaterally make a group addressable. (Requester-side
unilateral addressing of a group is a degraded bootstrap mode, not the definition.)

---

## The state machine

| Stage | What happens | Who learns what |
|---|---|---|
| **S0 Compose** (local) | Requester picks audience, coarse topic, time window ("today 3–4pm PT"). | Nothing leaves the device. |
| **S1 Availability ping** | Coordinator posts to the audience: "Someone in this community would like a one-on-one, window X. Available?" | Audience learns: a request exists, its window. **Not** the topic, **not** the requester. |
| **S2 Topic gate** | Coordinator asks *only the available responders*: "Willing to talk about *personal taxes*?" | Available responders learn the coarse topic. The wider audience never does. |
| **S3 Match + mutual consent** | Topic-willing responders are matched to the requester per the **reveal policy** (below); mutual consent; identities/contact info cross; scheduling. | The consummated pair learns each other. |
| **S4 Close-out** | Unchosen responders get "fulfilled — thank you" (requester-name reveal is opt-in, after the fact). No-match → coarse outcome + local fallbacks. | Nothing else, to anyone. |

**S3 reveal policy — a configurable coordinator option** (set per-audience at the opt-in
ceremony; all three are legal protocol modes):

1. **Anonymous cards, pair-only reveal** — requester picks from anonymous candidate cards
   (window overlap, timezone, steward-attested trust signals like tenure/vouches); identities
   cross only inside the chosen pair. Strongest default for super contacts.
2. **Names at S3** — requester sees topic-willing responders' names and picks. Warmer;
   natural default for pre-trusted egocentric audiences.
3. **Coordinator auto-match** — best window/timezone fit, consent handshake, minimal
   disclosure; trades away requester agency.

**Failure semantics.** Every request carries a mandatory TTL. On expiry the requester sees a
*coarse outcome only* — matched / no match — no counts, no who-declined (a zero at any stage
reads as personal rejection: G1). Escalation to a wider audience is **offered, never
automatic**. Available-but-unmatched responders always get a warm close-out. Failures are
invisible to the audience at large.

**Topics** come from a **coarse controlled vocabulary** (mental health, finance, legal,
medical, technical, work, relationships, …), steward-curatable per community. Freeform detail
is allowed only after the S3 consent gate, party-to-party. Coarseness is a privacy feature —
it keeps the anonymity set behind each topic large. The same vocabulary drives PRM tags,
resilience-check fallback slots (below), and request topics: one list, three uses.

---

## Fallback resources & the resilience check
*(the fallbacks themselves are a companion PNA feature, generated and stored locally; the
no-match handoff to them is protocol-level — see the requirement below. Unsolved; spin out
into its own note when it grows)*

For critical topics — mental health, finance, legal, medical — "no match" cannot be a
terminal state. The mitigation is **front-loaded fallback resources**: the user pre-registers
institutional resources per sensitive topic *before* any crisis — their accountant, the
local government office offering free financial advice, a suicide hotline — as
contacts/resources in their PNA, so they surface instantly when no human match arrives in
time. (Assume no LLM is attached to the PNA at the moment of need: this knowledge must be
pre-staged, not synthesized on demand.)

Fallbacks are generated by a **resilience check**: a guided health-check flow that walks the
user through their topic tags and groups, identifies which need *real-time* resilience, and
prompts the user to research and pre-load fallbacks for each.

**Protocol requirement.** For requests on a critical topic (mental health, finance, legal,
medical — a flag on the topic vocabulary), a conforming implementation MUST resolve the
no-match terminal state by surfacing the requester's pre-loaded fallback resources at S4.
This is what makes the talk's claim — "a protocol enabling opt-in access to broader
communities *with pre-generated fallbacks*" — true at spec level, while the fallbacks
themselves stay local.

Note the degradation property: the fallback path is **entirely local**. When the protocol
fails, the system falls back to data already on the user's device — zero privacy cost at the
moment of maximum vulnerability.

---

## The coordination substrate

Where staged state lives and moves is **pluggable**, and "centralized vs decentralized" is
the wrong single axis. The substrate spectrum has (at least) four:

- **Privacy capability** — cleartext ↔ encrypted blobs on a central host ↔ zero-knowledge.
- **Availability** — usable today ↔ ~2 years out ↔ possibly never.
- **Ease of use** — what the PNA layer must mask from users.
- **Forgetfulness** — can the substrate actually delete? (Git never forgets: a repo substrate
  needs rotation or crypto-shredding — encrypted blobs whose keys are destroyed.)

Waypoints, worst to best on privacy:

| Substrate | Available | Notes |
|---|---|---|
| Plain Signal/WhatsApp group broadcast | today | weakest guarantees; coordinator = bot in group |
| **Private GitHub repo shared by the group** | **today** | centralized host, but carries cleartext *and* encrypted artifacts; **the v1 experiment substrate** |
| encryptedspaces.org-style ZK space | experiments ~1yr; critical use ~2yr | the direction of travel |
| Fully decentralized protocol | possibly never | the ideal, held honestly as such |

**V1 binding:** a **community-steward-operated coordinator agent** (itself a PNA — a bot that
members' PNAs talk to via the shared substrate). Without cryptography, honest blinding needs
*some* distinguished party; the protocol names that trust rather than hiding it.

**Guarantee degradation table** (v0.1 sketch — the workshop discussion artifact; refine live):

| Guarantee | Signal broadcast | GitHub repo + steward bot | ZK space |
|---|---|---|---|
| S1 hides requester from audience | only if bot posts | yes (bot posts) | yes |
| S2 topic hidden from non-available members | no (group-visible) | yes | yes |
| Responses hidden from requester until S3 | no | yes | yes |
| Anything hidden from coordinator | no | **no — named trust** | yes (goal) |
| Per-request state deletable | no | only w/ rotation or crypto-shredding | yes (goal) |

---

## Threat model (seed — the step-3 gate requires a full threat-model pass, testing, and researcher engagement before any deployment)

Two attacks are duals of each other; both exist because the protocol *manufactures* sensitive
disclosures that didn't previously exist:

- **Attack A — the predatory responder.** An infiltrator in the community answers requests.
  At S3 they learn the identity, availability, and topic of a requester who is *by
  construction* vulnerable on that topic ("finance trouble" → crypto-scam target). The
  protocol selected the victim for the attacker. Mitigations: S3 reveal policy (anonymous
  cards), steward-attested trust signals on cards, report/flag loop to the steward, and —
  the real boundary — community membership hygiene, which the protocol inherits and cannot
  itself fix.
- **Attack B — the harvesting requester.** An infiltrator issues fake requests and farms S2
  yeses into a roster of who will privately discuss mental health, debt, legal trouble. S3's
  consent gate does not retroactively protect S2. Mitigations: responses flow only to the
  coordinator, never the requester; requester learns nothing but the final outcome;
  per-requester rate limits (N requests per topic per window); steward-visible aggregate
  audit; no funnel statistics disclosed to anyone (also kills differencing).
- **The ceiling — a compromised coordinator** sees everything in v1. Irreducible except by
  moving up the substrate spectrum; the protocol's job is to ensure *ordinary participants*
  can never do what a compromised coordinator could.

Standing threats inherited from the catalog: **G1** (a stigmatized or failure-visible channel
suppresses the help-seeking it exists to enable — drives the coarse-outcome failure design),
**Q-a/Q-b** (help-seeking traces leaking to surveillance marketing / commercial pivot — drives
the retention design), **RF1/K1** (isolation as the universal substrate risk — drives the
community-reach requirement).

## Data lifecycle

**Ephemeral by default.** The coordinator purges per-request state at S4 plus a short grace
window and keeps no per-request logs. The substrate must support forgetting (see the
forgetfulness axis). What persists: each participant's own side of their own interactions in
their own PNA (their data); the community's policy configuration; steward audit as
**aggregate counters only** (requests per topic per month — enough to spot abuse and
demonstrate value, useless as a surveillance record). Help-request metadata never feeds the
statistics/metrics layer except as consented aggregates.

---

## Placement in the talk's three-step plan

Step 3 of the plan is **"Design interventions from egocentric data sets"** — defined not by a
deliverable but by its gate: **threat modeling, development, testing, and researcher
engagement, all prior to deployment.** Per the threat catalog's dependency order, nothing
past guardrails is legitimate until the guardrails exist.

The step-3 content is carried by two named opportunities:

1. **Opportunity 1 — "Macrostructure from Microstructure": community analytics.**
   Sociocentric insight from egocentric data without aggregating identifying information
   (see `../measurement/community-network-health-explainer.md`). The *measuring* half.
2. **Opportunity 2 — "Connection Requests with Staged Disclosure": this protocol.** Opt-in
   access to broader communities, with pre-generated fallbacks. The *acting* half — the
   first designed intervention.

Egocentric-audience asks are ordinary communication (the risk a user already chooses when
they message a friend); super-contact asks are the danger zone and get the full staged
machinery — and the full step-3 gate.

## V1 experiment sketch

A Signal group that has run the opt-in ceremony; a steward-operated coordinator bot; a
private GitHub repo (shared by group members) as coordination substrate carrying encrypted
request artifacts; PNAs (PRM / fellows_local_db lineage) speaking the protocol on behalf of
members. Buildable today; every guarantee it *doesn't* provide is a named row in the
degradation table.

## Open problems (workshop critique fodder)

1. **Blinding without a trusted coordinator** — the substrate-spectrum problem; ZK spaces are
   the visible path, ~2 years from critical-use readiness.
2. **Forgetfulness on real substrates** — deletion guarantees on git/Signal/anything popular.
3. **The scheduling handoff** — "the system sends a calendar invite" is still magic
   hand-waving; calendar egress is itself a privacy surface.
4. **Analysis-initiated triggers** — reusing this state machine when the SNH layer, not a
   human, originates the request (consent model differs at S0).
5. **Infiltrator resistance beyond trust signals** — the protocol inherits community
   membership hygiene; can it do better than inherit?
6. **Cross-community escalation** — offering "widen the audience?" without consent decay
   across hops.
7. **Fallback-resource curation** — the resilience check needs its own design note: sourcing,
   verifying, and refreshing institutional resources per topic and locale.

---

*Related: `../threat_modelling/threat_catalog.md` (PROTO layer),
`../measurement/community-network-health-explainer.md` (the measuring counterpart),
`../research_library/planning/knowledge-base-plan.md` (thesis), PNT roadmap Tier 3–4 (mutual-aid PNA reference
design; reachability-for-help-seeking seam).*
