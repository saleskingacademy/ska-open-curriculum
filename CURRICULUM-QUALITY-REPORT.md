# Curriculum Quality Report — 2026-10-06

Audit of the full production curriculum (`ska_curriculum`, 14,427 rows / 995
subjects) at the point of this export, and what was and was not published.

The corpus was read from the verified nightly D1 export
(`temporalking-2026-10-06.sql.gz`, 63 MB, 151 tables), not from a live query, so
the audit and the publication are a single consistent snapshot. Extraction
recovered 14,427 rows across 995 subjects with zero statement errors, matching
the live row count exactly.

## What was published

| | |
|---|---:|
| Subjects published | 985 |
| Lesson records published | 13,635 |
| Lesson records in repo after merge | 14,620 |
| Lesson records in repo before | 1,415 |
| Titles repaired | 1,217 |
| Placeholders held back | 792 |

## Content depth

Depth is genuinely there for the large majority of the corpus. Lesson bodies
measured in characters:

| percentile | chars |
|---|---:|
| p10 | 3,432 |
| p50 | 5,342 |
| p90 | 6,411 |
| max | 11,273 |

By structure:

| class | lessons | share |
|---|---:|---:|
| Structured, with explicit objectives | 11,807 | 81.8% |
| Concept format | 1,220 | 8.5% |
| Template placeholder | 792 | 5.5% |
| Other | 608 | 4.2% |

Spot-checking confirms the material is real and on-subject: VLSI design covers
design hierarchy and logic gates, Russian covers the six-case paradigm, rocket
science calculates specific impulse, media ethics applies the Potter Box.

## Defects found

### 1. Template placeholders — 792 lessons, 10 subjects (held back)

Every one opens `This original Sales King Academy lesson develops <X> as a
structured learning problem`. That is a placeholder, not instruction. It lands
on exactly ten generic academic subjects, 80 lessons each (psychology 72):

`biology`, `chemistry`, `computer_science`, `history`, `literature`,
`philosophy`, `physics`, `programming`, `psychology`, `sociology`

These are **not** published. They are listed by id in
`content/QUARANTINE-placeholder-lessons.json` so they can be regenerated or
retired in production rather than quietly disappearing.

They also account for essentially all of the cross-subject duplication: only 12
duplicate groups / 36 rows exist corpus-wide, and most are this template
repeated under different subjects — which is why the same text appeared under
`chemistry`, `computer_science`, `literature` and `psychology` at once.

### 1b. Lessons filed under non-subject IDs — 388 lessons, 20 IDs (withdrawn)

Correction, 2026-10-06. The first version of this export published 20 lesson
files whose `subject_id` is not a subject at all: 7 named `sat_index_chunk_*`,
12 named `sat_index_sub_*`, and one named `test`. The lesson bodies are real
(for example "Introduction to Interdisciplinary Studies"), but they are filed in
production under internal index names, so there is no way to tell from the
record which subject they belong to. That is the same wrong-subject defect this
audit was meant to catch, and the first pass missed it.

All 20 files are withdrawn and the 388 lessons are listed in
`content/QUARANTINE-placeholder-lessons.json` with
`reason: filed_under_non_subject_id`. None of them existed in this repository
before the export and nothing else here referenced them. They need re-filing
under a real subject in production before they can be published.

Published totals after the correction: **972 lesson files, 14,232 lesson
records**.

### 2. Corrupted titles — 1,217 lessons (repaired on export)

8.4% of the corpus had titles beginning with `**`, left over from parsing a
`**TITLE:**` marker out of the lesson body. The site renders these literally:

```
** Understanding TypeScript's Type System
** Embracing the Present Moment: The Power of Acceptance
```

On export the markup is stripped and, where that leaves nothing usable, the real
heading is recovered from the body's `**Lesson N: ...**` line. **The underlying
rows in production are still corrupted** — this export repairs the published
copy only. Fixing production is a separate change.

### 3. Case-duplicate subjects — 4 groups, 36 rows (merged on export)

Four subjects exist twice under different capitalisation, which splits one
subject into two in the catalogue:

| normalised | production rows |
|---|---|
| `arithmetic` | `Arithmetic` (9) + `arithmetic` (31) |
| `biology` | `Biology` (9) + `biology` (80) |
| `chemistry` | `Chemistry` (9) + `chemistry` (80) |
| `geometry` | `Geometry` (9) + `geometry` (20) |

Export normalises `subject_id` to lowercase/underscore, merging them. **Production
still holds both forms.**

### 4. Assessment and study material gaps

| | lessons | share |
|---|---:|---:|
| Missing `quiz_json` | 14,039 | 97.3% |
| Missing `study_materials` | 6,692 | 46.4% |

This is the largest remaining depth gap. Content is deep; assessment is almost
entirely absent. Not auto-filled here — generating 14,000 quizzes is content
authoring, not a data repair.

### 5. Level coverage

954 of 995 subjects do not span all 8 levels. Median lessons per subject is 13
(min 1, max 100). The repository's own consistency checker now flags shallow
subjects individually; `calculated target × 8 × 10` remains a target, not
populated content.

## Subjects where the repository is richer than production

The exporter never overwrites a lesson file with fewer lessons or fewer
characters than it already has, because several subjects were expanded by hand
here beyond what production holds. Six were kept for that reason:

| subject | repo | production |
|---|---|---|
| `ska_business_ai_autonomous_operations` | 160 lessons / 187,816 ch | 80 / 70,540 |
| `software_engineering` | 80 / 91,633 ch | 9 / 9,292 |
| `chemistry` | 80 / 41,368 ch | 9 / 12,575 |
| `biology` | 80 / 40,825 ch | 9 / 11,048 |
| `psychology` | 80 / 41,078 ch | 8 / 30,601 |
| `sociology` | 80 / 39,885 ch | 20 / 129,121 |

`sociology` is a genuine conflict needing a decision rather than a rule: the
repository has 80 lessons averaging ~500 characters, production has 20 averaging
~6,450. More lessons here, deeper lessons there. Nothing was discarded on either
side — production remains authoritative in the platform, and this copy is
unchanged.

## Public/private boundary

Unchanged and respected. Only educational content is in this repository. No
learner accounts, scores, mastery records, certificates, CRM records, payments,
authentication state, ledger data or deployment credentials were exported; those
tables were never read out of the dump.
