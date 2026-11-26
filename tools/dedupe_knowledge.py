"""Remove repeated copies inside each subject, keeping the FIRST (original) occurrence.
  1. titled items: within one '## ' section, a later item whose bold title ("**Title**:") was
     already used in that section is removed, up to the next item marker, blank line or section end.
  2. sentences: an exact repeat (normalised, >= 12 words) of a sentence already seen anywhere in
     the subject body is removed.
Frontmatter is never touched. Usage: dedupe_edu.py ROOT [--write] [--show key]"""
import json, os, re, sys, collections
ROOT = sys.argv[1]; WRITE = "--write" in sys.argv
SHOW = sys.argv[sys.argv.index("--show") + 1] if "--show" in sys.argv else None
os.chdir(ROOT); paths = json.load(open("knowledge/paths.json"))
ITEM = re.compile(r"(?:(?<=\n)|(?<=^))(?:\d{1,2}\.\s+)?\*\*([^*\n]{6,60})\*\*\s*:|(?<=[.!?])\s+(?:\d{1,2}\.\s+)?\*\*([^*\n]{6,60})\*\*\s*:")
norm = lambda s: re.sub(r"[^a-z0-9 ]", "", s.lower()).strip()

def dedupe_section(sec):
    marks = [(m.start(), (m.group(1) or m.group(2)).strip().lower()) for m in ITEM.finditer(sec)]
    if len(marks) < 2: return sec, 0
    spans = collections.defaultdict(list)
    for i, (pos, title) in enumerate(marks):
        end = marks[i + 1][0] if i + 1 < len(marks) else len(sec)
        blank = sec.find("\n\n", pos)
        if blank != -1 and blank < end: end = blank
        spans[title].append((pos, end))
    cut = set()
    bag = lambda x: set(re.findall(r"[a-z0-9$%.]+", sec[x[0]:x[1]].lower()))
    for title, sp in spans.items():
        # same title AND the same scenario rewritten (word overlap >= 0.45): keep the fuller one.
        # Different scenarios that share a concept title are separate examples and all stay.
        for i in range(len(sp)):
            for j in range(i + 1, len(sp)):
                a_, b_ = sp[i], sp[j]
                if a_ in cut or b_ in cut: continue
                A, B = bag(a_), bag(b_)
                if len(A & B) / max(1, len(A | B)) >= 0.45:
                    cut.add(min((a_, b_), key=lambda x: (x[1] - x[0], -x[0])))
    cut = sorted(cut)
    out, last = [], 0
    for a, b in cut: out.append(sec[last:a]); last = b
    out.append(sec[last:])
    return "".join(out), len(cut)

def dedupe_sentences(body):
    seen, removed = set(), 0
    def fix_par(par):
        nonlocal removed
        if par.lstrip().startswith(("#", "|", "```")): return par
        parts = re.split(r"(?<=[.!?])(\s+)", par); keep = []
        for i in range(0, len(parts), 2):
            s = parts[i]; sep = parts[i + 1] if i + 1 < len(parts) else ""
            n = norm(s)
            if len(n.split()) >= 12 and n in seen: removed += 1; continue
            if len(n.split()) >= 12: seen.add(n)
            keep.append(s + sep)
        return "".join(keep).rstrip() if keep else ""
    pars = body.split("\n\n")
    return "\n\n".join(p for p in (fix_par(p) for p in pars) if p.strip() or p == ""), removed

tot = collections.Counter(); changed = []
for k, rel in sorted(paths.items()):
    t = open(rel, encoding="utf-8").read()
    m = re.match(r"^---\n.*?\n---\n", t, re.S); fm = m.group(0) if m else ""; body = t[len(fm):]
    secs = re.split(r"(?m)^(?=## )", body); n_items = 0; new = []
    for s in secs: s2, c = dedupe_section(s); new.append(s2); n_items += c
    body2, n_sent = dedupe_sentences("".join(new))
    # guard: a section that had real content keeps at least half of it, else it is left as it was
    o = {x.split("\n", 1)[0]: x for x in secs}; fixed = []
    for x in re.split(r"(?m)^(?=## )", body2):
        h = x.split("\n", 1)[0]
        if h in o and len(o[h].split()) >= 30 and len(x.split()) < 0.5 * len(o[h].split()): x = o[h]
        fixed.append(x)
    body2 = "".join(fixed)
    body2 = re.sub(r"\n{3,}", "\n\n", body2)
    if n_items or n_sent:
        changed.append((k, n_items, n_sent, len(body.split()), len(body2.split())))
        tot["items"] += n_items; tot["sentences"] += n_sent; tot["words_removed"] += len(body.split()) - len(body2.split())
        if WRITE: open(rel, "w", encoding="utf-8").write(fm + body2.rstrip("\n") + "\n")
        if SHOW == k:
            import difflib; sys.stdout.writelines(difflib.unified_diff(body.splitlines(1), body2.splitlines(1), "before", "after", n=0))
print(json.dumps({"subjects_changed": len(changed), **tot}))
print("largest:", sorted(changed, key=lambda x: -(x[3] - x[4]))[:6])
