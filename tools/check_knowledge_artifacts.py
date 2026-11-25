#!/usr/bin/env python3
"""Fails if a served knowledge page carries leaked tool output instead of teaching text.
Found 2026-11-25: 207 subject pages showed "name heuristic. unparsed reply: [object Object]"
or "name heuristic - model placement unavailable" as their course description.
run: python3 tools/check_knowledge_artifacts.py"""
import pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
BAD = re.compile(r"\[object Object\]|unparsed reply|model placement unavailable|name heuristic", re.I)
hits = []
for p in sorted((ROOT / "knowledge").rglob("*.md")):
    for i, line in enumerate(p.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
        if BAD.search(line):
            hits.append("%s:%d: %s" % (p.relative_to(ROOT), i, line.strip()[:120]))
print("\n".join(hits[:50]) or "No leaked tool output in knowledge pages.")
sys.exit(1 if hits else 0)
