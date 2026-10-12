# Lesson 19: Estimation and checking

Canonical ID: AR-L02-19. Discipline: established mathematics. Subject: Arithmetic.
Prerequisites: [estimation](lesson_07_estimation.md), [rounding](lesson_08_rounding.md), and [signed operations](lesson_18_signed_addition_subtraction.md).
Next: [operations mastery](lesson_20_operations_mastery.md).
Education-16 and Symbol256: new lesson mapping deferred pending academic and taxonomy validation.

## Entry check and outcomes

Round 247 and 153 to the nearest ten using the course's stated tie rule. Add them exactly. Explain why agreement with an estimate alone does not prove an answer. Responses: 250 and 150; exact 400; multiple nearby exact answers can share an estimate. Return to rounding if the selected place or tie convention is unclear.

By the end, estimate before calculating, derive simple error bounds, use directional and interval checks, verify inverse relationships, identify compensating errors and distinguish arithmetic agreement from verified input data. Accuracy is a property of the method and evidence, not the confidence of the narrator.

## Vocabulary and first principles

An **estimate** approximates a target. **Absolute error** is the nonnegative distance between estimate and exact value. A **bound** is a justified limit on possible values or error. A **check** tests a necessary relationship; it may reject a wrong answer without proving a remaining answer correct. An **independent representation** reorganizes the computation so that the same procedural error is less likely to recur.

Nearest-ten rounding changes a nonnegative whole number by at most five units. If both addends are rounded, the errors can reinforce or partially cancel. The largest combined error magnitude is at most ten units. This is a worst-case bound, not a prediction that every estimate is ten away. Exact tie direction affects particular cases but not this absolute bound.

For a sum of three such rounded inputs, at most fifteen units of total absolute error is possible by adding the three individual five-unit bounds. This lesson derives bounds from known input errors. A vague statement like “it looks close” supplies no numerical acceptance rule.

## Deriving the bound for sums and differences

Let A approximate a with error e, so A = a + e. Let B = b + f. Then A + B differs from a + b by e + f. If each error lies between −5 and +5, their sum lies between −10 and +10. For subtraction, (A − B) − (a − b) = e − f, which has the same bound. A minus sign does not make rounding errors disappear.

These letters are labels for known quantities and changes, not assumed prior algebra mastery. A concrete version suffices: if the first estimate is five too high and the second is five too low, subtracting the second estimate makes the difference ten too high. All combinations remain within ten units. Later numerical analysis treats larger systems and more general error propagation.

For negative inputs in this lesson, use explicit intervals or absolute magnitudes to avoid introducing an unstated negative tie convention. The earlier nearest-rounding procedure was taught for nonnegative values. A software rounding rule must be identified before reproducing its boundary results.

## Worked examples

**E1 — a plausible scale.** 398 + 207 is about 400 + 210 = 610 by nearest-ten rounding. The exact sum is 605, an error of five, inside the ten-unit bound. A proposed answer 6,050 is far outside the interval 600 through 620 and is rejected immediately. The estimate alone does not distinguish 605 from every other value inside the interval.

**E2 — subtraction.** 803 − 397 is approximately 800 − 400 = 400. The exact result is 406. The estimate is six low and satisfies the ten-unit bound. Check 406 + 397 = 803. Rounding errors here reinforce rather than cancel.

**E3 — close values.** 1,002 − 997 = 5, but rounding each input to the nearest ten gives 1,000 − 1,000 = 0. The absolute error five is within the bound, yet zero is a poor description of a small nonzero difference. Small absolute error need not mean a useful approximation relative to the target's size.

**E4 — interval inputs.** A count a is between 98 and 102 inclusive, and b between 47 and 49 inclusive. Their sum is between 145 and 151: combine both lower endpoints and both upper endpoints. Their difference a − b is between 49 and 55: the smallest difference uses the smallest first input and largest second input; the largest uses the reverse. Do not subtract lower from lower and upper from upper to claim the full difference range.

**E5 — signs and direction.** Without calculating exactly, −8 + 3 must be greater than −8 but still negative because the positive change is smaller than eight. Exact answer −5 satisfies that condition. A proposed +11 fails the sign/direction check.

**E6 — compensating errors.** The true inputs 240 and 160 sum to 400. Mistyped inputs 250 and 150 also sum to 400. Agreement of totals does not verify individual entries. Compare each input with its source; then verify the arithmetic. This separates a data audit from a calculation check.

## Guided practice

G1. Estimate 486 + 312 by nearest tens, then calculate. **Solution:** 490 + 310 = 800; exact 798, two below the estimate.

