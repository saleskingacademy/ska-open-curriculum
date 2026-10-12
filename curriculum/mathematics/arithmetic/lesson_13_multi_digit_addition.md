# Lesson 13: Multi-digit addition

Canonical ID: AR-L02-13. Discipline: established mathematics. Subject: Arithmetic.
Prerequisites: whole-number place value from Lesson 3; [addition meaning](lesson_11_meaning_of_addition.md) and [addition facts](lesson_12_addition_facts.md); [estimation](lesson_07_estimation.md).
Next: Lesson 14, Mental addition, in [the sequence](../arithmetic_zero_to_advanced.md).
Education-16 and Symbol256: deferred until source and assessment validation.

## Entry check and learning outcomes

Describe 247 as two hundreds, four tens and seven ones. Explain why ten ones can be exchanged for one ten without changing the quantity. Derive 8 + 7 = 15 and identify one ten and five ones in the result. If any task is uncertain, use bundles of ten and review Lessons 3 and 12 before the written algorithm.

By the end, add nonnegative multi-digit whole numbers by expanded place value and by aligned columns; explain regrouping as an equal-value exchange; handle different digit lengths, internal zeros and cascading carries; add three or more contributions; diagnose alignment and carry errors; estimate scale before calculating; and verify a result by a genuinely different decomposition. Decimal column addition and signed inputs are reserved for later lessons.

## Vocabulary, notation, and scope

A **column** groups digits of the same positional unit: ones with ones, tens with tens, hundreds with hundreds. **Alignment** places like units together. **Regrouping** exchanges ten of one unit for one of the next larger unit. A **carry** records that newly formed larger unit to include in the next column. A **running total** is a partial sum maintained as contributions are processed.

Write a final result as a numeral with its original quantity unit. Internal zeros must remain when they hold a position. A blank higher place in a shorter nonnegative whole numeral can be treated as zero for adding, but a blank unknown quantity is not a confirmed zero. The distinction is between a missing digit position in a known number and missing information about the number itself.

The algorithm here adds whole numbers. It does not authorize arbitrary right alignment for decimals: decimal alignment must match place units, not simply the last printed digit. That later treatment builds on the same principle.

## First principles: equal-value exchanges

Build twenty-seven counters as two bundles of ten and seven loose ones. Build fifteen as one bundle and five loose ones. Join corresponding units. There are three bundles of ten and twelve loose ones. Exchange ten of those loose ones for another bundle; the result has four tens and two ones, forty-two. The quantity did not change during exchange. This models 27 + 15 = 42.

The written carry procedure compresses this regrouping. Add ones seven and five to get twelve ones. Record two ones in the ones place and carry one ten to tens. Add tens two, one and the carried one to get four tens. The final numeral 42 is correct because its positional components match the regrouped collection.

Carry is not a magical extra digit. It is a count of larger units already created in the smaller column. Omitting it loses those units; adding it twice duplicates them. Naming the units in each column makes the bookkeeping visible.

## Conceptual and formal explanation of the algorithm

Place-value expansion writes a number as contributions such as 247 = 200 + 40 + 7. Addition's commutativity and associativity allow regrouping corresponding place contributions. Thus 247 + 135 = (200 + 100) + (40 + 30) + (7 + 5). The ones contribution twelve becomes ten and two, making the tens contribution eighty; total 382.

For a two-addend column, let d and e be the digits in that place and c the carry from the place immediately to the right. The column total t = d + e + c is a count of that column's unit. Decompose t into complete groups of ten and leftover units. Write the leftovers in that column and carry the complete groups to the next. For two addends, the carry is at most one: each digit is at most nine, and an incoming carry at most one gives a maximum nineteen.

With three or more addends, a carry can exceed one. For three digits of nine with an incoming carry two, the total can be twenty-nine; two larger units carry and nine remain. Therefore do not memorize “carry always means one” as a universal law. It is a property of adding two nonnegative whole numerals in base ten.

Work right to left because the grouping result from a smaller place determines what must be included in the next place. Expanded addition may be done in another order if it tracks all contributions correctly. The written method's direction is a convenient dependency order, not a rule that quantities can only be thought about from right to left.

## Worked examples and independent checks

**Example 1 — no regrouping.** Add 234 + 152. Ones: four plus two gives six. Tens: three plus five gives eight. Hundreds: two plus one gives three. Result 386. Expanded check: 200 + 100 gives 300, 30 + 50 gives 80, 4 + 2 gives 6; combined 386.

**Example 2 — one carry.** Add 247 + 135. Ones seven plus five gives twelve: write two and carry one ten. Tens four plus three plus carried one gives eight. Hundreds two plus one gives three. Result 382. Roughly 250 + 150 is about 400, which is a scale check; it does not prove the exact result. Expanded reasoning above verifies it exactly.

