"""Exact checks for Lessons 17-20 and both public Level 2 exam forms.

Parse published numeric practice/exam keys; source-labeled fixtures supplement
manual review of explanations, modeling assumptions, units and rubrics.
"""
from pathlib import Path
import ast
import json
import operator
import re

ROOT = Path(__file__).resolve().parents[1]
FOLDER = ROOT / 'curriculum/mathematics/arithmetic'
OPS = {ast.Add: operator.add, ast.Sub: operator.sub}

def value(text):
    node = ast.parse(text.replace(',', '').replace('−', '-'), mode='eval').body
    def walk(n):
        if isinstance(n, ast.Constant) and type(n.value) is int:
            return n.value
        if isinstance(n, ast.UnaryOp) and isinstance(n.op, ast.USub):
            return -walk(n.operand)
        if isinstance(n, ast.UnaryOp) and isinstance(n.op, ast.UAdd):
            return walk(n.operand)
        if isinstance(n, ast.BinOp) and type(n.op) in OPS:
            return OPS[type(n.op)](walk(n.left), walk(n.right))
        raise ValueError('Only integer addition/subtraction allowed')
    return walk(node)

def number(text):
    return int(re.search(r'[+−-]?\d[\d,]*', text).group().replace(',', '').replace('−', '-'))

