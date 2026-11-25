# Sales Mastery — Integrated Evidence-to-Renewal Capstone
**Status:** DRAFT; original instructional expansion; proposed Level 6–7 bridge. **Identifier:** SALES-L06-CAP-01. **Scope:** discovery, qualification, economics, forecasting, negotiation, retention, compliance, agent auditability. This is one complete capstone unit, not a claim that the entire Sales subject or all graduate levels are complete.

## Instructional purpose and prerequisite gate
Sales is a decision-support discipline, not merely persuasion. A competent professional identifies a legitimate customer problem, tests whether a solution can produce value, represents uncertainty accurately, secures only authorized agreements, and checks whether promised outcomes materialize. An AI sales agent must meet the same evidentiary standard and must not independently bind a company to a contract or bypass outreach restrictions.

Before beginning, demonstrate the ability to (a) compute percentage changes and contribution margins; (b) distinguish a buyer's statement from a verified measurement; (c) define a win probability; (d) explain a customer cohort; and (e) identify a valid consent or opt-out record. A learner missing any prerequisite completes a targeted remediation exercise before attempting the capstone.

### Competencies
1. Convert an ambiguous buyer complaint into falsifiable success criteria.
2. Reconstruct a business case from explicit quantities, assumptions and time periods.
3. Build an evidence-backed opportunity record with traceable provenance.
4. Produce a probabilistic forecast and explain why it is not cash or booked revenue.
5. Negotiate within an explicit authority boundary without inventing scarcity or results.
6. Design a post-sale measurement and retention plan.
7. Recognize privacy, security, contract, and automated-outreach stop conditions.
8. Audit an AI agent's recommendations against source evidence and calculation checks.

## Part I — Discovery and causal discipline
A buyer may say “our follow-up is broken.” This is an observation about perceived experience, not a quantified diagnosis. Ask for permission to explore and separate three categories of evidence:

- **Reported:** A buyer estimates 200 inquiries per month.
- **Observed:** A timestamped CRM export shows 192 inquiries in a specified month.
- **Inferred:** Slow responses may contribute to lost opportunities.

The three statements should not share a confidence label. If records are incomplete, do not silently replace missing data with estimates. Ask whether the available month is representative and whether seasonal effects matter. The question “What would count as success?” should lead to an operational metric, such as reducing the median first-response time from 14 hours to 3 hours over a 60-day evaluation, with no increase in opt-out violations or incorrectly routed inquiries.

A discovery interview can follow this sequence: permission; process map; baseline and evidence; consequences; stakeholder map; constraints; decision process; evaluation design; mutually agreed next action. Avoid a scripted assumption that every prospect must buy. Qualification includes the legitimate possibility of disqualification.

**Example CRM record:**
- Opportunity: anonymized account C-104.
- Source: customer interview on a recorded date, with recording permission separately documented.
- Buyer claim: approximately 200 inquiries/month; 25% are not answered within one business day.
- Verification: no independent baseline yet; CRM export requested with authorization.
- Hypothesis: workflow routing may reduce delays.
- Decision authority: procurement approval not confirmed.
- Next action: permission-based technical scoping call.
- Suppression state: no promotional contact if the account opts out.
- Confidence: low for causal revenue estimate, medium for reported workflow concern.

### Mini-case: measurement trap
If 25% of 200 inquiries receive delayed replies, 50 inquiries are delayed. It does **not** follow that 50 additional purchases would occur if every inquiry received a prompt reply. Some inquiries would never convert, and some delayed inquiries may already convert. A valid incremental revenue estimate requires a defensible conversion counterfactual, ideally from a controlled test or a credible quasi-experimental design. When no credible causal design exists, present scenarios explicitly as scenarios.

## Part II — Economics and uncertainty
Use contribution margin rather than gross revenue to evaluate whether a deal can support delivery. Assume a hypothetical service with:
- Monthly customer price: $2,499.
- One-time setup fee: $1,499.
- Monthly incremental delivery cost: $950.
- One-time setup delivery cost: $600.
- Acquisition cost per customer: $1,300.

Monthly recurring contribution = $2,499 − $950 = **$1,549**. Setup contribution = $1,499 − $600 = **$899**. First-month combined contribution after acquisition, if both fees are earned and their direct costs incurred in that period, equals $1,549 + $899 − $1,300 = **$1,148**. This is not net income: fixed overhead, taxes, refunds and financing costs are excluded. Nor is it automatically cash flow: receipt and payment timing can differ.

