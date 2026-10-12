# Academic Catalogue Metadata Reconciliation — 2026-10-10

Repository: saleskingacademy/ska-open-curriculum
Branch: ska-education-expansion-2026-10-02
Method: retrieved and parsed complete knowledge/index.json and knowledge/paths.json via GitHub connector. This is a metadata audit, not a complete filesystem or academic audit.

## Verified
- index.json declared count: 1118
- index.json actual rows: 1118
- unique subject keys: 1118
- duplicate keys: 0
- paths.json key count: 1118
- index entries missing in paths.json: 0
- index-to-paths.json path disagreements: 0
- deviations from knowledge/<program>/<key>.md convention: 0
- indexed program categories: 20

## Indexed counts by program
| Program | Records |
|---|---:|
| accounting_finance | 50 |
| agriculture | 34 |
| arts | 62 |
| business | 101 |
| computer_science | 66 |
| data_science | 23 |
| education | 26 |
| engineering | 86 |
| general | 1 |
| general_studies | 183 |
| hospitality | 9 |
| languages | 61 |
| law | 49 |
| marketing_sales | 59 |
| mathematics | 42 |
| medicine | 82 |
| natural_sciences | 63 |
| sales_king_academy | 17 |
| social_sciences | 89 |
| trades | 15 |

## Confirmed taxonomy issue requiring coordinated correction
adventure_tourism has program accounting_finance in index.json, paths.json, and its actual Markdown front matter at knowledge/accounting_finance/adventure_tourism.md. Its educational content is about tourism operations, safety, and sustainability, not accounting or finance. Candidate destination: hospitality; do not move without inspecting canonical mappings, links, generated study/symbol artifacts, and serving dependencies.

## Unverified
- Whether every referenced Markdown file exists
- Whether taxonomy is semantically correct for all 1118 records
- Whether the historical 369-subject audit refers to a different source scope
- Whether quizzes, private exams, solutions, and capstones meet standards
- Course certification completion percentages and accreditation readiness

## Next safe action
Run the read-only filesystem inventory workflow, review its artifact, then conduct semantic taxonomy review and surgical fixes with dependent artifact regeneration. Do not equate metadata consistency with academic completeness.
