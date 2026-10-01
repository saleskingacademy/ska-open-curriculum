# SKA Textbook Standard

Every SKA subject is **original material that is the equivalent of a textbook**: the same level, depth
and coverage a real textbook on that subject gives a student, written by SKA in its own words and
augmented with AI. SKA does not import or republish other textbooks.

## 1. Equivalence (what it teaches)
- Level matches the course level (introductory, intermediate, advanced, professional).
- Coverage matches what standard textbooks at that level cover. Published textbooks are used as
  **references for scope and level only**, the way any author or teacher learns from them.
- Every topic on the subject's scope checklist is taught, with the concepts, methods and applications
  a student at that level is expected to master.

## 2. Structure: 107 textbooks, each subject is one chapter (checked by `tools/textbook_check.py`)
`map/textbooks.json` groups all 1,117 subjects into 107 original SKA textbooks. Customers still buy by subject;
each subject is a full chapter. Per chapter:

| Element | Minimum |
|---|---|
| Words | 8,000 |
| Learning objectives | 1 block |
| Worked examples | 2 |
| Case study | 1 |
| Review questions (answers in the book's answer key) | 8 |
| Key terms | 1 block |

Per book: a glossary and an answer key.

**Sales King Academy program (exclusive requirements).** Every chapter also has:
- **SKA Lab**: a hands-on exercise done on the live saleskingacademy.com platform (Agent Builder,
  Automations, CRM, vault connections, chat source badges), not a simulation.
- **SKA Field Case**: a case from Sales King Academy's own operations, with real systems, decisions
  and measured results. Figures only the founder holds are left as marked blanks, never invented.
- Header `generated_by` records the writing model and `training_use` records how the text may be used
  for training. Text written with Claude may train SKA's specialized models (business, sales and marketing
  education and tools); under Anthropic's terms it may not train a general-purpose model that competes
  with Anthropic's own. Stand-alone subject standard (for reference):
| Element | Minimum |
|---|---|
| Words | 30,000 |
| Chapters (`## ` headings) | 12 |
| Learning objectives (one block per chapter) | 12 |
| Worked examples | 24 |
| Case studies | 12 |
| Review questions, answers in an answer key | 96 |
| Glossary (`## Glossary` or `## Key terms`) | 1 |

## 3. Originality (checked by `tools/originality_check.py`)
- No passage is copied from any source. No close paraphrase: explanations, examples, exercises,
  case studies and structure are SKA's own.
- Facts, formulas and widely known methods are not owned by anyone and may be taught, restated in SKA's words.
- Automatic gate: fails on any 12-word run shared with a reference, or more than 2% shared 8-word sequences.
- Figures and diagrams are drawn fresh; none are copied.
- Reference texts stay local (`refs/`, gitignored) and are never committed or published.

## 4. Terms adherence
- Licences: material under non-commercial or no-derivatives licences is read for learning only.
  Nothing from any source is reproduced beyond what its licence allows.
- AI providers: text written with an outside model follows that provider's terms. If those terms
  restrict using outputs to train competing models, the header's `training_use` records the limit and the
  training pipeline follows it.
  Each chapter records which model wrote or assisted it (`generated_by` in its header).
- Every chapter lists its references for further reading.

A subject is complete only when it passes sections 2 and 3 and its scope checklist is fully covered.

## 5. Levels: L1-L8 anchored to real education levels (UNESCO ISCED 2011)

SKA keeps its eight level names, but each one now means a real, checkable academic level.
A subject is complete only when every level meets the bar below.

| SKA level | Name | Equivalent | What the material must contain |
|---|---|---|---|
| L1 | Beginner | Secondary school (ISCED 2-3) | Plain-language definitions, everyday examples, no prerequisites |
| L2 | Foundations | First-year university (ISCED 6, year 1) | Core vocabulary, standard models, worked examples, the intro-course canon |
| L3 | Intermediate | Bachelor's year 2 | Methods applied to problems, case studies, graded problem sets |
| L4 | Advanced | Bachelor's years 3-4 (upper division) | Full theory with derivations or formal arguments, capstone-style problems |
| L5 | Expert | Master's (ISCED 7) | Graduate texts' depth, competing frameworks compared, professional practice |
| L6 | Master | Advanced master's / professional licensure | Judgement under uncertainty, standards and regulation, supervised-practice cases |
| L7 | Specialist | Doctoral (ISCED 8) | Qualifying-exam depth; primary literature read directly; research methods; every claim cited |
| L8 | Grandmaster | **Postdoctoral / research frontier** | The current state of the field: open problems, active debates, newest results, how to run original research. Rebuilt on a schedule, not written once |

### 5.1 Rules that make L7 and L8 trustworthy
- **Every factual claim at L7-L8 cites a real work** with a DOI or arXiv id, in the form
  `[R#] Authors (year). "Title". doi:... | arXiv:...`
- `tools/cite_check.py` verifies every reference against Crossref and arXiv and fails the chapter on
  an unresolvable id or a title that does not match. No invented sources can ship.
- L8 carries a **"current as of" date** and is regenerated from newly published literature every
  90 days. A frontier chapter older than that is marked stale on the site.
- L8 distinguishes three things explicitly: **established** (replicated, in textbooks),
  **contested** (active debate, both sides cited), **open** (unsolved, stated as a problem).
- AI-written L7-L8 material is labelled as AI-authored and source-grounded. It does not claim peer
  review it has not had. Subjects where errors cause harm (medicine, law, engineering safety,
  finance) carry a notice that the material supports study and does not replace a licensed professional.

### 5.2 What "beyond a textbook" means (the AI augmentation layer)
A printed textbook is fixed. Each SKA subject adds, at every level:
1. **Tutor grounded in the chapter**: the SKA agent answers from this subject's material and its
   cited sources, and says so when a question goes past them.
2. **Unlimited practice**: new problems generated per level, each with a checked answer.
3. **Mastery tracking**: spaced review of what a learner got wrong, with level progression gated by results.
4. **Living frontier**: L8 is refreshed from new papers, so the top of every subject stays current.
5. **Cross-subject links**: the Symbol256 map connects each chapter to related chapters in other subjects.

These are claims about features, not about the knowledge itself. Content quality is measured by the
checks in sections 2-5, not asserted.
