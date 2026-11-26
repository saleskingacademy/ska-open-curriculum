#!/usr/bin/env python3
"""Shape check for dictionary/words/*.json: every shard parses, every word has a unique
identifier, every definition has a part of speech, text and source."""
import glob, json, sys

seen, words, senses, bad = set(), 0, 0, []
for p in sorted(glob.glob("dictionary/words/*.json")):
    try:
        d = json.load(open(p, encoding="utf-8"))
    except Exception as e:
        bad.append("%s: %s" % (p, e)); continue
    for w, e in d.items():
        words += 1
        i = e.get("dna16")
        if not i or i in seen: bad.append("%s: %r missing or duplicate identifier" % (p, w))
        seen.add(i)
        for s in e.get("senses", []):
            senses += 1
            if not s.get("pos") or not s.get("src") or "def" not in s: bad.append("%s: %r sense incomplete" % (p, w))
            sid = s.get("dna16")
            if sid:
                if sid in seen: bad.append("%s: %r duplicate sense identifier" % (p, w))
                seen.add(sid)
print("words %d, definitions %d, problems %d" % (words, senses, len(bad)))
for b in bad[:50]: print(b)
sys.exit(1 if bad else 0)
