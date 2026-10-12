# Lesson 20: Addition and subtraction mastery

Canonical ID: AR-L02-20. Discipline: established mathematics. Subject: Arithmetic.
Prerequisites: Lessons 11–19, culminating in [estimation and checking](lesson_19_estimation_and_checking.md).
Next: Lesson 21, Meaning of multiplication, in [the canonical sequence](../arithmetic_zero_to_advanced.md).
Education-16 and Symbol256: new lesson mapping deferred pending academic and taxonomy validation.

## Purpose, entry and outcomes

This lesson integrates addition, subtraction, signed changes, estimation and verification. It does not introduce multiplication as an assumed skill. The learner must select a model and method without being told which operation to use. Completion of this lesson is a module milestone, not completion of the eighty-lesson Arithmetic course.

Entry tasks: explain a carry in 48 + 27; explain an exchange in 402 − 178; compute −6 − (−4); and state one limitation of an estimate. Responses: ten ones become one ten; a hundred is redistributed through tens while preserving 402; −2; an estimate does not uniquely establish an exact answer. Use the corresponding earlier lesson when an entry explanation fails.

By the end, translate multi-event stories into ordered calculations, distinguish states from changes, preserve units and source identity, justify method choices, apply independent checks and report limitations. A correct number attached to the wrong model does not meet the outcome.

## Vocabulary and organizing principles

A **state** is a quantity at a particular point. An **event** changes it. A **reconciliation** compares the calculated ending state with an independently observed ending state. A **discrepancy** is their signed difference. A **model assumption** states which events and categories the calculation includes.

For a sequence of events, ending state equals starting state plus all signed changes. Positive changes add and negative changes remove. This statement does not justify adding states from different times together: a balance after one event already includes the previous state. Counting both as independent contributions duplicates quantity.

Order may not affect the final sum of fixed signed changes, but it can affect intermediate states and whether an action was feasible. Starting with two physical items, adding three then removing four is feasible without a shortage. Removing four before receiving three is not feasible if negative physical stock is prohibited, although the formal final arithmetic gives one in either order. Interpret constraints at each step.

## Worked examples

**E1 — stock reconciliation.** A hypothetical store begins with 1,250 items, receives 375, ships 468 and receives 27 returned items that are approved for stock. State after receipt: 1,625. After shipment: 1,157. After returns: 1,184. Check totals: additions 402; ending 1,184 plus removals 468 equals starting 1,250 plus additions 402, both 1,652. This check presumes distinct events and consistent units.

**E2 — signed balance.** A simulation starts at −28 units, adds 45, removes 19 and adds 6. States are 17, −2 and 4. Grouping changes gives 45 + (−19) + 6 = 32; starting −28 plus 32 is 4. Report the intermediate negative state instead of hiding it behind a positive final total.

**E3 — discrepancy interpretation.** A calculated stock is 1,184 but the observed count is 1,179. Observed minus calculated is −5 items. This indicates five fewer observed items, not proof of theft or any unique cause. Recount and inspect event records, units and timing before assigning a cause.

**E4 — compare quantities correctly.** A workshop has 137 registered learners and another has 89. The combined count is 226 only if these are disjoint learner sets. The registration-count difference is 48 regardless of overlap, but it does not identify which learners appear in both. State whether the quantity is registrations or distinct people.

**E5 — exact and approximate checks.** Estimate 1,250 + 375 − 468 + 27 to nearest tens: 1,250 + 380 − 470 + 30 = 1,190. Four rounded terms give a conservative absolute-error bound twenty, though the first input was unchanged. Exact 1,184 lies inside the interval. Reconciliation provides a stronger exact relationship; neither verifies the raw records independently.

## Guided practice

G1. Start with 320 objects, receive 85, remove 97. **Solution:** 405 then 308. Check 308 + 97 = 320 + 85 = 405.

G2. Start at −9, add 14, remove 8. **Solution:** Five then −3. Removing eight from five crosses zero in a signed model; a physical-stock interpretation would require a shortage policy.

G3. A running total after the first receipt is 405. Should it be added to starting stock 320 again? **Solution:** No. The running total already includes 320. Add only new changes to it.

## Independent problem set and explanatory key

Compute each expression and explain one check. Treat minus signs as operations with the displayed operands.

P1. 248 + 176.
P2. 900 − 458.
P3. 37 + 63 + 28.
P4. 5,002 − 76.
P5. −18 + 25.
P6. −12 − (−7).
P7. 320 + 85 − 97.
P8. −9 + 14 − 8.
P9. 1,250 + 375 − 468 + 27.
P10. 1,179 − 1,184.

Solutions:

