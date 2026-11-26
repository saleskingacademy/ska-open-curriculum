"""knowledge/depth.json: one teaching-depth band per subject for the course catalogue badges.
Bands match the site legend: 1 placeholder, 2 outline, 3 taught, 4 deeply taught (by body length)."""
import json
paths = json.load(open("knowledge/paths.json")); out = {}
for k, rel in paths.items():
    try: t = open(rel, encoding="utf-8").read()
    except OSError: continue
    body = t.split("\n---\n", 1)[-1] if t.startswith("---") else t
    n = len(body.encode("utf-8"))
    out[k] = 4 if n >= 6000 else 3 if n >= 1500 else 2 if n >= 500 else 1
json.dump(out, open("knowledge/depth.json", "w"), separators=(",", ":"), sort_keys=True)
print(len(out), "subjects;", {b: sum(1 for v in out.values() if v == b) for b in (1, 2, 3, 4)})