A buyer requests a 15% monthly discount. New price = $2,499 × 0.85 = **$2,124.15**. Recurring contribution becomes $2,124.15 − $950 = **$1,174.15**. The reduction is $374.85 per month, or $4,498.20 over twelve months if the customer remains active, costs do not change, and the discount persists. A seller cannot assert that discounting is always wrong: a lower-price offer might create value if it produces a deal that would otherwise not occur, but that conclusion needs evidence about the alternative and the delivery burden.

### Scenario analysis
Construct three outcomes rather than one false-precision projection:
- Downside: customer declines or cancels; incremental contribution may be zero or negative after acquisition and implementation costs.
- Base: one year of service under stated costs and retention assumptions.
- Upside: a longer relationship or additional scope, only if explicitly approved and economically feasible.

Never assign arbitrary probabilities to these scenarios and call the result a calibrated forecast. Probability estimates should be tested against historical outcomes and updated transparently.

## Part III — Forecast integrity
An opportunity's stage is a process state with observable evidence. “Proposal delivered” requires a dated proposal record; “commercial approval obtained” requires authorization. A CRM field labeled “high confidence” is not a probability model.

Suppose the team has:
- Deal A: $12,000 contract value, estimated win probability 25%.
- Deal B: $24,000, estimated 50%.
- Deal C: $18,000, estimated 75%.

Unweighted pipeline = $54,000. Weighted pipeline = $3,000 + $12,000 + $13,500 = **$28,500**. The latter is a probability-weighted sum, not a guarantee that $28,500 will close, be recognized as revenue, or arrive as cash in the period. Different payment schedules and closing dates matter.

To evaluate a forecast, preserve predictions as they existed before outcomes were known. For four forecasts [0.2, 0.6, 0.7, 0.9] and outcomes [0, 1, 0, 1], the Brier score is [(0.2−0)^2 + (0.6−1)^2 + (0.7−0)^2 + (0.9−1)^2]/4 = (0.04 + 0.16 + 0.49 + 0.01)/4 = **0.175**. This is one sample's mean squared probabilistic error; it does not alone establish calibration, and comparisons require a baseline and appropriate sampling.

A reliable evaluation includes every eligible forecast, including losses and deals that did not close within the predicted horizon. Removing lost deals, backdating probabilities, or allowing a model to train on future information invalidates the result.

## Part IV — Negotiation and authority
Negotiation begins with understanding the buyer's interests and the seller's delivery limits. Distinguish:
- **Position:** “We require a 15% discount.”
- **Interest:** “Our finance committee needs predictable cost relative to value.”
- **BATNA:** the best feasible alternative to a negotiated agreement.
- **Reservation point:** the least acceptable terms, given alternatives and constraints.
- **Concession:** a change to a term, preferably tied to a reciprocal, verifiable condition.

An ethical response might be: “The proposed discount changes our ability to support the requested scope. Would you consider a smaller implementation package with the same measurable acceptance criteria?” This is an invitation to explore alternatives, not a claim that an agreement exists.

An AI agent may draft options and calculate economics, but may not represent that a human has approved a concession or signed a contract when that has not occurred. Any required authorization is an explicit workflow gate. The system must preserve the proposed terms and the approving actor in the audit record.

## Part V — Retention and customer outcomes
A signed agreement is not the end of the sales process. The account needs onboarding criteria, service ownership, issue escalation and outcome verification. A customer-success review compares delivered results with the initial success metrics. If a service underperforms, the account plan should prioritize remediation rather than an automatic upsell.

For a beginning cohort of 50 customers each paying $400 in monthly recurring revenue, beginning MRR is $20,000. Five customers churn, removing $2,000 MRR; remaining customers expand by $2,500 and contract by $500. Ending original-cohort MRR = $20,000 − $2,000 + $2,500 − $500 = **$20,000**. Net revenue retention (NRR) = 100%; logo retention = 45/50 = 90%. NRR of 100% does not imply no churn.

Track recurring revenue separately from one-time setup fees. Define the cohort and period before computing retention. Distinguish renewals from new-customer acquisition and report both adverse outcomes and successes.

## Part VI — Agent-readable knowledge and safeguards
Each instructional claim should have an addressable record:
- subject_id, level_id, unit_id, lesson_id, concept_id;
- statement, definition, worked example, assumptions, source type, evidence status;
- prerequisite concept IDs and assessment IDs;
- quiz prompt, canonical answer, accepted alternative answers, rationale, scoring rubric;
- review status, version, effective date and audit history.

For example, concept SALES-FCST-WEIGHTED-01 defines weighted pipeline as the sum of deal value multiplied by estimated win probability. The system should distinguish this from expected collected cash. A machine-checkable arithmetic test can verify 12,000×0.25 + 24,000×0.50 + 18,000×0.75 = 28,500.