def nearest_ten(n):
    assert n >= 0
    return ((n+5)//10)*10

def main():
    checks = []
    def check(label, actual, expected):
        if actual != expected:
            raise AssertionError((label, actual, expected))
        checks.append(label)

    for n in range(17,21):
        text = next(FOLDER.glob(f'lesson_{n}_*.md')).read_text()
        section = text.split('## Independent problem set and explanatory key',1)[1]
        prompts, keys = section.split('Solutions:',1)
        keys = keys.split('\n## ',1)[0]
        for i in range(1,11):
            expression = re.search(rf'^P{i}\. (.+)\.$',prompts,re.M).group(1)
            expected = number(re.search(rf'^P{i}\. (.+)$',keys,re.M).group(1))
            check(f'L{n} P{i} parsed',value(expression),expected)

    text = (FOLDER/'assessments/level_02_operations_examination.md').read_text()
    for form in ('A','B'):
        prompts = text.split(f'## Form {form} — learner paper',1)[1].split('## ',1)[0]
        keys = text.split(f'## Form {form} — explanatory key',1)[1].split('## ',1)[0]
        rows = {int(m[0]):m[1] for m in re.findall(r'^\| (\d+) \| ([^|]+) \|',keys,re.M)}
        check(f'Exam {form} key count',len(rows),25)
        story = ({4:'7+5',9:'23-16',15:'4-(-6)',18:'5+5+5',21:'735+148-269+17',
                  22:'628-631',23:'-24+39',24:'53-28',25:'-7-(-4)'} if form=='A' else
                 {4:'8+6',9:'29-18',15:'5-(-8)',18:'5+5+5+5',21:'846+157-328+19',
                  22:'697-694',23:'-31+47',24:'64-37',25:'-9-(-6)'})
        for i in list(range(1,19))+list(range(21,26)):
            if i in story:
                expression = story[i]
            else:
                prompt = re.search(rf'^{i}\. (.+)$',prompts,re.M).group(1)
                expression = re.search(r'Calculate ([\d,−+() −]+)',prompt).group(1).strip()
            check(f'Exam {form} item {i} published result',value(expression),number(rows[i]))
        bounds = (19,26) if form=='A' else (27,36)
        check(f'Exam {form} interval key',tuple(map(int,re.findall(r'\d+',rows[19]))),bounds)
        check(f'Exam {form} input validation judgment',rows[20].strip(),'No')
        final = -3 if form=='A' else -6
        check(f'Exam {form} item 23 final',number(rows[23].split('final')[1]),final)
        for i,(a,b,op) in ({16:(397,208,'+'),17:(802,396,'-')} if form=='A' else
                           {16:(486,317,'+'),17:(903,498,'-')}).items():
            nums = tuple(map(int,re.findall(r'\d+',rows[i])))
            exact = value(f'{a}{op}{b}')
            estimate = value(f'{nearest_ten(a)}{op}{nearest_ten(b)}')
            check(f'Exam {form} item {i} full estimate key',nums,(exact,estimate,abs(exact-estimate)))

    fixtures = {
      'L17 examples/guided': [('764-231',533),('52-28',24),('402-178',224),('3000-786',2214),('5006-89',4917),('1002-997',5),('2405-678',1727),('81-46',35),('600-257',343)],
      'L17 transfer/quiz/alternate': [('63-27',36),('4000-1275-48',2677),('408-93',315),('945-312',633),('64-29',35),('700-486',214),('8002-75',7927),('876-243',633),('83-47',36),('900-568',332),('6003-87',5916)],
      'L18 examples/guided': [('-8+(-5)',-13),('-7+12',5),('9+(-14)',-5),('-6-4',-10),('-6-(-4)',-2),('3-(-2)',5),('3-(-4)',7),('-9+4',-5),('6-(-8)',14),('-5+5',0)],
      'L18 transfer/quiz/alternate': [('-35+48-19',-6),('-5-(-12)',7),('2-(-3)',5),('-8+(-3)',-11),('-10+6',-4),('-4+(-7)',-11),('5-(-9)',14),('-8-(-3)',-5),('2-(-7)',9),('-13+8',-5),('-6+(-8)',-14),('7-(-4)',11),('-11-(-5)',-6),('3-(-9)',12)],
      'L19 examples/guided': [('398+207',605),('803-397',406),('1002-997',5),('98+47',145),('102+49',151),('98-49',49),('102-47',55),('-8+3',-5),('240+160',400),('250+150',400),('486+312',798),('704-286',418)],
      'L19 transfer/quiz/alternate': [('-5+3',-2),('-2+6',4),('500-198',302),('312+198',510),('196+308',504),('701-298',403),('10-7',3),('12-4',8),('287+416',703),('802-397',405),('20-9',11),('24-6',18)],
      'L20 examples/guided': [('1250+375',1625),('1625-468',1157),('1157+27',1184),('1184+468',1652),('1250+402',1652),('-28+45',17),('17-19',-2),('-2+6',4),('1179-1184',-5),('137+89',226),('137-89',48),('1250+380-470+30',1190),('320+85-97',308),('-9+14-8',-3)],
      'L20 investigation': [('680+145',825),('825-278',547),('547+16',563),('563-89',474),('474+207',681),('145+16+207',368),('278+89',367),('681+367',1048),('680+368',1048),('677-681',-4),('680+150-280+20-90+210',690)],
      'L20 quiz/alternate': [('450+125-238',337),('-16+21-9',-4),('340-337',3),('520+148-279',389),('-19+27-11',-3),('386-389',-3)],
    }
    for group, pairs in fixtures.items():
        for expression, expected in pairs:
            check(f'{group}: {expression}',value(expression),expected)

    # Check every numeric estimate in Lesson 19's first six published practice keys.
    l19 = next(FOLDER.glob('lesson_19_*.md')).read_text().split('Solutions:',1)[1].split('\n## ',1)[0]
    for i,(operands,op) in enumerate([([297,406],'+'),([684,219],'+'),([902,487],'-'),([1004,998],'-'),([149,251,98],'+'),([600,297],'-')],1):
        exact=value(op.join(map(str,operands)))
        estimate=value(op.join(str(nearest_ten(v)) for v in operands))
        key=re.search(rf'^P{i}\. (.+)$',l19,re.M).group(1)
        # Prose spells some errors in words; this fixture fixes their source location.
        check(f'L19 P{i} estimate fixture',estimate,[710,900,410,0,500,300][i-1])
        check(f'L19 P{i} error fixture',abs(estimate-exact),[7,3,5,6,2,3][i-1])

    # Independent digit-exchange implementation exercises zero chains and ordering.
    def column_sub(a,b):
        assert a>=b>=0
        digits=list(map(int,reversed(str(a))))
        sub=list(map(int,reversed(str(b))))
        for i in range(len(digits)):
            take=sub[i] if i<len(sub) else 0
            if digits[i]<take:
                j=i+1
                while digits[j]==0:
                    j+=1
                digits[j]-=1
                while j>i:
                    j-=1
                    digits[j]+=10
                    if j>i:
                        digits[j]-=1
            digits[i]-=take
        return int(''.join(map(str,reversed(digits))))
    count=0
    for a in range(201):
        for b in range(a+1):
            assert column_sub(a,b)==a-b
            count+=1
    for a,b in [(3000,786),(10000,1),(6020,597),(5006,89)]:
        check(f'Zero-chain algorithm {a}-{b}',column_sub(a,b),a-b)
    bound_count=0
    for a in range(101):
        for b in range(101):
            assert abs(nearest_ten(a)+nearest_ten(b)-(a+b))<=10
            assert abs(nearest_ten(a)-nearest_ten(b)-(a-b))<=10
            bound_count+=1
    report={'source_checks_passed':len(checks),'source_locations':checks,
            'parsed_lesson_practice_keys':40,'exam_forms':2,'exam_items_per_form':25,
            'column_subtraction_pairs':count,'rounding_bound_pairs':bound_count,
            'limits':'Numeric checks and agent source review; not proof of all prose, independent academic equivalence, private learner mastery or production serving.'}
    (FOLDER/'VALIDATION_17_20_REPORT.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='source_locations'},indent=2))

if __name__=='__main__':
    main()
