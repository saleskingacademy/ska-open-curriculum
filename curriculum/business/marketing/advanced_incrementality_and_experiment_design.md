# Marketing — Incrementality, Attribution and Experimental Design
Status: DRAFT. Level 5 advanced professional; progression tasks to research frontier. Proposed ID MKT-L05-INC-01.

## Outcomes
Distinguish attribution from causality; calculate incremental lift and contribution margin; design a randomized campaign test; interpret uncertainty; audit privacy and fairness; construct a replicable research proposal.

## Lesson
**Attribution** assigns credit for a conversion under a rule. Last-click attribution assigns credit to the final recorded touchpoint; it does not prove the touchpoint caused the conversion. **Incrementality** asks what additional outcome occurred because an intervention happened, compared with what would have happened otherwise. The missing counterfactual makes causal inference difficult.

Random assignment creates groups that should be comparable on average before treatment. In a marketing holdout test, randomly assign eligible customers to receive a campaign or not receive it, then compare prespecified outcomes over the same observation window. Define eligibility before randomization. Ensure opt-outs and consent requirements are respected in both arms. Avoid leakage: sales representatives must not selectively add campaign contacts to the holdout group. Track exclusions, attrition, crossover and contamination.

### Worked experiment
A hypothetical eligible audience is randomized evenly: 2,000 treatment and 2,000 control. Treatment yields 140 purchases; control yields 100. Treatment conversion = 140/2,000 = 7%; control conversion = 100/2,000 = 5%. Absolute lift = 2 percentage points; relative lift = (7%-5%)/5% = 40%. Estimated incremental purchases in the 2,000-person treated group = (0.07-0.05)×2,000 = 40. These are observed differences under the randomized design, not proof of a universally applicable 40% lift.

If contribution margin is $60 per incremental purchase and campaign cost is $1,500, estimated incremental contribution after campaign cost = 40×$60−$1,500 = $900. This is not gross revenue. A normal-approximation standard error for the difference in proportions is sqrt((.07×.93/2000)+(.05×.95/2000)) ≈ .00746; approximate 95% interval is .02 ± 1.96×.00746, or about 0.54 to 3.46 percentage points. Interpretation depends on valid randomization, outcome measurement and other assumptions; the interval is approximate.

### Experimental design checklist
Define the primary outcome and time horizon before launch; pre-register subgroup analyses; choose randomization unit (individual, account, geography); calculate sample size using a realistic minimum detectable effect; avoid repeatedly peeking at significance without sequential correction; report both absolute and relative effects; inspect heterogeneous effects without cherry-picking; document cost and marginal profitability. Protect participant privacy and minimize personal data.

### Failure modes
Selection bias from targeting only high-intent customers; platform-reported conversions counted as incremental; cross-channel contamination; repeated looks at p-values; ignoring returns/refunds; treating correlation as causation; using revenue instead of contribution margin; applying an aggregate effect to an untested market.

## Exercises
1. Recompute lift if treatment has 120 purchases and control 100, each with 2,000 participants. Explain why a smaller observed difference is less persuasive.
2. A 10,000-person campaign yields an estimated 1 percentage-point absolute incremental conversion lift and $35 contribution margin per incremental purchase. With $2,000 campaign cost, estimate incremental contribution.
3. Design a holdout test for a B2B service where multiple employees share the same purchasing decision. Justify the randomization unit and contamination controls.
4. Critique the statement: “80% of purchasers clicked an ad, so 80% of sales were caused by advertising.”

## Quiz and solutions
Q1. What does last-click attribution establish? A: Which recorded touchpoint received credit under the last-click rule; not causality.
Q2. What is absolute lift for 7% versus 5%? A: 2 percentage points.
Q3. What is relative lift for 7% versus 5%? A: 40%.
Q4. What is estimated incremental purchase count among 2,000 treated customers? A: 40.
Q5. With $60 margin and $1,500 campaign cost, estimated net incremental contribution? A: $900.
Q6. Why randomize at account level in some B2B tests? A: To limit contamination when several people share a buying decision.
Q7. Why is a prespecified primary outcome necessary? A: It reduces selective reporting and post-hoc outcome switching.
Q8. Does a statistically significant lift guarantee profit? A: No; profitability also depends on incremental contribution, campaign cost and uncertainty.

## Assessment rubric
10 points each: causal distinction, design, absolute/relative lift, margin analysis, uncertainty, leakage mitigation, privacy, interpretation, critique, reproducibility. Pass 80/100 with no material privacy violation. Reassessment: new randomized dataset with 3,000 per arm and 180 versus 135 conversions; require recomputation and new design rationale.

## Research progression
Master's: power calculations, stratified randomization and sensitivity analysis. Doctoral: preregister a multi-market experiment, formalize interference assumptions, and estimate heterogeneous treatment effects with correction for multiplicity. Postdoctoral: study transportability under distribution shift and partial interference; publish reproducible protocols and independent replications. Research tasks are not a claim of academic accreditation.

Editorial, quantitative and originality review required before COMPLETE.