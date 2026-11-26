#!/usr/bin/env python3
"""
SKA citation verifier (Level 7 doctoral and Level 8 research-frontier material).

Every reference in an L7/L8 section must be a real, resolvable work:
  - DOI      -> checked against Crossref   (api.crossref.org)
  - arXiv ID -> checked against arXiv      (export.arxiv.org)
and the title written in the chapter must match the registry title.

A reference line looks like:
  [R3] Vaswani et al. (2017). "Attention Is All You Need". arXiv:1706.03762
  [R4] Lewis et al. (2020). "Retrieval-Augmented Generation ...". doi:10.48550/arXiv.2005.11401

Fails (exit 1) on: unresolvable id, title mismatch, or a reference with no id.
Results are cached in tools/.cite_cache.json so rebuilds do not re-query.

Usage: python3 tools/cite_check.py <file.md> [more.md ...]
"""
import json, os, re, sys, time, urllib.parse, urllib.request
from difflib import SequenceMatcher

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, ".cite_cache.json")
UA = "SKA-cite-check/1.0 (mailto:outreach@saleskingacademy.com)"

REF_LINE = re.compile(r'^\s*\[R\d+\]\s+(.*)$', re.M)
TITLE = re.compile(r'"([^"]{8,})"')
DOI = re.compile(r'(?:doi:\s*|https?://(?:dx\.)?doi\.org/)(10\.\d{4,9}/[^\s"<>]+)', re.I)
ARXIV = re.compile(r'arXiv:\s*(\d{4}\.\d{4,5}(?:v\d+)?|[a-z\-]+(?:\.[A-Z]{2})?/\d{7})', re.I)


def _get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=25) as r:
        return r.read().decode("utf-8", "replace")


def _norm(t):
    return re.sub(r'[^a-z0-9 ]', '', re.sub(r'\s+', ' ', t.lower())).strip()


def lookup_doi(doi):
    try:
        j = json.loads(_get("https://api.crossref.org/works/" + urllib.parse.quote(doi)))
        t = (j.get("message", {}).get("title") or [""])[0]
        return {"ok": bool(t), "title": t}
    except Exception as e:
        return {"ok": False, "error": str(e)[:120]}


def lookup_arxiv(aid):
    try:
        x = _get("http://export.arxiv.org/api/query?id_list=" + urllib.parse.quote(aid.split("v")[0] if re.match(r'^\d', aid) else aid))
        m = re.findall(r'<entry>.*?<title>(.*?)</title>', x, re.S)
        if not m:
            return {"ok": False, "error": "not found"}
        return {"ok": True, "title": re.sub(r'\s+', ' ', m[0]).strip()}
    except Exception as e:
        return {"ok": False, "error": str(e)[:120]}


def check_file(path, cache):
    text = open(path, encoding="utf-8").read()
    results = []
    for line in REF_LINE.findall(text):
        tm = TITLE.search(line)
        claimed = tm.group(1) if tm else ""
        d, a = DOI.search(line), ARXIV.search(line)
        if d:
            key = "doi:" + d.group(1).rstrip(".,;)").lower()
        elif a:
            key = "arxiv:" + a.group(1)
        else:
            results.append(("FAIL", line[:90], "no DOI or arXiv id"))
            continue
        if key not in cache:
            cache[key] = lookup_doi(key[4:]) if key.startswith("doi:") else lookup_arxiv(key[6:])
            time.sleep(0.4)
        rec = cache[key]
        if not rec.get("ok"):
            results.append(("FAIL", key, "does not resolve: " + rec.get("error", "")))
            continue
        sim = SequenceMatcher(None, _norm(claimed), _norm(rec["title"])).ratio() if claimed else 0
        if sim < 0.85:
            results.append(("FAIL", key, "title mismatch (%.2f): registry says '%s'" % (sim, rec["title"][:80])))
        else:
            results.append(("PASS", key, rec["title"][:80]))
    return results


def main(paths):
    cache = json.load(open(CACHE)) if os.path.exists(CACHE) else {}
    bad = 0
    for p in paths:
        res = check_file(p, cache)
        print("==", p, "-", len(res), "references")
        for status, key, msg in res:
            print("  %s  %-34s %s" % (status, key, msg))
            bad += status == "FAIL"
    json.dump(cache, open(CACHE, "w"), indent=1, sort_keys=True)
    print("RESULT:", "FAIL (%d)" % bad if bad else "PASS")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]) if len(sys.argv) > 1 else 2)
