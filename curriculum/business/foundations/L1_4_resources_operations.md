---
title: "Resources and Operating Processes"
status: numbers_checked_editorial_review_pending
provenance: ai_drafted_chatgpt_pending_author_review
generated_by: "OpenAI ChatGPT (saleskingacademy GitHub account), PR #13"
training_use: "excluded from SKA model training (OpenAI output terms); teach and cite only"
reviewed: "2026-11-25 Claude: every worked figure recomputed by tools/validate_arithmetic_business_lessons.py; one correction (see file history)"
---

# Resources and Operating Processes

**Level:** 1. **Type:** Additive course expansion; hypothetical cases, not verified SKA operational results.

## Instruction, worked examples and assessment

A business process converts inputs into outputs under constraints. Inputs may include staff time, data, tools, equipment, supplier services and cash. Outputs include products, completed services, support resolutions and records. A process map should identify the trigger, owner, required inputs, decision rules, handoffs, failure handling and evidence of completion.

**Process example:** A hypothetical training provider receives a paid enrollment. The workflow verifies payment status, checks course eligibility, grants access, records the entitlement and sends a confirmation. A payment notification alone is not proof that funds settled, and repeated notifications must not grant duplicate entitlements. The access grant should be idempotent: processing the same authorized event twice has the same final effect as processing it once.

**Capacity example:** One reviewer can check 12 applications per hour. With 6 productive hours daily, theoretical capacity is 72 applications. If arrival volume averages 80 per day, the backlog grows by approximately 8 per day absent changes. Adding automation that processes 20 applications daily still requires quality assurance and exception handling; it does not necessarily remove the human review requirement. Distinguish nominal capacity from sustainable capacity under variability.

**Bottlenecks:** Throughput is constrained by the slowest required stage. If intake processes 100 cases daily, verification 65 and fulfillment 90, steady-state throughput cannot exceed 65 without changes or inventory accumulation. Improving intake alone may increase queues without increasing delivery.

**Controls:** Document who can approve a refund, what records are retained, how errors are reversed and how personally identifying information is protected. Automations should fail closed on authorization errors. Avoid unnecessary external calls, especially paid calls, when prerequisites have not passed.

**Exercise 1:** A three-stage process handles 40, 25 and 35 orders daily. What is its maximum sustainable throughput? **Answer:** 25 orders daily, assuming every order requires all three stages.

**Exercise 2:** A reviewer completes 9 cases per hour for 5 hours. Arrivals total 52. Estimate backlog growth. **Answer:** Capacity 45; backlog grows by 7 cases.

**Exercise 3:** Explain why a duplicate payment webhook must not grant a second purchased entitlement. **Answer:** It is a repeated notification about one underlying transaction, not a second verified purchase.

**Mastery gate:** Draw a process with one trigger, three steps, a bottleneck, an exception path and a durable completion record. **Transfer:** Map the same principles to a customer-support workflow.

## Editorial gate
Before merging, compare against the canonical subject record, verify mathematical answers and references, check originality, add graded alternate assessments and map to existing EDU16 identities without renumbering. This document does not certify course completion.
