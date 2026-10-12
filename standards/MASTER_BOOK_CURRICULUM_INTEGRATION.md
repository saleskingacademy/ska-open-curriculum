# Master Book -> Curriculum Integration

Status: active expansion control
Branch: ska-education-expansion-2026-10-02
Purpose: prevent duplicate curriculum while progressively integrating the Sales King Academy master book into the public zero-to-frontier educational system.

## Rules
1. Audit existing curriculum, knowledge, study, assessment, and standards material before adding content.
2. Reuse or extend the canonical existing subject when the competency already belongs there.
3. Do not create a second subject or lesson merely because the master book uses a different chapter title.
4. Add content only when it closes a demonstrated prerequisite, explanation, practice, assessment, remediation, governance, computational, AI-augmented, or frontier gap.
5. Preserve dependency order: zero-entry literacy -> foundations -> application -> analysis -> synthesis -> professional/computational practice -> AI-augmented practice -> frontier/research literacy.
6. Existing useful material is preserved unless incorrect, duplicated, misplaced, unsafe, or below the declared instructional standard.
7. Established knowledge, current sourced facts, active research, SKA-defined frameworks, and speculation must remain epistemically distinct.
8. Education-16/Symbol256 derivatives follow academic and taxonomy validation; they do not determine curriculum truth.

## Book chapters mapped so far

### Chapter 1 — Learning, Thinking, and Operational Literacy
Existing coverage:
- critical_thinking.json already covers logic, evidence, uncertainty, mental models, systems thinking, and epistemic humility.
Gap found:
- no explicit zero-entry operational-literacy lesson connecting information -> capability -> system decomposition -> measurable objectives -> evidence status -> governed automation.
Action:
- added critical_thinking_L1_2, "Operational Literacy: From Information to Reliable Action".
State:
- populated; assessment included; parent subject remains subject to full repository validation and cumulative-completion gates.

### Chapter 2 — Business as Value Creation and Exchange
Existing coverage:
- knowledge/business/business_fundamentals.md covers business definitions, revenue/profit, costs, cash flow, break-even analysis, operations, applications, common errors, and advanced extensions.
- accounting.json and corporate_finance.json contain deeper financial dependencies.
- business_strategy.json contains value-chain, business-model, usage-based economics, technology, data, AI, automation, governance, and execution material.
Action:
- do not duplicate Chapter 2 as a new curriculum subject.
Next work:
- audit business_fundamentals.md for internal semantic repetition and prerequisite gaps; surgically improve only demonstrated deficiencies.

### Chapter 3 — Markets, Customers, Competition, and Business Models
Existing coverage:
- business_strategy.json contains customer segmentation, jobs to be done, competitive intelligence, competitive advantage, positioning, business-model innovation, recurring revenue, usage-based economics, network effects, switching costs, scale economies, distribution advantage, AI strategy, automation strategy, and AI governance.
- marketing.json contains segmentation/targeting/positioning and customer journey.
- knowledge/general_studies/market_intelligence.md covers market sizing, customer segmentation, competitor analysis, research methods, AI/ML extensions, and data-quality failure modes.
Action:
- do not create duplicate TAM/SAM/SOM, segmentation, JTBD, positioning, or usage-pricing lessons until the existing versions are assessed for depth and progression.
Next work:
- strengthen only missing assessment, prerequisite, sourcing, or advanced integration layers.

## Progressive-completion control
For every mapped subject report separately:
- prerequisite coverage;
- declared lesson/outcome coverage;
- worked-example/practice coverage;
- assessment and solution coverage;
- cumulative/final assessment coverage;
- remediation coverage;
- computational/tool-assisted coverage;
- AI-augmented coverage;
- frontier/research literacy;
- taxonomy/provenance validation.

Do not invent one completion percentage when the programme scope is undefined. A subject advances through SKELETON -> SEQUENCED -> INSTRUCTIONALLY POPULATED -> ASSESSED -> VALIDATED -> COMPLETE under the canonical standards.

## Next integration target
Continue the master book with Chapter 4 while auditing entrepreneurship and business fundamentals. Book writing and curriculum deployment remain dual outputs: manuscript prose is transformed into curriculum only where it adds a missing competency or materially improves progression.


## 2026-10-04 quality re-audit — mandatory correction

A quantitative and structural audit of the recent 80-lesson expansions found that lesson-count completion materially exceeds instructional-depth completion. The expanded subjects are therefore classified as SEQUENCED / PARTIALLY INSTRUCTIONALLY POPULATED, not COMPLETE and not yet academic-equivalent course packages.

Audited subjects: entrepreneurship, marketing, accounting, cybersecurity, corporate finance, sales, sales psychology, AI foundations, cloud computing, crypto/blockchain, data science, economics, operations management, statistics.

Observed range across these subjects:
- 80 lesson records per subject;
- roughly 20,551–30,997 instructional-content words per subject in the lesson JSON;
- roughly 257–387 words per lesson on average;
- typically three formative quiz items per lesson;
- repeated scaffolding language in many newly expanded lessons.

These records provide useful sequence, outcomes, vocabulary context, practice prompts, failure-mode prompts, AI/tool prompts, and formative questions, but they do NOT by themselves satisfy the canonical Zero-to-Frontier or Academic-Equivalent standards.

### Required upgrade before VALIDATED or COMPLETE
Each lesson must be converted from scaffold to subject-specific textbook-quality instruction with, where applicable:
1. explicit prerequisites and dependency IDs;
2. subject-specific vocabulary/notation;
3. first-principles explanation;
4. mechanisms, derivations, formulas, algorithms, or causal reasoning;
5. multiple fully worked examples rather than generic example prompts;
6. guided practice;
7. substantial independent problem set / cases / exercises;
8. verified explanatory solutions or scoring criteria;
9. misconceptions, edge cases, counterexamples and failure diagnosis;
10. real-world and cross-disciplinary applications;
11. computational/tool-assisted work;
12. AI-augmented work with independent verification;
13. summary/retrieval cues;
14. stronger formative assessment with plausible distractors and reasoning;
15. mastery threshold and explicit remediation;
16. next-unit dependency links.

Each course additionally requires module examinations, assessment blueprints, cumulative checkpoints, comprehensive final examination, alternate reassessment forms, capstone/project/lab/case as appropriate, rubrics, accessibility/alternative demonstration considerations, and provenance for changing factual material.

### Deployment policy correction
Future turns optimize verified instructional depth per deployment, not raw lesson count. Do not expand another 8-record subject to 80 thin records merely to increase catalogue counts. First deepen the highest-priority dependency courses into genuine course packages, beginning with foundational mathematics/statistics/critical thinking and the master-book path through business, sales, finance, computing and AI.

### Recognition boundary
The target is instructional rigor capable of external academic review. Repository language must say academic-equivalent only after the internal evidence gates pass, and must never claim accreditation or institutional recognition before an authorized external body grants it.
