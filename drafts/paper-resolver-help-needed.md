# Paper-Resolver Skill — Assessment & How You Can Help

*Rich asked me to read the "skill experiment," assess whether we can use it to search/grab
papers, say whether it needs authentication, and write down how he can help. 2026-06-10.*

## What it is
The experiment is a **`paper-resolver`** skill. (The `readme.md` was empty — 0 bytes — but
`SKILL.md` is the real documentation.) It's a single dependency-light Python script
(`resolve.py`) that, given a **DOI, a title, or a topic search**, walks a tier of open scholarly
infrastructure — **OpenAlex → Unpaywall → Semantic Scholar → Europe PMC → Crossref** — and
returns rich metadata plus a **legal open-access full-text URL** wherever one exists. It can
optionally **download the OA PDF and extract its text**, storing everything in one SQLite file
that doubles as a cache and a corpus index. Papers with no legal OA copy are recorded as
`metadata_only` and queued in `unresolved.jsonl` for manual retrieval — it never tries to bypass
a paywall.

## Can we use it? — Yes, strong fit.
It's close to ideal for what we need now: enriching our reference list and finding **recent
(2025–2026)** open-access papers in exactly the fields with heavy paywalling but good OA shadow
coverage (psychology, public health, social-network health, computational social science). Three
modes map onto our needs:
- `doi 10.xxxx/...` — resolve a single reference.
- `batch refs.txt` — resolve our whole existing reference list at once (verify + fetch OA PDFs).
- `search "remote worker loneliness intervention" --limit 25` — harvest recent literature on a topic.

## Authentication? — Essentially none.
- **No accounts, API keys, OAuth, or logins required.** All five sources are read-only public HTTP.
- **One thing is required: a contact email.** Unpaywall mandates it and it puts OpenAlex calls in
  the faster "polite pool"; without it, full-text hit rates drop sharply. Set once via
  `RESOLVER_EMAIL` or `--email`. *(Currently unset.)*
- **Optional, not required:** a Semantic Scholar API key (`--s2-key` / `S2_API_KEY`) for higher
  rate limits; and **PyMuPDF** (`pip install pymupdf`) only for `--extract` (PDF→text).
  *(Currently PyMuPDF is not installed.)*
- Environment confirmed: **Python 3.11.9 present**; the core resolver needs **standard library only**.

## What I'd like from you to actually run it
1. **Contact email** — OK to use `richbodo@gmail.com` as `RESOLVER_EMAIL`? (It's sent to
   OpenAlex/Unpaywall as a politeness contact, not a login.) Or give me another.
2. **Network permission** — the script makes outbound HTTPS calls to those public APIs. I run
   commands in a sandbox that may block network. Tell me whether (a) you're OK with me running it
   with network access enabled, or (b) you'd rather run the commands yourself (I'll hand you exact
   command lines).
3. **PDF text extraction** — OK for me to `pip install pymupdf` so we can `--extract` full text?
   (Without it we still get metadata + OA URLs; we just don't auto-extract text.)
4. **(Optional) Semantic Scholar API key** — only if you happen to have one; it just raises rate
   limits. Not needed for a first run.
5. **Install as a skill, or just run the script?** — Simplest start is to run `resolve.py`
   directly. If you'd like it as a reusable Claude Code skill, I can drop `SKILL.md` + the script
   into `.claude/skills/paper-resolver/`. Your call.

## Proposed first run (once you confirm the above)
1. Pull the DOIs out of the reference list we're building (`drafts/references.md`) and
   `batch`-resolve them — verify each, fetch OA PDFs where legal, flag metadata-only ones for
   manual retrieval.
2. Run topic `search`es for **2025–2026** work on remote-worker mental health, community cohesion,
   AI displacement, and telepressure — enrich the reference list with current OA papers (directly
   addressing the "corpus is out of date" gap, and likely closing the thin K5/K6 citations).

## Validation status (per claude.ai, the skill's author) + the very first test
The skill's **offline logic is already validated**: DOI normalization, OpenAlex abstract
reconstruction, field-merge precedence, SQLite round-trip, and CLI parsing all pass. What's *not*
yet confirmed is the **live network path** (the author's sandbox couldn't reach the APIs — same
constraint I have). So the first thing to run is one real DOI with an email set:
```bash
export RESOLVER_EMAIL=you@example.com
python scripts/resolve.py doi 10.1371/journal.pone.0173644 --json
```
That PLOS DOI is genuinely OA, so a `fulltext` result with a PDF URL confirms Unpaywall + OpenAlex
are responding. **I can run this for you the moment you confirm the email + network access (item 2).**

**One optional extra tier — CORE.** CORE (the largest aggregator of actual OA full text) is *not*
wired in, because its v3 API needs a **registered key**. If you want it added, get a CORE key and
say so — it's the one source in the set that needs a key, and it would lift full-text hit rates.

## Housekeeping
Files moved to `drafts/skill_experiment/`. `paper-resolver.skill` is a packaged (zip) bundle of
the same script, for installing the skill elsewhere.
