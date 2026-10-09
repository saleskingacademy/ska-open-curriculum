#!/usr/bin/env python3
"""Fail closed on republished generic drafts, incorrectly labeled lesson files,
or public subject IDs with no canonical chapter or explicit supplemental label.

Quarantined drafts are retained verbatim in content/quarantine/; this validator
never mutates lesson content, deletes records, or invents new subject labels.
"""
import collections
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSONS = ROOT / "content" / "lessons"
ARCHIVE = ROOT / "content" / "quarantine" / "template-lessons"
QUARANTINE = ROOT / "content" / "QUARANTINE-placeholder-lessons.json"
CANONICAL = ROOT / "knowledge" / "paths.json"
SUPPLEMENTAL = ROOT / "curriculum" / "supplemental_lesson_subjects.json"

def read(p):
    return json.loads(p.read_text(encoding="utf-8"))

def review():
    paths = read(CANONICAL)
    supplemental = read(SUPPLEMENTAL)["subjects"]
    manifest = read(QUARANTINE)
    quarantined = {x["id"] for x in manifest["lessons"]}
    wrong_labeled = [x for x in manifest["lessons"] if x["reason"] == "filed_under_non_subject_id"]
    flagged = [x for x in manifest["lessons"] if x["reason"] == "template_placeholder"]
    archived_ids = set()
    errors = []
    published = []
    seen = set()
    seen_positions = set()
    missing_id_by_file = collections.Counter()

    for path in sorted(ARCHIVE.glob("*.json")):
        for lesson in read(path):
            archived_ids.add(lesson.get("id"))
            if lesson.get("id") not in quarantined:
                errors.append("archived without quarantine listing: " + str(lesson.get("id")))
            if not str(lesson.get("content") or "").startswith("This original Sales King Academy lesson develops"):
                errors.append("unexpected non-template in archived file: " + str(lesson.get("id")))
    if len(archived_ids) != 800 or len(flagged) != 800:
        errors.append(f"Expected 800 preserved template IDs; archive={len(archived_ids)} manifest={len(flagged)}")
    if len(wrong_labeled) != 388:
        errors.append(f"Expected 388 wrong-subject IDs, got {len(wrong_labeled)}")
    if archived_ids != {x["id"] for x in flagged}:
        errors.append("Archive and manifest template ID sets disagree")
    if manifest.get("count") != len(manifest["lessons"]):
        errors.append("Quarantine manifest count is stale")

    lesson_only_files = []
    for path in sorted(LESSONS.glob("*.json")):
        sid = path.stem
        if sid not in paths:
            lesson_only_files.append(sid)
        if sid not in paths and sid not in supplemental:
            errors.append(f"Unclassified supplemental subject: {sid}")
        values = read(path)
        if not isinstance(values, list):
            errors.append(f"{path.name} is not an array")
            continue
        for lesson in values:
            ident = lesson.get("id")
            pos = (sid, lesson.get("level"), lesson.get("lesson_number"))
            if not ident:
                missing_id_by_file[path.name] += 1
                errors.append("Missing lesson ID in " + path.name + ": " + str(pos))
            if ident in seen and ident:
                errors.append("Duplicate published lesson ID in " + path.name + ": " + str(ident))
            if ident:
                seen.add(ident)
            if lesson.get("subject_id") != sid:
                errors.append("Wrong subject assigned: " + str(ident))
            if ident in quarantined:
                errors.append("Quarantined lesson republished: " + str(ident))
            if str(lesson.get("content") or "").startswith("This original Sales King Academy lesson develops"):
                errors.append("Unfinished boilerplate published: " + str(ident))
            if not isinstance(lesson.get("level"), int) or lesson["level"] not in range(1,9):
                errors.append("Invalid level: " + str(ident))
            if pos in seen_positions:
                errors.append("Duplicate lesson position in " + path.name + ": " + str(pos))
            seen_positions.add(pos)
            published.append(pos)
    if len(published) != len(set(published)):
        errors.append("Duplicate subject/level/lesson position")
    if set(lesson_only_files) != set(supplemental):
        errors.append("Supplemental registry differs from published files: missing=" +
                      repr(sorted(set(lesson_only_files)-set(supplemental)))+" extra="+
                      repr(sorted(set(supplemental)-set(lesson_only_files))))
    print(json.dumps({
        "published_lessons":len(published), "archived_templates":len(archived_ids),
        "wrong_subject_ids_quarantined":len(wrong_labeled),
        "supplemental_subjects":len(lesson_only_files),
        "structural_errors":len(errors), "missing_id_files":dict(missing_id_by_file), "errors":errors[:60]
    }, indent=2))
    if errors:
        raise SystemExit(1)

if __name__ == "__main__":
    review()
