#!/usr/bin/env python3
"""
Tiered open-access paper resolver.

Given a DOI, a title, or a search query, this resolves the richest metadata it
can plus a *legal* full-text URL where one exists, by walking a tier of open
scholarly infrastructure:

    metadata : OpenAlex (primary)  -> Crossref / Semantic Scholar (fill gaps)
    fulltext : Unpaywall -> OpenAlex best_oa -> Semantic Scholar openAccessPdf
               -> Europe PMC (OA subset) -> Crossref TDM links (flagged)

Anything with no legal full text is recorded as `metadata_only` and written to
an `unresolved.jsonl` queue for manual follow-up, rather than the tool trying to
route around a paywall. The resolver only ever touches openly licensed copies.

All state lives in a single SQLite file (the cache *and* the corpus index), so
re-running is cheap and the result is a portable, local-first artifact.

This module is import-safe: the resolution functions can be lifted wholesale
into a FastMCP server later without modification.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone

USER_AGENT = "paper-resolver/1.0 (mailto:{email}; local-first OA resolver)"
# Some publishers (ACM, Wiley, SAGE, MDPI, Elsevier) reject non-browser User-Agents when serving
# their open-access PDFs. Metadata calls keep the polite UA; the PDF download uses a browser UA.
BROWSER_UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")
TIMEOUT = 30


# --------------------------------------------------------------------------- #
# HTTP helper with polite backoff
# --------------------------------------------------------------------------- #
def http_get(url, params=None, headers=None, email=None, retries=4, sleep=0.2):
    """GET JSON with exponential backoff on 429 / 5xx. Returns dict or None."""
    if params:
        url = url + ("&" if "?" in url else "?") + urllib.parse.urlencode(params)
    hdrs = {"User-Agent": USER_AGENT.format(email=email or "anonymous")}
    if headers:
        hdrs.update(headers)

    delay = 1.0
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=hdrs)
            with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                time.sleep(sleep)  # be polite between successful calls
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504) and attempt < retries - 1:
                # honour Retry-After if present, else exponential backoff
                wait = float(e.headers.get("Retry-After", delay))
                time.sleep(wait)
                delay *= 2
                continue
            if e.code == 404:
                return None
            return None
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
            if attempt < retries - 1:
                time.sleep(delay)
                delay *= 2
                continue
            return None
    return None


def normalize_doi(raw):
    """Strip URL prefixes / casing so the same paper always keys the same."""
    if not raw:
        return None
    doi = raw.strip()
    doi = re.sub(r"^https?://(dx\.)?doi\.org/", "", doi, flags=re.I)
    doi = re.sub(r"^doi:", "", doi, flags=re.I)
    return doi.lower() or None


# --------------------------------------------------------------------------- #
# Source adapters — each returns a partial record dict (or None)
# --------------------------------------------------------------------------- #
def reconstruct_abstract(inverted_index):
    """OpenAlex stores abstracts as {word: [positions]}. Rebuild the prose."""
    if not inverted_index:
        return None
    positioned = []
    for word, positions in inverted_index.items():
        for pos in positions:
            positioned.append((pos, word))
    positioned.sort()
    return " ".join(word for _, word in positioned) or None


def from_openalex(doi, email, sleep):
    data = http_get(f"https://api.openalex.org/works/doi:{doi}",
                    params={"mailto": email} if email else None,
                    email=email, sleep=sleep)
    if not data:
        return {}
    best = data.get("best_oa_location") or {}
    return {
        "title": data.get("title"),
        "year": data.get("publication_year"),
        "venue": ((data.get("primary_location") or {}).get("source") or {}).get("display_name")
                 if data.get("primary_location") else None,
        "authors": [a["author"]["display_name"]
                    for a in data.get("authorships", []) if a.get("author")],
        "abstract": reconstruct_abstract(data.get("abstract_inverted_index")),
        "is_oa": (data.get("open_access") or {}).get("is_oa"),
        "oa_status": (data.get("open_access") or {}).get("oa_status"),
        "pdf_url": best.get("pdf_url"),
        "full_text_url": best.get("landing_page_url") or best.get("pdf_url"),
        "license": best.get("license"),
        "_meta_src": "openalex",
    }


def from_unpaywall(doi, email, sleep):
    if not email:
        return {}  # Unpaywall mandates an email parameter
    data = http_get(f"https://api.unpaywall.org/v2/{doi}",
                    params={"email": email}, email=email, sleep=sleep)
    if not data:
        return {}
    best = data.get("best_oa_location") or {}
    return {
        "title": data.get("title"),
        "year": data.get("year"),
        "venue": data.get("journal_name"),
        "is_oa": data.get("is_oa"),
        "oa_status": data.get("oa_status"),
        "pdf_url": best.get("url_for_pdf"),
        "full_text_url": best.get("url"),
        "license": best.get("license"),
        "_meta_src": "unpaywall",
    }


def from_semanticscholar(doi, api_key, sleep):
    headers = {"x-api-key": api_key} if api_key else None
    fields = "title,abstract,year,venue,authors,openAccessPdf,isOpenAccess"
    data = http_get(f"https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}",
                    params={"fields": fields}, headers=headers, sleep=sleep)
    if not data:
        return {}
    oa = data.get("openAccessPdf") or {}
    return {
        "title": data.get("title"),
        "year": data.get("year"),
        "venue": data.get("venue"),
        "authors": [a.get("name") for a in data.get("authors", []) if a.get("name")],
        "abstract": data.get("abstract"),
        "is_oa": data.get("isOpenAccess"),
        "pdf_url": oa.get("url"),
        "full_text_url": oa.get("url"),
        "_meta_src": "semanticscholar",
    }


def from_europepmc(doi, sleep):
    q = http_get("https://www.ebi.ac.uk/europepmc/webservices/rest/search",
                 params={"query": f'DOI:"{doi}"', "format": "json",
                         "resultType": "core"}, sleep=sleep)
    if not q:
        return {}
    hits = (q.get("resultList") or {}).get("result", [])
    if not hits:
        return {}
    r = hits[0]
    out = {
        "title": r.get("title"),
        "year": int(r["pubYear"]) if r.get("pubYear", "").isdigit() else None,
        "venue": r.get("journalTitle"),
        "abstract": r.get("abstractText"),
        "is_oa": r.get("isOpenAccess") == "Y",
        "_meta_src": "europepmc",
    }
    # Machine-readable full text exists only for the OA subset.
    if r.get("isOpenAccess") == "Y" and r.get("source") and r.get("id"):
        out["full_text_url"] = (
            f"https://www.ebi.ac.uk/europepmc/webservices/rest/"
            f"{r['source']}/{r['id']}/fullTextXML"
        )
    return out


def from_crossref(doi, email, sleep):
    data = http_get(f"https://api.crossref.org/works/{urllib.parse.quote(doi)}",
                    params={"mailto": email} if email else None,
                    email=email, sleep=sleep)
    if not data:
        return {}
    msg = data.get("message") or {}
    authors = []
    for a in msg.get("author", []):
        name = " ".join(p for p in [a.get("given"), a.get("family")] if p)
        if name:
            authors.append(name)
    # Crossref `link` entries flagged for text-mining — may need entitlement,
    # so we surface them but never present them as confirmed OA.
    tdm = [l["URL"] for l in msg.get("link", [])
           if l.get("intended-application") == "text-mining" and l.get("URL")]
    title = msg.get("title") or []
    return {
        "title": title[0] if title else None,
        "year": (msg.get("issued", {}).get("date-parts", [[None]])[0][0]),
        "venue": (msg.get("container-title") or [None])[0],
        "authors": authors,
        "tdm_links": tdm,
        "_meta_src": "crossref",
    }


# --------------------------------------------------------------------------- #
# Orchestration
# --------------------------------------------------------------------------- #
def merge(base, extra):
    """Fill empty fields in base from extra; never overwrite a real value."""
    for k, v in extra.items():
        if k.startswith("_"):
            continue
        if v in (None, "", [], False) and k != "is_oa":
            continue
        if not base.get(k):
            base[k] = v
    return base


def resolve_doi(doi, email=None, s2_key=None, sleep=0.2):
    """Walk the tiers and assemble one record. Pure: no DB, no disk."""
    doi = normalize_doi(doi)
    if not doi:
        return None

    record = {"doi": doi, "authors": [], "tdm_links": [],
              "resolved_at": datetime.now(timezone.utc).isoformat()}

    # Metadata + first OA shot from OpenAlex (richest single source).
    oa = from_openalex(doi, email, sleep)
    record = merge(record, oa)

    # Unpaywall is the most reliable locator for a legal PDF.
    if not record.get("pdf_url"):
        record = merge(record, from_unpaywall(doi, email, sleep))

    # Semantic Scholar fills abstract gaps and sometimes has its own OA PDF.
    if not record.get("abstract") or not record.get("pdf_url"):
        record = merge(record, from_semanticscholar(doi, s2_key, sleep))

    # Europe PMC for the (often health-adjacent) OA full-text subset.
    if not record.get("full_text_url"):
        record = merge(record, from_europepmc(doi, sleep))

    # Crossref last: authoritative metadata + any text-mining links.
    record = merge(record, from_crossref(doi, email, sleep))

    has_fulltext = bool(record.get("pdf_url") or record.get("full_text_url"))
    record["status"] = "fulltext" if has_fulltext else "metadata_only"
    record["source_tier"] = record.pop("_meta_src", None)
    return record


def search_works(query, email, limit, sleep, from_year=None):
    """OpenAlex relevance search -> list of DOIs + light metadata."""
    params = {"search": query, "per_page": min(limit, 200)}
    if email:
        params["mailto"] = email
    if from_year:
        params["filter"] = f"from_publication_date:{from_year}-01-01"
    data = http_get("https://api.openalex.org/works", params=params,
                    email=email, sleep=sleep)
    out = []
    for w in (data or {}).get("results", [])[:limit]:
        out.append({
            "doi": normalize_doi(w.get("doi")),
            "title": w.get("title"),
            "year": w.get("publication_year"),
            "is_oa": (w.get("open_access") or {}).get("is_oa"),
        })
    return out


# --------------------------------------------------------------------------- #
# SQLite cache / corpus index
# --------------------------------------------------------------------------- #
def init_db(path):
    con = sqlite3.connect(path)
    con.execute("""CREATE TABLE IF NOT EXISTS papers (
        doi TEXT PRIMARY KEY, title TEXT, year INTEGER, venue TEXT,
        authors TEXT, abstract TEXT, is_oa INTEGER, oa_status TEXT,
        pdf_url TEXT, full_text_url TEXT, license TEXT, status TEXT,
        source_tier TEXT, pdf_path TEXT, text_path TEXT,
        record_json TEXT, resolved_at TEXT)""")
    con.commit()
    return con


def cache_get(con, doi):
    row = con.execute("SELECT record_json FROM papers WHERE doi=?", (doi,)).fetchone()
    return json.loads(row[0]) if row else None


def cache_put(con, rec):
    con.execute("""INSERT OR REPLACE INTO papers
        (doi,title,year,venue,authors,abstract,is_oa,oa_status,pdf_url,
         full_text_url,license,status,source_tier,pdf_path,text_path,
         record_json,resolved_at)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
        (rec.get("doi"), rec.get("title"), rec.get("year"), rec.get("venue"),
         json.dumps(rec.get("authors", [])), rec.get("abstract"),
         1 if rec.get("is_oa") else 0, rec.get("oa_status"), rec.get("pdf_url"),
         rec.get("full_text_url"), rec.get("license"), rec.get("status"),
         rec.get("source_tier"), rec.get("pdf_path"), rec.get("text_path"),
         json.dumps(rec), rec.get("resolved_at")))
    con.commit()


