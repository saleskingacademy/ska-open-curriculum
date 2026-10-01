#!/usr/bin/env python3
"""Research Frontier layer (Level 8, postdoctoral) - verified literature map per real subject.

Pulls real, citable works from OpenAlex (open scholarly index, metadata only: title, authors,
year, venue, DOI, citation count, open-access link). No paper text is copied. Every entry is a
work that exists and resolves by DOI, so SKA frontier chapters can cite only verified sources.

Two lanes per subject:
  reviews  - review articles since 2021, most cited first (where the field summarises itself)
  frontier - research articles since 2024, most cited first (where the field is moving now)
A relevance guard keeps only works whose title contains a core term of the subject.
Subjects with too few relevant works are flagged needs_curation (query terms need tuning).
"""
import json, re, sys, time, urllib.parse, urllib.request, urllib.error, datetime, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAIL = "outreach@saleskingacademy.com"
STOP = set("and or of the for in to a an with on at by from its their your business management "
           "principles introduction fundamentals applied advanced general studies systems theory "
           "practice skills technology integration".split())
SEL = "id,doi,title,publication_year,cited_by_count,primary_location,authorships,open_access,type"

def core_terms(title):
    words = [w for w in re.findall(r"[a-z][a-z\-]+", title.lower()) if w not in STOP and len(w) > 3]
    return words or re.findall(r"[a-z]+", title.lower())

def fetch(query, date_from, wtype, n=15):
    flt = f"title_and_abstract.search:{query},from_publication_date:{date_from},type:{wtype},cited_by_count:>4"
    url = ("https://api.openalex.org/works?" + urllib.parse.urlencode(
        {"filter": flt, "sort": "cited_by_count:desc", "per-page": n, "select": SEL, "mailto": MAIL}))
    for attempt in range(4):
        try:
            with urllib.request.urlopen(url, timeout=40) as r:
                return json.load(r).get("results", [])
        except Exception as e:
            time.sleep(2 * (attempt + 1))
    return []

def slim(w):
    src = ((w.get("primary_location") or {}).get("source") or {}).get("display_name")
    auth = [a["author"]["display_name"] for a in (w.get("authorships") or [])[:3] if a.get("author")]
    return {"title": w.get("title"), "authors": auth, "et_al": len(w.get("authorships") or []) > 3,
            "year": w.get("publication_year"), "venue": src, "doi": w.get("doi"),
            "cited_by": w.get("cited_by_count"), "open_access_url": (w.get("open_access") or {}).get("oa_url"),
            "openalex": w.get("id")}

class Unavailable(Exception): pass

def api(params):
    key = os.environ.get("OPENALEX_API_KEY")
    q = dict(params, mailto=MAIL, **({"api_key": key} if key else {}))
    url = "https://api.openalex.org/works?" + urllib.parse.urlencode(q)
    for attempt in range(6):
        try:
            with urllib.request.urlopen(url, timeout=40) as r:
                return json.load(r).get("results", [])
        except urllib.error.HTTPError as e:
            wait = 5
            try: wait = int(json.loads(e.read()).get("retryAfter", 5)) + 1
            except Exception: pass
            time.sleep(min(wait, 60))
        except Exception:
            time.sleep(3 * (attempt + 1))
    raise Unavailable("OpenAlex unavailable (rate limit) - result NOT written")

def home_subfields(q):
    """Where does the literature on this subject actually live? Take the 50 most relevant works
    and tally their primary topic's subfield; keep the subfields that hold most of them."""
    rows = api({"search": q, "per-page": 50, "select": "primary_topic"})
    tally = {}
    for w in rows:
        sf = ((w.get("primary_topic") or {}).get("subfield") or {})
        if sf.get("id"):
            k = sf["id"].split("/")[-1]; tally[k] = tally.get(k, 0) + 1; NAMES[k] = sf.get("display_name")
    ranked = sorted(tally.items(), key=lambda x: -x[1])
    keep, total = [], sum(tally.values()) or 1
    for sid, n in ranked:
        if n / total >= 0.12 or not keep: keep.append(sid)
        if len(keep) == 3: break
    return keep

