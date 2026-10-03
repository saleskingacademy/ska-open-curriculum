# Lesson 8: Rounding

Canonical ID: AR-L01-08. Discipline: established mathematics. Subject: Arithmetic.
Prerequisites: Lessons 3–5 for place value, comparison, and number lines; [Lesson 7](lesson_07_estimation.md) for approximation and purpose.
Next: [Lesson 9](lesson_09_mathematical_language.md).
Education-16 and Symbol256: source mapping deferred until the validation gates pass.

## Entry check and objectives

Identify the tens and hundreds digits in 3,476. Explain why 4.30 and 4.3 have equal numerical value. Locate 40, 45, and 50 at equal five-unit intervals on a line. If these tasks are unclear, revisit place value and number-line spacing before learning a digit procedure.

After this lesson, round nonnegative whole numbers to stated places; round nonnegative decimals to tenths and hundredths; explain the nearest-value method with a line; state and use a tie convention; recognize carry across place boundaries; avoid repeated-rounding errors; and distinguish nearest rounding from upward capacity planning. Negative-number rounding is an optional interpretation exercise with an explicitly stated convention, not a prerequisite for the next lesson.

## Vocabulary, symbols, and the chosen convention

The **rounding place** is the place whose unit determines the allowed reported values. Rounding to tens allows 0, 10, 20, 30, and so on. Rounding to hundreds allows 0, 100, 200, and so on. The **neighbors** are the adjacent allowed values around the input. Their **midpoint** is halfway between them. A **tie** occurs when the input is equally close to both neighbors.

For the main nonnegative exercises, use **nearest rounding with ties upward**: choose the closer neighbor; at an exact halfway value choose the larger one. This is a declared convention, not the only possible convention. Other systems use ties to even or other rules. If a tool or instruction uses a different tie rule, state that rule before comparing results.

The notation 347 ≈ 350, to the nearest ten, records an approximation and its place. It does not mean 347 = 350. A **retained digit** is the final digit kept at the requested place. The first discarded digit is immediately to its right. “Round to two decimal places” means retain hundredths, not two total digits.

## First principles: rounding as choosing a nearby allowed value

Mark 30 and 40 on a number line. There are ten one-unit intervals between them. The middle is 35, five intervals from either endpoint. A value such as 32 is two intervals from 30 and eight from 40, so nearest-ten rounding gives 30. A value such as 38 is eight from 30 and two from 40, so it gives 40. At 35, closeness cannot decide: the tie convention chooses 40.

This explains the digit rule. Within the span from 30 to just below 40, a ones digit below five lies on the lower side of the midpoint; a ones digit above five lies on the upper side. A ones digit five is either the midpoint itself or, when further decimal digits are present, on or above it. Thus for nonnegative nearest rounding with ties upward, inspect the first discarded digit: 0–4 keeps the retained value; 5–9 increases the retained place by one unit.

The formal idea extends to larger and smaller place units. For rounding to hundreds, neighbors differ by 100 and midpoints end in 50. For tenths, neighbors differ by 0.1 and midpoints lie 0.05 beyond the lower neighbor. The method stays the same because place value changes the unit, not the meaning of nearest.

## Procedure and interpretation

First state the place and convention. Next identify the adjacent allowed values, or identify the retained and first discarded digits after you understand the line. Select the nearer neighbor, resolving a tie by the stated rule. Replace lower whole-number places with zeros or omit discarded decimal places. Finally check that the answer is an allowed value and is close enough to the original.

A whole-number rounded result needs its placeholder zeros. Rounding 347 to tens gives 350, not 35. Dropping the last digit without preserving place changes the scale. In decimal rounding, 3.476 rounded to hundredths becomes 3.48, not 3.4806. Discarded digits are not pasted onto the rounded result.

A nearest rounding error is at most half of the rounding unit when the input is exact. For nearest tens, that is 5; for nearest hundreds, 50; for nearest tenths, 0.05. This follows because each input between adjacent neighbors is no farther than the midpoint distance from at least one endpoint. At a tie either endpoint has exactly that distance. This error bound concerns the rounding operation, not unknown error already present in the measurement.

## Worked examples with explicit checks

**Example 1 — whole number.** Round 3,476 to the nearest ten. Neighbors are 3,470 and 3,480; midpoint is 3,475. The input is above the midpoint, so choose 3,480. Digit check: retain the 7 in the tens place, inspect the 6 in ones, and increase the tens digit. The gap is four, within five.

