#!/usr/bin/env python3
"""SKA English Dictionary, full build: Open English WordNet 2024 + English Wiktionary.

WordNet (CC BY 4.0) gives carefully curated senses for nouns, verbs, adjectives and
adverbs. Wiktionary (CC BY-SA 4.0, via the kaikki.org extraction) adds everything else
English needs: pronouns, articles, prepositions, conjunctions, determiners, modern and
business words, proper nouns, and the inflected forms ("went" -> go, "is" -> be).

Anchors are append-only (see tools/build_dictionary.py): every existing DNA-16 is kept;
new words get the next word numbers, new senses the next sense numbers. A Wiktionary
sense that repeats an existing definition (>= 50% shared words) is skipped. Obsolete and
archaic senses are skipped. Each sense carries `src` (wn / wikt) and its Symbol256 `sym`.

Shards: dictionary/words/<abc>.json keyed by the first three letters ("_" padding).
Usage:  python3 tools/build_dictionary_full.py WORDNET.xml.gz KAIKKI.jsonl.gz
        python3 tools/build_dictionary_full.py --verify
"""
import gzip, json, os, re, sys, subprocess, collections, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_dictionary as B

ROOT = B.ROOT; OUT = B.OUT; TMP = os.path.join(ROOT, ".dict_tmp")
POS = {"noun": "noun", "verb": "verb", "adj": "adjective", "adv": "adverb", "prep": "preposition", "pron": "pronoun",
       "conj": "conjunction", "det": "determiner", "article": "article", "intj": "interjection", "num": "numeral",
       "name": "proper noun", "particle": "particle", "phrase": "phrase", "prep_phrase": "phrase", "proverb": "phrase",
       "contraction": "contraction", "abbrev": "abbreviation", "postp": "postposition"}
SKIP_TAGS = {"obsolete", "archaic", "misspelling", "nonstandard-spelling"}
def shard3(w):
    k = re.sub(r"[^a-z]", "", w.lower())[:3]
    return (k + "___")[:3] if k else "___"
def words(t): return set(re.findall(r"[a-z]{3,}", t.lower()))

class Sym:
    """one long-lived node process computing SYM256.stable for definitions"""
    def __init__(s):
        js = ("const S=require(process.argv[1]);const rl=require('readline').createInterface({input:process.stdin});"
              "rl.on('line',l=>{process.stdout.write(S.stable(JSON.parse(l))+'\\n')});")
        s.p = subprocess.Popen(["node", "-e", js, os.path.join(ROOT, "tools", "sym256.js")], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True, bufsize=1)
    def many(s, texts):
        out = []
        for i in range(0, len(texts), 2000):
            chunk = texts[i:i + 2000]
            s.p.stdin.write("".join(json.dumps(t) + "\n" for t in chunk)); s.p.stdin.flush()
            out += [s.p.stdout.readline().rstrip("\n") for _ in chunk]
        assert all(len(x) == 128 for x in out); return out

def pass1(kaikki):
    """stream Wiktionary into per-shard jsonl files of compact records"""
    if os.path.isdir(TMP): shutil.rmtree(TMP)
    os.makedirs(TMP); buf = collections.defaultdict(list); n = kept = 0; forms = 0
    def flush(force=False):
        for k in list(buf):
            if force or len(buf[k]) >= 200:
                with open(os.path.join(TMP, k + ".jsonl"), "a", encoding="utf-8") as f: f.write("".join(buf[k]))
                del buf[k]
    op = gzip.open if kaikki.endswith(".gz") else open
    with op(kaikki, "rt", encoding="utf-8") as f:
        for line in f:
            n += 1; d = json.loads(line)
            w, pos = d.get("word", ""), POS.get(d.get("pos"))
            if not w or not pos or len(w) > 60 or d.get("lang_code") not in (None, "en"): continue
            syn = [x.get("word") for x in d.get("synonyms", []) if x.get("word")][:6]
            senses = []
            for s in d.get("senses", []):
                tags = set(s.get("tags", []))
                if tags & SKIP_TAGS: continue
                fo = s.get("form_of") or s.get("alt_of")
                if fo and fo[0].get("word"):
                    senses.append({"form_of": fo[0]["word"], "tags": sorted(tags)[:4]}); forms += 1; continue
                g = (s.get("glosses") or [""])[-1].strip()
                if not g or len(g) < 3: continue
                ex = [e["text"][:220] for e in s.get("examples", []) if e.get("text") and e.get("type") != "quotation"][:2]
                senses.append({"def": g[:600], "ex": ex, "tags": [t for t in sorted(tags) if t not in ("form-of",)][:4]})
            if not senses: continue
            kept += 1
            buf[shard3(w)].append(json.dumps({"w": w, "pos": pos, "syn": syn, "s": senses}, ensure_ascii=False) + "\n")
            if n % 20000 == 0: flush()
            if n % 200000 == 0: print(f"  streamed {n:,} entries, kept {kept:,}", flush=True)
    flush(True)
    print(f"pass 1: {n:,} entries read, {kept:,} kept, {forms:,} form-of senses")

def load_existing():
    """every word and sense number already allocated (any shard layout)"""
    old, nxt = {}, 1
    if os.path.isdir(OUT):
        for f in os.listdir(OUT):
            for w, e in json.load(open(os.path.join(OUT, f))).items():
                old[w] = e; nxt = max(nxt, int(e["dna16"][2:10]) + 1)
    return old, nxt

