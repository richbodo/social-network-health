---
name: paper-resolver
description: >-
  Resolve academic papers to rich metadata plus a LEGAL open-access full-text
  URL (and optionally download the PDF and extract its text), by walking a tier
  of open scholarly infrastructure — OpenAlex, Unpaywall, Semantic Scholar,
  Europe PMC, and Crossref. Use this whenever the user wants to find, fetch,
  collect, or build a corpus of research papers from a DOI, a title, a list of
  DOIs, or a topic search — especially in psychology, sociology, social network
  health, public health, or any field where much literature sits behind
  publisher paywalls but has legally-posted open-access versions. Trigger this
  for phrases like "find the full text of", "get me this paper", "resolve these
  DOIs", "is there an open version of", "build a reading corpus on", or "pull
  the open-access PDFs for these references" — even when the user doesn't name a
  specific database. Do NOT use this to circumvent paywalls; it only ever
  surfaces openly licensed copies.
---

# Paper Resolver

Find the richest available metadata and a **legally open** full-text copy for
academic papers, using only open scholarly infrastructure. Paywalled papers that
have no open-access version are recorded as `metadata_only` and queued for
manual follow-up — the tool never attempts to route around a paywall.

## When to reach for this

Use it whenever the goal is to locate, fetch, or accumulate research literature
programmatically: a single DOI, a title to look up, a file of DOIs to batch, or
a topic to search and harvest. It is especially valuable in fields with heavy
paywalling but strong open-access shadow coverage (psychology, sociology, social
network health, public health, computational social science), where a large
fraction of nominally-paywalled work has a legal preprint or author manuscript
findable via Unpaywall or repository copies.

## The resolution tiers

For a given DOI the script assembles one record by walking these layers, taking
the richest value for each field and the first legal full-text it finds:

- **Metadata** — OpenAlex first (richest single source: abstract, authors,
  venue, OA status), with gaps filled from Semantic Scholar and Crossref.
- **Full text** — Unpaywall (best legal-PDF locator) → OpenAlex `best_oa` →
  Semantic Scholar `openAccessPdf` → Europe PMC (open-access subset, good for
  health-adjacent work) → Crossref text-mining links (surfaced but flagged,
  since these often require a subscription entitlement).

A paper resolves to `fulltext` if any legal full-text URL is found, otherwise
`metadata_only`.

## How to run it

The resolver is a single dependency-light Python script (standard library only;
PDF text extraction optionally uses PyMuPDF). Always pass a contact email — it
puts OpenAlex calls in the faster "polite pool" and is **required** by Unpaywall,
so without it full-text hit rates drop sharply. Set it once via the
`RESOLVER_EMAIL` environment variable or pass `--email`.

```bash
# Single DOI
python scripts/resolve.py --email you@example.com doi 10.1371/journal.pone.0173644

# A topic search (OpenAlex relevance), resolving each hit
python scripts/resolve.py --email you@example.com search "social network health intervention" --limit 25

# A batch from a file of DOIs (one per line, # comments allowed)
python scripts/resolve.py --email you@example.com batch refs.txt

# Build a downloaded, text-extracted corpus
python scripts/resolve.py --email you@example.com batch refs.txt --download --extract --out ./corpus
```

Key flags: `--download` fetches OA PDFs into `--out`; `--extract` pulls plain
text from them (needs PyMuPDF — `pip install pymupdf`); `--json` prints full
records; `--refresh` ignores the cache and re-resolves; `--s2-key` supplies a
Semantic Scholar key for higher rate limits.

## Output and state

All state lives in one SQLite file (`--db`, default `resolver.db`) that serves as
**both the cache and the corpus index** — re-running is cheap and idempotent, and
the database is a portable local-first artifact. Each row carries the full record
JSON plus indexed columns (doi, title, year, venue, status, pdf_url, paths).
Papers with no legal full text are also appended to `unresolved.jsonl` next to the
db, so the manual-retrieval queue is always one file.

To feed resolved papers into a downstream task (summarisation, a literature map,
context for another agent), read from the SQLite db or the extracted `.txt`
files rather than re-calling the APIs.

## Etiquette and limits

These are shared community resources. Keep the politeness delay (`--sleep`,
default 0.2s) in place, always send the email, and prefer `batch` over many
one-off calls so the cache does its job. OpenAlex suggests staying under ~100k
calls/day. The script already backs off on 429/5xx with `Retry-After`.

## Reporting back to the user

After a run, summarise concretely: how many papers resolved to full text vs.
metadata-only, where the corpus db and any downloaded files live, and — if the
metadata-only count is non-trivial — note that those are queued in
`unresolved.jsonl` for manual retrieval (e.g. via an institutional library), not
lost.

## Graduating to an MCP server (later, if needed)

This is deliberately a skill, not a server: it is read-only public HTTP with no
auth or persistent connection, so on-demand script execution is the right shape.
If a *running service* is later wanted — e.g. so another app can call resolution,
or to centrally manage publisher TDM keys — the functions in `resolve.py`
(`resolve_doi`, `search_works`, the `from_*` adapters) are import-safe and can be
wrapped in a FastMCP server with no rewrite. Keep the resolution logic in the
module; let the server be a thin transport layer over it.
