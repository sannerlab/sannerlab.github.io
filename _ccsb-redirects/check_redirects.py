#!/usr/bin/env python3
"""Check the ccsb.scripps.edu -> sannerlab.github.io redirects.

    python3 check_redirects.py           # rules and targets (run any time)
    python3 check_redirects.py --live    # also ask ccsb.scripps.edu (after the rules are deployed)

1. Replays ccsb-redirects.conf in Apache's first-match order and checks that every old path in
   redirects.tsv (and a sample path under each catch-all) ends at its intended new URL.
2. Checks that every new URL answers 200 and, for '#anchor' targets, that the anchor is on the page.
3. --live: requests each old path on https://ccsb.scripps.edu without following redirects and
   checks for a 301 to the intended new URL.
Exit status is the number of problems found.
"""
import csv, re, sys, urllib.error, urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
OLD_HOST = "https://ccsb.scripps.edu"
rows = list(csv.DictReader(open(HERE / "redirects.tsv"), delimiter="\t"))
rules = []  # (compiled regex, target or None for pass-through)
for line in open(HERE / "ccsb-redirects.conf"):
    m = re.match(r'RewriteRule\s+"?(\S+?)"?\s+"?(\S+?)"?\s+\[', line)
    if m:
        rules.append((re.compile(m.group(1)), None if m.group(2) == "-" else m.group(2)))

problems = 0
def bad(msg):
    global problems
    problems += 1
    print("PROBLEM", msg)

def first_match(path):
    for rx, target in rules:
        if rx.search(path):
            return target
    return "(no rule)"

# 1. first-match replay
for r in rows:
    path = r["old_path"]
    samples = [path[:-1] + "some/other/page/", path[:-2]] if path.endswith("/*") else [path, path.rstrip("/")]
    for p in samples:
        got = first_match(p)
        if got != r["new_url"]:
            bad(f"{p} -> {got}, expected {r['new_url']}")
print(f"rules: {len(rules)}, rows: {len(rows)}, first-match replay done")

# 2. targets exist (and anchors are on their pages)
def fetch(url, nbytes=None):
    req = urllib.request.Request(url, headers={"User-Agent": "check_redirects"})
    if nbytes:
        req.add_header("Range", f"bytes=0-{nbytes - 1}")
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.status, resp.read() if not nbytes else b""

pages = {}
for url in sorted({r["new_url"] for r in rows}):
    base, _, anchor = url.partition("#")
    try:
        if "/releases/download/" in base:
            status, _ = fetch(base, nbytes=1)
            ok = status in (200, 206)
        else:
            if base not in pages:
                pages[base] = fetch(base)
            status, body = pages[base]
            ok = status == 200 and (not anchor or f'id="{anchor}"'.encode() in body)
        if not ok:
            bad(f"target {url}: status {status}" + (f", anchor #{anchor} missing" if anchor else ""))
    except urllib.error.HTTPError as e:
        bad(f"target {url}: HTTP {e.code}")
print(f"targets checked: {len({r['new_url'] for r in rows})}")

# 3. live check of the deployed rules
if "--live" in sys.argv:
    class NoRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, *args, **kwargs):
            return None
    opener = urllib.request.build_opener(NoRedirect)
    for r in rows:
        path = r["old_path"][:-1] + "some/other/page/" if r["old_path"].endswith("/*") else r["old_path"]
        try:
            opener.open(urllib.request.Request(OLD_HOST + path, method="HEAD"), timeout=60)
            bad(f"live {path}: no redirect")
        except urllib.error.HTTPError as e:
            loc = e.headers.get("Location", "")
            if e.code != 301 or loc != r["new_url"]:
                bad(f"live {path}: HTTP {e.code} -> {loc or '-'}, expected 301 -> {r['new_url']}")
    print("live check done")

print(f"{problems} problem(s)")
sys.exit(min(problems, 255))