# --------------------------------------------------------------------------- #
# Optional download + text extraction
# --------------------------------------------------------------------------- #
def download_pdf(url, dest_dir, doi):
    os.makedirs(dest_dir, exist_ok=True)
    fname = re.sub(r"[^\w.-]", "_", doi) + ".pdf"
    dest = os.path.join(dest_dir, fname)
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": BROWSER_UA,
            "Accept": "application/pdf,*/*",
        })
        with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
            data = r.read()
        # Guard: a blocked/landing page often returns HTML with HTTP 200 — only keep real PDFs.
        if b"%PDF" not in data[:1024]:
            return None
        with open(dest, "wb") as f:
            f.write(data)
        return dest
    except Exception:
        return None


def extract_text(pdf_path):
    """Best-effort text extraction. Degrades gracefully if no PDF lib present."""
    try:
        import fitz  # PyMuPDF
    except ImportError:
        return None
    try:
        doc = fitz.open(pdf_path)
        text = "\n".join(page.get_text() for page in doc)
        out = pdf_path.rsplit(".", 1)[0] + ".txt"
        with open(out, "w", encoding="utf-8") as f:
            f.write(text)
        return out
    except Exception:
        return None


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def handle_record(rec, con, args):
    if rec.get("status") == "fulltext" and args.download:
        url = rec.get("pdf_url") or rec.get("full_text_url")
        if url:
            pdf = download_pdf(url, args.out, rec["doi"])
            rec["pdf_path"] = pdf
            if pdf and args.extract:
                rec["text_path"] = extract_text(pdf)
    cache_put(con, rec)
    if rec.get("status") == "metadata_only":
        with open(os.path.join(os.path.dirname(args.db) or ".", "unresolved.jsonl"),
                  "a", encoding="utf-8") as f:
            f.write(json.dumps({"doi": rec["doi"], "title": rec.get("title")}) + "\n")
    return rec


