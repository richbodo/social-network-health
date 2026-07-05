#!/usr/bin/env python3
"""Capture DWeb Camp deck screenshots from PRM against a throwaway demo home.

Adapted from prm/scripts/capture_screenshots.py (prm#91 anti-rot harness).
Adds: takeout-basic ingest (Alan Turing), Turing headshot via /api/set-photo,
cloud AI access enabled via /api/disclosure/consent, then two shots:
contacts view on Turing + External Access view with AI on.
"""
from __future__ import annotations

import base64
import json
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path

REPO = Path("/Users/rsb/src/prm")
sys.path.insert(0, str(REPO))

OUT = Path("/Users/rsb/src/social-network-health/presentations/dwebcamp-berlin-2026/public/screenshots")
TURING_JPG = Path("/Users/rsb/src/social-network-health/presentations/dwebcamp-berlin-2026/public/alan-turing.jpg")
PYTHON = sys.executable
VIEWPORT = {"width": 1440, "height": 900}
JPEG_QUALITY = 82
PORT = 8788


def sh(env, *args):
    subprocess.run([PYTHON, *args], env=env, check=True, cwd=REPO,
                   stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="prm-deck-shots-") as tmp:
        home = Path(tmp) / "home"
        env = {**os.environ, "PRM_HOME": str(home)}
        print("seeding throwaway demo home …")
        sh(env, "-m", "cli", "init", "--demo")
        print("ingesting takeout-basic (Alan Turing fixture) …")
        sh(env, "-m", "cli", "import", str(REPO / "tests/fixtures/google_takeout/sources/takeout-basic"))

        os.environ["PRM_HOME"] = str(home)
        from cli.config import resolve_home
        from daemon.server import route
        h = resolve_home(None)

        def get(path, query=None):
            code, _, body = route("GET", path, query or {}, h)
            assert code == 200, (path, code, body)
            return json.loads(body)

        def post(path, body):
            code, _, resp = route("POST", path, {}, h, body)
            assert code == 200, (path, code, resp)
            return json.loads(resp)

        results = get("/api/search", {"q": ["alan turing"], "limit": ["100"]})["results"]
        print("search hits:", [r["name"] for r in results])
        turing = next(r["id"] for r in results if r["name"] == "Alan Turing")

        print("attaching headshot …")
        post("/api/set-photo", {
            "contact_id": turing,
            "data_base64": base64.b64encode(TURING_JPG.read_bytes()).decode(),
            "mime": "image/jpeg",
        })

        print("enabling cloud AI access (EX-CLOUD-LLM) …")
        post("/api/disclosure/consent", {"mode": "cloud-exception"})

        print("starting server …")
        proc = subprocess.Popen([PYTHON, "-m", "cli", "serve", "--port", str(PORT)],
                                env=env, cwd=REPO,
                                stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        try:
            url_file = home / "workspace.url"
            for _ in range(80):
                if url_file.exists() and url_file.read_text().strip():
                    break
                if proc.poll() is not None:
                    raise SystemExit("server exited early — port in use?")
                time.sleep(0.25)
            session_url = url_file.read_text().strip()
            base = session_url.split("?")[0].rstrip("/")

            from playwright.sync_api import sync_playwright
            with sync_playwright() as pw:
                browser = pw.chromium.launch()
                page = browser.new_page(viewport=VIEWPORT)
                page.goto(session_url)
                page.wait_for_selector(".row", timeout=15000)

                page.goto(f"{base}/#/contacts/{turing}")
                page.wait_for_selector(".kv", timeout=15000)
                page.wait_for_timeout(700)
                page.screenshot(path=str(OUT / "prm-contact-turing.jpg"), type="jpeg", quality=JPEG_QUALITY)
                print("shot: prm-contact-turing.jpg")

                page.goto(f"{base}/#/access")
                page.wait_for_selector(".axcard", timeout=15000)
                page.wait_for_timeout(700)
                page.screenshot(path=str(OUT / "prm-access-ai-on.jpg"), type="jpeg", quality=JPEG_QUALITY)
                print("shot: prm-access-ai-on.jpg")

                browser.close()
        finally:
            proc.terminate()
            proc.wait(timeout=10)
    print("done →", OUT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
