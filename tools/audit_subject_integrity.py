#!/usr/bin/env python3
"""Audit real subject identity, lesson alignment and cross-subject contamination.

--repair-index updates ONLY derived knowledge/index.json from authoritative
paths and actual Markdown frontmatter; teaching prose is never rewritten.
Suspected topic drift is reported for human review, not silently moved.
"""
import argparse
import collections
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KNOW = ROOT / "knowledge"
PATTERNS = {
    "icp_definition": (r"\bintracranial pressure\b", r"\bcerebrospinal fluid\b"),
    "multithreading_deals": (r"\bCPU thread scheduling\b", r"\boperating.system threads\b"),
    "tonality_and_voice": (r"\bmusical key signature\b", r"\bchord progression\b"),
    "funnel_architecture": (r"\bmulti.resolution funnel architectures\b",
                            r"\bimage classification and object detection\b",
                            r"\bdata ingestion\b.{0,180}\bdata processing\b"),
    "ai_call_preparation": (r"\bkernel system calls\b",),
}
def read(path):
    return json.loads(path.read_text(encoding="utf-8"))
def frontmatter(content):
    match = re.match(r"\A---\r?\n(.*?)\r?\n---\r?\n", content, re.S)
    if not match:
        return {}, content
    meta = {}
    for line in match.group(1).splitlines():
        pair = re.match(r"^([a-zA-Z_0-9]+):\s*(.*)$", line)
        if pair:
            meta[pair.group(1)] = pair.group(2).strip().strip('"').strip("'")
    return meta, content[match.end():]
def audit(repair):
    paths = read(KNOW / "paths.json")
    index_path = KNOW / "index.json"
    index = read(index_path)
    existing = {s["key"]: s for s in index["subjects"]}
    corrected = {}
    structural, warnings = [], []
    paragraphs = collections.defaultdict(set)
    changed = 0
    for sid, rel in sorted(paths.items()):
        path = ROOT / rel
        if not path.is_file():
            structural.append({"id":sid, "issue":"missing_file", "path":rel})
            continue
        raw = path.read_bytes()
        content = raw.decode("utf-8")
        meta, body = frontmatter(content)
        folder = path.parent.name
        if path.stem != sid or meta.get("key") != sid or meta.get("program") != folder:
            structural.append({"id":sid, "issue":"filename_or_frontmatter_mismatch",
                               "file":path.stem, "key":meta.get("key"), "program":meta.get("program"), "folder":folder})
        h = re.search(r"^#\s+(.+)$", body, re.M)
        if h and re.sub(r"\W+", "", h.group(1).lower()) != re.sub(r"\W+", "", meta.get("title", "").lower()):
            warnings.append({"id":sid, "issue":"main_heading_differs_from_subject_title",
                             "heading":h.group(1)[:90], "title":meta.get("title")})
        for pattern in PATTERNS.get(sid, ()):
            if re.search(pattern, body, re.I | re.S):
                warnings.append({"id":sid, "issue":"wrong_discipline_concept", "pattern":pattern})
        for paragraph in re.split(r"\n\s*\n", body):
            normalized = re.sub(r"\s+", " ", paragraph.lower()).strip()
            if len(normalized) >= 350 and len(normalized.split()) >= 55:
                paragraphs[hashlib.sha256(normalized.encode("utf-8")).hexdigest()].add(sid)
        row = dict(existing.get(sid, {}))
        row.update({"key":sid, "title":meta.get("title") or sid.replace("_"," ").title(),
                    "program":folder, "course_level":int(meta.get("course_level") or row.get("course_level") or 1),
                    "path":rel, "dna16":meta.get("dna16") or None, "l4_address":meta.get("l4_address") or "",
                    "sections":list(dict.fromkeys(m.group(1).upper() for m in re.finditer(r"^##\s+(.+)$", body, re.M))),
                    "chars":len(content), "sha256":hashlib.sha256(raw).hexdigest()})
        corrected[sid] = row
        if row != existing.get(sid):
            changed += 1
            if not repair:
                structural.append({"id":sid, "issue":"stale_knowledge_index"})
    if repair:
        index["subjects"] = [corrected[k] for k in sorted(corrected)]
        index["count"] = len(corrected)
        index_path.write_text(json.dumps(index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    for sid in set(existing) - set(paths):
        structural.append({"id":sid, "issue":"index_without_canonical_path"})
    lesson_count = 0
    for path in sorted((ROOT/"content"/"lessons").glob("*.json")):
        try:
            rows=read(path)
            if not isinstance(rows,list):
                structural.append({"file":path.name,"issue":"lessons_not_list"})
                continue
            for row in rows:
                lesson_count += 1
                sid = row.get("subject_id")
                if sid != path.stem:
                    structural.append({"file":path.name,"lesson":row.get("id"),"actual_subject":sid,"issue":"lesson_subject_file_mismatch"})
                if sid not in paths:
                    warnings.append({"file":path.name,"lesson":row.get("id"),"issue":"lesson_subject_not_in_knowledge"})
                text = str(row.get("content") or "")
                if len(text.strip()) < 180:
                    warnings.append({"file":path.name,"lesson":row.get("id"),"issue":"thin_lesson"})
                for pattern in PATTERNS.get(str(sid),()):
                    if re.search(pattern,text,re.I|re.S):
                        warnings.append({"file":path.name,"lesson":row.get("id"),
                                         "issue":"wrong_discipline_concept","pattern":pattern})
        except (OSError,ValueError,TypeError) as exc:
            structural.append({"file":path.name,"issue":"invalid_lesson_json","error":str(exc)})
    duplicate = [{"sha256":p,"subjects":sorted(ids)} for p,ids in paragraphs.items() if len(ids)>1]
    report={"subjects":len(paths),"indexed":len(corrected),"lessons":lesson_count,
            "recomputed_index_rows":changed,"structural_errors":structural,
            "suspected_topic_mismatches":warnings,
            "cross_subject_duplicate_paragraph_groups":duplicate,
            "rule":"Only metadata is auto-repaired; topic suspicions require editorial inspection."}
    return report
if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--repair-index",action="store_true")
    parser.add_argument("--report",default="audit-results/subject-integrity.json")
    args=parser.parse_args()
    result=audit(args.repair_index)
    dst=ROOT/args.report
    dst.parent.mkdir(parents=True,exist_ok=True)
    dst.write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    for key in ("subjects","indexed","lessons","recomputed_index_rows"):
        print(key, result[key])
    for key in ("structural_errors","suspected_topic_mismatches","cross_subject_duplicate_paragraph_groups"):
        print(key,len(result[key]))
        for item in result[key][:20]:
            print("FINDING",json.dumps(item,ensure_ascii=False))
    if result["structural_errors"]:
        raise SystemExit(1)