def main():
    p = argparse.ArgumentParser(description="Tiered open-access paper resolver.")
    p.add_argument("--db", default="resolver.db", help="SQLite cache/corpus path")
    p.add_argument("--email", default=os.environ.get("RESOLVER_EMAIL"),
                   help="Contact email (OpenAlex polite pool + required by Unpaywall)")
    p.add_argument("--s2-key", default=os.environ.get("S2_API_KEY"),
                   help="Optional Semantic Scholar API key (higher rate limits)")
    p.add_argument("--sleep", type=float, default=0.2, help="Politeness delay between calls")
    p.add_argument("--download", action="store_true", help="Download OA PDFs")
    p.add_argument("--extract", action="store_true", help="Extract text (needs PyMuPDF)")
    p.add_argument("--out", default="./corpus", help="Directory for downloaded files")
    p.add_argument("--refresh", action="store_true", help="Ignore cache, re-resolve")
    p.add_argument("--json", action="store_true", help="Print full JSON records")

    sub = p.add_subparsers(dest="cmd", required=True)
    d = sub.add_parser("doi", help="Resolve a single DOI")
    d.add_argument("doi")
    b = sub.add_parser("batch", help="Resolve a file of DOIs (one per line)")
    b.add_argument("file")
    s = sub.add_parser("search", help="Search OpenAlex and resolve the hits")
    s.add_argument("query")
    s.add_argument("--limit", type=int, default=20)
    s.add_argument("--from-year", type=int, default=None,
                   help="Only return results published on/after this year (e.g. 2024)")

    args = p.parse_args()
    con = init_db(args.db)

    if not args.email:
        sys.stderr.write("warning: no --email/RESOLVER_EMAIL; Unpaywall will be "
                         "skipped and OpenAlex calls won't use the polite pool.\n")

    def resolve_one(doi):
        doi = normalize_doi(doi)
        if not doi:
            return None
        if not args.refresh:
            cached = cache_get(con, doi)
            if cached:
                return cached
        rec = resolve_doi(doi, args.email, args.s2_key, args.sleep)
        return handle_record(rec, con, args) if rec else None

    results = []
    if args.cmd == "doi":
        results = [resolve_one(args.doi)]
    elif args.cmd == "batch":
        with open(args.file, encoding="utf-8") as f:
            dois = [ln.strip() for ln in f if ln.strip() and not ln.startswith("#")]
        for i, doi in enumerate(dois, 1):
            sys.stderr.write(f"[{i}/{len(dois)}] {doi}\n")
            results.append(resolve_one(doi))
    elif args.cmd == "search":
        hits = search_works(args.query, args.email, args.limit, args.sleep, args.from_year)
        for i, h in enumerate(hits, 1):
            if not h["doi"]:
                continue
            sys.stderr.write(f"[{i}/{len(hits)}] {h['title']}\n")
            results.append(resolve_one(h["doi"]))

    results = [r for r in results if r]
    full = sum(1 for r in results if r.get("status") == "fulltext")
    meta = sum(1 for r in results if r.get("status") == "metadata_only")

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        for r in results:
            flag = "OA" if r.get("status") == "fulltext" else "  "
            print(f"[{flag}] {r.get('year') or '????'}  {r.get('title') or r['doi']}")
            if r.get("status") == "fulltext":
                print(f"       -> {r.get('pdf_url') or r.get('full_text_url')}")
    sys.stderr.write(f"\nresolved {len(results)}: {full} full-text, {meta} metadata-only.\n")
    sys.stderr.write(f"corpus db: {args.db}\n")


if __name__ == "__main__":
    main()
