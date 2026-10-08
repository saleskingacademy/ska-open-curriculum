#!/usr/bin/env python3
"""SKA Education-16: every unit of education gets a canonical address, a spent-memory location,
a Symbol256 state and a Chain256 attachment. Design: EDU16.md.

  EDU-16  FF SSS CCC L XXX PPP T  (16 digits, positional, append-only, never reused)
          FF field (ISCED-F broad)  SSS subject  CCC chapter  L level (0 = core, 1-8 ladder)
          XXX section  PPP paragraph  T unit type (1 subject, 2 chapter, 3 section, 4 paragraph)
  T16     the unit's address in SPENT memory: a real past instant after genesis that was never used,
          in the platform's canonical T16 format (worker CHAIN_ADDR.t16: MMDDYYYYHHMMSSCC, UTC,
          centisecond = the memory layer's resolution). Education starts at 0702201800000000 (one day
          after genesis, clear of the genesis-day agent/mode anchors and the S0-S16 spent seconds).
          offset_cs = ((((L*1000 + SSS)*100 + CCC)*100 + XXX)*100 + PPP): positional, no hashing,
          no collisions. Core (L0) spans ~116 days of 2018; all 8 levels end before Aug 2021.
  EDU-32  EDU-16 + T16 (the Chain32 pairing: stable anchor + its place in time).
  DNA-16  every unit is labeled by its EDU-16 alone (the `edu16` field) - that is its DNA-16.
          Nothing else chain-related is published: T16, EDU-32, the spent instant and the Chain256
          attachment are positional, so the worker derives them privately from the label.
  Chain256 attachment, context "education" (derived, not stored). Stable lanes (1,4,5,8,9,12,13,16):
          L1 genesis  L4 education anchor  L5 subject EDU-16  L8 subject T16
          L9 unit EDU-16  L12 unit T16  L13 Symbol256 digest  L16 integrity digest
          Interlocked lanes 2,3,6,7,10,11,14,15 are the live beat clock at the moment of use:
          computed by the worker, never stored. Chain64 is referenced (L1), never modified.

Allocation is append-only in map/edu16_registry.json: an existing unit keeps its numbers forever;
changed text gets a NEW paragraph number and the old one is kept as retired.
Usage:  python3 tools/edu16.py          build + verify
        python3 tools/edu16.py --verify verify only (exit 1 if any chain is broken)
"""
import json, os, sys, glob, hashlib, math, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REG = os.path.join(ROOT, "map/edu16_registry.json")
OUT = os.path.join(ROOT, "edu16")
GENESIS16 = "0701201800000000"
EDU_ANCHOR16 = "0701201800000094"   # genesis band: agents 01-26, modes 91-93, education 94
import datetime
EDU_REGION_MS = int(datetime.datetime(2018, 7, 2, tzinfo=datetime.timezone.utc).timestamp() * 1000)
CAP = {"chapters": 99, "sections": 99, "paragraphs": 99}   # two-digit radix in the instant mapping
TYPE = {1: "subject", 2: "chapter", 3: "section", 4: "paragraph"}

def d16(s):
    return str(int(hashlib.sha256(s.encode()).hexdigest(), 16) % 10**16).zfill(16)

def edu16(ff, sss, ccc=0, lvl=0, xxx=0, ppp=0, t=1):
    return f"{int(ff):02d}{sss:03d}{ccc:03d}{lvl:1d}{xxx:03d}{ppp:03d}{t:1d}"

def offset_cs(e):
    sss, ccc, lvl, xxx, ppp = int(e[2:5]), int(e[5:8]), int(e[8]), int(e[9:12]), int(e[12:15])
    return (((lvl * 1000 + sss) * 100 + ccc) * 100 + xxx) * 100 + ppp

def t16_ms(ms):
    d = datetime.datetime.fromtimestamp(ms / 1000, tz=datetime.timezone.utc)
    return f"{d.month:02d}{d.day:02d}{d.year:04d}{d.hour:02d}{d.minute:02d}{d.second:02d}{d.microsecond // 10000:02d}"

def t16(e):
    return t16_ms(EDU_REGION_MS + offset_cs(e) * 10)

