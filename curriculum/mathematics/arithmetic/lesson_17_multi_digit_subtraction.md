# Lesson 17: Multi-digit subtraction

Canonical ID: AR-L02-17. Discipline: established mathematics. Subject: Arithmetic.
Prerequisites: [subtraction meaning](lesson_15_meaning_of_subtraction.md), [subtraction facts](lesson_16_subtraction_facts.md), and [place-value addition](lesson_13_multi_digit_addition.md).
Next: [signed addition and subtraction](lesson_18_signed_addition_subtraction.md).
Education-16 and Symbol256: new lesson mapping deferred pending academic and taxonomy validation.

## Entry check and outcomes

Describe 302 as three hundreds, zero tens and two ones. Explain why one hundred can be exchanged for ten tens. Find 13 − 8 and check with addition. Responses: 300 + 0 + 2; both representations count one hundred units; five, because eight plus five equals thirteen. Return to place value or subtraction facts if any explanation is uncertain.

By the end, subtract whole numbers with a nonnegative result, align like units, regroup through zeros, explain why exchanges preserve the starting amount, and check a difference by addition. A correct answer must include a trace or decomposition, not only a calculator display. Signed results are taught next; decimal alignment is reserved for the decimal module.

## Vocabulary and first principles

An **exchange** changes a number's representation without changing its value. A **regrouped minuend** records the same starting amount in smaller units. In column subtraction, **borrowing** is traditional shorthand for such an exchange; it is not a loan that adds extra quantity. The donor column must decrease when the receiving column increases.

Build 52 with five bundles of ten and two loose counters. To remove 28, two loose ones are insufficient to remove eight ones. Open one ten-bundle. There are now four tens and twelve ones, still fifty-two. Remove two tens and eight ones, leaving two tens and four ones: twenty-four. The representation 4 tens + 12 ones has the same value as 5 tens + 2 ones.

The method works because corresponding place contributions can be removed separately once enough of each unit is represented. Every exchange replaces one unit of a place by ten units of the next smaller place. The invariant—the quantity that stays unchanged—is the total value of the minuend before removal. Tracking that invariant prevents adding ten ones without reducing the tens count.

## Algorithm and worked examples

Write whole numbers with ones under ones, then tens under tens, and so on. Work from the smallest place. If that place has fewer available units than needed, exchange from a higher place. Continue until each column can be subtracted. Preserve internal zero digits and check the result by adding it to the subtrahend. The check must reproduce the original minuend.

**E1 — no exchange.** 764 − 231 = 533. Ones four minus one is three; tens six minus three is three; hundreds seven minus two is five. Check 231 + 533 = 764.

**E2 — one exchange.** 52 − 28 = 24. Rewrite fifty-two as four tens and twelve ones. Twelve minus eight leaves four ones; four minus two leaves two tens. Check 28 + 24 = 52. If the tens digit remains five after exchanging, the erroneous answer would be thirty-four.

**E3 — a zero in the middle.** 402 − 178 = 224. Exchange one hundred to obtain three hundreds, ten tens and two ones. Exchange one of those tens to obtain three hundreds, nine tens and twelve ones. Subtract eight ones, seven tens and one hundred. The remaining quantities are four ones, two tens and two hundreds. Check 178 + 224 = 402.

**E4 — several zeros.** 3,000 − 786 = 2,214. Rewrite three thousand as two thousands, nine hundreds, nine tens and ten ones. Subtract six ones, eight tens and seven hundreds. Four ones, one ten, two hundreds and two thousands remain. Check 786 + 2,214 = 3,000. The two intermediate nines record units retained after passing one unit onward.

**E5 — unequal lengths.** 5,006 − 89 = 4,917. Match nine with six ones and eight with zero tens. Exchanges yield four thousands, nine hundreds, nine tens and sixteen ones. Removing eight tens and nine ones leaves four thousands, nine hundreds, one ten and seven ones. Check 89 + 4,917 = 5,006.

**E6 — a useful alternative.** 1,002 − 997 = 5 can be found by counting up: three from 997 to 1,000 and two to 1,002. Column subtraction is valid, but a small gap makes the addition-complement route efficient. Algorithm choice does not change the question.

**E7 — hypothetical stock.** Begin with 2,405 items and remove 678 distinct items. The remainder is 1,727 items. Check 678 + 1,727 = 2,405. The result assumes no other arrivals, departures or duplicates; verifying the arithmetic does not verify a real inventory record.

