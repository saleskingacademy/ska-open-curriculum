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
    ("resolved_poincare_marked_open", re.compile(r"(open questions?[^.!?\n]{0,80}Poincar[eé]|Poincar[eé] conjecture[^.!?\n]{0,100}(remains|still)[^.!?\n]{0,60}open)", re.I | re.S)),
    ("resolved_erdos_discrepancy_marked_open", re.compile(r"open questions?.{0,160}Erd[oő]s discrepancy problem", re.I | re.S)),
    ("navier_stokes_turbulence_breakdown", re.compile(r"Navier[-– ]Stokes.{0,180}(failure mode|breakdown).{0,120}turbulen", re.I | re.S)),
]

# Foundational courses may mention frontier problems as downstream context, but must
# not claim those problems are native open questions of the introductory course.
FOUNDATIONAL = {"arithmetic.md", "pre_algebra.md", "algebra_1.md", "algebra_2.md", "precalculus.md"}
NATIVE_OPEN = re.compile(r"open questions? (?:in|of) (?:this field|pre[- ]?algebra|algebra|precalculus|arithmetic).{0,240}(Riemann|P versus NP|P vs\. NP|Birch and Swinnerton)", re.I | re.S)

def find_issues(text, filename):
    """Return heuristic findings, not a proof of factual correctness."""
    found = []
    for name, rx in RULES:
        for match in rx.finditer(text):
            if name == "navier_stokes_turbulence_breakdown":
                # A narrowly identified RANS closure/near-wall limitation is not
                # a claim that turbulence invalidates the underlying equations.
                before = text[max(0, match.start()-24):match.start()]
                after = text[match.start():match.end()+80]
                if (re.search(r"Reynolds[-– ]Averaged\s+$", before, re.I)
                    and "(RANS)" in after
                    and re.search(r"failure mode is often associated with turbulence modeling and near-wall treatment", after, re.I)):
                    continue
            found.append(name)
            break
    if filename in FOUNDATIONAL and NATIVE_OPEN.search(text):
        found.append("frontier_problem_misclassified_in_foundational_course")
    return found


def main():
    issues = []
    for p in KNOW.rglob("*.md"):
        text = p.read_text(encoding="utf-8")
        issues.extend((str(p.relative_to(ROOT)), name) for name in find_issues(text, p.name))
    if issues:
        print("Curriculum integrity lint FAILED:")
        for path, rule in sorted(set(issues)):
            print(f"- {path}: {rule}")
        return 1
    print("Curriculum integrity lint passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
