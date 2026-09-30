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
// ---- natural phrasing (templates, no outside model) ----
let SUBJ_TF = new Map(), TITLE_W = new Set();
function phrase(text) { // most distinctive 1-2 word phrase; terms that recur in the subject win
  const w = text.replace(/[^A-Za-z0-9\s-]/g, " ").split(/\s+/).filter(Boolean); let best = "", bs = -1;
  for (let i = 0; i < w.length; i++) { const a = w[i].toLowerCase(); if (a.length < 4 || STOP.has(a)) continue;
    if (TITLE_W.has(a)) continue;
    const one = idf(a) * ((SUBJ_TF.get(a) || 0) >= 2 ? 1 : 0.35); if (one > bs) { bs = one; best = w[i]; }
    const b = (w[i + 1] || "").toLowerCase(); if (b.length >= 4 && !STOP.has(b)) { const bg = a + " " + b; const two = (idf(a) + idf(b) * 0.8) * ((SUBJ_TF.get(bg) || 0) >= 2 ? 1.4 : 0.3); if (two > bs) { bs = two; best = w[i] + " " + w[i + 1]; } } }
  return best.replace(/^[A-Z](?=[a-z])/, c => c.toLowerCase());
}
function naturalQ(dim, neg, a, title) {
  const subj = title, X = phrase(a.text) || "this";
  const def = a.text.match(/^(?:The |A |An )?([A-Za-z][\w\s\-()]{2,48}?) (is|are) (?:an? |the |defined as )|^(?:The |A |An )?([A-Za-z][\w\s\-()]{2,48}?) (refers to|means|describes) /);
  if (dim === "what" && !neg && def) return (def[2] === "are" ? "What are " : "What is ") + (def[1] || def[3]).trim().replace(/^[A-Z](?=[a-z])/, c => c.toLowerCase()) + "?";
  const T = { what: ["What does " + subj + " teach about " + X + "?", "What should be avoided with " + X + " in " + subj + "?"],
    how: ["How is " + X + " used in " + subj + "?", "How should " + X + " not be handled in " + subj + "?"],
    why: ["Why does " + X + " matter in " + subj + "?", "Why is " + X + " not always the right choice in " + subj + "?"],
    when: ["When is " + X + " applied in " + subj + "?", "When should " + X + " not be used in " + subj + "?"],
    where: ["Where does " + X + " come up in " + subj + "?", "Where does " + X + " not apply in " + subj + "?"],
    who: ["Who is involved with " + X + " in " + subj + "?", "Who should not be handling " + X + " in " + subj + "?"],
    which: ["Which approach to " + X + " fits " + subj + "?", "Which uses of " + X + " should be ruled out in " + subj + "?"],
    whether: ["Is " + X + " always required in " + subj + "?", "Is " + X + " ever unnecessary in " + subj + "?"] };
  return T[dim][neg ? 1 : 0];
}
function dims(sig) { // main dimension + strongest non-"what" dimension
  const out = [], d = dominant(sig); if (!d) return out; out.push(d); let best = 0, bk = -1, bn = 0;
  for (let k = 1; k < 8; k++) for (const n of [0, 1]) { const v = +sig[k * 2 + n]; if (v > best) { best = v; bk = k; bn = n; } }
  if (bk > 0 && !(bk === d.k && (bn === 1) === d.neg)) out.push({ k: bk, neg: bn === 1 }); return out;
}
const files = walk(path.join(ROOT, "knowledge")); const df = new Map(); const docs = [];
for (const f of files) { const d = parse(f); d.file = path.relative(ROOT, f); docs.push(d); const seen = new Set(); d.secs.forEach(s => s.paras.forEach(p => words(p).forEach(w => seen.add(w)))); seen.forEach(w => df.set(w, (df.get(w) || 0) + 1)); }
const N = docs.length, idf = w => Math.log((N + 1) / ((df.get(w) || 0) + 1));
fs.mkdirSync(path.join(ROOT, "out"), { recursive: true });
const pairsOut = fs.createWriteStream(path.join(ROOT, "out/pairs.jsonl"));
const vocab = []; const st = { subjects: 0, sections: 0, paragraphs: 0, sentences: 0, pairs: 0, ambiguous: 0, no_dim: 0, distractor: 0, what_thinned: 0, dims: {} };
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
  TITLE_W = new Set(words(d.fm.title || "")); SUBJ_TF = new Map(); sents.forEach(c => { const w = words(c.text); w.forEach((x, i) => { SUBJ_TF.set(x, (SUBJ_TF.get(x) || 0) + 1); if (w[i + 1]) SUBJ_TF.set(x + " " + w[i + 1], (SUBJ_TF.get(x + " " + w[i + 1]) || 0) + 1); }); });
  const subjPairs = [];
  const kw = x => [...new Set(words(x).filter(w => w.length > 3 && !STOP.has(w)))].sort((a, b) => idf(b) - idf(a)).slice(0, 3);
  sents.forEach((a, ai) => {
    if (a.text.indexOf("?") >= 0) { st.question_sentences = (st.question_sentences || 0) + 1; return; }
    const ds = dims(a.sig); if (!ds.length) { st.no_dim++; return; }
    const keys = kw(a.text); if (keys.length < 2) return;
    ds.forEach((dom, di) => {
    const dim = SYM.P[dom.k][0], pname = SYM.P[dom.k][dom.neg ? 1 : 0];
    if (dim === "what" && !dom.neg && (parseInt(sha(a.text).slice(8, 10), 16) % 100) >= 45) { st.what_thinned++; return; }
    const q = naturalQ(dim, dom.neg, a, d.fm.title);
    const live = SYM.read(q + " " + keys.join(" "));
    const sat = [];
    sents.forEach((c, ci) => { if (+c.sig[dom.k * 2 + (dom.neg ? 1 : 0)] < 1) return; const cw = new Set(words(c.text)); if (keys.filter(k => cw.has(k)).length < 2) return; sat.push({ ci, s: SYM.score(live, c.sig) + keys.filter(k => cw.has(k)).length * 10 }); });
    sat.sort((x, y) => y.s - x.s);
    if (!sat.length || sat[0].ci !== ai) return;
    if (sat.length > 1 && sat[1].s >= sat[0].s && sents[sat[1].ci].P !== a.P) { st.ambiguous++; return; }
    let ctx = a.para.split(/\s+/).slice(0, 160).join(" ");
    const pool = sents.filter(c => c.P !== a.P); let distractor = null;
    if (pool.length && (parseInt(sha(a.text + di).slice(0, 2), 16) % 10) < 3) { distractor = pool[parseInt(sha(a.text + di).slice(2, 8), 16) % pool.length]; ctx = distractor.para.split(/\s+/).slice(0, 80).join(" ") + "\n\n" + ctx; st.distractor++; }
    pairsOut.write(JSON.stringify({ id: sid("Q", S.id + a.P + ai + "|" + di), subject: key, S: S.id, C: a.sec.id, P: a.P, dim: pname, q, context: ctx, a: a.text,
      constraints: { subject: key, dimension: pname, key_terms: keys, min_terms: 2, unique: true, candidates: sat.length }, distractor: !!distractor }) + "\n"); st.pairs++;
    st.dims[pname] = (st.dims[pname] || 0) + 1;
    subjPairs.push({ q: q, a: a.text, dim: pname, keys: keys });
    });
  });
  // ---- interactive study pack: flashcards, fill-in-the-blank, matching (all from this subject's own text) ----
  (function () {
    const pick = (arr, n, salt) => arr.map(x => [sha(salt + JSON.stringify(x)), x]).sort((u, v) => u[0] < v[0] ? -1 : 1).slice(0, n).map(z => z[1]);
    const byDim = {}; subjPairs.forEach(x => { (byDim[x.dim] = byDim[x.dim] || []).push(x); });
    const cards = []; const dimsOrder = Object.keys(byDim).sort();
    for (let r = 0; cards.length < 30 && r < 60; r++) dimsOrder.forEach(dk => { const x = byDim[dk][r]; if (x && cards.length < 30) cards.push({ q: x.q, a: x.a, dim: dk }); });
    const concept = t => t.length > 4 && (SUBJ_TF.get(t) || 0) >= 3 && !/(ing|ed|ly|ize|ise|ate)$/.test(t);
    const pool = [...new Set(subjPairs.flatMap(x => x.keys))].filter(concept);
    const cloze = [];
    for (const x of pick(subjPairs, 80, "cz")) {
      if (cloze.length >= 20) break;
      const k = x.keys.find(concept); if (!k) continue; const re = new RegExp("\\b" + k.replace(/[^a-z0-9]/g, "") + "\\b", "i");
      if (!re.test(x.a)) continue;
      const others = pool.filter(t => t !== k && t.length > 3).slice(0);
      if (others.length < 3) continue;
      const wrong = pick(others, 3, x.a);
      cloze.push({ text: x.a.replace(re, "_____"), answer: k, choices: pick([k].concat(wrong), 4, "o" + x.a) });
    }
    const match = []; const seenT = new Set();
    for (const c of sents) {
      if (match.length >= 8) break;
      const m = c.text.match(/^(?:The |A |An )?([A-Za-z][\w\s\-()]{2,40}?) (?:is|are) (?:an? |the )(.{20,160}?)[.;]/);
      if (!m) continue; const term = m[1].trim(); if (seenT.has(term.toLowerCase()) || term.split(" ").length > 5) continue;
      seenT.add(term.toLowerCase()); match.push({ term: term, meaning: m[2].trim() });
    }
    const pack = { v: 1, subject: key, title: d.fm.title, S: S.id, flashcards: cards, cloze: cloze, matching: match, license: "CC-BY-SA-4.0" };
    fs.mkdirSync(path.join(ROOT, "study"), { recursive: true });
    fs.writeFileSync(path.join(ROOT, "study", key + ".json"), JSON.stringify(pack));
    st.study_cards = (st.study_cards || 0) + cards.length; st.study_cloze = (st.study_cloze || 0) + cloze.length; st.study_match = (st.study_match || 0) + match.length;
  })();
  const outp = path.join(ROOT, "symbols", prog, key + ".json"); fs.mkdirSync(path.dirname(outp), { recursive: true });
  fs.writeFileSync(outp, JSON.stringify(S));
}
fs.writeFileSync(path.join(ROOT, "symbols/vocab.json"), JSON.stringify({ v: 1, format: "symbol256-hier", levels: { S: "subject", C: "section", P: "paragraph" }, count: vocab.length, symbols: vocab }));
pairsOut.end(() => console.log(JSON.stringify(st)));