def main(wordnet_src, kaikki):
    old, nxt = load_existing()
    print(f"existing: {len(old):,} words, next word number {nxt:,}")
    if not old:   # first run: WordNet base via the original builder
        B.main(wordnet_src); old, nxt = load_existing()
    pass1(kaikki)
    # new words, allocated in sorted order after every existing number (append-only)
    new_words = set()
    for f in os.listdir(TMP):
        for line in open(os.path.join(TMP, f), encoding="utf-8"):
            w = json.loads(line)["w"]
            if w not in old: new_words.add(w)
    for w in sorted(new_words, key=lambda x: (x.lower(), x)):
        old[w] = {"dna16": B.dna16(nxt, 0, 1), "senses": []}; nxt += 1
    print(f"new words allocated: {len(new_words):,}")
    # regroup all words into 3-letter shards and merge Wiktionary senses
    by = collections.defaultdict(dict)
    for w, e in old.items(): by[shard3(w)][w] = e
    tmp_keys = {f[:-6] for f in os.listdir(TMP)}
    def wk_records(k):                     # one shard of Wiktionary at a time - bounded memory
        f = os.path.join(TMP, k + ".jsonl")
        return [json.loads(l) for l in open(f, encoding="utf-8")] if os.path.exists(f) else []
    sym = Sym(); added = forms = skipped = 0
    tmp_out = OUT + ".new"; os.makedirs(tmp_out, exist_ok=True)
    for k in sorted(set(by) | tmp_keys):
        shard = by.get(k, {}); pend = []
        for r in wk_records(k):
            e = shard.setdefault(r["w"], old[r["w"]])
            used = {int(s["dna16"][10:14]) for s in e["senses"]}
            have = [words(s.get("def", "")) for s in e["senses"]]
            for s in r["s"]:
                if "form_of" in s:
                    fl = e.setdefault("forms_of", [])
                    if s["form_of"] not in fl and len(fl) < 6: fl.append(s["form_of"]); forms += 1
                    continue
                ws = words(s["def"])
                if any(h and ws and len(h & ws) / len(h | ws) >= 0.5 for h in have): skipped += 1; continue
                sn = 1
                while sn in used: sn += 1
                if sn > 999: break
                used.add(sn); have.append(ws)
                sense = {"dna16": B.dna16(int(e["dna16"][2:10]), sn, 2), "id": "wikt:" + r["w"] + ":" + r["pos"] + ":" + str(sn),
                         "pos": r["pos"], "def": s["def"], "ex": s["ex"], "syn": r["syn"], "src": "wikt"}
                if s["tags"]: sense["tags"] = s["tags"]
                e["senses"].append(sense); pend.append(sense); added += 1
        for e in shard.values():
            for s in e["senses"]: s.setdefault("src", "wn")
        if pend:
            for s, sy in zip(pend, sym.many([s["def"] for s in pend])): s["sym"] = B.sparse(sy)
        shard = {w: e for w, e in shard.items() if e["senses"] or e.get("forms_of")}
        if shard: json.dump(shard, open(os.path.join(tmp_out, k + ".json"), "w"), ensure_ascii=False, separators=(",", ":"), sort_keys=True)
    shutil.rmtree(OUT); os.rename(tmp_out, OUT); shutil.rmtree(TMP)
    n_w = n_s = 0
    for f in os.listdir(OUT):
        d = json.load(open(os.path.join(OUT, f))); n_w += len(d); n_s += sum(len(e["senses"]) for e in d.values())
    json.dump({"version": 2, "band": "88", "words": n_w, "senses": n_s, "shard_key": "first three letters",
               "anchor": "88 WWWWWWWW SSSS T C (T: 1 word, 2 sense; C: Luhn)",
               "spent_memory": "derived privately: region 2021-06-01T00:00:00Z, offset_cs = W*1000 + S",
               "symbol": "Symbol256 stable of the definition, sparse pos:digit",
               "sources": [{"name": "Open English WordNet 2024", "src": "wn", "license": "CC BY 4.0", "url": "https://github.com/globalwordnet/english-wordnet"},
                           {"name": "English Wiktionary (kaikki.org extraction)", "src": "wikt", "license": "CC BY-SA 4.0", "url": "https://kaikki.org/dictionary/English/"}]},
              open(os.path.join(ROOT, "dictionary", "index.json"), "w"), indent=1)
    print(json.dumps({"words": n_w, "senses": n_s, "wiktionary_senses_added": added, "inflection_links": forms, "duplicates_skipped": skipped}))

def verify():
    seen, spent, bad, n = set(), set(), [], 0
    import datetime
    now = int(datetime.datetime.now(datetime.timezone.utc).timestamp() * 1000)
    for f in sorted(os.listdir(OUT)):
        for w, e in json.load(open(os.path.join(OUT, f))).items():
            n += 1
            if shard3(w) + ".json" != f: bad.append((w, f, "wrong shard"))
            for d in [e["dna16"]] + [s["dna16"] for s in e["senses"]]:
                if not (len(d) == 16 and d.isdigit() and d.startswith("88") and B.luhn(d[:15]) == d[15]): bad.append((w, d, "format"))
                if d in seen: bad.append((w, d, "duplicate anchor"))
                ms = B.spent_ms(d)
                if ms in spent: bad.append((w, d, "spent address reused"))
                if not (B.EDU_END_MS <= ms < now): bad.append((w, d, "spent address outside the dictionary region"))
                seen.add(d); spent.add(ms)
            for s in e["senses"]:
                if s["dna16"][2:10] != e["dna16"][2:10]: bad.append((w, s["dna16"], "sense not under its word"))
                if any(k in s for k in ("t16", "spent", "chain", "s128")): bad.append((w, s["dna16"], "chain digits published"))
    print(json.dumps({"words": n, "anchors": len(seen), "bad": len(bad)}))
    for b in bad[:20]: print("BAD", *b)
    return not bad

if __name__ == "__main__":
    if sys.argv[1:2] == ["--verify"]: sys.exit(0 if verify() else 1)
    main(sys.argv[1], sys.argv[2]); sys.exit(0 if verify() else 1)
