# Private Egocentric-to-Community Network Health: Research Note

_Date: 27 June 2026_

_Initial source conversation for this research note: <https://chatgpt.com/share/6a3f9a12-ebd0-83ec-afc8-391b79461f1c>_

## 1. Decision trail and current thesis

The conversation began with a broad question: whether social-network-health research has studied communities by starting from each individual’s own personal network rather than by first centralizing a whole sociocentric graph. If given a **personal relationship manager** that can analyze a user’s own egocentric network, can we surface useful, explainable feedback.

The working product/design thesis is now:

> A local-first personal relationship manager can use egocentric network analysis as a reflective maintenance layer: helping a person see support coverage, neglected ties, over-concentration, weak-tie bridges, costly relationships, and gaps in their own semantic understanding of relationships.

The stronger community thesis was refined into a defensible “version two”:

> Given opt-in local egocentric relationship data, explicit edge predicates, privacy-preserving identity/linkage mechanisms, secure aggregation, and differentially private release controls, selected community-network-health indicators can be estimated without centralizing raw relationship data.

No single paper or project was found that implements the full stack: **personal relationship manager → local/sandboxed account analyzers → egocentric relationship proofs → encrypted collaborative space → ZK/MPC/private aggregation → community social-network-health dashboard**. The pieces exist across several literatures, and the exact combination still looks like an open research/design contribution.

This note treats the design as research infrastructure and a lab prototype, not as a deployed intervention. The aim is to determine what can be measured, what cannot be safely measured, and what kinds of community-level insights can be supported without centralizing raw relationship data.

## 2. Social network health / egocentric network research

The relevant research vocabulary is **egocentric network analysis**, **personal network analysis**, **personal communities**, and sometimes **networked individualism**. The most useful design shift is to stop treating “community” as necessarily one bounded sociocentric graph and instead ask how many personally bounded networks overlap, conflict, reinforce, or fail to connect.

For the personal relationship manager, we propose a panel of explainable signals. The important insight is that different network shapes can be healthy in different ways. Dense clusters can provide belonging and redundancy, but can also be insular. Sparse networks can create bridges and autonomy, but can also indicate fragility or isolation. More ties are not automatically better.

Recommended personal-level metrics:

| Dimension | Product meaning | Possible local metric |
|---|---|---|
| Support coverage | Do I have people for the kinds of help I need? | Count of trusted alters by support type: emotional, practical, emergency, childcare, advice, professional |
| Support concentration | Am I overdependent on one or two people? | Concentration/Gini/Herfindahl-style index over support roles |
| Relationship diversity | Are my ties spread across life domains? | Distribution across family, local friends, old friends, work, neighbors, open-source, school, etc. |
| Maintenance load | How many relationships am I trying to keep warm? | Active ties × desired cadence × importance |
| Neglect / drift | Which important ties have gone quiet? | Importance-weighted time since meaningful contact |
| Resilience | If one person became unavailable, what breaks? | Single-point-of-failure checks by support category |
| Bridging | Do I have weak ties into different worlds? | Cluster count, effective size, low-overlap ties, structural-hole style indicators |
| Closure / belonging | Do I have groups where people know each other? | Alter-alter density within contexts, with unknown ties kept as unknown |
| Reciprocity | Are some ties mostly giving or mostly receiving? | User-rated giving/receiving balance |
| Ambivalence / cost | Which important ties are also stressful? | High importance + high stress/conflict ratings |
| Semantic confidence | How well-modeled are important relationships? | Relationship type, trust, context, channel, cadence, consent/privacy state, and support role completeness |

A first v0 personal engine should probably implement only six insight families: important-but-neglected ties, support gaps, support concentration, overdue maintenance, network diversity snapshot, and ambivalent/high-cost ties. The app should produce insight cards, not obscure centrality jargon.

### Social-network-health and egocentric-method references

These are the items to put in the research library.