## Guided practice

G1. 81 − 46. **Solution:** Eight tens and one one become seven tens and eleven ones. Eleven minus six is five, seven minus four is three: 35.

G2. 600 − 257. **Solution:** Five hundreds, nine tens and ten ones remain after exchange. Subtract to obtain 343; 257 + 343 = 600.

G3. Explain a result of 374 for 402 − 178. **Solution:** It cannot be accepted merely because it is positive. Adding 178 gives 552, not 402. Ask for the trace, reconstruct exchanges, and obtain 224. An incorrect output alone does not uniquely identify the learner's mistake.

## Independent problem set and explanatory key

Show unit alignment and each exchange. Verify at least three answers by addition.

P1. 853 − 421.
P2. 72 − 38.
P3. 503 − 267.
P4. 2,000 − 458.
P5. 7,004 − 86.
P6. 10,000 − 1.
P7. 4,321 − 4,321.
P8. 9,008 − 0.
P9. 6,020 − 597.
P10. 1,001 − 998.

Solutions:

P1. 432; each place subtracts without exchange.
P2. 34; six tens and twelve ones minus three tens and eight ones.
P3. 236; four hundreds, nine tens and thirteen ones support the removal.
P4. 1,542; exchange through both zero columns, then check 458 + 1,542 = 2,000.
P5. 6,918; six thousands, nine hundreds, nine tens and fourteen ones precede removal.
P6. 9,999; one ten-thousand is redistributed through every smaller place.
P7. 0; removing the entire quantity leaves none.
P8. 9,008; removing zero preserves the input.
P9. 5,423; after exchanges there are five thousands, nine hundreds, eleven tens and ten ones.
P10. 3; two to reach 1,000 and one more to 1,001.

## Error analysis and transfer

T1. A learner computes 63 − 27 as 44 by subtracting the smaller digit from the larger in each column. **Solution:** Ones represent three minus seven, not seven minus three. Exchange a ten: thirteen minus seven is six; five tens minus two tens is three tens. Correct answer 36. Digits cannot be reversed independently because that changes the original subtraction.

T2. A simulation shows 4,000 queued jobs, 1,275 completed and 48 cancelled. Find the remaining count, assuming these categories are disjoint and no new jobs arrive. **Solution:** Remove 1,323 altogether, leaving 2,677 jobs. Alternatively subtract 1,275 to obtain 2,725, then 48 to obtain 2,677. Agreement does not prove the event records are complete.

T3. Explain why 408 − 93 is not 485. **Solution:** A nonnegative removal cannot increase a nonnegative starting amount. That bound rejects 485 immediately. Exact subtraction gives 315; adding 93 recovers 408. Bounds detect some errors without giving the answer.

## Computational and AI checking

Specify a trace with columns for original place count, exchange received, exchange passed, removal and remainder. For 402 − 178, the final available counts before subtraction are three hundreds, nine tens and twelve ones. Verify their weighted value is 402. Then verify the remainder's weighted value is 224. This separates representation preservation from subtraction facts.

Audit a constructed AI statement: “When borrowing across a zero, change every zero to ten.” The intermediate tens and hundreds usually become nine after passing one unit onward; only the final receiving place gains ten units. Reconstruct 3,000 − 786 to disprove the blanket rule. Tool agreement without an exchange trace is not a derivation.

## Quiz, alternate form and mastery

Score each item out of two: one for the correct result or judgment, one for an explanation or inverse check.

Q1. 945 − 312. Q2. 64 − 29. Q3. 700 − 486. Q4. 8,002 − 75. Q5. Explain why exchanging one hundred for ten tens preserves value.

Answers: 633; 35; 214; 7,927; both representations are one hundred, so the donor hundred decreases by one as the tens increase by ten.

Alternate form: R1 876 − 243; R2 83 − 47; R3 900 − 568; R4 6,003 − 87; R5 explain one thousand exchanged into ten hundreds. Answers: 633; 36; 332; 5,916; both represent one thousand, with the donor reduced once.

Require nine of ten independent problems correct, 8/10 quiz points and a correct new zero-chain transfer with an inverse check. Correct every alignment or value-preservation error before progression. If exchanges fail, rebuild with bundles; if facts fail, return to Lesson 16. Oral, tactile and written explanations are accepted. Retrieve: match units, preserve value, record every exchange, subtract, then add back.