**Example 2 — a different place.** Round the same 3,476 to the nearest hundred. Neighbors are 3,400 and 3,500; midpoint 3,450. The input is nearer 3,500. Retain the hundreds digit 4 and inspect the tens digit 7; increase hundreds to 5 and write zeros in tens and ones. The gap is twenty-four, within fifty. A changed rounding place changes the task.

**Example 3 — exact tie.** Round 650 to hundreds. It is equally distant from 600 and 700. Under ties upward for nonnegative values, choose 700. Under ties to even, the hundreds counts 6 and 7 identify 600 as the even choice. The mathematical distances agree; only the tie policy differs. Always disclose which answer your exercise requires.

**Example 4 — hundredths.** Round 4.372 to two decimal places. The rounding place is hundredths: retain 7 and inspect the thousandths digit 2. Keep the retained hundredths, giving 4.37. Neighbors 4.37 and 4.38 have midpoint 4.375; 4.372 is below it. The gap is 0.002, within 0.005.

**Example 5 — carry.** Round 9.96 to tenths. The lower neighbor is 9.9, the upper neighbor 10.0, and the midpoint 9.95. Choose 10.0. Increasing the retained 9 tenths causes a regroup into the ones place. The notation 10.0 communicates the requested tenths place. The numerical value equals 10, but the reporting intention is clearer with the decimal zero.

**Example 6 — carry through several positions.** Round 9,995 to tens. It lies halfway between 9,990 and 10,000. Ties upward selects 10,000. There is no requirement that a rounded result retain the original number of digits. A boundary crossing is a correct consequence of the rule, not an exception to it.

**Example 7 — direct versus repeated rounding.** Round 2.449 directly to tenths. Neighbors 2.4 and 2.5 have midpoint 2.45. The original is below it, giving 2.4. If first rounded to hundredths, it becomes 2.45; rounding that changed value to tenths then gives 2.5 under ties upward. Avoid intermediate rounding when the original information remains available.

**Example 8 — guaranteed capacity.** There are 241 attendees; seating is arranged in complete groups of ten. Nearest-ten rounding gives 240, which cannot seat all 241. For a capacity at least the known count, choose the next allowed value upward, 250. This is upward rounding for coverage, not nearest rounding. If the count is exactly 240, capacity 240 suffices without an extra group.

## Guided practice

G1. Round 83 to tens. **Reasoning:** Neighbors 80 and 90, midpoint 85; 83 is below it. Answer 80, gap three.

G2. Round 1,250 to hundreds under the main convention. **Reasoning:** Halfway between 1,200 and 1,300; select 1,300 by ties upward. Do not inspect the thousands digit.

G3. Round 6.08 to tenths. **Reasoning:** The hundredths digit 8 moves 6.0 to 6.1. Trailing zero in the lower neighbor does not erase its position.

G4. A learner rounds 748 to hundreds and writes 8. **Diagnosis:** They lost positional weight. Correct 700 because the tens digit 4 keeps seven hundreds; even a different input that rounded upward would need 800, not 8.

## Independent practice and explanatory solutions

Use nonnegative nearest rounding with ties upward unless the task specifies otherwise. For each rounded answer, identify the rounding place or adjacent neighbors.

P1. Round 146 to tens.
P2. Round 146 to hundreds.
P3. Round 2,349 to hundreds.
P4. Round 2,350 to hundreds.
P5. Round 0.864 to hundredths.
P6. Round 7.05 to tenths.
P7. Round 99.95 to tenths.
P8. Round 3.449 directly to tenths, then compare with rounding first to hundredths and then to tenths.
P9. A known count of 371 items needs storage capacity in groups of one hundred. Give the smallest sufficient allowed capacity. Explain why nearest-hundred rounding is unsuitable.
P10. An exact value rounded to the nearest hundred is 500. What is the largest possible rounding error size? Could the unrounded value be 560?

Answers: P1 150, ones 6 increases tens; P2 100, tens 4 keeps hundreds; P3 2,300, below midpoint 2,350; P4 2,400, an exact tie resolved upward; P5 0.86, thousandths 4 retains hundredths; P6 7.1, halfway resolved upward; P7 100.0, halfway between 99.9 and 100.0 with carry; P8 direct 3.4 because original is below 3.45, but intermediate 3.45 rounds to 3.5; P9 400, since 300 cannot cover 371 and nearest rounding would give 400 in this instance, but the method needs an upper capacity in every case, such as 341 where nearest gives insufficient 300; P10 at most 50, and 560 is impossible because it rounds to 600.

For P9, the important explanation is methodological: the particular result happens to agree with nearest rounding, but the capacity rule must guarantee coverage for any valid input. Do not claim nearest rounding is unsuitable because it fails for 371; it does not fail for that count.

