#!/usr/bin/env python3
"""SKA English Dictionary: every English word and every one of its definitions is anchored -
a permanent DNA-16 and a place in spent memory - so agents can address and reason over exact meanings.

Source: Open English WordNet 2024 (CC BY 4.0, https://github.com/globalwordnet/english-wordnet).

DNA-16 (dictionary band)   88 WWWWWWWW SSSS T C
    88        dictionary band (education uses ISCED field codes 00-10)
    WWWWWWWW  word number, append-only, never reused
    SSSS      sense (definition) number within the word, 0000 = the word itself, max 999
    T         1 = word, 2 = sense
    C         Luhn check digit over the first 15 digits
Spent memory (derived, never published - the platform computes it privately from the DNA-16):
    region starts 2021-06-01T00:00:00.00Z, after education (2018-07-02 .. at most 2021-05-08)
    offset_cs = WWWWWWWW * 1000 + SSSS   -> each word owns a 10-second window, each definition 1/100 s
Numbers are append-only: the build reads the existing shards first, keeps every number it finds,
and allocates new numbers only for words and senses it has never seen.

Each sense carries `sym`, its Symbol256 meaning (SYM256.stable of the definition, the platform's own
tools/sym256.js), stored sparse as "position:digit" because most of the 128 digits are zero.

Output: dictionary/words/<xx>.json (xx = first two letters a-z, "_" padding otherwise), dictionary/index.json
Usage:  python3 tools/build_dictionary.py path/to/english-wordnet-2024.xml.gz
        python3 tools/build_dictionary.py --verify
"""
import gzip, json, os, re, subprocess, sys, datetime, collections, xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "dictionary", "words")
REGION_MS = int(datetime.datetime(2021, 6, 1, tzinfo=datetime.timezone.utc).timestamp() * 1000)
EDU_END_MS = int(datetime.datetime(2021, 5, 9, tzinfo=datetime.timezone.utc).timestamp() * 1000)
POS = {"n": "noun", "v": "verb", "a": "adjective", "s": "adjective", "r": "adverb",
       "c": "conjunction", "p": "adposition", "x": "other", "u": "unknown"}

def luhn(d15):
    s = 0
    for i, ch in enumerate(reversed(d15)):
        n = int(ch)
        if i % 2 == 0:
            n *= 2
            if n > 9: n -= 9
        s += n
    return str((10 - s % 10) % 10)

def dna16(w, s, t):
    b = "88" + f"{w:08d}" + f"{s:04d}" + str(t)
    return b + luhn(b)

def spent_ms(d):
    return REGION_MS + (int(d[2:10]) * 1000 + int(d[10:14])) * 10

def shard(key):
    k = re.sub(r"[^a-z]", "", key.lower())[:2]
    return (k + "__")[:2] if k else "__"

def parse(path):
    syn, entries = {}, collections.OrderedDict()
    for _, el in ET.iterparse(gzip.open(path), events=("end",)):
        if el.tag == "Synset":
            d = el.find("Definition")
            syn[el.get("id")] = {"def": (d.text or "").strip() if d is not None else "",
                                 "ex": [(x.text or "").strip() for x in el.findall("Example")][:2],
                                 "members": el.get("members", "").split()}
            el.clear()
        elif el.tag == "LexicalEntry":
            lem = el.find("Lemma")
            entries.setdefault(lem.get("writtenForm"), []).append(
                (el.get("id"), lem.get("partOfSpeech"), [(s.get("id"), s.get("synset")) for s in el.findall("Sense")]))
            el.clear()
    return syn, entries

def symbols(texts):
    js = ("const S=require(process.argv[1]);const rl=require('readline').createInterface({input:process.stdin});"
          "rl.on('line',l=>{process.stdout.write(S.stable(JSON.parse(l))+'\\n')});")
    p = subprocess.run(["node", "-e", js, os.path.join(ROOT, "tools", "sym256.js")],
                       input="\n".join(json.dumps(t) for t in texts) + "\n", capture_output=True, text=True, check=True)
    out = p.stdout.split("\n")[:len(texts)]
    assert len(out) == len(texts) and all(len(x) == 128 for x in out), "symbol build failed"
    return out

def sparse(sym):
    return ",".join(f"{i}:{c}" for i, c in enumerate(sym) if c != "0")