- Barry Wellman, **“The Community Question: The Intimate Networks of East Yorkers”**. Classic community-through-personal-networks paper; establishes a way to study community through linkages rather than bounded neighborhoods. <https://www.dhi.ac.uk/san/waysofbeing/data/communities-murphy-wellman-1979a.pdf>
- Barry Wellman, **“Physical Place and Cyberplace: The Rise of Networked Individualism”** / related networked individualism work. Useful theoretical background for person-centered communities. <https://www.dhi.ac.uk/san/waysofbeing/data/communication-zangana-wellman-2001b.pdf>
- Brea Perry, Bernice Pescosolido, and Stephen Borgatti, **Egocentric Network Analysis: Foundations, Methods, and Models**. Core methods reference. <https://assets.cambridge.org/97811071/31439/frontmatter/9781107131439_frontmatter.pdf>
- Birkett et al., **“Network Canvas: Key decisions in the design of an interviewer-assisted network data collection software suite.”** Practical reference for ego-network data collection tooling. <https://pubmed.ncbi.nlm.nih.gov/34054204/>
- `egor`, **R package for importing/analyzing/visualizing ego-centered network data.** Useful implementation reference. <https://cran.r-project.org/web/packages/egor/egor.pdf>
- O’Malley et al., **“Egocentric Social Network Structure, Health, and Pro-Social Behaviors in a National Panel Study of Americans.”** Empirical example relating ego-network features to health and prosocial behavior. <https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0036250>
- Berkman, Glass, Brissette, and Seeman, **“From social integration to health: Durkheim in the new millennium.”** Broad social epidemiology bridge from networks to health mechanisms. <https://pubmed.ncbi.nlm.nih.gov/10972429/>
- Rook et al., **“Ambivalent Versus Problematic Social Ties.”** Important reminder that not all ties are supportive; strong ties can also be costly or stressful. <https://pmc.ncbi.nlm.nih.gov/articles/PMC3827363/>
- Vassilev et al., **“Social Networks, the ‘Work’ and Work Force of Chronic Illness Self-Management.”** Useful for personal communities and the work/maintenance burden of social networks. <https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0059723>
- Jeffrey A. Smith, **“Macrostructure from Microstructure: Generating Whole Systems from Ego Networks.”** Key methodological anchor for estimating/simulating whole-network properties from ego-network data. <https://digitalcommons.unl.edu/sociologyfacpub/247/>
- Britton and Trapman, **“Inferring global network properties from egocentric data.”** Important caution: ego data may permit a wide range of global structures unless assumptions are added. <https://arxiv.org/abs/1201.2788>
- Krivitsky and Morris, **“Inference for social network models from egocentrically sampled data.”** Formal modeling reference for what can be estimated from ego samples. <https://projecteuclid.org/journals/annals-of-applied-statistics/volume-11/issue-1/Inference-for-social-network-models-from-egocentrically-sampled-data-with/10.1214/16-AOAS1010.full>
- Bolíbar, Martínez-Ariño, and Schiller, **“A Method to Aggregate Egocentric Network Survey Data.”** Relevant because it explicitly explores aggregation of ego-network surveys into larger structures. <https://journals.sagepub.com/doi/abs/10.1177/1525822X241262678>

## 3. Technology / crypto / privacy-preserving graph computation

The technology design is best understood as five layers:

1. **Local analyzers**: Gmail, Signal, WhatsApp, calendar, contacts, GitHub, and manual relationship editors run locally or in protected sandboxes.
2. **Personal relationship manager**: the user sees their own graph and local insight cards; this stage does not require community computation.
3. **Proof compiler**: the user chooses which predicates to contribute, and the system emits commitments/proofs rather than raw data.
4. **Encrypted community space**: membership, schemas, contribution rounds, proof verification, revocation, and audit logs are managed over encrypted shared state.
5. **Private aggregation/release layer**: MPC, secure aggregation, graph-specific private analytics, and differential privacy compute only thresholded/noisy aggregate metrics.

