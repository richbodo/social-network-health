# AGENTS.md — orientation for AI coding agents

This repo is the **organizing hub for the Social Network Health (SNH) research program** plus the
static website at https://socialnetwork.health. It contains research documents and a tiny static
site — no web framework, no package manager, no tests.

## Directory map

- `public/` — the entire live site (one self-contained HTML file + one SVG). Edit the HTML to
  change the site; deploy with `just deploy` (see the root `justfile` for all devops recipes).
- `ops/` — Ansible + Caddy provisioning and deploy for the site (see `ops/README.md`).
- `research/foundational/` — the threat catalog, the egocentric→community research note, the
  social-cohesion note.
- `research/library/` — `references.md` (append-only `[n]` numbering — never renumber) and
  `summaries/` (per-paper research primitives).
- `research/planning/` — `knowledge-base-plan.md`; read it before corpus/knowledge-base work.
- `tools/paper-resolver/` — Python tool resolving DOIs/titles/topics to metadata + legal
  open-access full text; see its `usage.md` before running.
- `presentations/` — talk preparation.
- `drafts/` — stub redirect only; don't add content there.

## Related repositories

**Read `RELATED_REPOS.md`.** All related repos (the PNA toolkit, PRM, reference designs, workshop
decks) are checked out as siblings of this repo — `../<name>` from the repo root, same layout on
every workstation. Resolve cross-repo paths relatively, never with absolute prefixes.
