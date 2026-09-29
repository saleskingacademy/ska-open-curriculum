// SKA SAT pair + symbol builder (Kaleb, 2026-09-29). Zero outside models.
// Reads knowledge/**/*.md, writes:
//   symbols/<program>/<key>.json  - hierarchical Symbol256: subject > section > paragraph (sentence sigs recomputable)
//   symbols/vocab.json             - every subject + section symbol (model vocabulary tokens)
//   out/pairs.jsonl                - SAT-selected (context, question) -> answer training pairs
// A parent's signature is the digit-wise MAX of its children, so one subject symbol carries
// the meaning map of the whole subject. Symbols are addresses + signatures, not zipped text.
const fs = require("fs"), path = require("path"), crypto = require("crypto");
const SYM = require("./sym256.js");
const ROOT = path.join(__dirname, "..");
const WH = { who: "Who", what: "What", when: "When", where: "Where", how: "How", why: "Why", which: "Which", whether: "Whether" };
const STOP = new Set("the a an and or of to in on for with by at from as is are was were be been being this that these those it its their they them than then into over under about can may might must should would could will not no but so if when while which what who how why also more most such each other any all some one two use used using within between".split(" "));
const sha = s => crypto.createHash("sha256").update(s).digest("hex");
const sid = (lvl, s) => lvl + parseInt(sha(s).slice(0, 12), 16).toString(36).padStart(9, "0");
const words = s => s.toLowerCase().replace(/[^a-z0-9\s-]/g, " ").split(/\s+/).filter(Boolean);
const maxSig = sigs => { if (!sigs.length) return "0".repeat(128); const o = []; for (let i = 0; i < 128; i++) { let m = 0; for (const g of sigs) { const d = +g[i]; if (d > m) m = d; } o.push(m); } return o.join(""); };
const sentences = p => p.replace(/\s+/g, " ").split(/(?<=[.!?])\s+(?=[A-Z0-9"(])/).map(s => s.trim()).filter(s => { const n = s.split(" ").length; return n >= 8 && n <= 60; });
function walk(d, out = []) { for (const f of fs.readdirSync(d)) { const p = path.join(d, f); fs.statSync(p).isDirectory() ? walk(p, out) : f.endsWith(".md") && out.push(p); } return out; }
function parse(file) {
  const md = fs.readFileSync(file, "utf8"); const fm = {}; let body = md;
  const m = md.match(/^---\n([\s\S]*?)\n---\n/); if (m) { body = md.slice(m[0].length); m[1].split("\n").forEach(l => { const i = l.indexOf(":"); if (i > 0) fm[l.slice(0, i).trim()] = l.slice(i + 1).trim().replace(/^"|"$/g, ""); }); }
  const secs = []; let cur = null;
  for (const block of body.split(/\n\s*\n/)) { const b = block.trim(); if (!b) continue;
    if (b.startsWith("# ") || b.startsWith("> ")) continue;
    if (b.startsWith("## ")) { cur = { title: b.slice(3).trim(), paras: [] }; secs.push(cur); continue; }
    if (!cur) { cur = { title: "Overview", paras: [] }; secs.push(cur); }
    cur.paras.push(b); }
  return { fm, secs };
}
// dominant (pair index, polarity) of a sentence among the question-word pairs
function dominant(sig) { let best = -1, bi = -1, pol = 0; for (let k = 0; k < 8; k++) for (const n of [0, 1]) { const d = +sig[k * 2 + n]; if (d > best) { best = d; bi = k; pol = n; } } return best > 0 ? { k: bi, neg: pol === 1 } : null; }
const files = walk(path.join(ROOT, "knowledge")); const df = new Map(); const docs = [];
for (const f of files) { const d = parse(f); d.file = path.relative(ROOT, f); docs.push(d); const seen = new Set(); d.secs.forEach(s => s.paras.forEach(p => words(p).forEach(w => seen.add(w)))); seen.forEach(w => df.set(w, (df.get(w) || 0) + 1)); }
const N = docs.length, idf = w => Math.log((N + 1) / ((df.get(w) || 0) + 1));
fs.mkdirSync(path.join(ROOT, "out"), { recursive: true });
const pairsOut = fs.createWriteStream(path.join(ROOT, "out/pairs.jsonl"));
const vocab = []; const st = { subjects: 0, sections: 0, paragraphs: 0, sentences: 0, pairs: 0, ambiguous: 0, no_dim: 0, distractor: 0 };
for (const d of docs) {
  const key = d.fm.key, prog = d.fm.program || "general", anchor = [d.fm.dna16, d.fm.l4_address, d.fm.chain256_anchor, key].join("|");
  const S = { id: sid("S", anchor), key, title: d.fm.title, program: prog, path: d.file, sections: [] };
  const sents = []; // flat for SAT search
  d.secs.forEach((sec, si) => {
    const C = { id: sid("C", anchor + "|" + si + "|" + sec.title), title: sec.title, paragraphs: [] };
    sec.paras.forEach((p, pi) => {
      const ss = sentences(p); const sigs = ss.map(x => SYM.stable(x));
      const P = { id: sid("P", anchor + "|" + si + "|" + pi + "|" + sha(p).slice(0, 8)), sig: maxSig(sigs), n: ss.length, words: p.split(/\s+/).length };
      ss.forEach((x, xi) => sents.push({ text: x, sig: sigs[xi], sec: C, secTitle: sec.title, para: p, P: P.id, si, pi }));
      C.paragraphs.push(P); st.paragraphs++; st.sentences += ss.length;
    });
    C.sig = maxSig(C.paragraphs.map(p => p.sig)); S.sections.push(C); vocab.push({ id: C.id, of: S.id, title: sec.title }); st.sections++;
  });
  S.sig = maxSig(S.sections.map(c => c.sig)); vocab.push({ id: S.id, key, title: d.fm.title, program: prog }); st.subjects++;
  // ---- SAT pairs: constraints = {subject, dimension k, polarity, >=2 of 3 key terms}; answer must be unique ----
  const kw = x => [...new Set(words(x).filter(w => w.length > 3 && !STOP.has(w)))].sort((a, b) => idf(b) - idf(a)).slice(0, 3);
  sents.forEach((a, ai) => {
    const dom = dominant(a.sig); if (!dom) { st.no_dim++; return; }
    const keys = kw(a.text); if (keys.length < 2) return;
    const pname = SYM.P[dom.k][dom.neg ? 1 : 0];
    const q = WH[SYM.P[dom.k][0]] + (dom.neg ? " should not / does not" : "") + " — " + d.fm.title + ", " + a.secTitle.toLowerCase() + ": " + keys.join(", ") + "?";
    const live = SYM.read(q);
    const sat = [];
    sents.forEach((c, ci) => { if (+c.sig[dom.k * 2 + (dom.neg ? 1 : 0)] < 1) return; const cw = new Set(words(c.text)); if (keys.filter(k => cw.has(k)).length < 2) return; sat.push({ ci, s: SYM.score(live, c.sig) + keys.filter(k => cw.has(k)).length * 10 }); });
    sat.sort((x, y) => y.s - x.s);
    if (!sat.length || sat[0].ci !== ai) return;
    if (sat.length > 1 && sat[1].s >= sat[0].s && sents[sat[1].ci].P !== a.P) { st.ambiguous++; return; }
    let ctx = a.para.split(/\s+/).slice(0, 160).join(" ");
    const pool = sents.filter(c => c.P !== a.P); let distractor = null;
    if (pool.length && (parseInt(sha(a.text).slice(0, 2), 16) % 10) < 3) { distractor = pool[parseInt(sha(a.text).slice(2, 8), 16) % pool.length]; ctx = distractor.para.split(/\s+/).slice(0, 80).join(" ") + "\n\n" + ctx; st.distractor++; }
    pairsOut.write(JSON.stringify({ id: sid("Q", S.id + a.P + ai), subject: key, S: S.id, C: a.sec.id, P: a.P, dim: pname, q, context: ctx, a: a.text, distractor: !!distractor }) + "\n"); st.pairs++;
  });
  const outp = path.join(ROOT, "symbols", prog, key + ".json"); fs.mkdirSync(path.dirname(outp), { recursive: true });
  fs.writeFileSync(outp, JSON.stringify(S));
}
fs.writeFileSync(path.join(ROOT, "symbols/vocab.json"), JSON.stringify({ v: 1, format: "symbol256-hier", levels: { S: "subject", C: "section", P: "paragraph" }, count: vocab.length, symbols: vocab }));
pairsOut.end(() => console.log(JSON.stringify(st)));
