"""Rebuild evidence inventory; do not promote status from size or heading counts.

Run from any directory: python tools/mathematics_manifest.py
Counts use whitespace tokens after excluding metadata, headings, tables, and code.
They are a reproducible prose proxy, not an independent substantive-content audit.
Legacy words and canonical new-path words are separately reported, never summed
across overlapping catalogue subjects as a unique mathematics corpus total.
"""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
MATH = ROOT / 'curriculum/mathematics'

def prose_words(path):
    text = path.read_text(encoding='utf-8')
    text = re.sub(r'```.*?```', '', text, flags=re.S)
    lines = []
    for line in text.splitlines():
        if re.match(r'^(#|\||Canonical ID:|Prerequisites:|Next:|Education-16|Version:|Status:)', line):
            continue
        lines.append(line)
    return len(' '.join(lines).split())

def relative(paths):
    return [str(p.relative_to(ROOT)) for p in sorted(set(paths))]

def main():
    names = '''Numeracy|Arithmetic|Pre-Algebra|Elementary Algebra|Intermediate Algebra|Geometry|Trigonometry|Precalculus|Single-Variable Calculus|Integral Calculus|Multivariable Calculus|Vector Calculus|Linear Algebra|Multilinear Algebra|Differential Equations|Partial Differential Equations|Discrete Mathematics|Combinatorics|Graph Theory|Mathematical Logic|Set Theory|Probability|Statistics|Bayesian Mathematics|Stochastic Processes|Real Analysis|Complex Analysis|Abstract Algebra|Group Theory|Ring Theory|Field Theory|Module Theory|Commutative Algebra|Representation Theory|Number Theory|Algebraic Number Theory|Analytic Number Theory|Numerical Analysis|Scientific Computing|Optimization|Operations Research|Topology|Algebraic Topology|Differential Topology|Measure Theory|Functional Analysis|Harmonic and Fourier Analysis|Differential Geometry|Algebraic Geometry|Category Theory|Homological Algebra|Proof Theory|Model Theory|Computability|Dynamical Systems|Chaos|Information Theory|Coding Theory|Game Theory|Decision Theory|Control Mathematics|Mathematical Physics|Financial Mathematics|Actuarial Mathematics|Cryptographic Mathematics|Computational Algebra|Computer Algebra|Mathematical Modeling|Simulation|Research Methods|Mathematical Writing|SAT and Constraint Mathematics|Formal Mathematics|AI-Augmented Mathematics|Frontier and Research Literacy'''.split('|')
    # Explicit aliases prevent substring matching from quietly misclassifying content.
    aliases = {'Elementary Algebra':['algebra_1'], 'Intermediate Algebra':['algebra_2'],
               'Single-Variable Calculus':['calculus_1'], 'Integral Calculus':['calculus_2'],
               'Multivariable Calculus':['calculus_3'],
               'Mathematical Logic':['mathematical_logic'],
               'Category Theory':['category_theory_cs','higher_category_theory']}
    catalogue = json.loads((ROOT/'map/real_subjects.json').read_text())['books']
    math_titles = ['Foundations of Mathematics','Algebra','Geometry and Trigonometry',
                   'Calculus','Discrete Mathematics and Logic','Probability and Statistics',
                   'Mathematical Analysis','Applied Mathematics and Operations Research',
                   'Financial and Actuarial Mathematics','Theory of Computation and Information']
    # Include original grouped subjects as well as the explicit expanded subjects.
    names += [n for n in math_titles if n not in names]
    names += [p.stem.replace('_',' ').title() for p in (ROOT/'knowledge/mathematics').glob('*.md')
              if p.stem.replace('_',' ').title() not in names
              and p.stem not in {a for v in aliases.values() for a in v}]
    rows=[]
    for name in dict.fromkeys(names):
        sid=re.sub(r'[^a-z0-9]+','_',name.lower()).strip('_')
        stems=aliases.get(name,[sid])
        sources=[ROOT/f'knowledge/mathematics/{s}.md' for s in stems]
        book=next((b for b in catalogue if b['title']==name),None)
        if book:
            sources += [p for s in book['topics_as_chapters'] for p in (ROOT/'knowledge').glob(f'*/{s}.md')]
        sources=sorted({p for p in sources if p.exists()})
        structured=[ROOT/f'curriculum/mathematics/{s}.json' for s in stems]
        structured=[p for p in structured if p.exists()]
        lesson_records=[]
        for p in structured:
            d=json.loads(p.read_text())
            lesson_records += [x for level in d.get('levels',{}).values() for x in level.get('lessons',[])]
        rows.append(dict(subject_id=sid,subject=name,status='SKELETON',
            status_basis='Programme scope identified; full lesson/assessment audit pending.',
            word_count=sum(prose_words(p) for p in sources),word_count_scope='legacy knowledge prose proxy; unvalidated',
            source_paths=relative(sources+structured),modules=None,lessons_planned=None,
            lessons_populated=0,legacy_lesson_records=len(lesson_records),quizzes=0,problem_sets=0,
            module_exams=0,final_exam=False,projects_capstones=0,
            solution_coverage='NOT AUDITED',prerequisite_coverage='NOT AUDITED',
            computational_coverage='NOT AUDITED',ai_augmented_coverage='NOT AUDITED',
            validation_status='PENDING',mapping_status='DEFERRED'))
    ar=next(r for r in rows if r['subject']=='Arithmetic')
    folder=MATH/'arithmetic'
    lessons=sorted(folder.glob('lesson_[0-9][0-9]_*.md'))
    legacy=folder/'level_01_lessons_01_05.md'
    exams=sorted((folder/'assessments').glob('*.md'))
    ar.update(status='SEQUENCED',status_basis='80-lesson map; partial full lesson population; course gates open.',
        word_count=sum(prose_words(p) for p in [legacy]+lessons+exams),
        word_count_scope='canonical lesson and assessment prose proxy; excludes map, README, metadata and headings',
        source_paths=relative([MATH/'arithmetic_zero_to_advanced.md',legacy]+lessons+exams),
        modules=8,lessons_planned=80,lessons_populated=len(lessons),
        partial_lesson_drafts=5,quizzes=len(lessons),problem_sets=len(lessons),
        module_exams=len(exams),final_exam=False,projects_capstones=int((folder/'lesson_10_foundation_mastery.md').exists()),
        project_note='Lesson 10 foundational investigation; full course capstone pending.',
        assessment_forms=2*len(exams),
        solution_coverage='New full lesson packages have explanatory keys; legacy draft practice coverage incomplete.',
        prerequisite_coverage='Local entry checks; earlier full-package gaps and advanced bridge gaps remain.',
        computational_coverage='Optional concrete algorithm traces in new lessons; advanced modules pending.',
        ai_augmented_coverage='Constructed incorrect claims audited independently in new lessons; advanced modules pending.',
        validation_status='Source-reviewed; exact checks in validation report; no independent academic review.',
        full_lesson_population_percent=round(100*len(lessons)/80,2),
        word_floor=120000,word_floor_percent=round(100*sum(prose_words(p) for p in [legacy]+lessons+exams)/120000,2),
        completion_percent=None,
        completion_percent_note='No defensible single completion percentage across heterogeneous course gates; report lesson population and word-floor progress separately.')
    report=dict(schema_version=1,inventory_date_utc='2026-10-03',
        governing_specs=['standards/ZERO_TO_FRONTIER_CURRICULUM_STANDARD.md',
          'standards/CURRICULUM_COMPLETION_AUDIT.md','standards/ACADEMIC_EQUIVALENCE_AND_ASSESSMENT_STANDARD.md',
          'curriculum/mathematics/MATHEMATICS_COMPLETION_MASTER_PLAN.md'],
        states=['SKELETON','SEQUENCED','INSTRUCTIONALLY POPULATED','ASSESSED','VALIDATED','COMPLETE'],
        caution='SKELETON is a conservative audited lower bound, not a finding that legacy files contain no instruction. Null means unestablished, zero means no verified canonical package counted. Overlapping source inventories must not be summed.',
        subjects=rows)
    (MATH/'MATHEMATICS_COMPLETION_MANIFEST.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'subjects':len(rows),'arithmetic':ar},indent=2))

if __name__=='__main__':
    main()
