---
theme: seriph
background: '#fffdf4'
colorSchema: light
themeConfig:
  primary: '#2179b8'
title: Rooting the Social Graph with Personal Network Applications
info: |
  DWeb Camp Berlin 2026 — Hackers Lab workshop.
  Rich Bodo · socialnetwork.health
class: text-center
drawings:
  persist: false
transition: slide-left
mdc: true
---

<img src="/snh-logo.svg" alt="Social Network Health" class="w-28 mx-auto mb-4" />

# Social Network Health Project

### Rooting the Social Graph with Personal Network Applications

<div class="flex items-center justify-center gap-3 mt-10">
  <img src="/rich-headshot-2016.jpeg" alt="Rich Bodo" class="w-14 h-14 rounded-full object-cover border-2 border-[#f7c948]" />
  <div class="text-left leading-tight">
    <div>Rich Bodo</div>
    <div class="text-sm opacity-70">DWeb Camp Berlin 2026 · Hackers Lab</div>
  </div>
</div>

<div class="text-sm opacity-70 mt-6">
socialnetwork.health · talk ~20 min, then we work
</div>

<!--
Format note up front: ~20 min of talk, then workshop. I'll gauge interest and zip
through slides — interrupt early, collaboration is the point.
-->

---

# Who am I

- TODO: 2–3 sentences of bio (past work, why this problem)
- Maintainer of the Social Network Health working group — research, educational materials, software
- Building "home-cooked meals": software made for specific people and communities, not markets

<!--
Keep this to 30 seconds. The credibility that matters for this room: I ship software
for a real, sensitive community, and I publish the research behind it.
-->

---

# The project: social network health for remote communities

- Working group studying **social-network health** (SNH) applied to digitally-connected, remote communities
- Public corpus: threat catalog · research library (~500 papers) · toolkit wiki · video archive
- Founding thesis: **if help-seeking becomes one-button simple, help-seeking increases**
- The threat catalog came first — *where the mines are*, before any intervention

<!--
One idea to land: we did the harm-model homework BEFORE building interventions.
The threat catalog (~50 threats, evidence-linked) gates everything that follows.
-->

---

# Building for a sensitive community

- The Edmund Hillary Fellowship fellows directory: contact data for a community that trusts each other — but shouldn't have to trust my code
- Built **fellows_local_db**: local-first directory archive — SQLite + PWA, data never leaves the device
- Informal survey: **~10× the daily active use** of the old SaaS directory
- Lesson: people engage with relationship data when they actually control it

<!--
The 10x DAU number is informal but real — say so honestly. This app is COMPLETE and
in use. It's also what forced every safety question the toolkit now answers.
-->

---

# 2025: the lost year

- Tried to build a personal relationship toolkit (PRT) — **failed**
- Tried to build something like the SNH notification protocol — **failed**
- Not a tooling problem — a *confidence* problem:
  - no way to be sure my own software was safe with my own data
  - no way to keep fast AI-assisted development from drifting

<!--
Be candid here — this slide buys trust for everything after it. The failures weren't
about code quality; there was no spec to hold the line on safety while moving fast.
-->

---

# What changed: tests with judgment

- Programming with LLMs enables a new kind of testing: **tests that exercise judgment against behavioral specs**
- Write the *commitments* down → machines continuously check the behavior, not just the functions
- That made rapid development of privacy-critical software feel safe enough to attempt again
- The missing piece of 2025, built in 2026: **the PNA Toolkit**

<!--
Key claim: LLM-era development isn't just faster coding — it changes what a SPEC can
do. A behavioral spec becomes executable oversight. This is the hinge of the talk.
-->

---

# The PNA Toolkit

An agent-ready toolkit for building **Personal Network Applications** — apps rooted in your own relationship data. Four goals:

1. **Own the root** — your personal network data, local, yours
2. **Integrity by validation** — software proves it behaves; *checked, not awarded*
3. **Govern egress** — nothing leaves without disclosure and consent
4. **Survive entropy & accidents** — durability against loss, drift, and time

<!--
github.com/richbodo/personal_network_toolkit — spec, contracts, lints, MCP servers,
conformance suite. "Checked not awarded" is the phrase to emphasize.
-->

---

# Positioning: what a 96-source survey found

- Coded the local-first / privacy field bottom-up by *behavior* → four families: **Substrate · Sovereignty · Verification · Disclosure**
- **Disclosure is a first-class family** — show the payload, pick the channel, treat an AI call as just another egress
- Privacy, sovereignty, durability are **additive, not inherited** from local-first
- **The wager:** the personal-network root is the highest-leverage, least-served corner of this space

