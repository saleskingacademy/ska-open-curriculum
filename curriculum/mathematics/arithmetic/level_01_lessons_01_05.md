# Level 1 Expanded Lessons — Arithmetic

These lessons implement the zero-to-advanced SKA arithmetic curriculum. They are written as original instructional exposition around standard mathematical knowledge. Each unit is designed for both human study and structured agent retrieval.

## Lesson 1: Counting and Quantity

Arithmetic begins before written numerals. A learner first needs the idea that a collection has a quantity independent of the objects being counted. Five stones, five sounds, and five marks share the same cardinality even though their physical properties differ. Counting establishes a one-to-one correspondence between objects and an ordered sequence of number words or symbols.

Three ideas must be separated. Cardinal number answers “how many?” Ordinal number answers “which position?” A numeral is a written representation of a number rather than the number itself. The symbol 7, the word seven, seven dots, and the Roman numeral VII can represent the same quantity.

A reliable counting procedure uses one-to-one correspondence, stable order, and the cardinality principle: after each object has been counted once, the final count word gives the size of the collection. Double-counting and skipping objects are process errors rather than arithmetic mysteries.

Worked example 1: A row contains ● ● ● ●. Touch each object once while saying 1, 2, 3, 4. The collection has cardinality four.

Worked example 2: A box has 3 red blocks and 2 blue blocks. Counting all objects gives 1,2,3,4,5. Color does not change the total quantity, so the cardinality is 5.

Worked example 3: If Maya finishes third in a race, “third” is ordinal. If three runners have finished, “three” is cardinal.

Application: Inventory, voting, manufacturing counts, database record counts, and computer loop counters all depend on discrete quantity. In software, an off-by-one error is a sophisticated descendant of an elementary counting error.

Common misconception: The physical size of objects does not determine the size of a set. Three trucks are fewer objects than ten coins even if the trucks occupy more space.

Practice: Count 8 objects arranged randomly. Draw two different collections with cardinality 6. Explain the difference between 4 and fourth. If a program processes items indexed 0 through 9, determine how many items it processes and explain why.

Mastery check: (1) What property is shared by seven books and seven sounds? (2) Is “fifth” cardinal or ordinal? (3) Why must each object be matched to exactly one count word? (4) Represent 9 in three different ways. (5) Diagnose the error when a learner counts one object twice.

Answers: (1) cardinality 7; (2) ordinal; (3) to preserve one-to-one correspondence; (4) examples include 9, nine, nine tally marks; (5) the procedure violates one-to-one correspondence and overcounts.

---

## Lesson 2: Numerals and Symbols

Numbers are abstract mathematical objects; numerals are symbol systems used to write them. This distinction becomes important when learners encounter different bases, historical numeral systems, computer representations, or symbolic mathematics.

The decimal digits are 0 through 9. A multi-digit numeral combines digit identity with position. The same digit can contribute different values: in 505, the first 5 represents five hundreds while the last represents five ones. Zero can represent a quantity and can also serve as a positional placeholder.

Mathematical symbols compress relationships. + denotes addition, − subtraction, × multiplication, ÷ division, = equality, < less than, and > greater than. Equality means that two expressions have the same value; it does not mean “the answer comes next.”

Worked example: 4 + 3 = 7 states that the expression on the left and the numeral on the right represent equal values. Therefore 7 = 4 + 3 is equally valid.

A symbol acquires meaning through a convention and a mathematical system. This prepares the learner for algebra, where letters can represent numbers, and computing, where bit patterns represent values according to an encoding.

Practice includes translating between words and numerals, interpreting operation symbols, writing equivalent equality statements, and distinguishing a number from one representation of it.

Error analysis: Treating '=' as a command can make a learner reject 8 = 5 + 3 or incorrectly fill 3 + 4 = __ + 2 with 7. The correct missing value is 5 because both sides must have equal value.

Mastery check: Explain number versus numeral; list decimal digits; explain the two roles of zero; solve 6 + 5 = __ + 4; rewrite 12 = 9 + 3 with the sides reversed.

Answers: a number is the abstract value and a numeral represents it; digits 0–9; zero can denote no quantity and hold place; missing value 7; 9 + 3 = 12.

---

## Lesson 3: Place Value

Decimal notation is a positional base-ten system. Each position has ten times the value of the position immediately to its right. From right to left the whole-number positions are ones, tens, hundreds, thousands, ten-thousands, hundred-thousands, millions, and so on. To the right of the decimal point are tenths, hundredths, thousandths, and progressively smaller powers of ten.

