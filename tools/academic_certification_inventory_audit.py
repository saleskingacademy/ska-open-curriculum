#!/usr/bin/env python3
"""Read-only SKA catalogue audit. No writes to curriculum or generated indexes."""
import argparse
import json
from collections import Counter
from pathlib import Path


def audit(root):
    index_file = root / "knowledge" / "index.json"
    if not index_file.is_file():
        raise FileNotFoundError(index_file)
    data = json.loads(index_file.read_text(encoding="utf-8"))
    subjects = data.get("subjects")
    if not isinstance(subjects, list):
        raise ValueError("knowledge/index.json: subjects must be a list")
    issues = []
    seen = Counter()
    programs = Counter()
    for i, entry in enumerate(subjects):
        key = entry.get("key")
        program = entry.get("program")
        path = entry.get("path")
        if not all(isinstance(v, str) and v for v in (key, program, path)):
            issues.append({"row": i, "type": "missing_required_metadata", "key": key})
            continue
        seen[key] += 1
        programs[program] += 1
        relative = Path(path)
        if relative.is_absolute() or ".." in relative.parts:
            issues.append({"row": i, "key": key, "type": "unsafe_path", "path": path})
            continue
        if not (root / relative).is_file():
            issues.append({"row": i, "key": key, "type": "missing_content_file", "path": path})
        if len(relative.parts) >= 3 and relative.parts[0] == "knowledge":
            if relative.parts[1] != program:
                issues.append({"row": i, "key": key, "type": "program_path_mismatch",
                               "program": program, "path": path})
        else:
            issues.append({"row": i, "key": key, "type": "unexpected_content_path", "path": path})
    for key, n in sorted(seen.items()):
        if n > 1:
            issues.append({"key": key, "type": "duplicate_subject_key", "count": n})
    declared = data.get("count")
    if declared != len(subjects):
        issues.append({"type": "declared_count_mismatch", "declared": declared,
                       "actual_index_rows": len(subjects)})
    return {
        "audit_scope": "index consistency and file existence only; not academic completion",
        "declared_count": declared,
        "indexed_rows": len(subjects),
        "unique_subject_keys": len(seen),
        "program_counts": dict(sorted(programs.items())),
        "issue_counts": dict(sorted(Counter(x["type"] for x in issues).items())),
        "issues": issues,
        "certification_ready_count": None,
        "note": "Taxonomy semantic validity, prerequisites, assessments, source accuracy, "
                "private tests and student delivery require separate reviews."
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--output", type=Path, help="Optional JSON report path")
    args = parser.parse_args()
    report = audit(args.root.resolve())
    output = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.write_text(output, encoding="utf-8")
    else:
        print(output)


if __name__ == "__main__":
    main()
