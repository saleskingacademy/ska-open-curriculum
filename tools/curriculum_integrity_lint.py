#!/usr/bin/env python3
"""Surgical curriculum integrity lint.

Flags high-confidence factual/taxonomy regressions without rewriting source.
It intentionally avoids broad stylistic rules: failures must be reviewed, not auto-fixed.
"""
from pathlib import Path
import re, sys

ROOT = Path(__file__).resolve().parents[1]
KNOW = ROOT / "knowledge"

RULES = [
    ("resolved_geometrization_marked_open", re.compile(r"geometrization conjecture.{0,100}(remains|still).{0,60}(open|active)", re.I | re.S)),
    ("resolved_poincare_marked_open", re.compile(r"(open questions?.{0,80}Poincar[eé]|Poincar[eé] conjecture.{0,100}(remains|still).{0,60}open)", re.I | re.S)),
    ("resolved_erdos_discrepancy_marked_open", re.compile(r"open questions?.{0,160}Erd[oő]s discrepancy problem", re.I | re.S)),
    ("navier_stokes_turbulence_breakdown", re.compile(r"Navier[-– ]Stokes.{0,180}(failure mode|breakdown).{0,120}turbulen", re.I | re.S)),
]

# Foundational courses may mention frontier problems as downstream context, but must
# not claim those problems are native open questions of the introductory course.
FOUNDATIONAL = {"arithmetic.md", "pre_algebra.md", "algebra_1.md", "algebra_2.md", "precalculus.md"}
NATIVE_OPEN = re.compile(r"open questions? (?:in|of) (?:this field|pre[- ]?algebra|algebra|precalculus|arithmetic).{0,240}(Riemann|P versus NP|P vs\. NP|Birch and Swinnerton)", re.I | re.S)

issues = []
for p in KNOW.rglob("*.md"):
    text = p.read_text(encoding="utf-8")
    for name, rx in RULES:
        if rx.search(text):
            issues.append((str(p.relative_to(ROOT)), name))
    if p.name in FOUNDATIONAL and NATIVE_OPEN.search(text):
        issues.append((str(p.relative_to(ROOT)), "frontier_problem_misclassified_in_foundational_course"))

if issues:
    print("Curriculum integrity lint FAILED:")
    for path, rule in sorted(set(issues)):
        print(f"- {path}: {rule}")
    sys.exit(1)

print("Curriculum integrity lint passed.")
