# Research Library

The corpus behind the SNH research notes, and the plans for turning it into a proper
knowledge base.

- `research_summaries/` — per-paper summaries and experiments: one subfolder per paper,
  holding the summary ("research primitive") and any code derived from it.
- `planning/knowledge-base-plan.md` — the plan for turning the reference corpus into a
  markdown-per-paper knowledge base with CI-derived artifacts. Read before corpus tooling work.
- `paper-corpus/` — gitignored generated artifacts (SQLite index + downloaded PDFs) produced
  by `tools/paper-resolver/`.

## External resources

- **snhdb — the research-document GitHub store:** https://github.com/richbodo/snhdb — public
  paper library (PDFs, markdown conversions, YAML metadata cards, `card-schema.yaml`). Will
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
