#!/usr/bin/env python3
"""Inventory source material without equating its presence with completion."""
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def build():
    index = json.loads((ROOT / 'curriculum/index.json').read_text())
    paths = json.loads((ROOT / 'knowledge/paths.json').read_text())
    categories = {s: k for k, c in index['categories'].items() for s in c['subjects']}
    math = json.loads((ROOT / 'curriculum/mathematics/MATHEMATICS_COMPLETION_MANIFEST.json').read_text())
    arithmetic = next(s for s in math['subjects'] if s['subject'] == 'Arithmetic')
    rows = []
    for sid in sorted(set(categories) | set(paths)):
        source = paths.get(sid)
        exists = bool(source and (ROOT / source).is_file())
        row = dict(subject_id=sid, category=categories.get(sid),
                   status='SKELETON', status_basis='Existing material preserved; course-wide outcome and assessment audit pending.',
                   source_path=source, source_exists=exists, word_count=None,
                   modules=None, lessons_planned=None, lessons_populated=None,
                   quizzes=None, problem_sets=None, module_exams=None,
                   final_exam=None, projects_capstones=None,
                   solution_coverage='NOT AUDITED', prerequisite_coverage='NOT AUDITED',
                   computational_coverage='NOT AUDITED', ai_augmented_coverage='NOT AUDITED',
                   validation_status='PENDING', completion_percent=None,
                   fallback_required=True, fallback_implementation='REQUIRED; PRODUCTION INTEGRATION NOT VERIFIED')
        if sid == 'arithmetic':
            for key in ('status','status_basis','word_count','modules','lessons_planned','lessons_populated','quizzes','problem_sets','module_exams','final_exam','projects_capstones','solution_coverage','prerequisite_coverage','computational_coverage','ai_augmented_coverage','validation_status'):
                row[key] = arithmetic[key]
            row['lesson_population_percent'] = arithmetic['full_lesson_population_percent']
            row['canonical_manifest'] = 'curriculum/mathematics/MATHEMATICS_COMPLETION_MANIFEST.json'
        rows.append(row)
    for sid, name in [('introduction_to_business','Introduction to Business'),('professional_selling','Professional Selling'),('engineering_fundamentals','Engineering Fundamentals')]:
        rows.append(dict(subject_id=sid+'_entry_course', scope='12-lesson entry course: '+name,
                         status='SEQUENCED', status_basis='Entry sequence in CROSS_DOMAIN_COMPLETION_PLAN; full packages not authored.',
                         lessons_planned=12, lessons_populated=0, lesson_population_percent=0,
                         completion_percent=None, validation_status='PENDING', fallback_required=True,
                         fallback_implementation='REQUIRED; PRODUCTION INTEGRATION NOT VERIFIED'))
    output = dict(schema_version=1, inventory_date_utc=datetime.now(timezone.utc).date().isoformat(),
                  percentage_policy='Null means no audited acceptance denominator. Lesson population is not overall completion.',
                  source_policy='SKELETON is a conservative lower bound pending review; existing instructional prose is retained. Do not sum overlapping inventories.',
                  length_policy='Coverage-based completion; no universal word floor.',
                  states=math['states'], subjects=rows,
                  fallback_policy='standards/INCOMPLETE_MATERIAL_WEB_FALLBACK.md')
    target=ROOT/'curriculum/PROGRAMME_COMPLETION_MANIFEST.json'
    assert len({r['subject_id'] for r in rows}) == len(rows), 'Duplicate scope identifiers'
    target.write_text(json.dumps(output, indent=2)+'\n')
    print(f'Inventoried {len(rows)} scopes; existing sources preserved.')

if __name__ == '__main__':
    build()