The key caution is that zero-knowledge proofs do not solve privacy by themselves. A ZK proof hides the witness, but the statement being proven can still leak. For example, “I have a high-trust tie to someone in this small subgroup” may be identifying even if the proof is cryptographically zero knowledge. The system therefore needs thresholding, differential privacy, query-budget accounting, purpose-specific pseudonyms, epoch rotation, and strong refusal rules for unsafe small-cell outputs.

### Technology/protocol references

These are better suited to a technology spreadsheet than the social-network-health research library.

- **Encrypted Spaces**. Research/prototype architecture for encrypted collaborative applications with cryptographically verifiable operations over untrusted infrastructure. <https://encryptedspaces.org/> and <https://github.com/encrypted-spaces/prototype>
- **Microsoft Research: Encrypted Spaces project page.** Short technical overview of encrypted collaborative state, group key management, and verifiable structures. <https://www.microsoft.com/en-us/research/project/encrypted-spaces/>
- Chase, Perrin, and Zaverucha, **“The Signal Private Group System and Anonymous Credentials Supporting Efficient Verifiable Encryption.”** Deployed precedent for private group membership and anonymous credentials. <https://eprint.iacr.org/2019/1416>
- Zhang et al., **DECO: Liberating Web Data Using Decentralized Oracles for TLS.** Relevant for proving facts about web-account data without revealing the underlying data. <https://arxiv.org/abs/1909.00938>
- Kukkala and Iyengar, **“MPC meets SNA: A Privacy Preserving Analysis of Distributed Sensitive Social Networks.”** Directly relevant MPC-for-social-network-analysis paper. <https://arxiv.org/abs/1705.06929>
- Wang et al., **PrivGED: Privacy-Preserving Analytics on Decentralized Social Graphs.** Users contribute local graph views for eigendecomposition-style analytics with cryptography and differential privacy. <https://arxiv.org/abs/2206.09388>
- Zheng et al., **“Graph Analysis in Decentralized Online Social Networks with Fine-Grained Privacy Protection.”** Fine-grained relationship differential privacy for decentralized local views; triangle and k-star counts. <https://arxiv.org/abs/2212.05253>
- Wang et al., **MAGO: Maliciously Secure Subgraph Counting on Decentralized Social Graphs.** Relevant when participants or infrastructure may be malicious. <https://ieeexplore.ieee.org/document/10113303/>
- Tan, Sfyrakis, and Groß, **“A Relational Credential System from q-SDH-based Graph Signatures.”** ZK relationship predicates and relational credentials. <https://eprint.iacr.org/2023/1181>
- Gehrke, Lui, and Pass, **“Towards Privacy for Social Networks: A Zero-Knowledge Based Definition of Privacy.”** Conceptual privacy framework for graph release. <https://www.cs.cornell.edu/~luied/zkPrivacyFinal.pdf>
- Fu et al., **“Privacy-Preserving Graph Machine Learning from Data to Computation: A Survey.”** Broad map of privacy-preserving graph computation. <https://arxiv.org/abs/2307.04338>
- Lavin et al., **“A Survey on the Applications of Zero-Knowledge Proofs.”** General ZK applications and implementation landscape. <https://arxiv.org/abs/2408.00243>

## 4. Building social-network-health analysis from egocentric datasets

The central design conclusion is that the community system should not attempt to reconstruct or publish the whole social graph. It should instead compute selected, bounded, privacy-reviewed indicators from many local egocentric datasets. Those indicators should be useful enough for community stewardship, but coarse enough that individual relationships, hidden bridges, and overloaded people are not revealed.

### Important design distinction: proofs are not privacy

ZK proofs can prove that a statement is true without revealing the private witness. That is useful for correctness, provenance, and compliance with protocol rules. However, the **statement itself** can still leak sensitive information. A proof that “I have a high-trust relationship with someone in this small subgroup” may be identifying even if the proof hides all underlying data.

The system therefore needs multiple privacy layers, each doing a different job:

