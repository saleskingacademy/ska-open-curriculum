# Education-16: addressing, spent memory and Chain256 attachment

Every unit of SKA education (subject, chapter, section, paragraph) is converted to symbolic form and
attached to Chain256. Built and verified by `tools/edu16.py` on every content change
(`build-training.yml`). A broken chain fails the build.

## Three layers (Adaptive Symbol256 Routing spec)

| Layer | Says | Where |
|---|---|---|
| Symbol256 | what kind of knowledge this is (64 positive/negative pairs) | `symbols/`, aggregated per section, chapter, subject in `edu16/` |
| Routing | the fewest base-100 pairs that single the unit out | measured each build, `map/edu16_stats.json` |
| Education-16 | exactly where it is | `edu16/<subject>.json`, `map/edu16_registry.json` |

Measured on the real corpus (40,249 units): the Symbol256 state alone resolves 37,433 units (93%) in an
average of 3.01 base-100 pairs. The other 2,816 share a semantic state with another unit and are resolved
by their Education-16 address. The symbol narrows; the address resolves.

## Education-16

`FF SSS CCC L XXX PPP T` (16 digits)

| Digits | Meaning |
|---|---|
| FF | field, UNESCO ISCED-F 2013 broad field (00-10) |
| SSS | subject, global (000-999) |
| CCC | chapter within subject (000 = the subject itself) |
| L | level (0 = core textbook; 1-8 = the level ladder, `LEVELS.md`) |
| XXX | section within chapter |
| PPP | paragraph within section |
| T | unit type: 1 subject, 2 chapter, 3 section, 4 paragraph |

Positional and append-only. A number, once given, is never reused or moved. Edited text gets a new
paragraph number; the old one stays in the registry as history.

## Spent memory

Education is stored in spent memory: real instants after genesis (2018-07-01 00:00:00 UTC) that were
never used. Each unit's address is a T16 in the platform's canonical format (`CHAIN_ADDR.t16`:
`MMDDYYYYHHMMSSCC`, UTC, centisecond resolution, the memory layer's resolution).

- Education region starts at `0702201800000000` (2018-07-02), one day after genesis. Genesis day holds
  the agent and mode anchors and the S0-S16 spent seconds; checked against both D1 registries
  (2026-09-30): the only identities born before 2026 are the genesis-day mode anchors.
- `offset_cs = ((((L*1000 + SSS)*100 + CCC)*100 + XXX)*100 + PPP)`, so each subject owns a window of
  10,000 seconds, each chapter 100 seconds, each section 1 second, each paragraph 1 centisecond.
  Positional, so no two units can collide (the older hashed lesson addresses could).
- Core textbooks (L0) span about 116 days of 2018; with all eight levels the region ends before
  August 2021. Chapters, sections and paragraphs are capped at 99 per parent.

`EDU-32` = Education-16 + T16: the Chain32 pairing of a stable anchor with its place in time, in the
same shape as `CHAIN_ADDR.chain32`.

Every use of a unit is recorded durably (worker `EDU_USE`, D1 table `edu_use` in temporalking) at the
live instant, in the user's lane, pointing back to the unit's spent instant. The space between the two
is computed with the platform's own formula (`CHAIN_ADDR.space`). The knowledge sits in the past; the
memory of using it sits in the present.

## Chain256 attachment (context: education)

Chain256 does several jobs on the platform: identity chains (Core64 / User64 / Agent64 / Action64),
event stamps (receipts, contracts, ledger, grants), Symbol256 semantic layers, and now education
addressing. Each is a separate context. The education attachment does not change any other chain, and
Chain64 is only referenced, never modified.

Roles in this repo and the worker: Symbol256 + SYMBOLIC_ROUTER route a chat to the owning agent
(identity/routing chain, `CHAIN_ADDR.chain32/chain128`); Education-16 addresses the knowledge itself.
They meet at the symbol layer: a routed query's Symbol256 state narrows to education units, and the
Education-16 address resolves the exact one.

| Lane | Kind | Education content |
|---|---|---|
| 1 | stable | genesis anchor `0701201800000000` |
| 2, 3 | interlocked | live beat clock at the moment of use (computed, never stored) |
| 4 | stable | education anchor `0701201800000094` (genesis band: agents 01-26, modes 91-93, education 94) |
| 5 | stable | subject Education-16 |
| 6, 7 | interlocked | live |
| 8 | stable | subject T16 (spent instant) |
| 9 | stable | this unit's Education-16 |
| 10, 11 | interlocked | live |
| 12 | stable | this unit's T16 (spent instant) |
| 13 | stable | Symbol256 digest of the unit |
| 14, 15 | interlocked | live |
| 16 | stable | integrity digest of the unit's text |

Stored as `s128` (the 8 stable lanes in order). The verifier refuses a unit when the genesis or
education anchor is wrong, the subject or unit address does not match its spent address, two units
share a spent address, or a chapter's text changed without a rebuild.

Copyright (c) 2026 Sales King Academy LLC. All rights reserved.
