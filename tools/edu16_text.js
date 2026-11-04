// Education-16 paragraph text by address (Kaleb, 2026-11-04: "use spent memory for addressed
// material first, then symbolistic compression"). The worker answers from these: a question is
// routed to chapters, the chapter's paragraphs are read by their Education-16 address, ranked by
// symbols + words, and the best sentence answers, with its address.
//
// Reads knowledge/**/*.md with the SAME parsing and paragraph ids as tools/sat_pairs.js and the
// paragraph addresses in edu16/<subject>.json, and writes:
//   edu16/text/<chapter key>.json  {key, title, edu16, subject, paras: [[edu16, sym16, text], ...]}
//   edu16/text/index.json          {chapters: {key: [edu16, title, subject, n_paras, top words]}}
// Paragraph text is the published curriculum itself (this repo is public); nothing new is written.
const fs = require("fs"), path = require("path"), crypto = require("crypto");
const ROOT = path.join(__dirname, "..");
const sha = s => crypto.createHash("sha256").update(s).digest("hex");
const sid = (lvl, s) => lvl + parseInt(sha(s).slice(0, 12), 16).toString(36).padStart(9, "0");
const STOP = new Set("the a an and or of to in on for with by at from as is are was were be been being this that these those it its their they them than then into over under about can may might must should would could will not no but so if when while which what who how why also more most such each other any all some one two use used using within between".split(" "));
function walk(d, out = []) { for (const f of fs.readdirSync(d)) { const p = path.join(d, f); fs.statSync(p).isDirectory() ? walk(p, out) : f.endsWith(".md") && out.push(p); } return out; }
function parse(file) {                       // identical to tools/sat_pairs.js parse()
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
const plain = s => s.replace(/[*_`>|#]+/g, " ").replace(/\[([^\]]+)\]\([^)]+\)/g, "$1").replace(/\s+/g, " ").trim();
// pid -> text, for every knowledge page
const byPid = new Map();
for (const file of walk(path.join(ROOT, "knowledge"))) {
  const d = parse(file), key = d.fm.key; if (!key) continue;
  const anchor = [d.fm.dna16, d.fm.l4_address, d.fm.chain256_anchor, key].join("|");
  d.secs.forEach((sec, si) => sec.paras.forEach((p, pi) => byPid.set(sid("P", anchor + "|" + si + "|" + pi + "|" + sha(p).slice(0, 8)), plain(p))));
}
const OUT = path.join(ROOT, "edu16", "text"); fs.mkdirSync(OUT, { recursive: true });
const index = {}; let paras = 0, missing = 0;
for (const f of fs.readdirSync(path.join(ROOT, "edu16")).filter(f => f.endsWith(".json")).sort()) {
  const subj = JSON.parse(fs.readFileSync(path.join(ROOT, "edu16", f), "utf8"));
  for (const ch of subj.chapters || []) {
    if (ch.cross_listed || !ch.sections) continue;
    const rows = [];
    for (const sec of ch.sections) for (const p of sec.paragraphs || []) {
      const t = byPid.get(p.pid); if (!t) { missing++; continue; }
      rows.push([p.edu16, p.sym16, t]);
    }
    if (!rows.length) continue;
    const tf = {}; rows.forEach(r => r[2].toLowerCase().replace(/[^a-z0-9\s-]/g, " ").split(/\s+/).forEach(w => { if (w.length > 3 && !STOP.has(w)) tf[w] = (tf[w] || 0) + 1; }));
    const top = Object.keys(tf).sort((a, b) => tf[b] - tf[a] || (a < b ? -1 : 1)).slice(0, 24);
    const title = (ch.key || "").replace(/_/g, " ");
    fs.writeFileSync(path.join(OUT, ch.key + ".json"), JSON.stringify({ key: ch.key, title, edu16: ch.edu16, subject: subj.id, paras: rows }));
    index[ch.key] = [ch.edu16, title, subj.id, rows.length, top.join(" ")];
    paras += rows.length;
  }
}
fs.writeFileSync(path.join(OUT, "index.json"), JSON.stringify({ v: 1, built: "tools/edu16_text.js", chapters: index }));
console.log(JSON.stringify({ chapters: Object.keys(index).length, paragraphs: paras, missing_text: missing }));
