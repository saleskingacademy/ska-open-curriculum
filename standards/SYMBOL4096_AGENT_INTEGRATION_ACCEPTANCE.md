# Symbol4096 and Agent Integration Acceptance Contract

Status: **NOT VERIFIED / NOT DEPLOYED**. This is an implementation and verification gate, not a claim that Symbol4096 is operational.

## Existing verified baseline (main operational repository)
- `docs/SYMBOLIC_ROUTING_ALIGNMENT.md` specifies an explicit Symbol256 state envelope with DNA16, T16, Chain32, Chain128 when available, agent identity, and existing Chain256 state.
- `public/sym/manifest.json` identifies format `symbol256`, version 2, with positive/negative dimension pairs and subject IDs.
- `tools/test-agent-responses.mjs` contains offline contract tests covering 26 agent IDs, specialist routing, response modes, cache isolation, and protected-module hashes.
- Search of the default branch surfaced `Symbol4096` in the test file but did not establish a production Symbol4096 encoder, decoder, artifact manifest, or agent-consumption path. Search results are not an exhaustive proof of absence.

## Non-negotiable compatibility
1. Preserve Chain64 core, existing Chain256 state, DNA16 identity, explicit agent selection, natural/deterministic/auto modes, and privacy isolation.
2. Do not reinterpret Symbol256 digits as Symbol4096 or silently expand the Symbol256 64-pair representation.
3. New symbol representations must be explicitly versioned and negotiated; unsupported versions must fall back to the existing verified Symbol256 + retrieved-text path.
4. Symbol4096 must carry an independently specified, testable encoding, decoding, meaning-recovery and location-recovery contract; token size alone does not establish factual fidelity.
5. Preserve exact source references, document versions, subject/program IDs, content hashes and provenance; stale artifacts must be rejected or regenerated.
6. Agent personas, specializations, permissions, and modes must remain independent. No cross-tenant or cross-agent private memory leakage.
7. Never allow a symbol-only result to invent a fact. Route to verified source material or explicitly state uncertainty.

## Curriculum taxonomy migration dependency
- `adventure_tourism` is incorrectly classified under accounting_finance in the public curriculum. Candidate target is hospitality.
- Migration must update front matter, both catalogue indexes, references, study and symbol artifacts, caches, D1 sync/serving mappings, and any generated search metadata. If regeneration is unavailable, do not activate the moved record.
- Preserve immutable subject identity and historical aliases during any transition.

## Required integration matrix
| Interface | Required test | Current state |
|---|---|---|
| Public curriculum -> operational ingestion | Correct subject, program, version, provenance | Unverified |
| Symbol256 encoder/decoder | Round trip and negation/contradiction fidelity | Existing baseline; full pass unverified |
| Symbol4096 encoder/decoder | Defined schema, round trip, deterministic output, collision checks | Unverified |
| Symbol4096 -> agent routing | All 26 agents retain identity and specialization | Unverified |
| Retrieval -> reasoning -> answer | Citation fidelity, semantic reconstruction, refusal of unsupported claims | Unverified |
| Natural/deterministic/auto | Each mode uses appropriate grounding without persona loss | Unverified |
| Multi-agent operation | Memory isolation, access control, bounded latency | Unverified |
| Production serving | Cache invalidation, D1 consistency, rollback | Unverified |

## Required acceptance sequence
A. Inventory current encoder, decoder, symbol manifests, artifact builders, routing functions, agent prompt/context assembly, and D1 ingestion.
B. Write a versioned Symbol4096 specification grounded in actual implementation; if none exists, implement behind a disabled feature flag.
C. Benchmark against Symbol256, retrieved text, and hybrid approaches on paraphrase, negation, source attribution, meaning/place recovery, collision rates, and latency.
D. Add automated tests for every one of 26 agents in all three modes, including explicit selection, domain routing, fallback, privacy isolation, and unsupported versions.
E. Run end-to-end curriculum update through generated artifacts to production-like serving. Require zero stale-path resolutions.
F. Only then consider controlled canary deployment with rollback and measured results.

**No completion percentages are asserted until evidence exists.**
