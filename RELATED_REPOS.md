# Related repositories & resources

This repo (`social-network-health`) is the organizing hub for the Social Network Health (SNH)
research program. The software, specs, and workshop materials live in sibling repositories.

## The sibling-checkout convention

**All project repos are checked out side by side in the same parent directory** (`~/src/` on this
machine, the equivalent on other workstations). So from this repo's root, every related repo is at
`../<name>`. When doing cross-repo work, resolve paths **relative to the repo root** (`../prm`,
`../personal_network_toolkit`, …), never as absolute paths — the absolute prefix differs per host.
Not every sibling directory is related to SNH; the tables below list the ones that are.

## Core software (active)

| Repo | Local path | Remote | Role |
|---|---|---|---|
| personal_network_toolkit | `../personal_network_toolkit` | github.com/richbodo/personal_network_toolkit | The PNA Toolkit — spec, contracts, skill, MCP servers, and lints for building/validating **Personal Network Applications**. The central toolkit; the PNA Spec and positioning paper live in its `spec/` and `docs/`. |
| prm | `../prm` | github.com/richbodo/prm | Personal Relationship Manager — local web app, PNA reference design (attested at Toolkit v0.2). |
| fellows_local_db | `../fellows_local_db` | github.com/richbodo/fellows_local_db | EHF Fellows Local Directory — local-first SQLite + PWA directory app; the toolkit's first reference design; hosts three v1 MCP servers. |
| prt | `../prt` | github.com/richbodo/prt | Personal Relationship Toolkit — Python TUI relationship manager; earlier generation, basis for prm (listed as archived on the website). |

## Talks & workshop material

All talk material now lives **in this repo** under `presentations/`. The PNT workshop Slidev deck
was imported from the standalone repo in July 2026:

| Repo | Local path | Remote | Role |
|---|---|---|---|
| pnt-workshop | `presentations/pnt-workshop/` (imported; standalone checkout at `../pnt-workshop` is now redundant) | github.com/richbodo/pnt-workshop (candidate for archiving) | Slidev slide deck + talk notes for Personal Network Toolkit workshops. Starting point for new decks (e.g. DWeb Camp Berlin 2026). |

## Data tooling & wiki (dormant / historical)

| Repo | Local path | Remote | Role | Status |
|---|---|---|---|---|
| snh_bridge_test | `../snh_bridge_test` | github.com/richbodo/snh_bridge_test | CLI test utility for the DataBridge API SNH project (PDF upload + query). | stale (2025) |
| snhtoolkitmw | `../snhtoolkitmw` | github.com/richbodo/snhtoolkitmw | MediaWiki extension bundle/config for the SNH toolkit wiki. | dormant (2024) |
| socialnetwork_toolkit | `../socialnetwork_toolkit` | github.com/richbodo/socialnetwork_toolkit | MediaWiki install/config + content for the toolkit wiki. **Its README warns secrets are checked in — treat as sensitive, never mirror publicly.** | dormant (2024) |
| slack2kumu_directory | `../slack2kumu_directory` | github.com/richbodo/slack2kumu_directory | Slack community → Kumu directory diagram script. | dormant (2024) |
| kumu_directory_from_slack | `../kumu_directory_from_slack` | (not a git repo) | Un-versioned precursor of slack2kumu_directory. | dormant |
| collaborationscience | `../collaborationscience` | github.com/richbodo/collaborationscience | Plain-text knowledge base on collaboration — predecessor thinking, tangential to SNH proper. | historical (2019) |

## Non-repo resources

- **Toolkit wiki (live):** https://toolkit.socialnetwork.health — MediaWiki of best practices and research findings; the primary body of published SNH work.
- **Paper corpus (Google Drive, public):** https://drive.google.com/drive/u/0/folders/1CQIZnHCojqnvGuiOmn9UR7Jbf9nGlICD — full papers & metadata behind `research/threat_modelling/references/references.md`.
- **SNH GPT — Researcher:** custom GPT grounded in the corpus (linked from the homepage).
- **Video archive:** https://www.youtube.com/@SocialNetworkHealth
- **Live site:** https://socialnetwork.health — served from this repo's `public/`, deployed via `ops/`.

*Compiled 2026-07-04 from a survey of `~/src/` on this host. When a related repo is added or retired, update this file — it is the single source of truth that `CLAUDE.md`, `AGENTS.md`, and the `/prime` command all point to.*
