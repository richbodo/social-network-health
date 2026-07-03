# Research Primitive — Whole-Network Simulation from Ego Samples

**Source:** Smith, Jeffrey A. 2012. "Macrostructure from Microstructure: Generating Whole Systems from Ego Networks." *Sociological Methodology* 42:155–205. DOI 10.1177/0081175012455628.

**Primitive type:** Statistical reconstruction — turns cheap local data into aggregate whole-network structure.

---

## Core problem
Measuring an entire community's network (everyone, every tie — the *sociocentric* graph) is usually impossible: it needs near-total participation and has no clean boundary in the wild. But *ego* data — one person's own ties, and ideally whether their contacts know each other — is cheap, collectible one survey or one contact-manager export at a time. The gap this primitive closes: **how do you get trustworthy whole-community structure out of a pile of disconnected personal fragments?**

## Method (compressed)
From a random sample of egocentric networks, Smith fits **one** size-invariant tie-formation model (an ERGM), then uses that model to **simulate many complete sociocentric graphs**. Aggregate structural statistics are read off the simulations, are statistically faithful to the true (unobserved) network, and are markedly better than simpler baseline estimators. Because it produces an *ensemble* of plausible graphs rather than one reconstructed named network, it yields uncertainty ranges, not just point guesses.

*Mechanically: each ego report contributes local "would this tie exist?" observations → the ERGM turns those into tie-probability parameters → simulation runs those parameters forward to grow full graphs. Note it is **one pooled model**, not a separate model per ego.*

## Terms, in plain language
- **Egocentric network** — one person's local view: them, their contacts, and (ideally) which of those contacts know each other. What a survey or PRM export reveals.
- **Sociocentric network** — the whole community graph. The thing you want but can't directly see.
- **Largest connected group** (Smith's "main component size") — the biggest cluster of people who can all reach each other through some chain of ties. Covers 90% of members → essentially one connected society; biggest island is 15% → fragmented. **This is your headline cohesion number.**
- **Distance / degrees of separation** — typical number of hops between two people. *This is an output the method estimates well — not a limitation.*
- **Degree** — how many ties one person has. *This is the main thing that governs whether the method works at all.*

## Use case — community SNH from released ego data
Community members export limited ego data from their contact managers / PRMs — their own ties, optionally with "do these two contacts know each other?" — into an encrypted aggregation space. The primitive fits one model over the pooled samples and simulates the community's whole-network structure, then releases *sociocentric health signals* back to the community (or on a need-to-know basis):

- **Cohesion / integration** — is the community one connected whole or a set of islands? *(largest-connected-group size, number of components)*
- **Reach** — how many hops separate typical members? *(distance)*
- **Isolation** — how many members sit structurally alone or on thin bridges? *(degree distribution, isolates)*

**Privacy fit:** the output is aggregate structure from an *ensemble*, never a reconstructed named who-knows-whom graph. You publish community-level health without exposing individual relationships.

## Where confidence is high vs low

| High confidence | Low confidence |
|---|---|
| Sparse network / **low average degree** | Dense network / **high average degree** |
| Ego data includes **alter–alter ties** (do my contacts know each other?) | Thin ego data (contact list only, no alter–alter links) |
| Large, reasonably **representative random** ego sample | Small, self-selected, or unknown-seed samples |
| Estimating **global / aggregate** properties (distance, component size, degree distribution) | Estimating **individual** facts ("is Alice the bridge?") |
| Population size *N* known or well-estimated | *N* unknown and unconstrained |
| Model terms match the network's real tendencies | Mis-specified or near-degenerate model |

**The limitation you flagged, corrected:** the breaking factor is high **degree** (many ties *per person* — a dense network), **not** long path distances. In a dense network the space of possible local neighborhoods explodes, so a sample can't pin down the configuration frequencies the simulation needs → low confidence. "Six degrees of separation" is *path distance*, which is one of the statistics the method reproduces **well**. So: **degree breaks it; distance is an output.**

## Hard scope boundaries (what it will never give you)
- **Not the real graph, not real individuals.** You get a statistically plausible reconstruction consistent with aggregate patterns — good for community stats, useless (by design) for "who specifically is connected to whom." For your privacy goal, that's a feature, not a bug.
- **Not causal, not dynamic.** It's a structural snapshot, not an account of how the network formed or where it's heading.
- **Clustering needs alter–alter data.** A raw contact export gives a person's contacts but usually *not* whether those contacts know each other. Without that, you can't estimate triadic closure — which is exactly what drives realistic component-size and distance estimates in clustered communities. **Design implication: to get good cohesion numbers, your data-release format must capture alter–alter ties, not just contact lists.**

## First experiments to run
1. **Ground-truth harness (do this first).** Take a known network, sample egos, reconstruct, compare simulated vs true distance and largest-connected-group. Your trust calibration before any real deployment — this is exactly what Smith did with the Add Health and coauthorship networks.
2. **Sample-fraction sweep.** How small can the ego sample get before estimates degrade? Sets your minimum community participation threshold.
3. **Alter–alter ablation.** Run with vs without alter–alter ties to quantify what clustering data buys you — directly informs your data-collection UX.
4. **Degree / density sweep.** Find the average-degree threshold where confidence collapses for *your* target community types.
