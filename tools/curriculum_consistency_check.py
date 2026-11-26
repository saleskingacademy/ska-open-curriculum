"""Check consistency of the public SKA curriculum corpus.

This is a reporting/QA tool. It deliberately distinguishes:
- indexed subjects,
- actual knowledge files,
- actual structured lesson records,
- calculated lesson targets.

It does not claim a calculated target is populated content.
"""

from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]

def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))

def main():
    subjects_file = ROOT / "curriculum" / "subjects.txt"
    index_file = ROOT / "curriculum" / "index.json"
    knowledge_index = ROOT / "knowledge" / "index.json"

    subject_ids = [x.strip() for x in subjects_file.read_text(encoding="utf-8").splitlines() if x.strip()]
    lesson_files = list((ROOT / "content" / "lessons").glob("*.json"))

    actual_lessons = 0
    lesson_subjects = {}
    for path in lesson_files:
        try:
            data = read_json(path)
            lessons = data if isinstance(data, list) else data.get("lessons", [])
            # Some legacy lesson files are JSON objects keyed by numeric indexes.
            if not lessons and isinstance(data, dict) and all(str(k).isdigit() for k in data):
                lessons = list(data.values())
            actual_lessons += len(lessons)
            for lesson in lessons:
                sid = lesson.get("subject_id")
                if sid:
                    lesson_subjects[sid] = lesson_subjects.get(sid, 0) + 1
        except Exception as exc:
            print(f"INVALID_JSON {path}: {exc}")

    curriculum = read_json(index_file)
    knowledge = read_json(knowledge_index)

    print("SKA CURRICULUM CONSISTENCY REPORT")
    print(f"subjects.txt unique subjects: {len(set(subject_ids))}")
    print(f"curriculum/index.json total_subjects: {curriculum.get('total_subjects')}")
    print(f"knowledge/index.json subjects: {len(knowledge.get('subjects', knowledge if isinstance(knowledge, list) else []))}")
    print(f"lesson dataset files: {len(lesson_files)}")
    print(f"actual structured lesson records: {actual_lessons}")
    print(f"calculated target in curriculum/index.json: {curriculum.get('total_lessons')}")
    print("NOTE: calculated targets are not treated as populated lessons.")

    duplicates = len(subject_ids) - len(set(subject_ids))
    if duplicates:
        print(f"ERROR duplicate subject identifiers: {duplicates}")

    for sid, count in sorted(lesson_subjects.items()):
        if count < 8:
            print(f"WARNING shallow structured subject: {sid} ({count} lessons)")

if __name__ == "__main__":
    main()
