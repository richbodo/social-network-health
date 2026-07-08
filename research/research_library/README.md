# Research Library

The corpus behind the SNH research notes, and the plans for turning it into a proper
knowledge base.

- `research_summaries/` — per-paper summaries and experiments: one subfolder per paper,
  holding the summary ("research primitive") and any code derived from it.
- `planning/knowledge-base-plan.md` — the plan for turning the reference corpus into a
  markdown-per-paper knowledge base with CI-derived artifacts. Read before corpus tooling work.
- `paper-corpus/` — gitignored generated artifacts (SQLite index + downloaded PDFs) produced
  by `tools/paper-resolver/`.

## Growing the corpus: the paper-resolver

`tools/paper-resolver/` is the acquisition tool for this library: give it a DOI, a title, a
DOI list, or a topic search and it walks open scholarly infrastructure (OpenAlex → Unpaywall →
Semantic Scholar → Europe PMC → Crossref) to return metadata plus a **legal** open-access
full-text URL, optionally downloading the PDF and extracting its text into `paper-corpus/`.
It never routes around paywalls — no-OA papers are queued in `unresolved.jsonl` for manual
pickup. Validated working 2026-06-10; see `tools/paper-resolver/usage.md` for the exact
invocations and gotchas (flag order matters, `RESOLVER_EMAIL` is required). Quick start:

```bash
# run from the repo root
export RESOLVER_EMAIL=<you@example.com>
python3 tools/paper-resolver/resolve.py \
  --db research/research_library/paper-corpus/resolver.db \
  --download --extract --out research/research_library/paper-corpus/pdfs \
  search "remote work loneliness wellbeing" --limit 15 --from-year 2024
```

Division of labor: the **paper-resolver acquires** papers into the local, gitignored
`paper-corpus/`; **[snhdb](https://github.com/richbodo/snhdb) curates and serves** the public
library (and its `/snhdb` skill answers questions over it). New finds worth keeping should
graduate from `paper-corpus/` into snhdb.

## External resources

- **snhdb — the research-document GitHub store:** https://github.com/richbodo/snhdb — public
  paper library (PDFs, markdown conversions, YAML metadata cards, `card-schema.yaml`).
  Searchable locally with Claude Code (in-repo, or from anywhere via its user-wide `/snhdb`
  skill — see its README for install and `docs/search-with-claude-code.md` for the test
  protocol). Will
  sync with the Google Drive folder below and power the AI search engine planned for
  toolkit.socialnetwork.health. The card format descends from the schema drafted in
  `planning/knowledge-base-plan.md`.
- **Full papers & metadata (Google Drive, public):**
  https://drive.google.com/drive/u/0/folders/1CQIZnHCojqnvGuiOmn9UR7Jbf9nGlICD — the source
  folder for the research corpus.
- **Search with Claude Desktop (instructions):**
  https://docs.google.com/document/d/1QlV5VQE1dEqhYEget6jJUSHRhCDfgrynyYdgXm6BoWU — the most
  commonly used how-to for querying the library with AI tools.
- **SNH GPT — Researcher (the original custom GPT):**
  https://chatgpt.com/g/g-67c7b452ac188191aa2fab75ce290cc4-social-network-health-researcher —
  grounded in hundreds of papers and articles on social network health, focused on remote and
  distributed teams. Useful for fast literature-aware answers with citations; predates (and
  will eventually be superseded by) the knowledge-base plan above.

The threat-catalog bibliography lives with its document:
`../threat_modelling/references/references.md`.
