# SKA Level Ladder: secondary to postdoctoral

Every real subject (see `REAL_SUBJECTS.md`) is taught across the platform's eight mastery levels, grouped
in four volumes. Level meanings and content rules are set in `TEXTBOOK_STANDARD.md` section 5. Level names
describe depth of study, not accreditation: SKA does not grant degrees.

| Level | Name | Academic equivalent (ISCED 2011) | Volume |
|---|---|---|---|
| 1 | Beginner | Secondary school (ISCED 2-3) | Textbook |
| 2 | Foundations | First-year university (ISCED 6) | Textbook |
| 3 | Intermediate | Bachelor's year 2 | Textbook |
| 4 | Advanced | Bachelor's years 3-4 | Textbook |
| 5 | Expert | Master's (ISCED 7) | Graduate |
| 6 | Master | Advanced master's / professional licensure | Graduate |
| 7 | Specialist | Doctoral (ISCED 8) | Doctoral |
| 8 | Grandmaster | Postdoctoral / research frontier | Research Frontier |

## Volume sizes

**Textbook (L1-L4).** `TEXTBOOK_STANDARD.md` sections 1-4: 120,000+ words, 12+ chapters, worked examples,
cases, review questions with answer key. Checked by `tools/textbook_check.py` and `tools/originality_check.py`.

**Graduate (L5-L6).** 60,000+ words per subject: formal derivations where the field uses them, competing
frameworks with their evidence, primary-literature readings from the subject's frontier map, 60 graduate
problems with full solutions.

**Doctoral (L7).** 40,000+ words per subject: research methods, literature synthesis by question, a
100-question qualifying bank with model answers, open questions tied to the works that leave them open.
Every claim cited; `tools/cite_check.py` must pass.

**Research Frontier (L8, postdoctoral).** 15,000+ words per subject plus a living literature map
(`frontier/<subject>.json`, rebuilt monthly by `tools/frontier.py` from the OpenAlex scholarly index):
what changed in the last 24 months, open problems, five research-project briefs, and methods to attack
them. Every recent-research statement cites a work in the map; AI-proposed directions are labelled as
proposals; no paper text is reproduced.

## Addressing

Each level's material gets its own Education-16 level digit (1-8) and its own spent-memory address
(`EDU16.md`). Level 0 is the core textbook body built today.

Copyright (c) 2026 Sales King Academy LLC. All rights reserved.
