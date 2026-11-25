#!/usr/bin/env python3
"""Exact checks for the worked figures in the business lessons merged on 2026-11-25
(ChatGPT drafts, PRs #13-#15). Each case recomputes a figure with exact fractions and
confirms the lesson file states that figure, so a later edit cannot silently break it.

run: python3 tools/validate_arithmetic_business_lessons.py
"""
from fractions import Fraction as F
from math import sqrt
import pathlib, sys, json

ROOT = pathlib.Path(__file__).resolve().parents[1]
S = "curriculum/business/sales/"
L1 = "curriculum/business/sales/level1/"
BF = "curriculum/business/foundations/"


def pct(a, b):
    return F(a) / F(b) * 100


def money(x):
    """$1,234 or $1,234.56 exactly as written in the lessons"""
    x = F(x)
    s = "{:,.2f}".format(float(x))
    return "$" + (s[:-3] if s.endswith(".00") else s)


def num(x, places=None):
    x = F(x)
    if places is None:
        return ("{:,}".format(int(x))) if x.denominator == 1 else str(float(x))
    return "{:.{p}f}".format(float(x), p=places)


# (file, value computed exactly, text that must appear in the file)
CASES = [
    # finance: unit economics and cash runway
    ("curriculum/business/finance/unit_economics_and_cash_runway.md", F(2499 - 800), "$1,699/customer-month"),
    ("curriculum/business/finance/unit_economics_and_cash_runway.md", F(999 - 1200), "−$201"),
    ("curriculum/business/finance/unit_economics_and_cash_runway.md", F(999 + 1699 - 1200), "$1,498"),
    ("curriculum/business/finance/unit_economics_and_cash_runway.md", F(1200, 1699), "0.71 months"),
    ("curriculum/business/finance/unit_economics_and_cash_runway.md", F(40000, 6000), "6.67 months"),
    ("curriculum/business/finance/unit_economics_and_cash_runway.md", F(40000, 8000), "runway becomes 5 months"),
    ("curriculum/business/finance/unit_economics_and_cash_runway.md", F(52000, 7500), "6.93 months"),
    ("curriculum/business/finance/unit_economics_and_cash_runway.md", F(52000, 23500 - 13000), "4.95 months"),
    # marketing: incrementality
    ("curriculum/business/marketing/advanced_incrementality_and_experiment_design.md", pct(140, 2000), "= 7%"),
    ("curriculum/business/marketing/advanced_incrementality_and_experiment_design.md", (F(7) - 5) / 5 * 100, "= 40%"),
    ("curriculum/business/marketing/advanced_incrementality_and_experiment_design.md", 40 * 60 - 1500, "= $900"),
    # sales: ethical discovery
    (S + "ethical_discovery_and_qualification.md", F(4 * 80), "$320"),
    (S + "ethical_discovery_and_qualification.md", F(250) * F(12, 100), "250×.12=30"),
    (S + "ethical_discovery_and_qualification.md", F(6 * 55), "6×$55=$330"),
    (S + "ethical_discovery_and_qualification.md", F(180) * F(15, 100), "27 missed requests"),
    (S + "ethical_discovery_and_qualification.md", F(5 * 70), "$350 contribution"),
    # sales: deal diagnosis
    (S + "advanced_evidence_based_deal_diagnosis.md", F(35 * 45), "$1,575/month"),
    (S + "advanced_evidence_based_deal_diagnosis.md", F(3, 10) * 1200 - 100, "= $260"),
    (S + "advanced_evidence_based_deal_diagnosis.md", F(5, 100) * 1200 - 100, "−$40"),
    (S + "advanced_evidence_based_deal_diagnosis.md", F(100, 1200) * 100, "8.33%"),
    # sales: module assessment
    (S + "assessment_advanced_evidence_and_forecasting.md", F(50 * 38), "$1,900/month"),
    (S + "assessment_advanced_evidence_and_forecasting.md", F(2499 * 12 + 1499), "$31,487"),
    (S + "assessment_advanced_evidence_and_forecasting.md", F(1900 * 12 - 31487), "−$8,687"),
    (S + "assessment_advanced_evidence_and_forecasting.md", F(25, 100) * 2000 - 200, "=$300"),
    (S + "assessment_advanced_evidence_and_forecasting.md", F(28 * 52 * 12), "$17,472"),
    (S + "assessment_advanced_evidence_and_forecasting.md", F(1850 * 12 + 1200), "$23,400"),
    (S + "assessment_advanced_evidence_and_forecasting.md", F(28 * 52 * 12 - (1850 * 12 + 1200)), "−$5,928"),
    # sales: account management and retention
    (S + "account_management_and_retention.md", F(20000 - 2000 + 3000 - 1000), "=$20,000"),
    (S + "account_management_and_retention.md", F(24000 - 2400 + 4000 - 1200), "=$24,400"),
    (S + "account_management_and_retention.md", F(24400, 24000) * 100, "101.67%"),
    (S + "account_management_and_retention.md", F(14500, 15000) * 100, "96.67%"),
    # sales: negotiation
    (S + "negotiation_and_mutual_value.md", F(2499) * F(8, 10), "$1,999.20"),
    (S + "negotiation_and_mutual_value.md", F(2499) * F(8, 10) - 900, "$1,099.20"),
    (S + "negotiation_and_mutual_value.md", (F(2499) - F(2499) * F(8, 10)) * 12, "$5,997.60"),
    (S + "negotiation_and_mutual_value.md", F((1524 - 1124) * 18), "=$7,200"),
    (S + "negotiation_and_mutual_value.md", F(2299 - 1050), "$1,249/month"),
    # sales: pipeline forecasting and calibration (Brier scores)
    (S + "sales_pipeline_forecasting_and_calibration.md", F(2000 + 8000 + 9000 + 4000), "=$23,000"),
    (S + "sales_pipeline_forecasting_and_calibration.md",
     (F(2, 10) ** 2 + F(6, 10) ** 2 + F(4, 10) ** 2 + F(8, 10) ** 2) / 4, "=.30"),
    (S + "sales_pipeline_forecasting_and_calibration.md",
     (F(1, 10) ** 2 + F(3, 10) ** 2 + F(8, 10) ** 2 + F(6, 10) ** 2) / 4, "average .275"),
    (S + "sales_pipeline_forecasting_and_calibration.md", F(3000 + 12000 + 4000), "weighted $19,000"),
    # sales: integrated capstone
    (S + "advanced_sales_mastery_integrated_capstone.md", F(2499) * F(85, 100), "$2,124.15"),
    (S + "advanced_sales_mastery_integrated_capstone.md", (F(2499) - F(2499) * F(85, 100)) * 12, "$4,498.20"),
    (S + "advanced_sales_mastery_integrated_capstone.md", F(12000) / 4 + F(24000) / 2 + F(18000) * 3 / 4, "$28,500"),
    (S + "advanced_sales_mastery_integrated_capstone.md",
     (F(2, 10) ** 2 + F(4, 10) ** 2 + F(7, 10) ** 2 + F(1, 10) ** 2) / 4, "0.175"),
    (S + "advanced_sales_mastery_integrated_capstone.md", F(2200) * F(9, 10) - 850, "$1,130"),
    (S + "advanced_sales_mastery_integrated_capstone.md", F(2400) * F(95, 100), "$2,280"),
    # sales: corrected foundations / prospect research / solution design
    (S + "sales_foundations_buyer_journey.md", F(3, 10) * F(1, 3) * F(1, 4), "=.025"),
    (S + "sales_foundations_buyer_journey.md", pct(24, 72), "33.33%"),
    (S + "sales_prospect_research_and_contact.md", pct(90, 400), "22.5%"),
    (S + "sales_prospect_research_and_contact.md", pct(150, 240), "62.5%"),
    (S + "sales_solution_design_and_proposals.md", F((1800 - 700) * 3 - 900), "$2,400"),
    (S + "sales_solution_design_and_proposals.md", F(2000 * 3 - 1800 * 3), "$600"),
    # level-1 drafts
    ("curriculum/computer_science/ai_foundations/L1_1_what_ai_is_and_how_to_evaluate_it.md", pct(35, 45), "77.8%"),
    ("curriculum/computer_science/ai_foundations/L1_1_what_ai_is_and_how_to_evaluate_it.md", pct(18 + 74, 100), "92%"),
    (BF + "L1_1_value_exchange.md", F(1200, 68), "17.65"),
    (BF + "L1_1_value_exchange.md", F(30 * 80 - (500 + 30 * 12 + 700)), "$840"),
    (BF + "L1_2_customer_research.md", pct(20, 48), "41.7%"),
    (BF + "L1_3_offer_value_proposition.md", pct(35, 60), "58.3%"),
    (BF + "L1_5_revenue_expenses_profit.md", F(12000 - 3000 - 1000 - 1500 - 2000 - 500), "$4,000"),
    (BF + "L1_6_cash_working_capital.md", F(2500 + 4000 - 2200 - 1100 - 800), "$2,400"),
    (BF + "L1_8_unit_economics.md", F(225, 60), "3.75"),
    (BF + "L1_8_unit_economics.md", F(50 * 42 - 1680), "$420"),
    (L1 + "L1_1_discovery_fit_evidence.md", F(80 * 2 + 40 * 4), "320 minutes"),
    (L1 + "L1_2_buying_context.md", F(12 * 400 + 1000 + 1000), "$6,800"),
    (L1 + "L1_2_buying_context.md", F(12 * 300 + 1000 + 1000), "$5,600"),
    (L1 + "L1_6_qualification_uncertainty.md", F(5000) / 5 + F(8000) * 4 / 10 + F(12000) / 2, "$10,200"),
    (L1 + "L1_7_value_demonstration.md", F(80 * 3 - 100), "140 minutes"),
]