## Applied problem and error diagnosis

A record contains exact measured lengths 18.46 cm and 18.44 cm. A report rounds each to tenths. Determine the reports and explain whether the original lengths are equal. Reports are 18.5 cm and 18.4 cm, and originals are unequal. Now consider 18.41 cm and 18.44 cm: both report 18.4 cm, but remain unequal. Equal rounded reports do not establish exact equality.

Diagnose the statement “0.049 rounded to hundredths is 0.04 because 4 is less than 5.” The student inspected the retained hundredths digit rather than the first discarded thousandths digit 9. Correct answer 0.05. Mark the place before inspecting a digit.

Diagnose “Rounding 4,999 to thousands gives 4,000 because the first digit is four.” The neighbors are 4,000 and 5,000, and the input is much nearer 5,000. The first discarded hundreds digit 9 determines the move. Correct answer 5,000.

## Edge cases and optional negative extension

An already allowed value stays fixed: 240 rounded to tens is 240. Zero rounded to tens remains zero. For whole-number nearest rounding, leading zeros do not change value, while zeros in lower places may be required in the result. A precise-looking decimal report does not prove that the underlying measurement had equal precision.

The phrase “round up” is ambiguous for negatives. For an optional extension, declare **nearest with ties away from zero** for all signed inputs. Then −25 rounded to tens is −30: both −20 and −30 are five away, and −30 is farther from zero. Under nearest with ties toward positive infinity, the same tie becomes −20. For −24 the nearest result is −20 under either policy because it is four away rather than six. Do not apply a nonnegative tie sentence silently to negative values. Signed rounding policy deserves explicit treatment in computational arithmetic later.

## Calculator, programming, and AI verification

For a calculator result, first identify the requested place and the device's tie policy if it is known. Display settings may shorten a visible number without changing the stored value. Copying a rounded display into a later calculation may change the input, as the repeated-rounding example shows. This is a distinction to check, not a claim about every calculator.

Optional algorithm description: take an exact nonnegative whole number and a requested place; locate the neighboring multiples of the place unit; compare distances; at a tie choose the upper neighbor. Trace 146 at tens, 650 at hundreds, and 9,995 at tens. The expected outputs are 150, 700, and 10,000. Explain each trace before attempting an implementation in a later programming lesson.

AI-audit exercise: a constructed solution rounds 2.449 to 2.45 and then announces “therefore nearest tenth is 2.5.” Identify the intermediate information loss and independently round the original. Correct 2.4. Agreement from multiple tools cannot override the original's position below the midpoint. Later numerical analysis studies propagation of such errors.

## Summary, review, and quiz

Use nearest allowed values, not an isolated digit trick. Specify place and tie convention. Keep placeholder zeros when whole-number scale requires them. Check carry, preserve the original for final rounding, and use a genuine upward capacity method when all items must fit. The nearest rounding error bound is half of the place unit for an exact input.

Quiz, two points each: one for the answer and one for place-based reasoning.

Q1. Round 275 to tens under ties upward.
Q2. Round 1,949 to hundreds.
Q3. Round 3.995 to hundredths under ties upward.
Q4. Explain why an exact 198 cannot be replaced by rounded 200 in a proof of exact equality.
Q5. There are 204 items and capacity is available only in tens. What is the smallest sufficient capacity?

Answers: Q1 280, tie between 270 and 280; Q2 1,900, below 1,950; Q3 4.00, tie between 3.99 and 4.00 with carry; Q4 rounding changes the value by two and approximation is not equality; Q5 210, because 200 is insufficient. Writing 4 is numerically correct for Q3, but retain 4.00 to show the requested reporting place.

Reassessment: R1 685 to hundreds; R2 0.095 to hundredths; R3 301 items, capacity in hundreds. Answers: 700 because above 650; 0.10 by a tie and carry; 400 because 300 is insufficient.

## Mastery and remediation

Require at least 8/10 quiz points, at least 9/10 independent tasks correct, and a correct direct-versus-repeated-rounding explanation for P8. Correct all place-value and capacity errors before progressing. Explain one ordinary case, one tie, and one carry with a number line.

If the wrong digit is inspected, mark the rounding place and its immediate right neighbor in five numerals. If zeros disappear, write both the place name and expanded rounded value. If carry fails, locate neighbors across a boundary instead of trying to repair a digit in isolation. If capacity and nearest rounding are mixed, compare 241 and 249 with a ten-place capacity rule. Retake alternate items unaided. Connections: Lesson 7's approximation bounds become quantitative here; later money, measurement, algorithms, and numerical precision require the same distinctions.
