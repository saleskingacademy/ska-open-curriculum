---
title: "Permission and Opening Communication"
status: numbers_checked_editorial_review_pending
provenance: ai_drafted_chatgpt_pending_author_review
generated_by: "OpenAI ChatGPT (saleskingacademy GitHub account), PR #13"
training_use: "excluded from SKA model training (OpenAI output terms); teach and cite only"
reviewed: "2026-11-25 Claude: every worked figure recomputed by tools/validate_arithmetic_business_lessons.py; one correction (see file history)"
---

# Permission and Opening Communication

**Level:** 1. **Type:** Additive course expansion; hypothetical cases, not verified SKA operational results.

## Instruction, worked examples and assessment

An opening communication establishes identity, purpose, relevance and the recipient's ability to decline. Persuasion does not excuse misleading identity, false urgency or ignoring opt-outs. Requirements vary by jurisdiction, channel, recipient and message type; a training exercise is not legal clearance for a campaign.

**Permission architecture:** Before a message is sent, the system should check channel eligibility, suppression status, available consent or other lawful basis, organizational policies and any required human approval. These checks belong in deterministic authorization logic, not in an AI model's judgment. A generated draft must never be interpreted as permission to send.

**Opening framework:** Identify yourself accurately; refer to a specific, supportable business context; ask one short, relevant question; avoid exaggerated claims; provide an appropriate route to decline. For example: “I work with teams evaluating how they handle inbound inquiries. Is reducing manual routing an active priority for your team?” This is illustrative wording, not an assertion that unsolicited delivery is permitted.

**Worked case:** A company has 500 records from several sources. Only 320 have sufficient provenance to evaluate contact eligibility, 90 are on a suppression list and 40 have unresolved ownership or source restrictions. These groups may overlap. It is invalid to subtract 90 and 40 from 320 without knowing the intersections. A correct implementation evaluates each record independently and produces an eligibility decision with evidence. Unknown permission status should not be silently treated as authorized.

**Reply handling:** An opt-out must update suppression promptly and durably. A reply expressing interest should be routed to a human or authorized workflow with the original context. An out-of-office response should not be counted as a positive sales reply. Avoid repetitive automated follow-ups when the recipient has declined.

**Exercise 1:** Why is “the model says this person is likely interested” insufficient permission? **Solution:** Predicted interest does not establish a lawful or authorized contact basis.

**Exercise 2:** A person requests no further messages. What should happen? **Solution:** Stop relevant outreach, record the suppression and prevent scheduled retries from sending.

**Exercise 3:** Explain why subtracting overlapping categories can produce a false eligible count. **Solution:** A record present in multiple categories would be subtracted more than once.

**Mastery gate:** Design a message workflow that fails closed on missing permission, supports durable opt-outs and separates drafting from sending. **Transfer:** Apply the same gate to an AI agent proposing follow-up messages.

## Editorial gate
Before merging, compare against the canonical subject record, verify mathematical answers and references, check originality, add graded alternate assessments and map to existing EDU16 identities without renumbering. This document does not certify course completion.