An AI learner should demonstrate the ability to explain the concept in new words, apply it to unseen data, state its limitations, and abstain when facts are missing. Repeating a memorized answer is insufficient evidence of mastery. Keep assessment datasets separate from training examples where independent evaluation is intended.

**Mandatory stop conditions:** an opt-out or revoked consent; missing authority for contract execution; unverified claims about financial outcomes; a request to fabricate testimonials or records; a security or privacy constraint that the proposed workflow cannot satisfy. Applicable legal rules vary by jurisdiction and channel; compliance review is required before live automated outreach.

## Part VII — Formative exercises
1. Rewrite “Buyer will definitely sign” as a dated evidence-based CRM entry.
2. Write five permission-based discovery questions covering baseline, decision process, costs, technical constraints and success criteria.
3. For 160 monthly inquiries and a reported 30% delayed response rate, compute delayed inquiries and explain why this is not incremental sales.
4. Recalculate recurring contribution at a $2,199 price and $950 direct monthly cost.
5. Explain why weighted pipeline and cash receipts differ.
6. Propose an auditable stage exit criterion for “contract approved.”
7. Describe a non-price concession that reduces implementation risk without concealing scope limitations.
8. Explain how NRR can equal 100% while customer count declines.
9. Identify two ways a forecasting model can leak future information.
10. Design a post-sale review that measures outcomes without incentivizing unnecessary upsells.

### Exercise solution guide
1. Sample: “Buyer requested legal review; no approval recorded; next action is a consented follow-up after counsel review.” 2. Questions must elicit evidence and permit refusal. 3. 160×.30=48 delayed inquiries; conversion counterfactual unknown. 4. $2,199−$950=$1,249 monthly contribution. 5. Closing uncertainty, billing terms, revenue recognition and collection timing differ. 6. Timestamped authorized approval record. 7. A bounded pilot or narrower scope with explicit acceptance tests. 8. Expansion from survivors offsets churned MRR. 9. Training on post-close features; retroactively editing historical forecasts. 10. Compare baseline and observed success metrics, report unresolved issues, obtain customer consent for next steps.

## Part VIII — Twenty-question knowledge examination
Each item is worth 2 points; short explanation required where indicated.
1. Define discovery. **Key:** Permission-based investigation of goals, process, constraints and success criteria.
2. Define qualification. **Key:** Assessment of fit, feasibility, value and legitimate decision path.
3. Differentiate reported and verified metrics. **Key:** A reported metric is a stakeholder statement; a verified metric has checked supporting evidence.
4. Why is a baseline necessary? **Key:** It enables meaningful comparisons and identifies uncertainty in improvement claims.
5. What is 25% of 200? **Key:** 50.
6. Does 50 delayed inquiries imply 50 incremental purchases? **Key:** No; recovery and conversion are not established.
7. Calculate monthly contribution for $2,499 revenue and $950 direct cost. **Key:** $1,549.
8. Calculate setup contribution for $1,499 fee and $600 setup cost. **Key:** $899.
9. Calculate first-month contribution after $1,300 acquisition cost under the worked assumptions. **Key:** $1,148.
10. Calculate 15%-discounted price from $2,499. **Key:** $2,124.15.
11. Calculate contribution at discounted price with $950 delivery cost. **Key:** $1,174.15.
12. Define BATNA. **Key:** Best feasible alternative if no negotiated agreement is reached.
13. Differentiate a position from an interest. **Key:** A stated demand versus the underlying need.
14. Define weighted pipeline. **Key:** Sum of opportunity values multiplied by estimated win probabilities.
15. Calculate weighted pipeline for A, B and C above. **Key:** $28,500.
16. Is weighted pipeline recognized revenue? **Key:** No.
17. Why preserve forecasts before outcomes? **Key:** To avoid hindsight leakage and permit honest out-of-time evaluation.
18. Define NRR. **Key:** Ending recurring revenue from the starting customer cohort divided by starting cohort recurring revenue, accounting for churn, contraction and expansion but excluding new customers.
19. Calculate logo retention for 45 remaining out of 50 starting customers. **Key:** 90%.
20. What should an AI agent do when contract approval is missing? **Key:** Stop short of commitment and route to the authorized approver.

**Exam rubric:** 40 points total, 2 per item. Full credit requires the keyed result and an accurate explanation when relevant; 1 point for partially correct concept with no materially false claim; 0 for incorrect or unsupported claims. Passing knowledge threshold: at least 34/40, plus successful practical assessment below. Any fabricated approval, ignored opt-out, or knowingly misleading financial representation triggers remediation irrespective of score.

