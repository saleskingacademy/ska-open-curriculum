# Web-search fallback for incomplete material

The learner must be offered source-backed material whenever the requested subject, lesson, outcome or prerequisite lacks validated SKA instruction. This obligation applies even when a chapter exists or an AI can produce plausible prose. A COMPLETE course does not imply that every new topic is covered.

## Required runtime behavior

1. Resolve the learner's subject and intended meaning from the taxonomy, course scope, level and prerequisites. Use that context in the query; sales ICP means ideal customer profile when the learner is in a sales course.
2. Check the requested outcome against the authoritative completion manifest and lesson records. Missing or unaudited outcome coverage triggers web search. Preserve useful local instruction and show the external material as a supplement.
3. Search for accessible, authoritative material at the learner's level. Prefer original research, official documentation, university/open educational resources and recognized technical organizations as appropriate. A result list or instant-answer snippet is not enough to validate an explanation.
4. Read the relevant source, record its URL, title, retrieval date and the passage or section supporting the claim. Verify calculations, assumptions and prerequisite fit independently. For business, engineering and other changing topics, check the current edition or date.
5. Explain the material in original SKA wording, cite the supporting sources and distinguish sourced facts from an AI's inference. Offer a worked example, a check the learner can perform and a route back to the course prerequisites. Respect source licenses; do not copy entire copyrighted lessons or test banks.
6. If search or verification fails, report that specific failure and keep the topic incomplete. Do not return a generic knowledge block under the requested title or present uncited AI generation as validated instruction.
7. External search, generated supplements and learner progress must not automatically promote a subject to COMPLETE or become assessed training material. Academic, taxonomy, prerequisite and assessment review precede Education-16 and Symbol256 mapping.

## Integration state and acceptance checks

This document defines the required behavior; it does not assert a deployed implementation. The operations repository's education lesson route currently uses database content, AI generation, generic knowledge blocks or a pending response. Its chat search helper is not proof of mandatory education fallback. The programme manifest marks fallback required and production integration unverified.

The integration must demonstrate all of these cases: missing lesson; present chapter with an uncovered outcome; ambiguous sales terminology; correct beginner prerequisite level; unsupported or broken source; provider timeout; contradictory sources; a calculation independently checked; a topic outside a COMPLETE course's scope; and unchanged completion status after providing a supplement. Each result must carry its source provenance and explicit validation status. A production test must show the education endpoint actually invokes search and provides verified material, rather than merely describing this policy.
