#!/usr/bin/env python3
"""One-time surgical publication repair for duplicate subject/level/lesson slots.

The original first lesson is kept at its published slot (existing lookup
behavior). Each conflicting lesson is preserved in a separate review archive,
with its original ID, title, text, and assessments. No content is rewritten.
This tool fails if an archive already exists, to avoid accidental overwrite.
"""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
PUBLISHED=ROOT/"content"/"lessons"
ARCHIVED=ROOT/"content"/"quarantine"/"overlapping-lessons"
ARCHIVED.mkdir(parents=True,exist_ok=True)
total=0
for path in sorted(PUBLISHED.glob("*.json")):
    rows=json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(rows,list):
        raise SystemExit("Malformed lesson array: "+str(path))
    seen=set()
    keep, collisions=[], []
    ids=set()
    for x in rows:
        if not x.get("id"):
            raise SystemExit("Missing ID must be repaired first: "+str(path))
        if x["id"] in ids:
            raise SystemExit("Duplicate same ID needs manual review: "+str(x["id"]))
        ids.add(x["id"])
        if x.get("subject_id")!=path.stem:
            raise SystemExit("Misfiled subject: "+str(path))
        position=(x.get("level"),x.get("lesson_number"))
        if position in seen:
            collisions.append(x)
        else:
            seen.add(position)
            keep.append(x)
    if collisions:
        archive_path=ARCHIVED/(path.stem+"_conflicting_positions.json")
        if archive_path.exists():
            raise SystemExit("Would overwrite existing review archive: "+str(archive_path))
        archive={"reason":"Distinct lessons shared a subject/level/lesson slot.",
                 "policy":"The first occurrence keeps the original public slot; all competing content is retained verbatim as structured lesson fields for review.",
                 "subject_id":path.stem,
                 "lessons":collisions}
        archive_path.write_text(json.dumps(archive,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
        path.write_text(json.dumps(keep,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
        total+=len(collisions)
        print(path.name,"quarantined conflicts:",len(collisions),"kept:",len(keep))
print("Total colliding lessons preserved for review:",total)
