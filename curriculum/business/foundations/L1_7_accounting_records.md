---
title: "Basic Accounting Records"
status: numbers_checked_editorial_review_pending
provenance: ai_drafted_chatgpt_pending_author_review
generated_by: "OpenAI ChatGPT (saleskingacademy GitHub account), PR #13"
training_use: "excluded from SKA model training (OpenAI output terms); teach and cite only"
reviewed: "2026-11-25 Claude: every worked figure recomputed by tools/validate_arithmetic_business_lessons.py; one correction (see file history)"
---

# Basic Accounting Records

**Level:** 1. **Scope:** Additive instructional draft with hypothetical cases; not a certified completed lesson.

## Outcomes
Explain assets, liabilities and equity; construct simple journal entries; reconcile a transaction trail and identify an unsupported financial claim.

## Instruction
The accounting equation is **Assets = Liabilities + Equity**. A journal entry records the economic effect of an event. Under double-entry bookkeeping, total debits equal total credits. A debit does not always mean a decrease, and a credit does not always mean an increase: the direction depends on the account type.

Assets generally increase with debits; liabilities and equity generally increase with credits. Revenue increases equity through earnings, while expenses reduce it. The chart of accounts and accounting policy determine how specific events are classified.

**Worked entry 1 — owner investment:** An owner contributes $5,000 cash to a new company. Debit Cash $5,000; credit Owner Equity $5,000. This is financing, not customer revenue.

**Worked entry 2 — service on account:** The company completes $900 of service and invoices the customer. Debit Accounts Receivable $900; credit Service Revenue $900. When payment arrives, debit Cash $900 and credit Accounts Receivable $900. Do not record revenue twice.

**Worked entry 3 — expense:** The business pays $250 for an expense recognized immediately. Debit the appropriate Expense account $250; credit Cash $250. Whether a purchase should instead be capitalized depends on applicable accounting policy and materiality.

**Reconciliation:** Match recorded payment events to independent provider or bank evidence, account for timing differences and document adjustments. A webhook receipt is not independently verified settlement. Audit logs should distinguish attempted, authorized, settled, reversed and refunded events.

## Exercises and solutions
1. A business borrows $2,000 cash. **Answer:** Debit Cash $2,000; credit Loan Payable $2,000; borrowing is not revenue.
2. A customer pays a previously recorded $700 receivable. **Answer:** Debit Cash $700; credit Accounts Receivable $700.
3. Total assets $14,000, liabilities $5,500. **Answer:** Equity $8,500.
4. Why is a duplicate settlement event dangerous? **Answer:** It can overstate cash or revenue unless deduplicated and reconciled.

## Mastery
Prepare three balanced entries and reconcile a fictional invoice to its settlement record. Transfer: trace a refund from original purchase through reversal and customer communication.

## Editorial and continuity checks
Validate arithmetic and accounting assumptions, compare against existing canonical lessons, add alternate assessment and references where needed, and preserve EDU16 and other stable identities. No live payment, customer contact, or production deployment is authorized by this instructional draft.
