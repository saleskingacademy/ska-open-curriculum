# Sales King Academy — Open Curriculum

This repository is the public educational-content plane for Sales King Academy.

## Purpose

This repository contains the instructional corpus that can be published openly:
- subjects and curriculum maps
- structured lessons
- examples and practice exercises
- quizzes and assessment material intended for public use
- prerequisite and progression metadata
- provenance and editorial guidance

It does **not** contain learner accounts, individual scores, mastery records, private analytics, payments, CRM records, authentication data, deployment credentials, or other private platform state.

## Curriculum model

SKA curriculum is organized from foundational learning through advanced and research-oriented study. The intended progression is:

**Learn → Practice → Demonstrate → Test → Remediate → Retest → Master → Apply → Synthesize**

Public curriculum content is separate from private learner records. The private platform can use this corpus to deliver lessons and record learner-specific assessment results without publishing those records here.

## Content provenance

The curriculum teaches established subjects and concepts using independently authored SKA instructional material. Facts, theories, formulas, methods, historical events, and other underlying ideas are not claimed as proprietary merely because SKA teaches them. Original expression, sequencing, exercises, assessments, metadata, and organization are maintained as SKA curriculum material to the extent permitted by applicable law.

See EDUCATION-CONTENT-PROVENANCE.md for the editorial/provenance standard.

## Source migration

This repository is being populated from the educational portions of the private SKA platform repository. Private application code and user-specific data remain private.

## Knowledge base (`knowledge/`)

1,101 subjects of teaching material across 18 programs, exported from the Sales King Academy
knowledge base on 2026-09-28. One Markdown file per subject: `knowledge/<program>/<subject>.md`.
Each file's header carries the subject's DNA-16, L4 address and Chain256 anchor, so every
subject has a permanent address. `knowledge/index.json` lists every subject with its path,
sections, size and SHA-256; `knowledge/paths.json` is the slim key-to-path map the website uses.

Cleaning applied on export: exact duplicate paragraphs removed, and corrupted model output
(runs of stray quote characters) dropped. Nothing else was rewritten.

## Branches

- `main` is the working copy. Edits land here first.
- `live` is what saleskingacademy.com serves. It only moves when **Actions > Promote main to live** is run
  (fast-forward only), so nothing reaches paying students unreviewed.

## Access

The text here is openly licensed (CC BY-SA 4.0) and anyone can read it on GitHub.
The guided courses at [saleskingacademy.com](https://saleskingacademy.com) — lessons delivered and
explained by the SKA agents, quizzes, level progression, progress tracking and certificates —
are paid, in Beats.
