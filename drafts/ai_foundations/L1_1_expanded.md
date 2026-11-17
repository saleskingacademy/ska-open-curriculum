---
title: "AI Foundations — Level 1, Lesson 1: What AI Is and How to Evaluate It"
subject_id: ai_foundations
level: 1
lesson_number: 1
expansion_of: ai_foundations_L1_1
status: DRAFT
publication_ready: false
generated_by: OpenAI GPT-6 assisted draft
training_use: review provider terms before model training
review_required: [subject_matter, assessment, originality, accessibility, source_verification]
---

# What AI Is and How to Evaluate It

## Learning outcomes
After this lesson, a learner can (1) define AI without claiming that software thinks like a human; (2) distinguish rules, learned models and generative systems; (3) identify inputs, outputs, errors and human oversight in a business example; (4) calculate basic classification accuracy; and (5) describe one privacy or fairness risk and an appropriate safeguard.

**Prerequisites:** reading comprehension, percentages, and basic familiarity with software. **Estimated learning time:** 60–90 minutes, including practice.

## 1. What does artificial intelligence mean?
Artificial intelligence (AI) refers to computational methods that perform tasks commonly associated with intelligence, such as recognizing patterns, interpreting language, making predictions, planning actions, or generating content. There is no single test that establishes that a system possesses human understanding. An AI system can perform a narrow task impressively while failing at an apparently simple variation of that task.

An email spam classifier is one example. It receives a message and returns a label or probability. A speech-to-text system receives an audio signal and returns words. A generative language model receives a sequence of tokens and produces a continuation. These systems do not all use the same algorithms and should not be evaluated by the same measures.

**Vocabulary:** An *input* is the information supplied to a system. An *output* is its result. A *model* is a mathematical or computational representation used to produce results. *Training* adjusts a model using data and an objective. *Inference* is using an already trained model to produce an output. *Generalization* means performing acceptably on examples not used for training.

## 2. Three approaches to a task
**Explicit rules.** A programmer might write: “If a lead has opted out, do not contact them.” The result is predictable given the same inputs and code. Rules are particularly valuable for permission checks, billing limits and legal constraints.

**Machine learning.** A model may learn from labeled historical messages to estimate whether a new message is spam. Its prediction is statistical; even a high confidence score can be wrong. The model should be tested on data held out from training.

**Generative AI.** A language model can draft a follow-up email from a permitted customer brief. It generates candidate wording, not verified facts. An operator must still check recipient consent, factual claims, tone and applicable requirements. The generative model must not override a deterministic opt-out rule.

These approaches can coexist. A responsible application can use a learned model for a recommendation, a language model for a draft and fixed rules for authorization.

## 3. Worked example: classify customer inquiries
Suppose a small company receives 100 inquiries. A human reviewer determines that 40 are genuine sales inquiries and 60 are not. A model flags 35 of the 40 genuine inquiries correctly but incorrectly flags 10 of the 60 others as genuine.

| | Actually genuine | Actually not genuine |
|---|---:|---:|
| Model says genuine | 35 | 10 |
| Model says not genuine | 5 | 50 |

**Accuracy** = (35 + 50) / 100 = **85%**. **Precision** for the “genuine” label = 35 / (35 + 10) = **77.8%**. **Recall** = 35 / (35 + 5) = **87.5%**.

Accuracy alone hides the cost of the ten false positives and five missed opportunities. If outreach to a wrongly flagged contact would violate consent requirements, even a statistically good classifier must be placed behind a separate permission check. If the business cares most about missed qualified leads, recall may matter more than overall accuracy. The choice depends on real consequences.

**Interpretation check:** A score of 0.95 is not a guarantee that a statement is 95% true. Confidence scores require calibration testing before they can be interpreted as probabilities.

## 4. Data, evaluation and failure
A model learns patterns in examples. Poorly labeled or unrepresentative examples can produce poor predictions. A model trained only on inquiries from one region or industry may perform worse on a different population. This is a *distribution shift*. A model may also memorize quirks in training examples rather than generalize; this is *overfitting*.

A basic evaluation separates data into training and testing sets. Do not test on the exact examples used to tune the model and then report that score as independent performance. Record the sample size, label definitions, evaluation date, and important subgroups. For small datasets, percentages can fluctuate substantially: 85 correct out of 100 is weaker evidence than 8,500 correct out of 10,000 under comparable sampling.

AI systems can make confident factual mistakes. A generated paragraph may sound authoritative without having a reliable source. Retrieval of supporting documents can improve grounding, but retrieved text can itself be outdated or incorrect. Claims with financial, legal, medical or safety consequences require appropriate review.

## 5. Worked business design: safe lead-assistance workflow
A business wants to reduce time spent triaging inbound requests. Define the workflow before selecting a model:

