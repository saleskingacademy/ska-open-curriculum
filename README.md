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

The knowledge corpus currently contains 1,118 indexed subject records across the public program tree. The textbook map currently evaluates 1,117 subject records; legacy curriculum identifiers remain separately tracked and are not treated as proof that every calculated lesson target is populated. One Markdown file per subject: `knowledge/<program>/<subject>.md`.
Each file's header carries the subject's DNA-16, L4 address and Chain256 anchor, so every
subject has a permanent address. `knowledge/index.json` lists every subject with its path,
sections, size and SHA-256; `knowledge/paths.json` is the slim key-to-path map the website uses.

Cleaning applied on export: exact duplicate paragraphs removed, and corrupted model output
(runs of stray quote characters) dropped. Nothing else was rewritten.

## Current depth

The public corpus is intentionally being expanded in two dimensions: broad subject coverage and deep textbook-quality development. The repository now contains a 12-chapter textbook standard, textbook scoring, originality screening, structured lesson datasets, study packs, and the SKA-exclusive business/AI/autonomous-operations sequence. A subject count or calculated lesson target is not treated as a completed textbook or populated lesson set.

## Branches

- `main` is the working copy. Edits land here first.
- `live` is what saleskingacademy.com serves. It only moves when **Actions > Promote main to live** is run
  (fast-forward only), so nothing reaches paying students unreviewed.

## Access

The material here is owned by Sales King Academy LLC, all rights reserved (see LICENSE). It is public to read, not to copy or resell; full access is sold at saleskingacademy.com.
The guided courses at [saleskingacademy.com](https://saleskingacademy.com) — lessons delivered and
explained by the SKA agents, quizzes, level progression, progress tracking and certificates —
are paid, in Beats.
