# Paper-Resolver — Usage Notes (working scratch → will formalize once the workflow settles)

*Started 2026-06-10. Goal: capture exactly how we run the paper-resolver so we can pick the
context back up instantly next time. We'll tidy this into a clean "how we use it" doc once the
workflow is settled.*

## Status: VALIDATED WORKING (2026-06-10)
First live test succeeded — resolved a PLOS DOI to full metadata + a legal OA PDF (gold, CC-BY).
OpenAlex + Unpaywall are responding from this machine.

## The validated invocation
```bash
RESOLVER_EMAIL=richbodo@gmail.com \
python3 /Users/rsb/src/host-happily-hub/drafts/skill_experiment/unzipped/resolve.py \
  --db /Users/rsb/src/host-happily-hub/drafts/paper-corpus/resolver.db \
  --json doi 10.1371/journal.pone.0173644
```

## Validated enrichment-search command (topic harvest → OA PDFs + extracted text)
```bash
export RESOLVER_EMAIL=richbodo@gmail.com
S=/Users/rsb/src/host-happily-hub/drafts/skill_experiment/unzipped/resolve.py
D=/Users/rsb/src/host-happily-hub/drafts/paper-corpus/resolver.db
O=/Users/rsb/src/host-happily-hub/drafts/paper-corpus/pdfs
python3 "$S" --db "$D" --download --extract --out "$O" search "<topic query>" --limit 15
```
Global flags (`--db --download --extract --out`) go BEFORE `search`; `--limit` is a search-subcommand
arg and goes AFTER the query. Each hit is resolved → (if legally OA) PDF downloaded to `$O` → text
extracted next to it; metadata-only papers queue in `unresolved.jsonl`. First enrichment run
(2026-06-10): K5 embodiment/co-presence ×2, K6 hard-to-reach/selection-bias ×1, current remote-worker
SNH ×2. *Note:* OpenAlex `search` is relevance-ranked, NOT year-filtered — to bias toward recent work,
filter results by `year` after the run (the script has no `--from-year` flag yet; a candidate future tweak).

## Settings we're using
- **Email:** `richbodo@gmail.com` (via `RESOLVER_EMAIL`; required by Unpaywall, polite pool for OpenAlex).
- **Script:** `drafts/skill_experiment/unzipped/resolve.py` (the loose copy; `paper-resolver.skill`
  is the installable bundle).
- **Corpus db:** `drafts/paper-corpus/resolver.db` (the SQLite cache *and* corpus index — reruns are
  cheap/idempotent).
- **Downloads (when used):** plan to use `--download --extract --out drafts/paper-corpus/pdfs`.

## Gotchas (learned the hard way)
1. **Global flags BEFORE the subcommand.** `... --json doi <DOI>` works; `... doi <DOI> --json`
   errors with "unrecognized arguments: --json". Same for `--db`, `--download`, `--extract`, `--out`.
2. **Email is effectively required** — without it Unpaywall is skipped and OA hit-rate tanks.
3. **Network:** in this CLI the script needs to run with network access enabled (sandbox off for
   the call). Authorized by Rich.
4. **`--extract` needs PyMuPDF** — **installed 2026-06-10 (v1.27.2.3)**, so text extraction is on.
5. **CORE not wired in** (needs a registered key) — optional future tier.

## The three modes
- `doi <DOI>` — resolve one paper.
- `batch <file>` — resolve a file of DOIs (one per line, `#` comments OK).
- `search "<query>" --limit N` — OpenAlex relevance search, then resolve each hit. ← our main tool
  for finding NEW papers.

## Intended workflow (proposed — to confirm with Rich)
1. **Validate field coverage:** batch-resolve the references we already have DOIs for → see the
   full-text-vs-metadata-only split (the real test of OA coverage in our field).
2. **Enrich:** topic `search`es for recent (2025–2026) OA papers on our thin/key areas (K5
   embodiment, K6 hard-to-reach selection bias, current remote-worker SNH) → candidate new sources.
3. **Fill gaps:** title-`search` the 133 references that lack identifiers → recover DOIs for
   `references.md` + fetch OA PDFs; the rest go to `unresolved.jsonl` for manual/library pickup.

## First-run learnings & validated workflow (2026-06-10)
- **OA coverage in our field is excellent** — nearly every resolved paper came back full-text
  open-access. Exceptions are older *methods* classics (e.g. Heckathorn's 1997 RDS paper) → metadata-only.
- **Fixed a crash** in the working copy: `from_openalex` raised `'NoneType' … get` on papers with a
  null `source` (venue). Patched to `((… or {}).get("source") or {}).get("display_name")`. (The
  `.skill` bundle is untouched — easy to have claude.ai regenerate if preferred.)
- **Added `--from-year`** to `search`: topic searches now accept a recency floor (OpenAlex
  `filter=from_publication_date:<year>-01-01`). Use it for *current* work; omit it for foundational/
  methods topics where you want the canonical sources.
- **Query lesson (important):** broad multi-keyword queries pull noise (keyword collisions — "survey"/
  "selection" dragged in *astronomy & biology*) and old highly-cited classics. **Tight, field-specific
  queries win.** `"remote work loneliness wellbeing" --from-year 2024` → a clean 2024–25 set;
  `"hard-to-reach populations research recruitment strategies"` → on-target methods papers.
- **Corpus is idempotent** — re-runs are cached by DOI, so iterating on queries is cheap.
- **Downloader hardened (2026-06-10):** PDF download now uses a browser User-Agent + a `%PDF`
  content check (so HTML landing/error pages aren't saved as fake PDFs). This recovered several
  UA-blocked publishers — BUT **SAGE, Wiley, Elsevier, ACM, INFORMS, and MDPI (ijerph) still block**
  scripted OA-PDF fetch (cookies/JS); those resolve to a full-text URL but need a real browser or
  manual pickup. Failed downloads stay queued (status=`fulltext`, `pdf_path` empty) — re-runnable
  later via `batch <failed-dois> --refresh --download`. A headless-browser fetch tier is the next
  upgrade if we want those.

## Output to read downstream
The SQLite db (`papers` table: full record JSON + indexed columns) and, if `--extract` is used, the
`.txt` files next to each PDF. `unresolved.jsonl` is the manual-retrieval queue.
