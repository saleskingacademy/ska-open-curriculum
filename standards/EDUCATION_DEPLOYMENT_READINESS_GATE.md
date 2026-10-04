# Education Deployment Readiness Gate

Expansion is paused while this gate is RED. It becomes GREEN only when all blocking checks below pass on the same source revision.

## Blocking checks

1. **Source integrity** — curriculum integrity lint has no high-confidence factual/taxonomy regression.
2. **Taxonomy integrity** — every catalogue topic maps to exactly one canonical subject unless an explicit cross-domain alias is documented; no accidental duplicate ownership.
3. **Prerequisite integrity** — declared beginner units have no hidden prerequisite; dependency references resolve; no dependency cycle exists in machine-readable curriculum graphs.
4. **Assessment integrity** — newly declared COMPLETE/VALIDATED courses satisfy the Academic-Equivalent Instruction and Assessment Standard: meaningful lesson assessment, module/cumulative/final assessment, solutions/rubrics, remediation/reassessment, and appropriate capstone evidence.
5. **Address integrity** — EDU16 registry remains append-only; existing EDU16 values are not renumbered; regenerated source hashes and T16/Chain256 attachments match the corrected source revision.
6. **Symbol routing integrity** — Symbol256 build completes; collisions remain address-resolvable; Locator16 remains a physical locator rather than canonical identity; EDU16 crosswalk entries, where present, match content hashes.
7. **Security boundary** — public repository contains publishable education/build metadata only. No production secrets, private user/session state, privileged agent logic, private databases, or private runtime configuration are introduced.
8. **Build integrity** — public training/education build completes from a clean checkout and its generated manifests are internally consistent.

## Nonblocking observations

Word count, subject count, and lesson count are inventory metrics. They do not independently block or authorize deployment.

A subject may remain SKELETON, SEQUENCED, INSTRUCTIONALLY POPULATED, or ASSESSED while expansion continues elsewhere. Only VALIDATED/COMPLETE claims require the full course-package gate.

## Resume rule

Bulk educational expansion may resume when checks 1, 2, 5, 6, 7, and 8 are GREEN repository-wide and the expansion tooling cannot silently bypass them. Check 3 must be GREEN for the dependency wave being expanded. Check 4 must be GREEN before any affected course is promoted to VALIDATED or COMPLETE.

After the gate turns GREEN, expansion resumes in dependency waves:
A foundations -> B core disciplines -> C technical/professional -> D specializations -> E computational/AI/frontier extensions.

Every subsequent expansion batch must rerun the gate before derived EDU16/Symbol256 artifacts are promoted.
