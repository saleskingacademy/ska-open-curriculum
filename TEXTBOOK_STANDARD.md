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

## 2. Structure (checked by `tools/textbook_check.py`)
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
  restrict using outputs to train other models, that text is excluded from ska_own training data.
  Each chapter records which model wrote or assisted it (`generated_by` in its header).
- Every chapter lists its references for further reading.

A subject is complete only when it passes sections 2 and 3 and its scope checklist is fully covered.
