# Public curriculum → SKA knowledge intelligence integration contract

Status: proposed implementation contract; **not deployed**. Source of truth: this public repository. Private runtime: `saleskingacademy/sales-king-academy-complete` on Cloudflare Workers, D1, R2, KV and Durable Objects.

## Verified infrastructure audit (2026-11-09)
- `ska-open-curriculum` is public; default branch `main`.
- Cloudflare Worker `sales-king-academy` has `DB`, `TEMPORAL_DB`, `R2_ASSETS`, `R2_BACKUPS`, `SKA_KV`, and `SKA_TIMERS` bindings.
- Worker runtime settings report `CHAIN4096_INTEGRATION=true`, `NL_WEB_FIRST=true`, `OWN_MODEL_ENABLED=false`.
- These settings **do not** prove public curriculum ingestion, transformer inference, or 26-agent retrieval.
- 2026-10-06 public corpus audit documented placeholders, misfiled lessons, and malformed titles; do not use that historical snapshot as live counts.

## Ownership boundary
**Public repository:** canonical lessons, licensed research notes, prerequisite graphs, taxonomy, worked examples, quizzes with solutions, provenance records, nonprivate indexes, deterministic test fixtures, and education release manifests.

**Private repository / Cloudflare:** authenticated users, DNA16 mapping, student progress, mastery scores, CRM, Beats/Square financial data, secrets, proprietary agent prompts and customer memory, production data migrations, private retrieval caches and indexes.

Public research is not a license exemption: record license, author, URL, date, attribution, and permitted reuse for each external source. Do not commit copied restricted content or private data.

## Publication contract
Each lesson/source must carry a stable ID, canonical subject, level (1–8), prerequisites, learning objectives, original/derivative designation, source provenance, licensing/reuse status, reviewed timestamp, evidence confidence, version and content digest, and status:
`draft | quarantined | reviewed | approved | published | superseded`.

A publication manifest must enumerate immutable source commit SHA, approved lesson IDs and hashes, index schema version, counts, excluded records and reason codes. Only approved, license-cleared records can be promoted. Repeated import of the same manifest must be idempotent.

## Execution route
1. PR to a feature branch in this **public repo**. Run schema, quality, license, prerequisite, answer-key and duplicate tests.
2. Review and merge approved educational material to public `main`; keep the unpublished master book separate.
3. A **private** deployment pipeline fetches a pinned public commit/manifest, verifies hashes and provenance, and builds staging search indexes. Never read arbitrary mutable `main` in production.
4. Evaluate BM25/TF-IDF baseline against hybrid embeddings and Symbol256/Symbol4096 on held-out questions; report P@1, P@5, Recall@10, MRR, negation stability, latency, abstention and cost.
5. Verify DNA16 isolation and prompt-injection resistance; publish the validated index atomically and retain rollback pointer.
6. Agents access indexed public educational facts through private authenticated runtime; private tenant context must never flow back into the public repo.
7. Daily Beat-addressed ingestion check and weekly quality audit only after durable execution receipts (issue #40) and backup restore verification (issue #168). Internal jobs never debit customer Beats.

## Initial coverage priorities
Foundational mathematics, language and logic, probability/statistics, evidence and research methods; ethical sales, marketing, finance, accounting, operations; AI/ML, agents, software engineering, cloud, cybersecurity; natural sciences, engineering, humanities, trades, languages and regulated fields with specialist review.

Follow `standards/COVERAGE_BASED_COMPLETION_POLICY.md`. Instructional depth and verified assessment coverage matter more than raw word count.

## Acceptance tests
- Public-to-private manifest import is deterministic, versioned, idempotent and reversible.
- Quarantined lessons, unknown licenses, malformed titles and orphan subject IDs cannot publish.
- A revoked or corrected lesson invalidates derived search entries and stale caches.
- Retrieval comparisons use held-out labeled queries; no unsupported Symbol4096 superiority claims.
- Cross-tenant retrieval returns no other tenant's private data.
- Import failure leaves prior validated index serving; terminal receipt distinguishes failure from success.
- No production writes, automatic deployments, customer charges or public release of unfinished master-book material before review.

## Current state
This file documents the integration boundary and test plan. It does **not** constitute a running ingest pipeline, a new lesson, or a live Cloudflare change.