The numeral 47,305.62 can be expanded as 4×10,000 + 7×1,000 + 3×100 + 0×10 + 5×1 + 6×0.1 + 2×0.01. This is also a first encounter with powers of ten.

Place value explains arithmetic algorithms. Carrying in addition exchanges ten units of one place for one unit of the next place. Regrouping in subtraction performs the reverse exchange. Decimal alignment matters because digits must be combined with digits representing the same unit.

Worked example: In 6,482 the digit 6 contributes 6,000. In 0.06482 the same digit contributes six hundredths. Digit identity stayed fixed; positional weight changed.

Worked example: 3.4 and 3.40 are equal because the added zero contributes zero hundredths. By contrast 3.04 is smaller because the 4 is in the hundredths position.

Computational connection: Binary is also positional, but each place is a power of two. Understanding decimal place value therefore becomes a prerequisite for understanding digital representation.

Practice: expand 508,031; write “seventy-two thousand forty-six” as a numeral; identify the value of 8 in 18.205; compare 4.09 and 4.9; explain why multiplying a decimal by 10 shifts positional weights.

Mastery answers: 500,000+8,000+30+1; 72,046; 8; 4.09<4.9; multiplication by ten makes each positional contribution ten times as large.

---

## Lesson 4: Comparing and Ordering

Comparison determines whether one numerical value is less than, equal to, or greater than another. The symbols <, =, and > encode these relations. On a conventional horizontal number line, values increase to the right.

For positive whole numbers with different digit counts, the number with more digits is larger. With equal digit counts, compare corresponding places from greatest to least until the first difference appears. Decimal comparison follows the same principle after aligning decimal points and, when useful, appending trailing zeros.

Negative numbers reverse an intuition based on digit magnitude. −8 is less than −3 because −8 lies farther left on the number line. Absolute value measures distance from zero, so |−8|=8, but absolute value does not preserve sign.

Worked example: Compare 0.507 and 0.57. Write 0.507 and 0.570. Tenths are equal (5); hundredths differ (0<7), so 0.507<0.57.

Worked example: Order −2, 4, −7, 0, 3. Number-line order is −7, −2, 0, 3, 4.

Applications include sorting prices, ranking measurements, evaluating thresholds, and computer comparison operations. A comparison algorithm should distinguish numerical ordering from lexicographic text ordering: as text, “100” may sort before “20,” while numerically 100>20.

Practice and mastery: compare 45,901 with 45,910; compare 2.30 with 2.3; order −1.5, −1.05, 0, 1.05; explain why −100<−2; identify a software context in which string and numeric sorting differ.

Answers: 45,901<45,910; equal; −1.5,−1.05,0,1.05; −100 is farther left; examples include filenames, database fields, or user-input strings.

---

## Lesson 5: Number Lines and Zero

A number line turns arithmetic into spatial relationships. Zero is the origin. Positive values extend in one direction and negative values in the other. Distance between values is represented by absolute difference.

Zero has several roles: it is the additive identity because a+0=a; it separates positive and negative numbers; it can represent absence of quantity; and it is essential as a positional digit. Zero is neither positive nor negative.

Addition can be modeled as movement. Starting at 3 and adding 4 moves four units right to 7. Adding −4 moves four units left. Subtraction a−b can be interpreted as the signed difference or as adding the opposite: a−b=a+(−b).

Worked example: −3+5 starts at −3 and moves five units right, ending at 2. For 4−7, rewrite as 4+(−7), ending at −3.

Distance is nonnegative. The distance from −4 to 3 is |3−(−4)|=7. This distinction between signed displacement and distance later appears in geometry, physics, optimization, and error metrics.

Mastery: locate −5,0,4; compute −2+6; compute 3−8; find distance between −6 and 2; explain why division by zero is not defined in ordinary arithmetic.

Answers: locations follow order −5<0<4; 4; −5; 8; division by zero cannot produce a finite number whose product with zero recovers a nonzero dividend.

---

## Level 1 cumulative checkpoint
A learner should now be able to distinguish quantities from representations, count reliably, interpret decimal symbols, explain positional value, compare signed and unsigned values, and use a number line. Do not advance a learner who cannot explain *why* place value and equality work; procedural guessing will compound into later algebra errors.