def main(src):
    syn, entries = parse(src)
    member_word = {leid: w for w, les in entries.items() for leid, _, _ in les}
    old_w, old_s, next_w = {}, {}, 1
    if os.path.isdir(OUT):
        for f in os.listdir(OUT):
            for word, e in json.load(open(os.path.join(OUT, f))).items():
                wn = int(e["dna16"][2:10]); old_w[word] = wn; next_w = max(next_w, wn + 1)
                for s in e["senses"]: old_s[s["id"]] = int(s["dna16"][10:14])
    words = sorted(entries, key=lambda w: (w.lower(), w))
    for w in words:
        if w not in old_w: old_w[w] = next_w; next_w += 1
    flat = [(w, sid, pos, ssid) for w in words for _, pos, senses in entries[w] for sid, ssid in senses]
    syms = symbols([syn.get(s, {}).get("def", "") for _, _, _, s in flat])
    used = collections.defaultdict(set)
    for w, sid, _, _ in flat:
        if sid in old_s: used[w].add(old_s[sid])
    shards = collections.defaultdict(dict)
    for (w, sid, pos, ssid), sym in zip(flat, syms):
        e = shards[shard(w)].setdefault(w, {"dna16": dna16(old_w[w], 0, 1), "senses": []})
        if sid in old_s: sn = old_s[sid]
        else:
            sn = 1
            while sn in used[w]: sn += 1
            used[w].add(sn)
        assert sn <= 999, (w, "more than 999 senses")
        s = syn.get(ssid, {})
        e["senses"].append({"dna16": dna16(old_w[w], sn, 2), "id": sid, "pos": POS.get(pos, pos),
                            "def": s.get("def", ""), "ex": s.get("ex", []),
                            "syn": sorted({member_word[m] for m in s.get("members", []) if member_word.get(m, w) != w})[:6],
                            "sym": sparse(sym)})
    os.makedirs(OUT, exist_ok=True)
    for k, d in shards.items():
        json.dump(d, open(os.path.join(OUT, k + ".json"), "w"), ensure_ascii=False, separators=(",", ":"), sort_keys=True)
    json.dump({"version": 1, "band": "88", "words": len(words), "senses": len(flat), "shards": sorted(shards),
               "anchor": "88 WWWWWWWW SSSS T C (T: 1 word, 2 sense; C: Luhn)",
               "spent_memory": "derived privately: region 2021-06-01T00:00:00Z, offset_cs = W*1000 + S",
               "symbol": "Symbol256 stable of the definition, sparse pos:digit",
               "source": "Open English WordNet 2024", "source_url": "https://github.com/globalwordnet/english-wordnet",
               "license": "CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/)"},
              open(os.path.join(ROOT, "dictionary", "index.json"), "w"), indent=1)
    print(json.dumps({"words": len(words), "senses": len(flat), "shards": len(shards)}))

def verify():
    seen, spent, bad = set(), set(), []
    now = int(datetime.datetime.now(datetime.timezone.utc).timestamp() * 1000)
    for f in sorted(os.listdir(OUT)):
        for w, e in json.load(open(os.path.join(OUT, f))).items():
            if shard(w) + ".json" != f: bad.append((w, f, "wrong shard"))
            for d in [e["dna16"]] + [s["dna16"] for s in e["senses"]]:
                if not (len(d) == 16 and d.isdigit() and d.startswith("88") and luhn(d[:15]) == d[15]): bad.append((w, d, "format"))
                if d in seen: bad.append((w, d, "duplicate anchor"))
                ms = spent_ms(d)
                if ms in spent: bad.append((w, d, "spent address reused"))
                if not (EDU_END_MS <= ms < now): bad.append((w, d, "spent address outside the dictionary region"))
                seen.add(d); spent.add(ms)
            if e["dna16"][10:15] != "00001": bad.append((w, e["dna16"], "word anchor"))
            for s in e["senses"]:
                if s["dna16"][2:10] != e["dna16"][2:10]: bad.append((w, s["dna16"], "sense not under its word"))
                if any(k in s for k in ("t16", "spent", "chain", "s128")): bad.append((w, s["dna16"], "chain digits published"))
    print(json.dumps({"anchors": len(seen), "bad": len(bad)}))
    for b in bad[:20]: print("BAD", *b)
    return not bad

if __name__ == "__main__":
    # Superseded: the dictionary now holds WordNet AND Wiktionary in 3-letter shards.
    # Running this alone would write WordNet-only 2-letter shards, so it refuses;
    # its functions are reused by tools/build_dictionary_full.py.
    sys.exit("use tools/build_dictionary_full.py (WordNet + Wiktionary); this builder is now a library")
