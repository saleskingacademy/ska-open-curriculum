#!/usr/bin/env python3
"""Assign stable, deterministic IDs ONLY where a lesson is missing its ID.

Keeps every lesson under its original subject, level, and lesson position;
preserves title, content and all assessment fields. Does not touch quarantine.
"""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
changed=[]
for path in sorted((ROOT/"content"/"lessons").glob("*.json")):
    rows=json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(rows,list):
        raise SystemExit("Malformed lessons: "+str(path))
    identities={str(x["id"]) for x in rows if x.get("id")}
    used_positions=set()
    repairs=0
    for row in rows:
        if row.get("subject_id") != path.stem:
            raise SystemExit("Wrong-subject row: "+str(path))
        pos=(row["subject_id"],row["level"],row["lesson_number"])
        if pos in used_positions:
            raise SystemExit("Duplicate position: "+str(pos))
        used_positions.add(pos)
        if row.get("id"):
            continue
        if not (1<=row["level"]<=8 and 1<=row["lesson_number"]<=30):
            raise SystemExit("Invalid lesson number: "+str(pos))
        replacement=f"{path.stem}_L{row['level']}_{row['lesson_number']}"
        if replacement in identities:
            raise SystemExit("New ID would collide: "+replacement)
        row["id"]=replacement
        identities.add(replacement)
        repairs+=1
    if repairs:
        path.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
        changed.append((str(path.relative_to(ROOT)),repairs))
print("Stable lesson IDs restored:",sum(x[1] for x in changed))
for item in changed:
    print(item[0],item[1])
