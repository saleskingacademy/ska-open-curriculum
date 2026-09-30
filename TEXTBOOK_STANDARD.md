# SKA Textbook Standard

A subject counts as **textbook-equivalent** only when `tools/textbook_check.py` passes it. Minimums per subject:

| Element | Minimum |
|---|---|
| Words | 30,000 |
| Chapters (`## ` headings) | 12 |
| Learning objectives (`### Learning objectives`, one per chapter) | 12 |
| Worked examples (`### Example ...`) | 24 (2 per chapter) |
| Case studies (`### Case study ...`) | 12 (1 per chapter) |
| Review questions (numbered lines ending in `?`), answers in an answer key | 96 (8 per chapter) |
| Glossary (`## Glossary` or `## Key terms`) | 1 |

Each chapter: objectives, explanation, worked examples, a case study, a summary, key terms, review questions.
Scores are 0-100; `map/textbook_map.json` holds every subject's current score, source strategy and priority tier.
Sources: open textbooks only where the licence allows commercial use (CC BY / CC BY-SA), credited per chapter;
everything else is original material written to this standard.
