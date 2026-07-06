# Social Network Health

This research project has the goal of improving social network health in digitally connected but remote communities.

It aggregates several efforts:
- Implementations of protocols to communicate needs and community health metrics
- Efforts to create software better suited to individual and community health
- Production of educational materials that support understanding of social network health interventions

This repo is the **organizing hub**: the https://socialnetwork.health website, research documents,
and pointers to the software efforts we are developing in other places.

## Layout

- `research/measurement/` — measuring community network health from egocentric data: the
  egocentric→community research note, the explainer, the social-cohesion note
- `research/threat_modelling/` — the threat catalog and its bibliography (`references/`)
- `research/protocols/` — protocol design notes (the SNH notification protocol)
- `research/research_library/` — per-paper `research_summaries/` (where papers applicable to
  proposed protocols are summarized and tested), the knowledge-base plan (`planning/`), and
  the gitignored paper corpus
- `tools/paper-resolver/` — tool for resolving papers to metadata + legal open-access full text
- `presentations/` — talk preparation
- `public/` + `ops/` — the static website and its droplet deploy

## Related repositories

The software (PNA toolkit, PRM, reference designs) lives in sibling repos — see
[`RELATED_REPOS.md`](RELATED_REPOS.md) for the map. Convention: all related repos are checked out
side by side, one level up from this repo root.
