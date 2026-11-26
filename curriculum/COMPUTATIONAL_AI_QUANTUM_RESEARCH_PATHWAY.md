# Computational, AI-augmented and quantum research pathway

Status: SEQUENCED extension plan, not an instructionally complete course.
Version: 2026-10-10 UTC.
Governing documents: [zero-to-frontier standard](../standards/ZERO_TO_FRONTIER_CURRICULUM_STANDARD.md), [assessment standard](../standards/ACADEMIC_EQUIVALENCE_AND_ASSESSMENT_STANDARD.md), [mathematics spine](mathematics/MATHEMATICS_COMPLETION_MASTER_PLAN.md), and [cross-domain programme](CROSS_DOMAIN_COMPLETION_PLAN.md).

## Purpose and claim boundary

Develop learners who can understand computational representations, reason mathematically, implement and evaluate algorithms, use AI tools critically, and undertake progressively independent research. The target is demonstrable capability, not a claim that a human becomes a computer or matches the total knowledge or speed of an AI system. There is no single defined credential called “AI-equivalent education.” Measure specific tasks, accuracy, independence, transfer and resource use instead.

The pathway preserves the existing mathematical build order. Intermediate entrants may use placement assessments to demonstrate prerequisites; they do not need to repeat mastered instruction. Until those placement assessments are authored and reviewed, self-reported familiarity is not a validated prerequisite waiver. Postdoctoral research describes specialized work beyond doctoral training, not a universal final textbook level or a promise of mastering every discipline.

## Dependency and evidence map

| Stage | Entry competencies | Instruction to populate | Required evidence before stage completion |
|---|---|---|---|
| Foundation | Numeracy entry check | Arithmetic, fractions, ratios, units, algebra, reading and explanation | Independent calculations, quantitative modeling, cumulative tests and remediation |
| Intermediate computational literacy | Arithmetic and elementary algebra | Binary and hexadecimal representation, Boolean logic, data structures, algorithms, programming and debugging | Base conversions, circuit truth tables, traced programs, boundary cases and tests |
| Undergraduate mathematical computing | Algebra, functions and programming | Calculus, linear algebra, discrete mathematics, probability, statistics, numerical methods and optimization | Derivations, proofs, implemented models, error analysis and reproducible projects |
| AI foundations and augmentation | Linear algebra, probability, optimization and programming | Learning objectives, training versus inference, evaluation, retrieval, uncertainty, tool use, provenance and verification | Held-out evaluation, leakage audit, ablations, independent checks and failure analysis |
| Quantum information foundations | Complex numbers, vectors, matrices, inner products and probability | State vectors, gates, measurement, composite systems, entanglement and circuit reasoning | Hand calculations, small simulator exercises, prediction of distributions and interpretation of results |
| Advanced graduate specializations | Validated foundations in the selected branch | Advanced algorithms, formal methods, statistical learning theory, quantum information and error correction as appropriate | Theorem critique, advanced implementation, literature review and replication with limitations |
| Doctoral research preparation | Graduate methods and research literacy | Question formulation, originality searches, experimental design, proof development, research writing and peer critique | Defensible research proposal, reproducible replication, original contribution attempt and external review |
| Postdoctoral-style research practice | Demonstrated doctoral-level expertise in the specialty | Independent research agenda, collaboration, mentoring, artifact maintenance and cross-field synthesis | Independently scrutinized research portfolio, sustained reproducibility and explicit unresolved questions |

These rows are planned outcomes. They do not certify that their lessons, examinations, labs or projects already exist. Use the [Arithmetic reading order](mathematics/arithmetic/README.md) for verified file-level progress in the current foundation build. Existing legacy quantum and AI topics require a separate lesson-level audit before they count toward this pathway.

## Binary and quantum distinction

Binary representation uses digits zero and one to encode information. Quantum study adds a different mathematical state model; it is not merely binary arithmetic performed faster. A single pure qubit can be represented by a normalized complex two-component vector. Standard-basis measurement yields a classical outcome with probabilities determined by squared amplitude magnitudes. Learners must distinguish a state description from the outcomes obtainable in a measurement. Composite systems require additional mathematical structure, including tensor products. These topics follow linear algebra and probability rather than replacing them.

Introductory quantum work can use a classical simulator. Label every run as simulation or hardware execution, record the circuit and measurement basis, and distinguish predicted probabilities from finite observed counts. Neither a circuit drawing nor a simulated output is evidence of a hardware advantage. Performance comparisons require a specified task, classical baseline, resources, accuracy criterion and measured results. Claims of universal quantum speedup or automatic solutions to every hard problem must not enter learner material as established facts.

## Human-AI learning and assessment design

Every augmented task should include three artifacts: an independent learner attempt, a record of tool assistance, and a final justified result with corrections. Assess independent competence and assisted performance separately. The learner must identify assumptions, verify citations, check calculations, recognize uncertainty and explain why a proposed answer follows. A fluent generated explanation is a candidate answer, not grading evidence by itself.

Computational capstones should integrate a business, engineering or scientific decision with a defensible model. A proposed business case could compare manual and automated allocation methods on a synthetic dataset. Require an explicit objective, constraints, input provenance, test cases, costs, error analysis and failure behavior. A quantum extension is optional and must be justified by the task rather than added as a label. Synthetic outcomes remain simulations and must not be reported as actual company revenue or production performance.

Research assessments require reviewers competent in the specialty. Use originality as a question to investigate, not a status inferred from unfamiliar terminology. Separate reproduced results, incremental findings, conjectures and unsupported claims. Failed replications can be valuable when their methods, scope and limitations are documented. Merely completing a reading list does not establish research competence.

## Completion and continuation gates

For each stage, author the missing instruction in prerequisite order and attach an outcome-to-assessment blueprint. Provide worked examples, guided and independent practice, explanatory keys, alternate assessments, cumulative examination and a scored capstone. Audit technical claims and date-sensitive tool instructions against primary sources. Require external academic review before claiming independently verified equivalence. No word count or generated lesson count substitutes for these gates.

Immediate continuation: Arithmetic Lessons 21–30 (multiplication and division), following the populated Lessons 17–20 and the authored two-form Level 2 cumulative assessment. Completion of those learner assessments must be demonstrated, not inferred from file presence. Binary computation remains explicitly scheduled in Arithmetic Lessons 61–62. Quantum foundations follow validated linear algebra, complex-number and probability packages. Research specialization remains open until its instructional and review requirements are actually met.

## Primary references and provenance

This is original SKA planning and assessment design. The references below support topic selection and prerequisite alignment, not endorsement or accreditation. Reviewed 2026-10-10 UTC.

- [MIT OpenCourseWare, Quantum Computation syllabus](https://ocw.mit.edu/courses/18-435j-quantum-computation-fall-2003/pages/syllabus/): mathematical models and linear-algebra preparation.
- [IBM Quantum Learning, Single systems](https://learning.quantum.ibm.com/course/basics-of-quantum-information/single-systems): state representation, operations and measurement.
- [IBM Quantum Learning, Multiple systems](https://learning.quantum.ibm.com/course/basics-of-quantum-information/multiple-systems): composite quantum systems.
- [MIT OpenCourseWare, Quantum Information Science syllabus](https://ocw.mit.edu/courses/mas-865j-quantum-information-science-spring-2006/pages/syllabus/): advanced graduate scope and prior quantum-mechanics knowledge.

References provide stable conceptual scope; they are not a claim about the latest hardware benchmarks. Refresh technology-specific references when implementing the advanced modules.