1. **Input:** a customer-submitted inquiry, with a record of how it was collected and any relevant communication permissions.
2. **Permission gate:** reject disallowed processing or outreach using explicit rules; a model cannot waive this gate.
3. **Prediction:** classify inquiry type and estimate whether a human sales representative should review it.
4. **Draft:** optionally generate a suggested reply from approved product information.
5. **Review:** a person verifies facts, permissions and appropriateness before external delivery.
6. **Record:** log the model version, review decision, errors and outcome without retaining unnecessary personal data.
7. **Monitor:** compare performance across time and relevant groups; investigate changes before increasing automation.

This design distinguishes assistance from autonomous action. An AI suggestion is not the same as an authorized email send, a contract acceptance, or a completed sale.

## 6. Ethics, privacy and security
**Privacy:** Do not send sensitive customer records to an external model unless there is a lawful basis, a clear business purpose, and appropriate contractual and technical safeguards. Prefer data minimization and access controls.

**Fairness:** A classifier can reproduce historical exclusion patterns. Compare error rates where lawful and appropriate, investigate disparate outcomes and offer a route for human correction.

**Security:** Text supplied by customers can contain instructions intended to manipulate an AI agent. Treat customer messages and retrieved documents as untrusted content, not as authority to call tools or expose data.

**Accountability:** Assign a human owner to the workflow, define escalation thresholds and provide a way to stop the automation when errors are detected.

## 7. Guided practice
**Exercise A — classify the system.** For each case, identify whether the core mechanism is an explicit rule, a learned model or a generative model: (a) a program blocks sends to opted-out contacts; (b) a model predicts likely customer churn; (c) a model drafts a product description.

**Exercise B — compute a metric.** A classifier correctly flags 18 of 20 urgent requests and incorrectly flags 6 of 80 nonurgent requests. Calculate precision, recall and accuracy.

**Exercise C — design a safeguard.** A generative assistant drafts answers using a company knowledge base. Describe two ways it might still give an incorrect answer and one verification step.

**Exercise D — transfer.** Replace the lead-triage example with an education tutoring application. Identify the learner input, the model output, a potential error, a deterministic permission rule and a human escalation path.

## 8. Assessment (formative; not certification-ready)
1. Define inference in one sentence.
2. Why can a fixed opt-out rule be preferable to a model prediction?
3. What is the difference between a false positive and a false negative?
4. Why should a model be evaluated on held-out data?
5. Can a generated answer be trusted because it is fluent? Explain.
6. Give one example of distribution shift.
7. What is the purpose of a human review gate?
8. Name one privacy safeguard and one security safeguard.

### Answer key and worked solutions
**Exercise A:** (a) explicit rule, (b) learned model, (c) generative model.

**Exercise B:** TP=18, FN=2, FP=6, TN=74. Precision = 18/24 = **75%**. Recall = 18/20 = **90%**. Accuracy = (18+74)/100 = **92%**.

**Exercise C:** The retrieved source may be outdated; the model may invent details not present in the source. Verification: require a reviewer to compare every consequential claim with a current authoritative record.

**Exercise D, sample:** Learner submits an algebra question; model proposes a worked solution; possible error is a sign mistake; deterministic rule prohibits disclosure of another learner's records; instructor reviews repeated or high-stakes errors.

**Assessment:** (1) producing an output with an existing model; (2) consent must be enforced reliably, not predicted; (3) false positive flags a negative case, false negative misses a positive case; (4) to estimate generalization; (5) no, fluency is not verification; (6) deployment on a new industry unlike training data; (7) catch errors and preserve accountable decisions; (8) minimize personal data and reject untrusted tool instructions.

## 9. Mastery gate and progression
**Proposed gate, not yet implemented:** At least 7/8 assessment answers correct, correct explanation of both precision and recall, and an acceptable safeguard in Exercise D. Remediate weaknesses before proceeding to the next lesson on machine-learning paradigms. Recheck with a fresh scenario after seven days to assess retention.

## 10. SKA lab (conditional, not verified as executed)
In a permitted training environment, configure an agent to classify **synthetic** customer inquiries. Test at least ten cases, including opt-out language and prompt-injection attempts. Verify that the permission rule takes precedence over any model-generated recommendation. Record observations, not assumed outcomes. Do not send external messages or consume paid Beats without authorized test conditions.

## 11. Scope and editorial evidence
This lesson introduces concepts rather than asserting academic equivalence, external accreditation or certification readiness. Before publication, check examples against current primary documentation, validate assessment wording with a subject-matter reviewer, run the repository originality checker, and confirm that the lesson can be ingested without altering stable EDU16 identities. No external sources were fetched or independently verified during drafting.

**Next lesson:** Core paradigms of machine learning — supervised, unsupervised and reinforcement learning, with labeled data and evaluation exercises.
