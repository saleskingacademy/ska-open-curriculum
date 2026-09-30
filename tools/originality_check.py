"""Originality gate: SKA material must be original. Reference textbooks are read for scope and
level only; their wording must never be copied or closely paraphrased.
Usage: python3 tools/originality_check.py <subject.md> <reference.txt> [more references...]
Fails if any run of 12+ consecutive words is shared with a reference, or if more than 2% of the
subject's 8-word sequences also appear in a reference. Reference files stay local (refs/ is
gitignored) and are never committed or published."""
import re, sys, json
def words(t): return re.findall(r"[a-z0-9']+", t.lower())
def grams(w, n): return {" ".join(w[i:i+n]) for i in range(len(w) - n + 1)}
def check(subject_text, ref_texts):
    sw = words(subject_text); s8 = grams(sw, 8); r8 = set(); r12 = set()
    for r in ref_texts:
        rw = words(r); r8 |= grams(rw, 8); r12 |= grams(rw, 12)
    shared12 = sorted(grams(sw, 12) & r12)
    ratio = len(s8 & r8) / max(1, len(s8))
    return {"shared_12_word_runs": len(shared12), "examples": shared12[:3],
            "overlap_8gram_pct": round(ratio * 100, 2),
            "original": not shared12 and ratio <= 0.02}
if __name__ == "__main__":
    subj = open(sys.argv[1], encoding="utf-8").read()
    refs = [open(p, encoding="utf-8", errors="ignore").read() for p in sys.argv[2:]]
    out = check(subj, refs); print(json.dumps(out)); sys.exit(0 if out["original"] else 1)
