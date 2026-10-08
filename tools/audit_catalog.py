#!/usr/bin/env python3
"""Fail when curriculum subject names, categories or calculated totals diverge."""
import json
from pathlib import Path

root=Path(__file__).resolve().parents[1]
index=json.loads((root/"curriculum/index.json").read_text(encoding="utf-8"))
groups=index["categories"]
all_ids=[sid for group in groups.values() for sid in group["subjects"]]
ids=set(all_ids)
subject_list=set((root/"curriculum/subjects.txt").read_text(encoding="utf-8").split())
meta=set(index["subjects"])
errors=[]
for key,group in groups.items():
    if group["count"] != len(group["subjects"]):
        errors.append("category "+key+": wrong count")
if len(ids) != len(all_ids):
    errors.append("duplicate subject ID in categories")
if index["total_subjects"] != len(ids):
    errors.append("total_subjects differs from subject IDs")
target=len(ids)*index["total_levels"]*index["lessons_per_level"]
if index["total_lessons"] != target:
    errors.append("calculated lesson target differs from catalog size")
if subject_list != ids:
    errors.append("subjects.txt absent: "+repr(sorted(ids-subject_list)[:20])+
                  " extra: "+repr(sorted(subject_list-ids)[:20]))
if meta != ids:
    errors.append("subject metadata absent: "+repr(sorted(ids-meta)[:20])+
                  " extra: "+repr(sorted(meta-ids)[:20]))
for sid,details in index["subjects"].items():
    if details.get("category") not in groups or sid not in groups[details["category"]]["subjects"]:
        errors.append(sid+" assigned to wrong catalog category")
print("Catalog subjects:",len(ids),"| calculated lesson target:",target,"| errors:",len(errors))
for err in errors[:40]:
    print("ERROR",err)
if errors:
    raise SystemExit(1)
