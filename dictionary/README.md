# SKA English Dictionary

Every English word and every one of its definitions, anchored so the platform's agents can
address, cite and reason over an exact meaning.

- **1,395,225 words, 1,209,564 definitions and 657,516 inflection links** ("went" -> go): Open English WordNet 2024
  (CC BY 4.0) for curated nouns, verbs, adjectives and adverbs, plus English Wiktionary (CC BY-SA 4.0, via kaikki.org)
  for everything else - pronouns, articles, prepositions, conjunctions, modern and business words. See LICENSE.
- **DNA-16 anchor** on every word and every definition: `88 WWWWWWWW SSSS T C`
  (`88` dictionary band, word number, sense number with `0000` for the word itself,
  `T` 1 = word / 2 = definition, `C` Luhn check digit). Numbers are append-only and never reused.
- **Spent memory**: each anchor owns a never-used past instant (each word a 10-second window,
  each definition one hundredth of a second). The platform derives it privately from the DNA-16;
  no chain or time digits are published here.
- **Symbol256** meaning signature on every definition (`sym`, sparse `position:digit`).

Files: `words/<abc>.json`, keyed by the first three letters of the word. Each sense records its source (`src`: wn / wikt). `index.json` holds the counts.
Agents pick the definition that fits the sentence (grammar, overlap with the definition, examples
and synonyms, and the Symbol256 reading of the sentence).

Rebuild: `python3 tools/build_dictionary_full.py english-wordnet-2024.xml.gz kaikki.org-dictionary-English.jsonl.gz`
(keeps every existing number). Check: `python3 tools/build_dictionary_full.py --verify`.
