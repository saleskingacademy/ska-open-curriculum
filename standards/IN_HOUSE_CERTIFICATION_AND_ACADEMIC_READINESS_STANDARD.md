# SKA In-House Certification and Academic Readiness Standard

Status: proposed internal operating standard; not accreditation or government authorization.
Scope: all SKA disciplines, subjects, courses, and certification tracks.
Dependencies: ZERO_TO_FRONTIER_CURRICULUM_STANDARD.md and ACADEMIC_EQUIVALENCE_AND_ASSESSMENT_STANDARD.md. Their stricter completion gates remain authoritative.

## Claims and regulatory launch gate
SKA certificates are private institutional credentials, not accredited degrees, licenses, guaranteed transferable college credit, or Title IV-eligible awards. Do not advertise accreditation, FAFSA, Pell, or federal student-loan eligibility without documented approvals. Before offering paid career training, obtain documented Arkansas regulatory classification, required license or exemption, and applicable consumer disclosures. Academic development can proceed while authorization is evaluated.

## Canonical course manifest
Each course must have: immutable course_id; canonical discipline and subject; title; content version and review date; competency band; prerequisite IDs; measurable course and module outcomes; syllabus and instructional sequence; instructional modality and workload estimate with method; learning materials; assessment blueprint; question bank and controlled answer keys; practical/capstone rubric; remediation/reassessment policy; accessibility provisions; source/provenance references; reviewer identity/qualification and approval; taxonomy and Education-16/Symbol256 mapping status; and release status.

## Completion and certification gates
Gate A - Inventory: all course assets and links enumerated, no unresolved stale references.
Gate B - Academic: outcomes, prerequisite closure, level-appropriate instruction, independent practice, accurate references.
Gate C - Assessment: mapped lesson quizzes, module tests, cumulative final, capstone/equivalent, validated solutions, alternate assessment forms and scoring rubrics.
Gate D - Quality: subject-matter review, accessibility check, integrity and factual review, resolved critical defects.
Gate E - Delivery: student enrollment and progress records, identity verification proportionate to credential stakes, controlled grading, appeals, accommodations, certificate verification and revocation workflow, privacy/security checks.
Gate F - Regulatory: required state authorization/exemption and consumer disclosures documented before paid public launch.

A course may be internally CERTIFICATION_READY only if A-E pass with documented evidence. PUBLIC_ENROLLMENT_READY also requires F. A missing gate is not a passing gate. The existing academic COMPLETE definition remains independently mandatory.

## Academic alignment and evidence
Map each course to at least two relevant external curricular references when available, including documented learning outcomes and discipline-appropriate competencies. Store a comparison matrix with: reference, date, topic, expected level, SKA lesson IDs, assessment IDs, identified gaps, reviewer and disposition. A mapping is evidence of curriculum design, not external endorsement or transfer equivalency. Proposed credit-hour equivalents must be labeled planning estimates until appropriate authorization and policy are established.

## Credential evidence and transcript
Record learner ID; enrollment and course versions; assessment blueprint/version; attempt date; outcome-level scores; accommodations (restricted access); capstone evidence; evaluator; pass decision; appeal/reassessment history; issuance date; unique certificate ID; expiration if applicable; revocation status; verification endpoint. Do not expose private scores or personal information on public verification pages.

## Reporting
For each course publish internal audit fields: inventory status; taxonomy status; prerequisite coverage; outcome coverage; lesson coverage; assessment coverage; solution validation; capstone status; accessibility; reviewer approval; delivery readiness; regulatory readiness; blockers; evidence links; last verified timestamp. Completion percentages must be calculated from enumerated verified requirements, never guessed from file counts or word counts.

## Deployment discipline
Audit before edits; preserve existing material and architecture; avoid modifying Chain64 or production agent routing. Develop on the existing education expansion branch. Validate generated indexes, lesson-serving paths, Symbol256 artifacts and study packs after any curriculum changes. Do not mark an untested production behavior as verified.

## Initial implementation sequence
1. Inventory public curriculum and private serving dependencies.
2. Generate per-course gap matrix from real repository evidence.
3. Resolve taxonomy, path, assessment and prerequisite defects.
4. Complete one pilot certification end-to-end.
5. Review Arkansas authorization/exemption and public disclosures before enrollment.
6. Expand to remaining subjects using the same gates.