P1. 424; 248 + 100 + 70 + 6 gives the same sum.
P2. 442; 458 + 442 = 900.
P3. 128; pair 37 and 63 to make 100.
P4. 4,926; 4,926 + 76 = 5,002.
P5. 7; eighteen opposite pairs cancel.
P6. −5; add positive seven, then check −5 + (−7) = −12.
P7. 308; reconcile 308 + 97 = 405.
P8. −3; states five then negative three.
P9. 1,184; reconcile both sides to 1,652.
P10. −5; observed count is five below calculated count.

## Module investigation: auditable event ledger

Use synthetic data only. Opening state is 680 items. Events in order are receipt A of 145, shipment B of 278, approved return C of 16, shipment D of 89 and receipt E of 207. An independent final count is 677. Produce an event ledger, exact ending state, reconciliation equation, signed discrepancy, estimate with an explicit bound and a short investigation note. Mark every event once. A calculator or AI tool may be used only after the independent trace is recorded.

Reference solution: states 825, 547, 563, 474 and 681. Total additions are 368; removals are 367. Reconciliation is 681 + 367 = 680 + 368 = 1,048. Observed minus calculated is 677 − 681 = −4 items. Nearest-ten inputs give 680 + 150 − 280 + 20 − 90 + 210 = 690. The six-term conservative bound is thirty; absolute error nine satisfies it. Opening state is exact and unchanged, so twenty-five is a tighter bound from the other five terms alone. Both are justified bounds.

The investigation note should say that four fewer items were observed than calculated. Possible follow-up checks include recounting, checking whether the return was approved by count time and reviewing omitted or duplicated events. Do not assert a cause from the discrepancy alone. The example does not describe a production system or actual company inventory.

Rubric, twenty points: input/units/event identity (four); ordered exact states (four); reconciliation and signed discrepancy (four); estimate and justified bound (four); independent tool audit and limitations (four). Score each dimension zero to four: four complete and correct, three minor noncritical omission, two partial with a substantive error, one fragmentary, zero absent. Require at least sixteen overall and at least three in every dimension, with all arithmetic and event-identity errors corrected. These are local module criteria, not a full-course capstone.

## Transfer, computational checking and AI audit

T1. A learner adds the five running states instead of the five changes. Explain why the total does not represent final stock. **Solution:** Each running state repeats earlier contributions. A final state is the opening state plus each event once, not the sum of snapshots.

T2. An AI system says the four-item discrepancy proves a warehouse employee stole four items. **Solution:** Reject the causal claim. Arithmetic identifies the discrepancy under the stated records, but cannot distinguish theft, miscount, timing, damage or a recording error without evidence. Keep the numerical observation and possible explanations separate.

T3. Design a software trace without writing a program. **Solution:** Record event identifier, previous state, signed change, new state and units for every row. Verify new state minus previous state equals that row's change. Check duplicate identifiers separately. Finally compare the calculated state with an independently timed observation. These checks have different failure targets.

## Quiz and alternate reassessment

Two points each: one for the correct result/judgment and one for justification.

Q1. Start 450, add 125, remove 238. Q2. Start −16, add 21, remove 9. Q3. Calculated 337, observed 340: report observed minus calculated. Q4. Does an inverse arithmetic check establish that no event was omitted? Q5. Why retain an intermediate negative state when the final state is positive?

Answers: 337; −4; +3; no, it verifies a relation among supplied inputs; intermediate state may reveal a constraint violation or timing issue. Q5 requires a concrete example or explanation.

Alternate form: R1 start 520, add 148, remove 279; R2 start −19, add 27, remove 11; R3 calculated 389, observed 386; R4 does matching estimates prove exact equality? R5 explain why receipts and snapshot balances cannot all be added as independent inputs. Answers: 389; −3; −3; no; balances already contain earlier events.

## Cumulative assessment, remediation and exit

Complete the [Level 2 examination](assessments/level_02_operations_examination.md), which has two twenty-five-item forms, an outcome blueprint, explanatory keys and domain gates. Use one as the assessment and the other after targeted remediation. Do not mark the whole Arithmetic course complete after this module.

Require nine of ten independent problems correct, 8/10 lesson quiz points, the investigation rubric gates and the cumulative examination thresholds. Review Lesson 13 for carries, 14 for exact mental transformations, 15–17 for subtraction models and exchanges, 18 for signed changes and 19 for bounds. Reassessment must use fresh work with explanations.

Retrieval cues: distinguish state from event; include every change once; preserve units; check intermediate constraints; reconcile exactly; report uncertainty honestly. Multiplication begins next as a new operation built from equal-group structure, not as a prerequisite silently assumed here.