def rendered(v):
    """every way a lesson might write v (integer, money, rounded decimals, leading-dot decimals)"""
    out = set()
    v = F(v)
    for p in (0, 1, 2, 3):
        s = "{:,.{p}f}".format(float(v), p=p)
        out |= {s, s.lstrip("0") if s.startswith("0.") else s, s.replace("-", "−")}
    if v.denominator == 1:
        out.add("{:,}".format(int(v)).replace("-", "−"))
    return out


def main():
    fails = []
    texts = {}
    for f, v, needle in CASES:
        p = ROOT / f
        if not p.exists():
            fails.append(f + ": missing file")
            continue
        t = texts.setdefault(f, p.read_text(encoding="utf-8"))
        if needle not in t:
            fails.append("%s: stated figure %r not found" % (f, needle))
            continue
        digits = needle.replace("$", "").replace("/customer-month", "").replace("/month", "")
        if not any(r in digits for r in rendered(v)):
            fails.append("%s: %r does not match the exact value %s" % (f, needle, float(v)))
    # the corrected interval in the incrementality lesson
    se = sqrt(.07 * .93 / 2000 + .05 * .95 / 2000)
    mk = (ROOT / "curriculum/business/marketing/advanced_incrementality_and_experiment_design.md").read_text(encoding="utf-8")
    want = "about %.2f to %.2f percentage points" % ((.02 - 1.96 * se) * 100, (.02 + 1.96 * se) * 100)
    sev = ("%.5f" % se).lstrip("0")
    if ("≈ " + sev) not in mk or ("1.96×" + sev) not in mk or want not in mk or ".00746" in mk:
        fails.append("incrementality: standard error / interval must read %.5f and %r" % (se, want))
    # these lessons are ChatGPT output: they must stay out of SKA model training
    for f in sorted(set(c[0] for c in CASES)):
        t = texts.get(f) or (ROOT / f).read_text(encoding="utf-8")
        if "provenance: ai_drafted" not in t or "training_use: \"excluded" not in t:
            fails.append(f + ": missing ai_drafted provenance / training exclusion header")
    print(json.dumps({"cases": len(CASES), "files": len(set(c[0] for c in CASES)), "failures": fails}, indent=1))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