<!--
From the positioning paper (working draft, PNT repo). Stated as findings of a survey
and a falsifiable wager — not proofs. Peers in the all-four-families cell: EUDI
wallet, IDS-RAM, Solid. The PNA occupies a corner none of them do.
-->

---
layout: center
---

# The layers

**TODO:** layers diagram from the PNA spec ("how the pieces fit together")

<!--
Pull the figure from personal_network_toolkit/spec (figures/). One walk-through
sentence per layer, no more. This slide is a picture, not a paragraph.
-->

---

# Contracts in plain language

- Every commitment the spec makes has a **plain-language twin** — readable by the person whose data is at stake
- "Four goals in plain language" / "Why this matters" (PNT docs)
- Goal: the user *understands the privacy trade-offs they are making* — informed use, not blind trust

<!--
This is the education half of the safety story: constraints exist so a human can
build a correct mental model, not just so a linter passes.
-->

---

# Home-cooked meals

<div class="grid grid-cols-2 gap-6 items-start">
<div>

| | status |
|---|---|
| **fellows_local_db** | ✅ complete, in use |
| **PRM** | 🔨 in progress |

- Both are **reference designs**: they prove the toolkit's constraints are livable
- Made *for* specific people, rapidly — the home-cooked-meal model

<div class="text-xs opacity-60 mt-2">TODO: fellows_local_db directory screenshot (Rich's contact page) — needs the fellows DB</div>

</div>
<div>

<img src="/screenshots/prm-contact-turing.jpg" alt="PRM contacts view — Alan Turing (fixture data)" class="rounded-lg shadow-lg border border-gray-300" />
<div class="text-xs opacity-60 mt-1 text-center">PRM on fixture data — every contact stays on this device</div>

</div>
</div>

<!--
prt (the 2025 attempt) is the ancestor of PRM — the same idea, now survivable
because the toolkit holds the safety line.
-->

---

# AI egress in practice

<div class="grid grid-cols-2 gap-6 items-start">
<div>

- Assumption: to be *usable*, a PNA must talk to AIs — local or cloud
- So the spec models the AI as **egress, runtime adversary, and consumer of the spec itself**
- Granting cloud AI access = a **named, visible, reversible exception** (EX-CLOUD-LLM) — never a silent default
- Solving AI egress solves the general case: OS automation, integrations, whatever's next

<div class="text-xs opacity-60 mt-2">TODO: fellows_local_db settings screenshot (Claude Desktop integration) — needs the fellows DB</div>

</div>
<div>

<img src="/screenshots/prm-access-ai-on.jpg" alt="PRM External Access view with cloud AI access active" class="rounded-lg shadow-lg border border-gray-300" />
<div class="text-xs opacity-60 mt-1 text-center">PRM External Access — cloud AI on: banner, data floor, revoke, return to PNA mode</div>

</div>
</div>

<!--
Show, don't tell: the disclosure UX — payload preview, channel choice, consent —
in real screenshots. This is where I spent the newest design effort.
-->

---

# The threat continuum keeps advancing

**TODO:** diagram — advancing threats to private relationship data, one axis, over time

SaaS silos → cloud AI → local AI agents → OS-level automation → **brain-computer interfaces (not yet handled)**

- Each step moves the reading of your private life closer to the substrate you think with
- The conformance suite handles today's steps; BCI is named as the next one we have *not* considered

<!--
The honest edge of the slide: we name the threat we haven't handled. For this
audience, naming the unhandled threat is more credible than claiming coverage.
-->

---

# Safety as continuous validation

<div class="grid grid-cols-2 gap-6 items-start">
<div>

- Assumed future: home-cooked apps built and rebuilt in **near real time**, per person, per community
- The only safety story that survives that pace: **specify the commitments and constraints, validate them continuously**
- Spec → conformance suite → every rebuild re-earns trust — *checked, not awarded*
- The user's mental model is part of the system under test

</div>
<div>

<img src="/screenshots/fellows-conformance-report.jpg" alt="fellows_local_db PNA conformance report" class="rounded-lg shadow-lg border border-gray-300 max-h-90" />
<div class="text-xs opacity-60 mt-1 text-center">fellows_local_db conformance report — 37/41 rows, evidence-linked</div>

</div>
</div>

<!--
This closes Part I. Pause here — first natural workshop beat. "Does this development
model match where you think software is going?"
-->

---
layout: center
---

# The three-step plan

1. **Take back the root** — move the personal network root local, away from SaaS
2. **Add communications analysis** — support coverage, resilience — on your own device
3. **Design interventions from egocentric data sets** — threat modeling, testing, and researcher engagement *before deployment*

<!--
Steps 1–2 are what you just saw (toolkit + apps + analysis). Step 3 is where the
rest of the talk lives — and it's defined by its GATE, not its deliverable.
-->

---

# Step 3's gate

- Interventions release **incredibly sensitive information to other people** — that's the point, and the danger
- Nothing deploys before: **threat model → development → testing → researcher engagement**
- The threat catalog is the standing gate: G1 (chilling effects), Q-a/Q-b (help-seeking data harms), RF1 (isolation itself)
- Your own tagged contacts = ordinary communication risk; **communities = the danger zone**

<!--
The egocentric/community distinction here sets up why Opportunity 2 needs staged
machinery at all.
-->

---

# Opportunity 1 — Macrostructure from Microstructure

- Want: community health facts (cohesion · reach · isolation). Have: **egocentric fragments** — always
- Privacy gating *manufactures* missing data — on purpose. **Gate more, model more**
- The reusable pattern: **Fit → Simulate → Quantify → Derive** (Smith 2012 is one instantiation)
- Trap: a 50-person group chat is **not** 1,225 friendships — affiliation ≠ ties

<!--
One-slide compression of the explainer (research/foundational/). If interest is
high, the routing diagram and estimator menu are in the repo — point, don't present.
-->

---

# Opportunity 2 — Connection Requests with Staged Disclosure

Help-seeking, one button, minimum disclosure:

- **S0** compose (local): audience · coarse topic · time window
- **S1** ping: "someone wants a 1:1, window X" — *no topic, no identity*
- **S2** topic gate: topic → *available responders only*
- **S3** match + **mutual consent** → identities cross (reveal mode is a policy knob)
- **S4** close-out: warm thanks · no-match → **pre-generated fallbacks (local)**

<!--
The audience abstraction: a PRM tag group OR a whole community ("super contact" —
a 100-person Signal group addressable as one contact, by the community's own
opt-in ceremony). Same protocol, different disclosure policy.
-->

---

# Opportunity 2 — the design decisions that matter

- **Super contacts exist only by community consent** — steward proposes, group opts in, coordinator bot is visible and ejectable
- **Coordinator is a role over a pluggable substrate** — Signal broadcast ↔ private GitHub repo (today) ↔ ZK spaces (~2 yrs) ↔ fully decentralized (maybe never)
- Substrate axes: privacy · availability · ease of use · **forgetfulness** (git never forgets)
- **Ephemeral by default**; attack duals named: predatory responder ↔ harvesting requester

<!--
Full design note: research/protocols/notification-protocol.md — including the
guarantee degradation table (substrate × binding → which blindings actually hold).
That table is the next slide's workshop artifact.
-->

---

# Open problems — the critique menu

1. Blinding without a trusted coordinator (the substrate problem)
2. Forgetfulness on real substrates
3. The scheduling handoff (calendar egress is also egress)
4. Analysis-initiated triggers (when the SNH layer, not a human, asks)
5. Infiltrator resistance beyond trust signals
6. Cross-community escalation without consent decay
7. Fallback-resource curation (the resilience check)

**Pick one. Break it. That's the workshop.**

<!--
This is the pivot to collaboration. Encrypted-spaces folks: #1 is yours. Protocol
people: #4 and #6. Community organizers: #5 and #7.
-->

---

# Demo (pre-recorded)

**TODO:** record — fellows_local_db + PRM exercising AI integration

- Watch the spec shape the UX: disclosure preview, channel choice, consent moments
- The constraints aren't friction — they're the *education* of the user, in the flow of use

<!--
Pre-recorded so it can't fail on conference wifi. 2–3 minutes max, narrated live.
-->

---
layout: center
class: text-center
---

# Thanks — now let's work

**socialnetwork.health** · toolkit wiki · research library

github.com/richbodo/personal_network_toolkit · github.com/richbodo/social-network-health

<div class="text-sm opacity-70 mt-8">
Protocol design note: research/protocols/notification-protocol.md<br>
Explainer: research/foundational/community-network-health-explainer.md
</div>

<!--
Workshop logistics: split by open-problem interest, 25–30 min, reconvene for
5-minute report-backs, I capture everything into the repo's brainstorms.
-->