1. **ZK proofs / verifiable computation**: prove that a contribution was computed according to the approved predicate and analyzer version without revealing the raw local data.
2. **MPC or secure aggregation**: combine contributions so no single server or analyst receives individual edge claims or local metrics.
3. **Differential privacy and thresholding**: prevent released aggregate statistics from revealing individual participation, edges, or small-cell facts.
4. **Purpose-specific pseudonyms or commitments**: allow limited linkage within a cohort/epoch/query while avoiding a global stable anonymous identity that can be tracked across contexts.
5. **Query-budget accounting**: prevent repeated “safe” queries from being combined over time to reconstruct the hidden graph.
6. **Consent and edge semantics**: distinguish unilateral observations from mutual attestations and avoid treating inferred communication metadata as proof of trust, support, friendship, or consent.
7. **Refusal rules**: allow the system to return “unsafe to release” when a metric would expose a small group, a unique bridge, a hub, or a sensitive tie category.

This distinction is the main reason the design should be staged and conservative. The cryptography can make the computation trustworthy, but privacy also depends on metric selection, cohort size, semantics, release policy, and human consent.

### Plausible architecture

A plausible architecture has five layers.

**1. Local analyzers**  
Gmail, Signal, WhatsApp, calendar, contacts, GitHub/open-source, and manual relationship editors run locally or in protected sandboxes. They should not export message bodies or raw contact graphs. In early versions, manual self-report and explicit contact metadata are safer than automated message analysis.

**2. Personal relationship manager**  
The user sees their own egocentric graph and local insight cards. This stage is useful by itself and does not require any community-level computation.

**3. Proof compiler**  
The user chooses which bounded predicates to contribute. The proof compiler emits commitments and proofs rather than raw data. Example contribution statements might be:

```text
I am an eligible member of cohort C.
I ran analyzer version X over local source Y.
I found K edges satisfying predicate P, binned according to the approved schema.
For mutual predicates, the counterparty submitted a matching commitment.
The contribution is well-formed, non-duplicative, and within allowed bounds.
```

**4. Encrypted community space**  
The cohort’s encrypted space manages membership, schemas, consent, contribution rounds, proof verification, revocation, and audit logs. Encrypted Spaces is a relevant substrate for this layer, though it should be treated as research/prototype infrastructure rather than a complete solution.

**5. Private aggregation and release layer**  
MPC, secure aggregation, graph-specific private analytics, and differential privacy compute only thresholded/noisy aggregate metrics. The release layer refuses small cells, tracks privacy budget, and publishes uncertainty rather than exact raw counts.

### Meaningful community insights that might be possible

The most interesting social-network-health insight is probably not “the network is dense.” Better outputs would help stewards understand fragility, integration, and support load without naming the people who create those patterns. Examples:

- “Newcomers are mostly connected to organizers, but not to each other.”
- “Climate, web3, and open-source clusters overlap through only a very small number of bridge roles.”
- “Advice-seeking is highly centralized; burnout risk may be concentrated.”
- “There are many recognition edges, but fewer recent meaningful-interaction edges.”
- “The community has strong bonding clusters but weak cross-cluster redundancy.”
- “Several subgroups overlap through only a small number of bridge roles; exact bridge identities are not released.”

These are useful because they point toward community-care questions without requiring the dashboard to reveal individual relationships. The practical value is in aggregate diagnosis and research, not automated intervention.

## 5. Computable community metrics from egocentric contributions

The first community dashboard should avoid individual rankings and “who is most central” outputs. It should compute aggregate, thresholded, noisy indicators that are useful for stewardship while resisting re-identification.

Candidate edge predicates:

- **Recognition edge**: I know who this person is and can place them in context.
- **Recent meaningful interaction**: I had a meaningful interaction with this person in the last N days.
- **Advice/help edge**: I would ask this person for advice/help in this domain.
- **Collaboration edge**: We have worked together on a project/event/repo.
- **Mutual support edge**: both parties attest to some bounded support/collaboration predicate.

Candidate aggregate metrics:

