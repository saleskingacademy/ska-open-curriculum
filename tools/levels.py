#!/usr/bin/env python3
"""Adds the 8-level ladder (TEXTBOOK_STANDARD.md section 5; L8 = postdoctoral research frontier) to every real subject
in map/real_subjects.json and totals the words each level needs. Run after real_subjects.py."""
import json, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VOLUMES = [
 {"volume": "Textbook", "levels": [1,2,3,4], "isced": "2-3 to 6 (secondary to bachelor)", "min_words": None},
 {"volume": "Graduate", "levels": [5,6], "isced": "7 (master's, professional)", "min_words": 60000},
 {"volume": "Doctoral", "levels": [7], "isced": "8 (doctoral)", "min_words": 40000},
 {"volume": "Research Frontier", "levels": [8], "isced": "beyond 8 (postdoctoral research)", "min_words": 15000},
]
p = os.path.join(ROOT, "map/real_subjects.json"); d = json.load(open(p))
tot = {v["volume"]: 0 for v in VOLUMES}
for b in d["books"]:
    vols = []
    for v in VOLUMES:
        w = b["words_target"] if v["min_words"] is None else v["min_words"]
        have = b["words_now"] if v["volume"] == "Textbook" else 0
        vols.append({"volume": v["volume"], "levels": v["levels"], "isced": v["isced"],
                     "words_target": w, "words_now": have, "words_needed": max(0, w - have)})
        tot[v["volume"]] += max(0, w - have)
    b["volumes"] = vols
d["levels"] = {"ladder": VOLUMES, "words_needed_by_volume": tot, "words_needed_total": sum(tot.values())}
json.dump(d, open(p, "w"), indent=1, ensure_ascii=False)
print(json.dumps(d["levels"]["words_needed_by_volume"], indent=1), "total", sum(tot.values()))
