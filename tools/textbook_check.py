"""Score subject material against the SKA textbook standard (TEXTBOOK_STANDARD.md).
Usage: python3 tools/textbook_check.py [file.md ...]   (no args = all knowledge/**/*.md)"""
import re, sys, glob, json
STD = {"words": 30000, "chapters": 12, "examples": 24, "review_questions": 96, "case_studies": 12, "glossary": 1, "objectives": 12}
def score(text):
    t = text.split("\n---\n", 1)[-1] if text.startswith("---") else text
    m = {"words": len(t.split()),
         "chapters": len(re.findall(r"(?m)^## ", t)),
         "examples": len(re.findall(r"(?im)^#{3,4} (worked )?example|^\*\*example", t)),
         "review_questions": len(re.findall(r"(?m)^\s*\d+\.\s.*\?\s*$", t)),
         "case_studies": len(re.findall(r"(?im)^#{2,4} .*case study", t)),
         "glossary": 1 if re.search(r"(?im)^## (glossary|key terms)", t) else 0,
         "objectives": len(re.findall(r"(?im)^#{3,4} (learning )?objectives", t))}
    parts = {k: min(1.0, m[k] / STD[k]) for k in STD}
    w = {"words": 30, "chapters": 15, "examples": 15, "review_questions": 15, "case_studies": 10, "glossary": 5, "objectives": 10}
    m["score"] = round(sum(parts[k] * w[k] for k in w), 1)
    m["textbook_equivalent"] = all(m[k] >= STD[k] for k in STD)
    return m
if __name__ == "__main__":
    files = sys.argv[1:] or sorted(glob.glob("knowledge/*/*.md"))
    out = {f: score(open(f, encoding="utf-8").read()) for f in files}
    print(json.dumps({"standard": STD, "passing": sum(v["textbook_equivalent"] for v in out.values()), "files": len(out)}))
