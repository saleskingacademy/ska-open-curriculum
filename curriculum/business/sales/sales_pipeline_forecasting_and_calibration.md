# Sales — Pipeline Forecasting and Calibration
Status: DRAFT | Proposed Level 6 | ID SALES-L06-FCST-01
Prerequisites: opportunity qualification, probability, contribution margin, CRM evidence hygiene.

## Learning objectives
Define opportunity stages operationally, distinguish weighted pipeline from expected revenue, compute forecast error, assess probability calibration, detect leakage and selection bias, and explain a decision under uncertainty.

## Instruction
A pipeline is a set of opportunities at defined stages. Stage labels must represent **observable entry and exit criteria** rather than seller optimism. For example, “proposal sent” is evidenced by an actual dated proposal, while “decision approved” requires an authorized decision record. A deal's value, forecast close date and probability are separate fields. Weighted pipeline sums opportunity amount multiplied by estimated win probability; it is a descriptive expectation under assumptions, not a promise of cash receipts or a validated revenue forecast. Recognized revenue and cash collections follow different accounting and timing rules.

### Worked example
Four hypothetical opportunities have contract values and win probabilities: A $10,000 at 20%; B $20,000 at 40%; C $15,000 at 60%; D $5,000 at 80%. Weighted pipeline is $2,000+$8,000+$9,000+$4,000=$23,000. Unweighted pipeline is $50,000. Neither number implies $23,000 will be collected this month. Forecast quality depends on probabilities being calibrated, opportunities sharing a clear time horizon, and deal values being comparable.

Calibration asks whether opportunities predicted at probability p win approximately p of the time across many independent observations. The Brier score for binary outcomes is the average squared difference between forecast probability and outcome (1 for win, 0 for loss); smaller is better. For four outcomes [0,1,1,0] and forecasts [.2,.4,.6,.8], the squared errors are .04,.36,.16,.64, so Brier score=(1.20)/4=.30. This small sample cannot establish long-run calibration. A baseline forecast using historical conversion by stage should be evaluated out-of-time against alternatives.

### Forecast governance
Freeze forecasts before outcomes are known; retain lost deals; distinguish opportunity creation from forecast dates; prevent agents from retroactively changing old predictions; report cohort size and uncertainty; check calibration by segment and horizon; audit for data leakage, duplicates, and selection effects. Recalibrate only using past outcomes available at the prediction date. Flag unsupported high-confidence predictions for review.

## Practice
1. Calculate weighted pipeline for two opportunities: $8,000 at 25% and $12,000 at 50%.
2. Explain why a 70% probability derived from a seller's confidence is not a calibrated estimate.
3. Propose a stage exit criterion that can be independently verified.
4. Explain how excluding lost opportunities biases reported conversion.
5. Design a monthly out-of-time calibration report.

## Quiz with explanations
Q1. What is weighted pipeline? **Answer:** Sum of each opportunity value times its estimated win probability; it is not booked revenue.
Q2. What is weighted pipeline for $8,000 at 25% plus $12,000 at 50%? **Answer:** $2,000+$6,000=$8,000.
Q3. What is the unweighted value of the four-deal worked example? **Answer:** $50,000.
Q4. What is its weighted value? **Answer:** $23,000.
Q5. What does a Brier score measure? **Answer:** Mean squared error between predicted probabilities and observed binary outcomes.
Q6. What is the Brier score in the worked example? **Answer:** .30.
Q7. Why freeze forecasts before outcomes? **Answer:** To prevent hindsight leakage and permit honest evaluation.
Q8. Does a high weighted pipeline establish sufficient cash runway? **Answer:** No; payment timing, win uncertainty, costs and cash balances remain relevant.

## Examination and answer key
A. A team has opportunities: $30,000 at 30%, $10,000 at 50%, $20,000 at 10%. Calculate unweighted and weighted pipeline. **Solution:** $60,000 unweighted; $9,000+$5,000+$2,000=$16,000 weighted.
B. Forecasts [.1,.7,.8,.4] and outcomes [0,1,0,1]. Compute Brier score. **Solution:** squared errors [.01,.09,.64,.36], sum 1.10, average .275.
C. Explain why a model trained on eventual deal outcomes and tested on the same deals may overstate performance. **Solution:** Training/test leakage and overfitting; use time-separated held-out evaluation.
D. Identify three controls for auditable forecasts. **Solution:** Immutable timestamped predictions, recorded stage criteria, inclusion of wins and losses; other valid controls accepted.
E. Write an ethical corrective action for an agent inflating probabilities to hit a quota. **Solution:** Preserve the original forecast, correct the estimate with evidence, document the revision and prevent incentive-driven misreporting.

## Mastery rubric
100 points: pipeline math 25; probability scoring 25; leakage and bias analysis 20; audit controls 20; ethical corrective action 10. Pass 80/100 with no falsification of records. Reassessment variant: opportunities $12,000 at 25%, $16,000 at 75%, $8,000 at 50% yield weighted $19,000 and unweighted $36,000. Require independent explanation of assumptions.

## Research-level transfer
Master's: compare logistic calibration, isotonic regression and decision-curve analysis with nested validation. Doctoral: design a preregistered, multi-team experiment comparing calibrated forecasts to subjective stage-weight forecasts. Postdoctoral: evaluate temporal drift, cross-sector transportability, partial observability and reproducible benchmarking. These are advanced research prompts, not proof of complete doctoral education.

Publication gates: accuracy, original writing, editorial review, assessment validity, alignment with the eight-level Sales map.