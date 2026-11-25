---
title: "Value Exchange and Operating Records"
status: numbers_checked_editorial_review_pending
provenance: ai_drafted_chatgpt_pending_author_review
generated_by: "OpenAI ChatGPT (saleskingacademy GitHub account), PR #13"
training_use: "excluded from SKA model training (OpenAI output terms); teach and cite only"
reviewed: "2026-11-25 Claude: every worked figure recomputed by tools/validate_arithmetic_business_lessons.py; one correction (see file history)"
---

# Value Exchange and Operating Records

**Curriculum expansion:** Additive instructional draft; not a replacement for canonical lesson identifiers. **Level:** 1. **Evidence status:** worked cases are hypothetical and no live operational outcomes are claimed.

## Learning objectives
Explain value exchange; distinguish a customer, user and payer; record a transaction without confusing revenue with cash; identify operational evidence and ethical constraints.

## Conceptual foundation
A business coordinates resources to deliver something that a customer values enough to exchange money, time or another consideration for. Value is not identical to price: a buyer's perceived benefit depends on the problem solved, alternatives, risk and effort. A firm can create value while failing to capture enough revenue to remain solvent. Conversely, a transaction may be profitable in the short term yet undermine trust or legal compliance.

An **offer** specifies what will be delivered, to whom, under what conditions, for what consideration. A **customer** buys or contracts; a **user** consumes; a **payer** funds. They may be different people. For example, an employer pays for training used by an employee. Sales claims should be directed to the actual decision makers and verified against delivery capabilities.

A **transaction** is an economic event. **Revenue** is recognized under the applicable accounting basis when earned, which need not coincide with cash collection. **Cash flow** tracks money entering and leaving the organization. **Profit** is revenue minus recognized expenses over a defined period. **Accounts receivable** represents amounts owed by customers when a sale is made on credit.

## Worked case 1 — prepaid service
A company receives $600 for six months of service in advance. Under an accrual model, assuming equal monthly service and no unusual contract terms, cash increases by $600 on receipt; initially a $600 contract liability (deferred revenue) is recorded. After one month of service, $100 is recognized as revenue and the liability falls to $500. Under a cash-basis bookkeeping system the treatment may differ; tax and reporting rules must be checked separately.

**Reasoning:** Cash receipt does not establish that all six months of service have been delivered. If the firm spends the entire $600 immediately, it still owes future service. A dashboard showing “$600 collected” must not label that amount “$600 earned” without a supported accounting basis.

## Worked case 2 — unit economics
Suppose a workshop sells 30 seats at $80 each. Total sales = 30 × 80 = $2,400. The venue costs $500, teaching materials cost $12 per attendee and a facilitator costs $700. Total specified costs = 500 + 30 × 12 + 700 = $1,560. Contribution after these specified costs = $840. This is **not necessarily net profit**: taxes, payment processing, marketing, insurance and other overhead are excluded. At 20 attendees, sales are $1,600 and specified costs are $1,440, leaving $160 before omitted costs.

Break-even seats for these specified costs satisfy 80n = 1,200 + 12n, so 68n = 1,200 and n ≥ 18 (rounding up from 17.65). The model assumes every seat has the same price and material cost and capacity is sufficient.

## Operating records and evidence
Maintain a record of the offer version, date, counterparty, permission or contract, amount, delivery milestone, refund obligation, and evidence of completion. Separate personally identifying records from publicly shareable teaching examples. An automated ledger must be reconciled against the payment provider rather than assuming every webhook is a settled payment. Duplicate notifications should not create duplicate revenue.

## Practice and assessment
1. A parent pays for a course attended by a student. Identify payer, user and possible customer.
2. A business invoices $900 today for work completed today, with payment due next month. Explain the difference between revenue and cash.
3. Recalculate the workshop's specified-cost contribution at 25 seats.
4. Name two records needed to support a refund decision.
5. Describe one situation where maximizing sales today could harm long-term customer value.

### Solutions
1. Parent is payer; student is user; customer depends on who enters the contract.
2. Under accrual accounting, $900 of revenue and receivable may be recorded today; cash arrives later.
3. Sales $2,000; costs $500 + $300 + $700 = $1,500; contribution $500 before omitted expenses.
4. Agreed refund terms and documented delivery/payment status, for example.
5. Selling capacity that cannot be delivered may cause refunds and reputational damage.

## Mastery and transfer
A learner must correctly distinguish cash from earned revenue and solve the 25-seat scenario with assumptions stated. Transfer task: build a three-column record for a hypothetical subscription showing cash collected, service earned and outstanding service obligations for three months. Reassess after seven days with different numbers. This draft is not a verified certification.

## SKA lab
Using synthetic data only, design a prepaid educational-service ledger with separate purchased credits, consumed credits, refunds and earned revenue. Do not claim that a credit issuance equals recognized revenue. No production transactions or paid calls are authorized by this lesson.
