# SKA English Dictionary

Every English word and every one of its definitions, anchored so the platform's agents can
address, cite and reason over an exact meaning.

- **1,395,225 words, 1,209,564 definitions and 657,516 inflection links** ("went" -> go): Open English WordNet 2024
  (CC BY 4.0) for curated nouns, verbs, adjectives and adverbs, plus English Wiktionary (CC BY-SA 4.0, via kaikki.org)
  for everything else - pronouns, articles, prepositions, conjunctions, modern and business words. See LICENSE.
- **A permanent identifier** on every word and every definition (field `dna16`). Numbers are
  append-only and never reused, so a citation to a definition stays valid.
- **A compact meaning signature** on every definition (`sym`), used by the platform to rank
  definitions against a sentence. It is an internal index value, not part of the definition.

Files: `words/<abc>.json`, keyed by the first three letters of the word. Each sense records its source (`src`: wn / wikt). `index.json` holds the counts.
Agents pick the definition that fits the sentence (grammar, overlap with the definition, examples
and synonyms).

The dictionary is rebuilt privately from the two sources above (every existing number is kept).
Shape check: `python3 tools/check_dictionary.py`.