**Example 3 — carry across columns.** Add 586 + 279. Ones six plus nine gives fifteen, write five/carry one. Tens eight plus seven plus one gives sixteen, write six/carry one. Hundreds five plus two plus one gives eight. Result 865. Check by partitioning 279 into 200, 70 and 9: 586 + 200 = 786; +70 = 856; +9 = 865.

**Example 4 — different lengths.** Add 4,706 + 85. Match 85's five ones with six ones and its eight tens with zero tens. Ones gives eleven, write one/carry one. Tens zero plus eight plus one gives nine. Hundreds seven plus zero gives seven; thousands four plus zero gives four. Result 4,791. Aligning 85 under the thousands would represent a different addend.

**Example 5 — new highest place.** Add 9,999 + 1. Ones nine plus one gives ten, write zero/carry one. Each subsequent nine plus carry also gives ten, so write zero and carry again. The final carry forms one ten-thousand. Result 10,000. Internal zeros preserve all place positions. A sum may need more digits than either addend.

**Example 6 — three addends.** Add 468 + 257 + 389. Ones eight plus seven plus nine gives twenty-four: write four and carry two tens. Tens six plus five plus eight plus two gives twenty-one: write one and carry two hundreds. Hundreds four plus two plus three plus two gives eleven: write one and carry one thousand. Result 1,114. Check pairwise: 468 + 257 = 725, then 725 + 389 = 1,114. The carry two is legitimate and essential.

**Example 7 — stock record with multiple contributions.** Start with 1,208 units, add 375 distinct delivered units, then 46 more. Pairwise, 1,208 + 375 = 1,583, and 1,583 + 46 = 1,629. Alternatively 375 + 46 = 421 and 1,208 + 421 = 1,629. Record units and delivery identity so the same shipment is not counted twice. Matching numerical routes check arithmetic; shipment records check input integrity.

## Guided practice

G1. Add 36 + 48. **Response:** Ones six plus eight gives fourteen, four ones and one carried ten. Tens three plus four plus one gives eight. Result 84.

G2. Add 305 + 27. **Response:** Match ones and tens. Five plus seven gives twelve; zero tens plus two plus carry one gives three; hundreds remain three. Result 332.

G3. Add 698 + 7. **Response:** Ones fifteen gives five/carry one; tens nine plus one gives ten, zero/carry one; hundreds six plus one gives seven. Result 705.

G4. A learner gets 72 for 36 + 48 by writing each column's units digit and ignoring carry. **Diagnosis:** Correct tens must include the carried ten from fourteen ones; the stated 72 also has the ones wrong. Recompute both columns and obtain 84 rather than assuming only one error occurred.

## Independent problem set and explanatory key

Show aligned units or an expanded decomposition. Check at least P4, P7 and P10 by another route.

P1. 213 + 145.
P2. 268 + 157.
P3. 509 + 86.
P4. 786 + 459.
P5. 4,008 + 75.
P6. 999 + 9.
P7. 587 + 246 + 398.
P8. 12,345 + 6,789.
P9. A warehouse has 1,475 cartons, receives 286 new cartons, then receives 39 different cartons. Find final stock.
P10. A record gives 1,007 + 98 = 1,015. Diagnose a plausible carry/placement mistake and compute the correct sum.

Solutions:

P1. 358; columns 8 ones, 5 tens, 3 hundreds, without regrouping.
P2. 425; ones fifteen yields five/carry one; tens six plus five plus one gives twelve, write two/carry one; hundreds two plus one plus one gives four.
P3. 595; ones nine plus six gives fifteen, tens zero plus eight plus one gives nine, hundreds five.
P4. 1,245; ones fifteen, tens fourteen after carry, hundreds twelve after carry, producing a new thousands unit. Check 786 + 400 = 1,186, +50 = 1,236, +9 = 1,245.
P5. 4,083; ones thirteen, tens eight including carry, hundreds zero retained, thousands four.
P6. 1,008; ones eighteen produces eight, and the carry passes through tens/hundreds into thousands.
P7. 1,231; ones twenty-one yields one/carry two; tens eight plus four plus nine plus two gives twenty-three, three/carry two; hundreds five plus two plus three plus two gives twelve, two/carry one. Pairwise 587 + 246 = 833; plus 398 gives 1,231.
P8. 19,134; ones fourteen, tens thirteen, hundreds eleven, thousands nine after carry, ten-thousands one. Check 12,345 + 6,000 = 18,345; +700 = 19,045; +80 = 19,125; +9 = 19,134.
P9. 1,800 cartons; first 1,475 + 286 = 1,761, then +39 = 1,800. Deliveries are different contributions.
P10. Correct 1,105. Ones seven plus eight gives fifteen; tens zero plus nine plus carry one gives ten, producing a hundreds carry. Dropping the hundreds carry alone would produce 1,005, not the reported 1,015. The displayed answer therefore needs further explanation; request the learner's trace instead of asserting a unique cause.

## Applied reasoning and error-diagnosis tasks