G2. Estimate 704 − 286. **Solution:** 700 − 290 = 410; exact 418, eight above the estimate and within ten.

G3. Can a proposed exact answer of 427 pass the preceding ten-unit bound? **Solution:** No; it lies seventeen from 410, outside 400 through 420. A value of 415 would pass that bound but would still be wrong.

## Independent problem set and explanatory key

Calculate exactly, then check by a different representation. For P1–P6 also estimate using nearest tens and state the estimate's absolute error. For P7–P10 use inverse and sign checks instead.

P1. 297 + 406.
P2. 684 + 219.
P3. 902 − 487.
P4. 1,004 − 998.
P5. 149 + 251 + 98.
P6. 600 − 297.
P7. −12 + 5.
P8. 7 − (−8).
P9. −4 − 9.
P10. 305 + 96.

Solutions:

P1. 703; estimate 710, error seven.
P2. 903; estimate 900, error three.
P3. 415; estimate 410, error five.
P4. 6; estimate zero, error six; a small difference is obscured.
P5. 498; estimate 500, error two, within the three-input bound fifteen.
P6. 303; estimate 300, error three.
P7. −7; adding five moves right from −12 without reaching zero.
P8. 15; subtract negative eight by adding eight; 15 + (−8) = 7.
P9. −13; removing positive nine moves left; −13 + 9 = −4.
P10. 401; add 100 then remove four, or verify 401 − 96 = 305.

## Transfer and failure diagnosis

T1. Two independent counts are each reported rounded to the nearest hundred. Their displayed sum is 1,200. What absolute-error bound follows for the sum of the unrounded counts? **Solution:** Each rounding changes its count by at most fifty; combined error is at most one hundred. The true sum therefore lies within 1,100 through 1,300, though endpoint attainability depends on the tie convention. Do not infer that each displayed count was itself an observed exact count.

T2. A job count a lies between −5 and −2 in a signed accounting convention, and adjustment b between 3 and 6. Find the range of a + b. **Solution:** −2 through 4 inclusive, by endpoint addition. The interval crosses zero, so the sign cannot be inferred without more information.

T3. A program reports 500 − 198 = 312. A learner accepts it because it is near 300. **Solution:** Exact answer 302. Nearest-ten approximation is 300 with a ten-unit error bound; 312 is outside that bound. Inverse checking also rejects it because 312 + 198 = 510. Both are meaningful checks; “near” without tolerance was not.

## Computational and AI-augmented practice

Use a checking sequence: verify source inputs and units; estimate or bound; calculate exactly; test an inverse relation; reconcile any discrepancy. Do not repeatedly ask the same tool until it agrees with an expected answer. Preserve the original disagreement and identify whether it came from transcription, interpretation, arithmetic or a rounding convention.

Constructed AI claim: “My total matches the spreadsheet total, so every record is correct.” Use the 240/160 and 250/150 example to refute the inference. Totals can conceal offsetting errors. Independent checking means choosing a different error-detection mechanism, not simply opening a second chat window.

Computational experiments can enumerate integer inputs and verify a stated rounding bound over a declared finite range. Such tests provide useful evidence and catch code defects; the error derivation explains why the mathematical rule holds beyond the tested range. Distinguish finite evidence, general reasoning and unverified extrapolation.

## Quiz, alternate form and mastery

Award two points per item: one for the result/judgment, one for justification.

Q1. Exact value and nearest-ten estimate of 196 + 308. Q2. Same for 701 − 298. Q3. Maximum absolute error from adding two nearest-ten rounded inputs. Q4. If 10 ≤ a ≤ 12 and 4 ≤ b ≤ 7, bound a − b. Q5. Does matching a total prove each input correct?

Answers: Q1 exact 504, estimate 510. Q2 exact 403, estimate 400. Q3 ten. Q4 three through eight. Q5 no; offsetting input errors can preserve the total.

Alternate form: R1 287 + 416; R2 802 − 397; R3 error bound for three nearest-ten rounded inputs; R4 20 ≤ a ≤ 24 and 6 ≤ b ≤ 9, bound a − b; R5 explain why a value inside an estimate interval can still be wrong. Answers: exact 703/estimate 710; exact 405/estimate 400; fifteen; eleven through eighteen; the interval is a necessary check, not a unique solution.

Require nine of ten independent exact answers correct, correction of all estimate/bound errors, 8/10 quiz points and a justified new interval or data-integrity transfer. Review rounding for approximation errors, Lesson 18 for signed direction, and inverse operations for failed checks. Retrieve: check inputs, bound the result, compute, add back, and explain what each check actually establishes.