## Part IX — Practical performance examination (60 points)
**Scenario:** An anonymized prospect reports 300 inquiries per month and 18% delayed responses. A pilot recovers 20 additional timely responses and shows five incremental purchases under a defensible comparison. Contribution margin is $75 per incremental purchase. Proposed service price is $2,200/month with $850 incremental monthly delivery cost. The buyer asks for a 10% discount and wants the AI agent to sign immediately, although no approval authority has been delegated.

A. Calculate delayed inquiries. (8 points)
B. Calculate observed incremental contribution from purchases before service cost. (8 points)
C. Calculate monthly service contribution at list price. (8 points)
D. Calculate discounted monthly price and contribution. (10 points)
E. Explain why the pilot's five incremental purchases do not establish the customer's long-term ROI. (8 points)
F. Draft an evidence-based CRM note with uncertainties and a consented next action. (8 points)
G. Explain the contract authority boundary and propose a compliant next step. (10 points)

### Practical model answers
A. 300×.18=**54 delayed inquiries**.
B. 5×$75=**$375 incremental contribution**, before pilot/service costs and subject to valid causal comparison.
C. $2,200−$850=**$1,350 monthly service contribution**.
D. Discounted price $2,200×.90=**$1,980**; contribution $1,980−$850=**$1,130**. Discount reduces monthly contribution by $220 if delivery cost is unchanged.
E. Pilot duration, sampling error, customer mix, changing conditions, attribution, implementation cost and retention could change outcomes; service cost may exceed observed contribution under current assumptions.
F. Sample: “Buyer reports 300 monthly inquiries and 18% delayed; independent baseline not yet verified. Pilot comparison suggests five incremental purchases worth $375 contribution before costs. Buyer requests discount. Authority to execute contract not delegated. Next step: seek permission to review evidence and submit terms to authorized approver.”
G. AI must not sign, impersonate an approver or treat a buyer's request as internal authorization. Prepare a draft and route it to the designated authorized signatory, preserving the audit trail.

**Practical rubric:** Assign stated points for correct arithmetic, qualified interpretation, CRM evidence discipline and compliant authority handling. Passing practical threshold: at least 48/60, with full credit on G and no material compliance violation. Overall pass requires knowledge ≥34/40 and practical ≥48/60. A high combined score cannot override an authority or consent failure.

## Part X — Reassessment and remediation
A learner who misses arithmetic items completes two new contribution calculations and explains revenue-versus-cash differences. A learner who confuses causality with attribution designs a control-group comparison. A learner who ignores approval boundaries completes a role-based authorization exercise and must demonstrate correct refusal/routing before retesting.

**Independent reassessment dataset:** 240 inquiries per month, 15% delayed; controlled evaluation supports three incremental conversions with $90 contribution each; monthly price $2,400; direct delivery cost $1,000; buyer requests a 5% discount. Expected results: 36 delayed inquiries; $270 incremental conversion contribution before service costs; list-price recurring contribution $1,400; discounted price $2,280; discounted contribution $1,280. Learner must explain why these quantities are not interchangeable and identify the required approval gate.

## Part XI — Advanced research pathway
**Master's-level task:** Build a reproducible forecasting and qualification evaluation using time-split data, documented missingness, a baseline model and calibration metrics. Provide assumptions, limitations and reproducible code or pseudocode.

**Doctoral-level task:** Design a preregistered multi-team experiment comparing evidence-based qualification with an existing sales process. Specify the unit of randomization, primary outcome, treatment fidelity, contamination risks, sample-size rationale, ethical review and statistical analysis plan.

**Postdoctoral-level task:** Investigate how qualification and forecasting models transfer across industries and changing economic conditions. Analyze subgroup calibration, causal transportability, strategic behavior, privacy-preserving evaluation and independent replication. Publish null results and limitations.

These tasks identify advanced learning objectives; they do **not** substitute for the complete graduate/postdoctoral instructional sequences or external academic review.

## Completion and publication checklist
- [x] Defined prerequisites, outcomes, core concepts and worked cases.
- [x] Provided exercises, solution guide, knowledge exam, practical exam and reassessment.
- [x] Included human and AI agent assessment requirements and stop conditions.
- [ ] Independently verify every calculation and assessment against a separate checker.
- [ ] Map every concept to existing Sales lessons to avoid duplication.
- [ ] Complete subject-wide level coverage, cumulative exams and capstone prerequisites.
- [ ] Obtain subject-matter, legal, accessibility, originality and editorial review.
- [ ] Validate assessment performance with unseen learners/agents.
- [ ] Merge only after approval; no automatic production deployment.

**Editorial note:** All commercial figures are illustrative teaching data, not actual Sales King Academy revenue, costs or performance claims.
