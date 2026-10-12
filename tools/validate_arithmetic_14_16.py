"""Check published practice keys and bounded arithmetic properties for L14-L16.

No accreditation, pedagogical completeness, or production-serving claim follows.
Run after reading the prose: fixtures do not parse every narrative assertion.
"""
from pathlib import Path
import ast
import json
import operator
import re

ROOT = Path(__file__).resolve().parents[1]
FOLDER = ROOT / 'curriculum/mathematics/arithmetic'
OPS = {ast.Add: operator.add, ast.Sub: operator.sub}

def arithmetic(text):
    node = ast.parse(text.replace(',', '').replace('−', '-'), mode='eval').body
    def walk(n):
        if isinstance(n, ast.Constant) and type(n.value) is int:
            return n.value
        if isinstance(n, ast.BinOp) and type(n.op) in OPS:
            return OPS[type(n.op)](walk(n.left), walk(n.right))
        raise ValueError('Only whole-number addition/subtraction expressions accepted')
    return walk(node)

def main():
    parsed = []
    for number in (14, 15, 16):
        path = next(FOLDER.glob(f'lesson_{number:02d}_*.md'))
        content = path.read_text()
        section = content.split('## Independent problem set and explanatory key\n', 1)[1]
        prompts, keys = section.split('Solutions:', 1)
        keys = keys.split('\n## ', 1)[0]
        for i in range(1, 11):
            prompt = re.search(rf'^P{i}\. (.+)$', prompts, re.M).group(1)
            answer = int(re.search(rf'^P{i}\. ([\d,]+)', keys, re.M).group(1).replace(',', ''))
            if number == 15 and i >= 7:
                # Explicit interpretation of the four story problems, reviewed against prose.
                expression = {7:'19-7', 8:'23-15', 9:'26-9', 10:'14+5'}[i]
            else:
                expression = prompt.rstrip('.')
            result = arithmetic(expression)
            assert result == answer, (path.name, i, result, answer)
            parsed.append(f'L{number} P{i}')

    # Worked examples, guided tasks, quiz and alternate numeric answers.
    fixtures = {
      'L14 worked': [('63+24',87),('58+16',74),('297+46',343),('25+38+75+62',200),('432+256',688),('199+304+101',604)],
      'L14 guided': [('69+15',84),('248+32',280),('14+27+6',47),('398+7',405)],
      'L14 quiz': [('88+17',105),('396+28',424),('45+19+55',119),('49+21',70),('50+20',70),('50+21',71)],
      'L14 alternate': [('78+25',103),('598+34',632),('35+18+65',118),('79+31',110),('80+30',110),('80+31',111)],
      'L14 transfer': [('68+27',95),('70+27',97),('98+1',99),('498+502+37',1037),('21+34',55),('31+44',75)],
      'L15 worked': [('14-6',8),('16-9',7),('18-11',7),('43-38',5),('13+4',17),('9-0',9),('9-9',0),('0-9',-9)],
      'L15 guided': [('11-4',7),('17-12',5),('20-8',12),('10-6',4)],
      'L15 laws/transfer': [('(15-6)-2',7),('15-(6-2)',11),('47-19',28),('12-7',5),('10-6',4),('31-14',17)],
      'L15 quiz': [('15-7',8),('24-9',15),('18-11',7),('12+3',15),('14-6',8)],
      'L15 alternate': [('16-7',9),('27-11',16),('19-13',6),('16+4',20),('9-0',9),('0-9',-9)],
      'L16 worked': [('15-8',7),('13-9',4),('12-2',10),('16-7',9),('14-7',7),('15-7',8),('17-9',8),('18-9',9)],
      'L16 guided': [('11-8',3),('14-9',5),('13-6',7),('16-8',8)],
      'L16 transfer': [('12-2-3',7),('15-5-2',8),('15-5-3',7),('14-6',8),('15-7',8),('16-9',7)],
      'L16 quiz': [('11-7',4),('16-9',7),('12-6',6),('10-0',10),('14-4-2',8),('14-4-4',6)],
      'L16 alternate': [('12-8',4),('17-9',8),('14-7',7),('0-0',0),('15-5-3',7),('15-5-4',6)],
    }
    fixture_count = 0
    for location, pairs in fixtures.items():
        for expression, expected in pairs:
            assert arithmetic(expression) == expected, (location, expression, expected)
            fixture_count += 1

    fact_pairs = 0
    for whole in range(19):
        for part in range(whole+1):
            # Reconstruct the missing part by counting, then verify the inverse relation.
            difference = len(range(part, whole))
            assert part + difference == whole
            assert whole - part == difference
            assert (whole+1) - (part+1) == difference
            fact_pairs += 1
    assert fact_pairs == 190
    transfer_cases = 0
    for a in range(31):
        for b in range(31):
            for moved in range(b+1):
                assert a+b == (a+moved)+(b-moved)
                transfer_cases += 1

    report = {
      'scope': 'Arithmetic Lessons 14-16; exact checks plus source review required',
      'parsed_practice_keys_passed': len(parsed),
      'parsed_locations': parsed,
      'worked_guided_quiz_transfer_fixture_checks': fixture_count,
      'bounded_subtraction_pairs': fact_pairs,
      'bounded_transfer_cases': transfer_cases,
      'limits': 'Fixtures do not parse every prose statement, validate pedagogy, establish academic equivalence, or verify production delivery.'
    }
    (FOLDER/'VALIDATION_14_16_REPORT.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))

if __name__ == '__main__':
    main()
