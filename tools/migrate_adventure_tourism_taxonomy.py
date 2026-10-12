#!/usr/bin/env python3
"""Coordinated, guarded local taxonomy migration. Run on a clean development checkout.

Defaults to dry-run. --apply changes the tracked source and two catalogues, then
requires normal build/regeneration and downstream validation before merging.
"""
import argparse
import json
from pathlib import Path

KEY = "adventure_tourism"
OLD = f"knowledge/accounting_finance/{KEY}.md"
NEW = f"knowledge/hospitality/{KEY}.md"

def run(root: Path, apply: bool):
    old, new = root / OLD, root / NEW
    if not old.is_file() or new.exists():
        raise RuntimeError("Expected source absent or destination already exists; refusing change")
    raw = old.read_text(encoding="utf-8")
    if not raw.startswith("---\n") or "\n---\n" not in raw:
        raise RuntimeError("Unexpected course front matter")
    head, body = raw.split("\n---\n", 1)
    old_field = "program: accounting_finance"
    if head.count(old_field) != 1:
        raise RuntimeError("Unexpected program front matter")
    revised = head.replace(old_field, "program: hospitality", 1) + "\n---\n" + body
    idx_path, paths_path = root / "knowledge/index.json", root / "knowledge/paths.json"
    idx_raw, paths_raw = idx_path.read_text(encoding="utf-8"), paths_path.read_text(encoding="utf-8")
    idx, paths = json.loads(idx_raw), json.loads(paths_raw)
    records = [r for r in idx["subjects"] if r.get("key") == KEY]
    if len(records) != 1 or records[0].get("program") != "accounting_finance" or records[0].get("path") != OLD or paths.get(KEY) != OLD:
        raise RuntimeError("Unexpected catalogue state; refusing change")
    if idx_raw.count('"key":"adventure_tourism"') != 1:
        raise RuntimeError("Unexpected index serialization; refusing change")
    old_index_segment = '"key":"adventure_tourism","title":"Adventure Tourism","program":"accounting_finance"'
    new_index_segment = '"key":"adventure_tourism","title":"Adventure Tourism","program":"hospitality"'
    if idx_raw.count(old_index_segment) != 1:
        raise RuntimeError("Unexpected index record layout; refusing change")
    if idx_raw.count('"path":"'+OLD+'"') < 1:
        raise RuntimeError("Expected indexed path missing")
    new_idx = idx_raw.replace(old_index_segment, new_index_segment, 1)
    # Restrict path replacement to the adventure_tourism record, not other records.
    start = new_idx.index('"key":"adventure_tourism"')
    end = new_idx.find('},{"key":', start)
    if end < 0:
        end = len(new_idx)
    fragment = new_idx[start:end]
    if fragment.count('"path":"'+OLD+'"') != 1:
        raise RuntimeError("Unexpected path count in target record")
    new_idx = new_idx[:start] + fragment.replace('"path":"'+OLD+'"', '"path":"'+NEW+'"', 1) + new_idx[end:]
    old_paths_entry = '"adventure_tourism":"'+OLD+'"'
    if paths_raw.count(old_paths_entry) != 1:
        raise RuntimeError("Unexpected paths mapping layout")
    new_paths = paths_raw.replace(old_paths_entry, '"adventure_tourism":"'+NEW+'"', 1)
    assert json.loads(new_idx)["subjects"][next(i for i,r in enumerate(idx["subjects"]) if r["key"]==KEY)]["path"] == NEW
    assert json.loads(new_paths)[KEY] == NEW
    print(json.dumps({"subject": KEY, "from": OLD, "to": NEW, "apply": apply,
                      "files": [OLD, NEW, "knowledge/index.json", "knowledge/paths.json"]}, indent=2))
    if apply:
        new.parent.mkdir(parents=True, exist_ok=True)
        new.write_text(revised, encoding="utf-8")
        idx_path.write_text(new_idx, encoding="utf-8")
        paths_path.write_text(new_paths, encoding="utf-8")
        old.unlink()
        print("Source/catalogue migration complete. Regenerate and validate all downstream artifacts before merging.")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--root", type=Path, default=Path("."))
    p.add_argument("--apply", action="store_true")
    args = p.parse_args()
    run(args.root.resolve(), args.apply)