def spent(e):
    ms = EDU_REGION_MS + offset_cs(e) * 10
    return datetime.datetime.fromtimestamp(ms / 1000, tz=datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.") + f"{(ms % 1000) // 10:02d}Z"

def lanes(subj_e, unit_e, sym16, int16):
    return [GENESIS16, EDU_ANCHOR16, subj_e, t16(subj_e), unit_e, t16(unit_e), sym16, int16]

def agg_sig(sigs):
    """Prevalence signature: digit = how many children (0-9 scale) have that dimension active."""
    sigs = [s for s in sigs if s]
    if not sigs: return ""
    n = len(sigs); L = min(len(s) for s in sigs)
    return "".join(str(math.ceil(9 * sum(1 for s in sigs if s[i] != "0") / n)) for i in range(L))

def load_reg():
    if os.path.exists(REG): return json.load(open(REG))
    return {"version": 1, "anchor": EDU_ANCHOR16, "subjects": {}, "chapters": {}, "sections": {}, "paragraphs": {}}

def alloc(table, key, parent_prefix, reg):
    if key in reg[table]: return reg[table][key]
    used = [v for k, v in reg[table].items() if k.rsplit("/", 1)[0] == parent_prefix] if parent_prefix else list(reg[table].values())
    n = (max(used) + 1) if used else (0 if table == "subjects" else 1)
    if n > CAP.get(table, 999): raise SystemExit(f"EDU-16 overflow in {table} under {parent_prefix} (cap {CAP.get(table, 999)})")
    reg[table][key] = n; return n

def build():
    reg = load_reg()
    books = json.load(open(os.path.join(ROOT, "map/real_subjects.json")))["books"]
    sym = {os.path.basename(p)[:-5]: p for p in glob.glob(os.path.join(ROOT, "symbols/**/*.json"), recursive=True)
           if not p.endswith("vocab.json")}
    os.makedirs(OUT, exist_ok=True)
    chapters_index, seen_topic, units = {}, {}, []
    for b in books:
        sss = alloc("subjects", b["id"], None, reg); ff = b["field_code"]
        se = edu16(ff, sss, t=1)
        ch_out, ch_sigs, ch_int = [], [], []
        for topic in b["topics_as_chapters"]:
            if topic in seen_topic:          # cross-listed: canonical home is its first subject
                ch_out.append({"key": topic, "cross_listed": True, "edu16": seen_topic[topic]}); continue
            if topic not in sym: continue
            ccc = alloc("chapters", b["id"] + "/" + topic, b["id"], reg)
            ce = edu16(ff, sss, ccc, t=2); seen_topic[topic] = ce
            js = json.load(open(sym[topic])); md = os.path.join(ROOT, js["path"])
            md_text = open(md, encoding="utf-8").read() if os.path.exists(md) else ""
            sec_out, sec_sigs, sec_ints = [], [], []
            for sec in js["sections"]:
                skey = topic + "/" + sec["id"]
                xxx = alloc("sections", skey, topic, reg)
                xe = edu16(ff, sss, ccc, 0, xxx, 0, 3)
                p_out, p_sigs, p_ints = [], [], []
                for p in sec["paragraphs"]:
                    ppp = alloc("paragraphs", skey + "/" + p["id"], skey, reg)
                    pe = edu16(ff, sss, ccc, 0, xxx, ppp, 4)
                    s16, i16 = d16(p["sig"]), d16(p["id"] + "|" + p["sig"] + "|" + str(p.get("words")))
                    p_out.append({"edu16": pe, "pid": p["id"], "words": p.get("words"),
                                  "sym16": s16, "int16": i16})
                    p_sigs.append(p["sig"]); p_ints.append(i16); units.append(pe)
                xs = agg_sig(p_sigs); xi = d16("|".join(p_ints)); xs16 = d16(xs)
                sec_out.append({"edu16": xe, "id": sec["id"], "title": sec["title"],
                                "sig": xs, "sym16": xs16, "int16": xi, "paragraphs": p_out})
                sec_sigs.append(xs); sec_ints.append(xi); units.append(xe)
            cs = agg_sig(sec_sigs); ci = d16(md_text) if md_text else d16("|".join(sec_ints)); cs16 = d16(cs)
            ch_out.append({"key": topic, "edu16": ce, "path": js["path"],
                           "sig": cs, "sym16": cs16, "int16": ci, "sections": sec_out})
            chapters_index[topic] = {"edu16": ce, "subject": b["id"], "subject_edu16": se,
                                     "int16": ci}
            ch_sigs.append(cs); ch_int.append(ci); units.append(ce)
        ss = agg_sig(ch_sigs); si = d16("|".join(ch_int)); ss16 = d16(ss)
        rec = {"edu16": se, "id": b["id"], "title": b["title"],
               "field_code": ff, "field": b["field"], "sig": ss, "sym16": ss16, "int16": si, "chapters": ch_out}
        json.dump(rec, open(os.path.join(OUT, b["id"] + ".json"), "w"), ensure_ascii=False, separators=(",", ":"))
        units.append(se)
    json.dump(reg, open(REG, "w"), separators=(",", ":"), sort_keys=True)
    json.dump({"version": 1, "anchor": EDU_ANCHOR16, "genesis": GENESIS16, "chapters": chapters_index},
              open(os.path.join(ROOT, "map/edu16_chapters.json"), "w"), separators=(",", ":"), sort_keys=True)
    return units

def routing_stats(ids):
    """Adaptive routing (Symbol256 routing spec): how many base-100 pairs of the address are needed
    before a unit is unique. Average and worst case over the real corpus."""
    ids = sorted(set(ids)); depth = {}
    for k in range(1, 9):
        c = collections.Counter(i[:2 * k] for i in ids)
        for i in ids:
            if i not in depth and c[i[:2 * k]] == 1: depth[i] = k
    for i in ids: depth.setdefault(i, 8)
    dist = collections.Counter(depth.values())
    return {"units": len(ids), "avg_pairs": round(sum(depth.values()) / len(ids), 3), "max_pairs": max(depth.values()),
            "by_pairs": dict(sorted(dist.items()))}

def symbol_routing(pairs):
    """Routing spec, three layers: Symbol256 state narrows, the address resolves the rest.
    pairs = [(sym16, edu16)]. Count base-100 pairs of sym16 consumed until unique; units whose
    semantic state is identical to another's resolve by address (that is the address's job)."""
    c_full = collections.Counter(s for s, _ in pairs); depth = collections.Counter(); same = 0
    for k in range(1, 9):
        c = collections.Counter(s[:2 * k] for s, _ in pairs)
        for s, e in pairs:
            if c[s[:2 * k]] == 1 and (s, e) not in depth: depth[(s, e)] = k
    total = 0
    for s, e in pairs:
        if (s, e) in depth: total += depth[(s, e)]
        else: same += 1; total += 8
    dist = collections.Counter(depth.values())
    return {"units": len(pairs), "avg_symbol_pairs": round(total / len(pairs), 3),
            "resolved_by_symbol": len(depth), "same_symbol_state_resolved_by_address": same,
            "by_pairs": dict(sorted(dist.items()))}

NOW_MS = int(datetime.datetime.now(datetime.timezone.utc).timestamp() * 1000)

def verify():
    bad, n, ids, spents = [], 0, [], set()
    def chk(u, se):
        nonlocal n; n += 1
        # Published units carry only their DNA-16 label (edu16) plus symbol and
        # integrity digests. The chain attachment is derived, never published:
        # rebuild it here and check it, exactly as the worker does privately.
        e = u["edu16"]
        if not (len(e) == 16 and e.isdigit()): bad.append((e, "DNA-16 label")); return
        if any(k in u for k in ("s128", "t16", "edu32", "spent")): bad.append((e, "chain digits published"))
        L = lanes(se, e, u["sym16"], u["int16"])
        if L[2][2:5] != L[4][2:5]: bad.append((e, "subject prefix"))
        sp = spent(e)
        if sp in spents: bad.append((e, "spent address reused"))
        if not (EDU_REGION_MS <= EDU_REGION_MS + offset_cs(e) * 10 < NOW_MS): bad.append((e, "spent address not in the past"))
        spents.add(sp); ids.append((u["sym16"], e))
    for f in sorted(glob.glob(os.path.join(OUT, "*.json"))):
        s = json.load(open(f)); se = s["edu16"]; chk(s, se)
        for c in s["chapters"]:
            if c.get("cross_listed"): continue
            md = os.path.join(ROOT, c["path"])
            if os.path.exists(md) and d16(open(md, encoding="utf-8").read()) != c["int16"]:
                bad.append((c["edu16"], "chapter text changed since attachment - rebuild"))
            chk(c, se)
            for x in c["sections"]:
                chk(x, se)
                for p in x["paragraphs"]: chk(p, se)
    return n, bad, ids

if __name__ == "__main__":
    if "--verify" not in sys.argv: build()
    n, bad, ids = verify()
    rs = {"address_only": routing_stats([e for _, e in ids]), "symbol_then_address": symbol_routing(ids)}
    print(json.dumps({"units": n, "broken_chains": len(bad), "routing": rs}, indent=1))
    for b in bad[:20]: print("BROKEN", *b)
    json.dump({"units": n, "broken": len(bad), "routing": rs}, open(os.path.join(ROOT, "map/edu16_stats.json"), "w"), indent=1)
    sys.exit(1 if bad else 0)