A1. Three event counts are 198, 203 and 97. Estimate the combined scale, then compute exactly. **Solution:** About 200 + 200 + 100 = 500; exact 198 + 203 = 401, then +97 = 498. A result near 5,000 would fail the scale check. An estimate of 500 is compatible with 498 but does not prove it.

A2. A spreadsheet reports 499 + 501 = 910. Is scale estimation sufficient to identify the exact error? **Solution:** A rough total of about 1,000 suggests checking 910, but without a justified tolerance it does not conclusively reject it or identify the process. Exact regrouping or the decomposition 499 + 500 + 1 = 1,000 gives the correct sum. Review entered values and cell references before attributing the error to carry.

A3. A student aligns 72's seven with the hundreds digit of 405 and its two with tens. What addition did the placement actually represent? **Solution:** 405 + 720, giving 1,125, rather than 405 + 72 = 477. Misalignment changes input meaning, not merely the appearance of the work.

## Misconceptions and edge cases

Do not concatenate column totals: ones twelve and tens seven do not make “712.” Interpret twelve ones as one ten/two ones and include the ten before completing the next column. Do not carry a written digit directly without its unit. A carried two from a ones column means two tens, not two ones to be counted again.

Zero columns must remain in their positions even when their sum is zero. A blank higher position in a known shorter whole number contributes zero; an unknown stock field does not. Different-length numerals require right alignment only because their final digits are ones in this whole-number scope. Decimal inputs require a different printed alignment that still follows matching units.

Adding zero preserves a multi-digit numeral. For two addends, no result can exceed the sum obtained from all-nine upper bounds for the given lengths; however such a coarse bound rarely proves a precise answer. For many addends, carry may exceed one. For arbitrarily large numerals, the place-value method still describes a finite calculation, although its workload grows. Computational resource limits are a later subject, not evidence that whole-number addition changes its laws.

## Computational treatment and AI verification

Algorithm specification: begin at ones with carry zero. Add the two current digits and the incoming carry. Exchange each full group of ten for one next-place unit. Write the leftover digit, retain the carry, and move one place left. Continue through all input places and any final carry. Missing higher digits in known shorter whole numerals count as zero. Keep a record of each place's digit total and exchange.

Trace table exercise: for 58 + 67, record ones inputs eight/seven/carry zero, total fifteen, output five/carry one; then tens five/six/carry one, total twelve, output two/carry one; then hundreds zero/zero/carry one, output one. Result 125. The trace demonstrates that every created larger unit is processed exactly once. A later program can implement this, but the specification must be understood independently.

Calculator check: enter known addends and compare the display with your hand result. Then verify one sum by expanded decomposition as well, so both methods do not merely repeat an input mistake. If original values were mistyped consistently into both tools, agreement alone is weak evidence.

Constructed AI-audit claim: “468 + 257 + 389 = 914 because each carry is at most one.” The two-addend carry bound was extended to three addends incorrectly. The actual ones total is twenty-four, requiring carry two; tens then total twenty-one, also carry two; correct sum 1,114. Show the trace and independent pairwise check. The audit separates a true limited rule from its invalid generalization.

## Review, quiz, and reassessment

Retain matching-unit alignment, equal-value regrouping, carry inclusion once, and final carry preservation. Review one no-carry case, one single carry, one chain of carries, one unequal-length case and one three-addend case. Explain a carry in words before practicing a faster layout.

Quiz, two points per item: one for the result and one for a correct trace or decomposition.

Q1. 324 + 152.
Q2. 487 + 268.
Q3. 2,009 + 96.
Q4. 9,999 + 2.
Q5. Explain why three-addend column sums can carry two, using 8 + 7 + 9 in the ones column.

Answers: Q1 476 with no carry; Q2 755 with ones fifteen and tens fifteen after carry; Q3 2,105 with ones fifteen and tens ten after carry; Q4 10,001 through cascading carries; Q5 twenty-four ones exchange for two tens with four ones left. For Q5 award one point for the decomposition and one for explaining the carried unit.

Reassessment: R1 356 + 178; R2 5,007 + 84; R3 8,999 + 3; R4 279 + 386 + 458. Answers: 534; 5,091; 9,002; 1,123, with ones twenty-three/carry two, tens twenty-two/carry two, hundreds eleven/carry one. Require the place-unit reasoning.

## Mastery and remediation

Require at least 8/10 quiz points, nine of ten independent problems correct, correction of all alignment/carry errors, and an independent exact check of a new three-addend problem. Show one large sum through expanded notation and aligned columns, explaining why their values agree.

If alignment fails, write headings for every place and insert higher zero contributions deliberately. If carry fails, model groups with loose counters and ten-bundles, then label each carried unit. If a carry is duplicated, tick it only when included in the next column. If three-addend cases fail, write the actual column total before exchanging groups rather than assuming a carry of one. Return to Lesson 12 when small fact errors are the source. Later mental addition uses alternative decompositions; decimal and computational addition reuse matching-unit and bookkeeping principles. Continue to Lesson 14 after these foundations are reliable.
