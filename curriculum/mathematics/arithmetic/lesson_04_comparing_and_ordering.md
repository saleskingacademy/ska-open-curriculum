# Lesson 4 companion: Comparing and ordering

Canonical ID: AR-L01-04. Established mathematics; Arithmetic.
Read [existing Lesson 4](level_01_lessons_01_05.md#lesson-4-comparing-and-ordering) with this companion. Prerequisite: [place value](lesson_03_place_value.md) and quantity comparison. Next: [Lesson 5](lesson_05_number_lines.md).
Education-16 and Symbol256: deferred until validation. Negative comparison is introduced through position; full negative interpretation follows in Lesson 6.

## Learning outcomes, vocabulary, and notation

Compare nonnegative whole numerals by value, compare decimals with matching place units, arrange a list least-to-greatest, read and reverse inequalities, and diagnose unreliable digit-count or printed-string comparison. Interpret negative order from a supplied signed line without assuming signed calculation rules.

Less than means smaller numerical value; greater than means larger. Equal means the same value. Ascending order proceeds least-to-greatest. Descending order reverses it. The symbols <, > and = record comparisons. Use ≤ and ≥ only when equality is permitted too; Lesson 9 develops these boundaries. A numerical comparison differs from sorting written symbols alphabetically.

## First principles and formal explanation

Pair objects from collections of three and five. After every object in the smaller collection is paired, two remain in the larger. Thus three is fewer than five. On a standard horizontal number line, the same order is represented by three lying left of five. These models connect quantity comparison to numerical order.

For positive whole numerals without leading zeros, more digit positions means a larger value. The smallest three-digit positive whole number is 100, larger than the largest two-digit one, 99. With equal lengths, compare the greatest place first. If it matches, continue right until the first different place; that place determines order because lower-place contributions cannot overturn it.

For decimals, matching units is essential. Rewrite 0.6 as 0.60 before comparing with 0.58. Six tenths exceeds five tenths; the additional eight hundredths cannot bridge that tenth boundary. Trailing zeros allow aligned comparison without changing value. The number of printed decimal digits does not by itself measure size.

On a supplied signed line, left is smaller and right larger. Thus −8 < −3. Distance from zero is a different comparison: eight units is farther than three. Do not replace the negative reading with its unsigned digits when the question asks numerical order.

## Worked examples

Example 1: Compare 7,205 and 7,250. Thousands and hundreds match. Tens are zero versus five, so 7,205 < 7,250. Comparing ones first would answer incorrectly because the greatest differing place controls value.

Example 2: Compare 4.09 and 4.9 by rewriting the latter 4.90. Whole units match; tenths zero versus nine determines 4.09 < 4.90.

Example 3: Sort −4, 2, −1 and 0 with a labeled line. Ascending order is −4, −1, 0, 2. Reversing gives descending 2, 0, −1, −4. The same values are present; only order changes.

## Guided and independent practice

G1. Compare 80 and 8. Answer: 80 > 8, eight tens exceeds eight ones.
G2. Compare 2.50 and 2.5. Answer: equal, added zero hundredths contributes nothing.
G3. Reverse 6 < 9 without changing meaning. Answer: 9 > 6.

P1. Compare 9,099 and 9,100.
P2. Compare 305 and 350.
P3. Compare 0.407 and 0.47 by alignment.
P4. Compare 6.20 and 6.2.
P5. Order 18, 8, 80, 108 least-to-greatest.
P6. Order −2, −6, 3 and 0 on a supplied signed line.
P7. Rewrite 4 > 1 with reversed sides.
P8. Explain why “more decimal digits means larger” fails for 0.09 and 0.9.
P9. A numerical threshold requires a value greater than 10. Do 9, 10 and 11 qualify?
P10. A system orders the strings “100” and “20” by their first character. Explain why that is not a valid numerical comparison of one hundred and twenty.

Solutions: P1 9,099 < 9,100, first differing hundreds; P2 305 < 350, first differing tens; P3 0.407 < 0.470, first differing hundredths; P4 equal by zero contribution; P5 8, 18, 80, 108; P6 −6, −2, 0, 3; P7 1 < 4; P8 nine hundredths is smaller than nine tenths despite more printed places; P9 only 11, because greater than is strict and excludes 10; P10 written-symbol order is a different rule, whereas numerical place value establishes 100 > 20.

## Applications, error diagnosis, and edge cases

Sorting prices, measured lengths and counts requires consistent units. A numeral 12 cannot be compared meaningfully as a length with a numeral 9 whose unit is unknown. First establish what each represents; unit conversion is later. Likewise, numerical rank does not automatically imply desirability: a smaller error may be better, while a larger capacity may be useful. Separate numerical order from the decision criterion.

Diagnosis exercise: a learner compares 0.8 with 0.75 and says 75 > 8 so 0.75 is larger. They discarded positional units. Align 0.80 and 0.75; eight tenths exceeds seven tenths, so 0.8 is larger. Diagnosis exercise: “−100 must exceed −2 because it has more digits.” The positive-whole digit-count rule was used outside its scope. A signed line places −100 farther left.

Equal numerical values may have different written forms. Leading zeros are not extra positional magnitude in ordinary numerical comparison. Duplicate values in a sorted list remain present; sorting does not require deleting them. Zero is below positive values and above negative ones. Near-equal rounded reports do not prove exact equality of underlying measurements.

## Computation, tools, and AI

Optional comparison algorithm: first confirm values are in a supported domain and convention, then compare greatest place units before smaller places. For nonnegative whole numerals, ignore leading numerical zeros and compare lengths, then equal-length digits. Do not apply that specification to arbitrary signed or decimal strings. Test 100/20, 305/350 and 007/7 as numerical values; expected >, < and =.

A calculator or program requires correct input interpretation. Constructed AI claim: “0.507 is greater than 0.57 because 507 is greater than 57.” Preserve decimal place weights and compare 0.507 with 0.570. The claim is false. Verify with a chart; the hundredths discrepancy decides order.

## Review, quiz, reassessment, and mastery

Retain: compare like units; numerical order is left-to-right on a standard line; equal-length positive whole numerals are decided by the greatest differing place; decimal trailing zeros preserve value. Practice predicting the first deciding place before writing the relation.

Quiz, two points per item for relation and reason:
Q1. Compare 4,901 and 4,910.
Q2. Compare 0.305 and 0.35.
Q3. Is 8.00 equal to 8?
Q4. Order −3, 1, −8, 0 on a signed line.
Q5. Reverse 7 > 2 with equivalent meaning.

Answers: 4,901 < 4,910 by tens; 0.305 < 0.350 by hundredths; yes, zero decimal contributions add nothing; −8, −3, 0, 1; 2 < 7. Reassessment: compare 6,087/6,078, compare 0.606/0.66, and sort −1, −5, 2. Expected > by tens; < by hundredths after alignment; −5, −1, 2.

Require 8/10 quiz points, nine of ten independent tasks correct and correction of all positional/sign errors. Use an accessible line for signed comparisons rather than memorizing a slogan. Remediation: rebuild like-unit pairs on a chart, compare five pairs one place at a time, and read reversed inequalities aloud. Later number lines, thresholds, algebraic inequalities and algorithm sorting all depend on preserving numerical meaning and scope.
