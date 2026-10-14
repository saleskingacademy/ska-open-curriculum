# Priority Domain Completion Standard

Status: active quality gate for Sales King Academy priority disciplines.

This standard applies to the proprietary and core learning paths that directly support SKA's business operating system: artificial intelligence and modern technology, business, sales, marketing, finance/accounting, cryptocurrency, blockchain/Web3, and autonomous operations.

## Completion means demonstrated instructional coverage

A subject or pathway MUST NOT be marked complete because it reached a word count, lesson count, or generated-row count. Completion requires all of the following:

1. **Correct identity and placement.** The canonical subject key, title, program, prerequisite path, and level placement match the material actually taught. Cross-domain material is linked, not copied into the wrong subject.
2. **Prerequisite closure.** A learner can enter from the declared prerequisite state and progress without unexplained dependency jumps.
3. **Instructional depth.** Definitions, first principles, mechanisms, methods, implementation, failure modes, quantitative reasoning where applicable, applied workflows, and advanced/frontier material are all present at the depth appropriate to the discipline.
4. **Original teaching, not padding.** Repeated paragraphs, template boilerplate, same-example-with-different-numbers padding, circular restatement, and inflated word count are defects.
5. **Worked application.** The pathway contains distinct worked examples, cases/labs, realistic constraints, and practice that require transfer rather than recall alone.
6. **Assessment evidence.** Questions and performance tasks sample the declared competencies. Answer keys/rubrics explain why an answer is correct and identify common failure modes.
7. **Currency and epistemic labeling.** Fast-moving AI, crypto, security, regulation, and platform claims are dated or researched before publication. Established fact, current product behavior, research, and speculation are not blended.
8. **Deterministic address integrity.** Existing DNA-16, L4, Chain256, Symbol and Education-16 identities are preserved. Rewrites update derived artifacts through the repository's canonical builders; identifiers are never casually re-keyed.
9. **Agent-teaching compatibility.** Material has enough semantic structure for the owning agent to retrieve the correct subject, prerequisites, examples, and assessment context without relying on marketing counts.
10. **No false credential claims.** SKA in-house certificates and academic-equivalent instructional design are not represented as external accreditation, licensure, degrees, or guaranteed transfer credit.

## Priority pathways

The priority-domain manifest in `curriculum/PRIORITY_DOMAIN_MANIFEST.json` is the release inventory. Every item is explicitly `in_progress`, `review_ready`, or `complete`.

Only `complete` items are allowed to fail closed on all completion gates. `in_progress` items remain publishable only when they pass identity, provenance, deterministic-address, and subject-placement safety checks.

## Expansion order

1. Close factual and subject-placement defects.
2. Remove repetition and weak assessments.
3. Fill prerequisite and mechanism gaps.
4. Add worked examples, cases and labs.
5. Extend advanced/frontier material.
6. Rebuild study, symbol, Education-16 and index artifacts.
7. Run originality, curriculum-integrity, textbook/chapter, assessment and priority-domain checks.
8. Change status to `complete` only after evidence passes.

The goal is not the largest corpus. The goal is a corpus from which a motivated learner can actually acquire the declared capability, and from which SKA agents can teach and recover the right knowledge deterministically.
