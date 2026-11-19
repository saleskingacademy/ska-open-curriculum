---
title: "Value Explanation and Demonstration"
lesson_key: L1_7_value_demonstration
status: DRAFT
publication_ready: false
review_required: [subject_matter, source_verification, originality, assessment, canonical_integration]
---
# Value Explanation and Demonstration

**Level:** 1. **Scope:** Additive instructional draft with hypothetical cases; not a certified completed lesson.

## Outcomes
Connect a verified feature to a customer outcome, design a representative demonstration and distinguish a working prototype from validated production performance.

## Instruction
A product demonstration should answer the buyer's decision question rather than showcase every feature. Begin with an agreed scenario, inputs, success criteria and limitations. Demonstrate the normal path and at least one failure or exception path. Do not use real customer data without appropriate authorization.

**Feature-to-outcome chain:** “Automated routing” is a feature; “fewer manual handoffs” is a possible benefit; “median first-response time falls from 90 to 50 minutes” is an outcome only if measured in a representative evaluation. A demonstration that processes one prepared example proves little about reliability under diverse inputs.

**Worked pilot design:** A fictional service desk handles 200 tickets weekly. The pilot's primary metric is median time to assign a ticket, with baseline and pilot measured on comparable weeks. Secondary metrics include incorrect assignments, human overrides and customer complaints. The test excludes messages containing sensitive records and requires escalation of urgent requests. A favorable result is not accepted if the error rate exceeds the agreed threshold.

**Calculation:** If 100 representative assignments take an average of 6 minutes manually and 4 minutes with reviewed automation, gross time saved is 200 minutes. If review and exception handling add 90 minutes, net time saved is 110 minutes. Average is not median; the report must not substitute one for the other.

## Exercises and solutions
1. Why is a polished demo not proof of production reliability? **Answer:** It may use curated inputs and omit failures, load and edge cases.
2. Calculate net savings for 80 cases, 3 minutes gross saving each and 100 minutes total review overhead. **Answer:** 80 × 3 − 100 = 140 minutes.
3. Name two guardrail metrics. **Answer:** Error rate and unauthorized action count.
4. Draft a limitation statement. **Answer:** “This prototype has not been tested against your production workload or approved for unattended actions.”

## Mastery
Design a demonstration with baseline, sample, success threshold, failure threshold, reviewer and stop condition. Transfer: demonstrate an AI tutoring assistant while measuring answer correctness, not only response speed.

## Editorial and continuity checks
Validate arithmetic and accounting assumptions, compare against existing canonical lessons, add alternate assessment and references where needed, and preserve EDU16 and other stable identities. No live payment, customer contact, or production deployment is authorized by this instructional draft.