NAMES = {}
QUERY = {}  # curated overrides: subject id -> search terms (tools/frontier_queries.json)

def build(book):
    terms = core_terms(book["title"])
    q = QUERY.get(book["id"]) or " ".join(terms[:4])
    subs = home_subfields(q)
    out = {}
    for lane, since, wtype in (("reviews", "2021-01-01", "review"), ("frontier", "2024-01-01", "article")):
        flt = (f"title_and_abstract.search:{q},from_publication_date:{since},type:{wtype},cited_by_count:>4"
               + (",primary_topic.subfield.id:" + "|".join(subs) if subs else ""))
        rows = api({"filter": flt, "sort": "cited_by_count:desc", "per-page": 12, "select": SEL})
        out[lane] = [slim(w) for w in rows if w.get("doi")][:10]
    n = len(out["reviews"]) + len(out["frontier"])
    return {"id": book["id"], "title": book["title"], "field": book["field"], "query": q, "subfields": [{"id": x, "name": NAMES.get(x)} for x in subs],
            "built": datetime.date.today().isoformat(), "status": "ok" if n >= 8 else "needs_curation",
            "reviews": out["reviews"], "frontier": out["frontier"]}

def main():
    qf = os.path.join(ROOT, "tools/frontier_queries.json")
    if os.path.exists(qf): QUERY.update(json.load(open(qf)))
    books = json.load(open(os.path.join(ROOT, "map/real_subjects.json")))["books"]
    only = set(sys.argv[1:])
    from concurrent.futures import ThreadPoolExecutor
    todo = [b for b in books if not only or b["id"] in only]
    summary = []
    def one(b):
        try: rec = build(b)
        except Unavailable:
            print(f"skipped (rate limited)  {b['title']}", flush=True)
            return (b["field"], b["title"], b["id"], "not_built", 0, 0)
        json.dump(rec, open(os.path.join(ROOT, "frontier", b["id"] + ".json"), "w"), indent=1, ensure_ascii=False)
        print(f"{rec['status']:14} r={len(rec['reviews']):2} f={len(rec['frontier']):2}  {b['title']}", flush=True)
        return (b["field"], b["title"], b["id"], rec["status"], len(rec["reviews"]), len(rec["frontier"]))
    with ThreadPoolExecutor(max_workers=int(os.environ.get('FRONTIER_WORKERS', '1'))) as ex:
        summary = list(ex.map(one, todo))
    summary = []
    import glob
    for f in glob.glob(os.path.join(ROOT, "frontier", "*.json")):
        r = json.load(open(f))
        summary.append((r["field"], r["title"], r["id"], r["status"], len(r["reviews"]), len(r["frontier"])))
    if True:
        ok = sum(1 for s in summary if s[3] == "ok")
        L = ["# SKA Research Frontier (Level 8 - postdoctoral)", "",
             "Verified literature map for every real subject, built from the OpenAlex scholarly index by",
             "`tools/frontier.py`. Metadata only (title, authors, year, venue, DOI, citations); no paper text.",
             "Every work resolves by DOI, so frontier chapters cite only sources that exist.", "",
             f"Updated {datetime.date.today().isoformat()}. {len(summary)} of {len(books)} subjects built; {ok} ok, the rest need curated search terms.", "",
             "| Field | Subject | Status | Reviews | Frontier |", "|---|---|---|---|---|"]
        for f, t, i, st, r, fr in sorted(summary):
            L.append(f"| {f} | [{t}](frontier/{i}.json) | {st} | {r} | {fr} |")
        L += ["", "Copyright (c) 2026 Sales King Academy LLC. All rights reserved. Bibliographic metadata from OpenAlex (CC0)."]
        open(os.path.join(ROOT, "FRONTIER.md"), "w").write("\n".join(L) + "\n")

if __name__ == "__main__":
    main()