| Metric | Required ego inputs | Community insight | Main constraint/risk |
|---|---|---|---|
| Binned degree distribution | Count of alters satisfying predicate P | Are many people isolated or overloaded? | Avoid exposing exact degrees for small groups |
| Near-isolate count | Number of participants below edge threshold | Newcomer or marginal-member fragility | Needs careful consent and non-stigmatizing framing |
| Newcomer integration | Participant cohort status + binned ties | Are first-time people connected to repeat participants? | Small newcomer groups are identifying |
| Context-mixing matrix | User-declared contexts + edge predicates | Are subgroups bridging or siloed? | Small cells must be suppressed/noised |
| Support/advice concentration | Binned advice/help edges by role/category | Is too much support load falling on a few people? | Do not identify overloaded people without consent |
| Triangle / clustering count | Alter-alter ties or mutual commitments | Are people embedded in small trusted clusters? | Requires more sensitive data than simple ego degrees |
| k-star / hub-load count | Local degree patterns | Are many ties routed through a few hubs? | Hub outputs are re-identification magnets |
| Bridge redundancy | Cluster memberships + cross-cluster edges | Are clusters connected by one fragile bridge? | Needs coarse release; no named bridges |
| Recency decay | Time-binned interaction predicates | Is the community active or mostly historical? | Time windows can reveal events/relationships |
| Semantic confidence aggregate | Completeness of relationship metadata | Is the community relationship map under-specified? | Should measure model quality, not people quality |
| Ambivalent/high-cost tie prevalence | Positive + stress/friction ratings | Are support networks also carrying stress? | Highly sensitive; likely only safe as broad aggregate |

The safest early metrics are binned degree distributions, near-isolate counts, context-mixing matrices with suppression, recency decay, and semantic-confidence aggregates. More sensitive metrics — bridge redundancy, hub-load, triangle counts, and ambivalent/high-cost tie prevalence — should require larger cohorts, stronger privacy controls, and more careful review.

## 6. Suggested test parameters

A first serious test should be a lab/research prototype, not an intervention.

- **Cohort**: 30–200 opt-in participants from a bounded community such as a DWebCamp session, open-source working group, or small decentralized-web cohort.
- **Data source**: start with manual/self-report plus imported contacts metadata only if explicitly chosen. Avoid scraping message bodies in v0.
- **Predicates**: use three or four modest predicates: recognition, recent meaningful interaction, advice/help, collaboration.
- **Bins**: use coarse bins: last 30/90/365 days; weak/medium/strong; unilateral/mutual.
- **Identity**: use cohort-scoped commitments, not global stable anonymous IDs. Rotate by epoch and purpose.
- **Consent**: distinguish unilateral observations from mutual attestations. Higher-sensitivity claims should require mutuality or stronger suppression.
- **ZK/verifiability**: prove that contributions are well-formed and derived from approved predicates/analyzers without revealing raw local data.
- **Secure aggregation**: combine contributions through MPC or secure aggregation so no coordinator sees individual edge claims.
- **Differential privacy and thresholding**: suppress small cells, add noise where appropriate, and publish confidence intervals rather than exact raw counts.
- **Purpose-specific pseudonyms**: use cohort/epoch/query-scoped commitments and avoid globally reusable anonymous identifiers.
- **Query-budget accounting**: limit repeated releases so analysts cannot reconstruct edges through differencing attacks.
- **Release/refusal rules**: allow the system to decline unsafe metrics, especially named hubs, unique bridges, small subgroups, and sensitive tie categories.
- **Validation**: compare against synthetic ground truth, a small fully consented plaintext baseline, a conventional belonging/psychological-safety/access-to-help survey, and adversarial reconstruction tests.
- **Success criteria**: useful aggregate insights with bounded error; no raw edges, named hubs, named bridges, message contents, or small-cell relationship claims exposed.

The research contribution would be the combined design pattern: **local-first personal relationship graphs plus privacy-preserving egocentric-to-community inference for social network health**.
