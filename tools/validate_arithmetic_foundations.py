"""Exact checks for published Arithmetic examples/keys, not a curriculum proof.

Fractions avoid binary floating point in decimal/tie examples. Every fixture has
an explicit source location so it can be reviewed against prose. Source review
must also check explanations, assumptions, units, prerequisites and omitted cases.
"""
from fractions import Fraction as F
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]
CHECKS=[]
def check(source,actual,expected):
    if actual != expected:
        raise AssertionError(f'{source}: {actual!r} != {expected!r}')
    CHECKS.append(source)

def nearest(value,unit):
    """Exact nonnegative nearest; ties upward, per Lesson 8."""
    value,unit=F(str(value)),F(str(unit))
    assert value>=0 and unit>0
    lower=(value//unit)*unit
    return lower if value-lower < unit/2 else lower+unit

def main():
    for label,actual,expected in [
        ('L6 E2',-8 < -3,True),('L6 E3',abs(-4),4),
        ('L6 E4',-2+3,1),('L6 E5',abs(4-(-3)),7),
        ('L6 E6',4*0,0),('L6 P2',sorted([-6,2,0,-1,5]),[-6,-1,0,2,5]),
        ('L6 P3',-9 < -4,True),('L6 P4',abs(-8),8),
        ('L6 P5',-3,-3),('L6 P6',-3+4,1),('L6 P7',abs(-7-(-2)),5),
        ('L6 P9',0//5,0),('L6 P10',2-(-4),6),
        ('L6 Q2',-12 < -2,True),('L6 Q3',abs(-6),6),('L6 Q4',-1+2,1),
        ('L6 R1',-11 < -3,True),('L6 R2',abs(-10),10),
        ('L7 E1',abs(50-47),3),('L7 E2 bounds',(7*10+1,7*10+9),(71,79)),
        ('L7 E3',198+203,401),('L7 E4',3*19,57),
        ('L7 G3',abs(30-34),4),('L7 P2',4*20,80),
        ('L7 P3',(5*10+1,5*10+9),(51,59)),('L7 P5',abs(70-66),4),
        ('L7 P6',[x for x in [44,46,51,52] if abs(x-48)<=3],[46,51]),
        ('L7 P7',302+197,499),('L7 Q2',3*100,300),
        ('L7 Q4',abs(85-81),4),('L7 R1',5*10,50),('L7 R3',abs(40-43),3)]:
        check(label,actual,expected)
    for label,value,unit,expected in [
        ('L8 E1',3476,10,3480),('L8 E2',3476,100,3500),('L8 E3',650,100,700),
        ('L8 E4','4.372','.01','4.37'),('L8 E5','9.96','.1',10),
        ('L8 E6',9995,10,10000),('L8 E7','2.449','.1','2.4'),
        ('L8 E8',241,10,240),('L8 G1',83,10,80),('L8 G2',1250,100,1300),
        ('L8 G3','6.08','.1','6.1'),('L8 G4',748,100,700),
        ('L8 P1',146,10,150),('L8 P2',146,100,100),('L8 P3',2349,100,2300),
        ('L8 P4',2350,100,2400),('L8 P5','.864','.01','.86'),
        ('L8 P6','7.05','.1','7.1'),('L8 P7','99.95','.1',100),
        ('L8 P8','3.449','.1','3.4'),('L8 P9',371,100,400),
        ('L8 P9 counterexample',341,100,300),('L8 P10',560,100,600),
        ('L8 applied A','18.46','.1','18.5'),('L8 applied B','18.44','.1','18.4'),
        ('L8 applied C','18.41','.1','18.4'),('L8 diagnosis A','.049','.01','.05'),
        ('L8 diagnosis B',4999,1000,5000),('L8 Q1',275,10,280),
        ('L8 Q2',1949,100,1900),('L8 Q3','3.995','.01',4),
        ('L8 R1',685,100,700),('L8 R2','.095','.01','.10')]:
        check(label,nearest(value,unit),F(str(expected)))
    check('L8 E7 double rounding',nearest(nearest('2.449','.01'),'.1'),F('2.5'))
    check('L8 P8 double rounding',nearest(nearest('3.449','.01'),'.1'),F('3.5'))
    for label,count,unit,expected in [('L8 E8 capacity',241,10,250),('L8 P9 capacity',371,100,400),('L8 Q5',204,10,210),('L8 R3',301,100,400)]:
        check(label,((count+unit-1)//unit)*unit,expected)
    # Exhaustively verify nearestness and tie behavior on integer hundredths.
    for cents in range(0,10001):
        value=F(cents,100);result=nearest(value,'.1')
        assert abs(result-value)<=F('0.05')
        assert result/F('.1') == int(result/F('.1'))
        assert nearest(result,'.1') == result
    check('nearest exhaustive nonnegative hundredths',10001,10001)
    for label,actual,expected in [
        ('L9 E2 domain', [n for n in range(14) if n<=12], list(range(13))),
        ('L9 E4',abs(3-(-2)),5),('L9 E5 false link',3+4 == 7+2,False),
        ('L9 G2',[n for n in range(7) if 2<=n<5],[2,3,4]),
        ('L9 P3',min(n for n in range(20) if n>7),8),
        ('L9 P4',[n for n in range(10) if 3<=n<7],[3,4,5,6]),
        ('L9 P5',1 > -4,True),('L9 P7 false link',5+1 == 6+3,False),
        ('L9 P10 inclusive',list(range(10,16)),[10,11,12,13,14,15]),
        ('L9 P10 strict',list(range(11,15)),[11,12,13,14]),
        ('L9 Q2',[n for n in range(7) if 1<n<=4],[2,3,4]),
        ('L9 R2',[n for n in range(8) if 2<n<6],[3,4,5]),
        ('L10 E1',6*10+4,64),('L10 E2',2-(-3),5),
        ('L10 E4 compare',F('4.096')>F('4.09'),True),
        ('L10 E5 boundary',[n>=30 for n in [29,30,31]],[False,True,True]),
        ('L10 G1',700+8,708),('L10 G2',abs(-6-(-1)),5),
        ('L10 P1 marks/gaps',(len(range(9)),8-0),(9,8)),
        ('L10 P2',60000+200+4,60204),('L10 P3',F('.507')<F('.57'),True),
        ('L10 P4',sorted([5,-3,0,-8,2]),[-8,-3,0,2,5]),
        ('L10 P5',abs(3-(-4)),7),('L10 P7',min(c for c in [100,150,200] if c>=151),200),
        ('L10 P8',[n for n in range(10) if 4<n<=8],[5,6,7,8]),
        ('L10 AI audit',(len(range(-3,4)),3-(-3)),(7,6)),
        ('L10 Q1',(len(range(-2,3)),2-(-2)),(5,4)),
        ('L10 Q2',6*1000,6000),('L10 Q3',-2 > -7,True),
        ('L10 R1',(len(range(-4,2)),1-(-4)),(6,5)),
        ('L10 R2',5*10000,50000),('L10 R4',[n for n in range(7) if 2<=n<5],[2,3,4]),
        ('Exam A1',8,8),('Exam A3',12,12),('Exam A4',len(range(10)),10),
        ('Exam A6',40000+500+7,40507),('Exam A7',8*1000,8000),
        ('Exam A8',F('3.40')==F('3.4') and F('3.04')!=F('3.4'),True),
        ('Exam A9',45901<45910,True),('Exam A10',F('.507')<F('.57'),True),
        ('Exam A11',sorted([-2,4,-7,0,3]),[-7,-2,0,3,4]),
        ('Exam A12',abs(-6),6),('Exam A13',abs(4-(-3)),7),
        ('Exam A14',4*20,80),('Exam A15',(7*10+1,7*10+9),(71,79)),
        ('Exam A16',(80>=79,75>=79),(True,False)),('Exam A17',(abs(50-47),50>47),(3,True)),
        ('Exam A23',[n for n in range(8) if 2<=n<5],[2,3,4]),
        ('Exam A24',(3+4,7+2),(7,9)),
        ('Exam B1',10,10),('Exam B3',17,17),('Exam B4',len(range(13)),13),
        ('Exam B6',70000+300+6,70306),('Exam B7',6*1000,6000),
        ('Exam B8',F('2.50')==F('2.5') and F('2.05')!=F('2.5'),True),
        ('Exam B9',62809<62890,True),('Exam B10',F('.406')<F('.46'),True),
        ('Exam B11',sorted([-5,1,-9,0,6]),[-9,-5,0,1,6]),
        ('Exam B12',abs(-8),8),('Exam B13',abs(5-(-4)),9),
        ('Exam B14',3*30,90),('Exam B15',(6*10+1,6*10+9),(61,69)),
        ('Exam B16',(70>=69,65>=69),(True,False)),('Exam B17',(abs(60-64),60<64),(4,True)),
        ('Exam B23',[n for n in range(9) if 3<n<=6],[4,5,6]),
        ('Exam B24',(2+5,7+1),(7,8))]:
        check(label,actual,expected)
    for label,value,unit,expected in [
        ('L10 E1 rounding',64,10,60),('L10 E4 rounding','4.096','.01','4.10'),
        ('L10 G3',95,10,100),('L10 G3 counterexample',91,10,90),
        ('L10 P6 tens',1995,10,2000),('L10 P6 hundreds',1995,100,2000),
        ('L10 Q4','8.995','.01',9),('L10 R3','7.995','.01',8),
        ('Exam A18 tens',3476,10,3480),('Exam A18 hundreds',3476,100,3500),
        ('Exam A19',650,100,700),('Exam A20','9.96','.1',10),
        ('Exam B18 tens',5683,10,5680),('Exam B18 hundreds',5683,100,5700),
        ('Exam B19',750,100,800),('Exam B20','8.97','.1',9)]:
        check(label,nearest(value,unit),F(str(expected)))
    check('Exam A21 covering capacity',((241+9)//10)*10,250)
    check('Exam B21 covering capacity',((321+9)//10)*10,330)
    check('Exam A21 nearest',nearest(241,10),240)
    check('Exam B21 nearest',nearest(321,10),320)
    # Numerical answers in the linked foundation companions.
    for label,actual,expected in [
        ('L1 P1 count',6,6),('L1 P4',8,8),('L1 P5',7+1,8),('L1 P6',7-1,6),
        ('L1 P7',len(range(5)),5),('L1 P9',6>4,True),('L1 Q1',5,5),
        ('L1 R labels',len(range(7)),7),('L2 P2 digits',len(str(508)),3),
        ('L2 P8 equality',4+5,9),('L2 P9 blank',4+2-1,5),
        ('L2 P10 invalid link',2+3==5+1,False),('L2 Q2',len(range(10)),10),
        ('L2 Q3',3+4,7),('L2 Q4',2+3-1,4),('L2 R blank',3+3-2,4),
        ('L3 P1',2000+400+7,2407),('L3 P2',5000+60+2,5062),
        ('L3 P3',8*1000,8000),('L3 P4',8*F('.01'),F('.08')),
        ('L3 P6',72000+46,72046),('L3 P7',F('4.30')==F('4.3'),True),
        ('L3 P8',5000+400+20+9,5429),('L3 P9',200+4,204),
        ('L3 P10',12*10+5,125),('L3 Q1',3000+200+8,3208),
        ('L3 Q2',600+5,605),('L3 Q3',9*F('.01'),F('.09')),
        ('L3 Q4',F('7.20')==F('7.2'),True),('L3 Q5',207!=27,True),
        ('L3 R1',4000+9,4009),('L3 R2',80000+20+3,80023),
        ('L3 R3',6*F('.01'),F('.06')),('L4 P1',9099<9100,True),
        ('L4 P2',305<350,True),('L4 P3',F('.407')<F('.47'),True),
        ('L4 P4',F('6.20')==F('6.2'),True),('L4 P5',sorted([18,8,80,108]),[8,18,80,108]),
        ('L4 P6',sorted([-2,-6,3,0]),[-6,-2,0,3]),('L4 P7',1<4,True),
        ('L4 P8',F('.09')<F('.9'),True),('L4 P9',[n>10 for n in [9,10,11]],[False,False,True]),
        ('L4 diagnosis',F('.8')>F('.75'),True),('L4 Q1',4901<4910,True),
        ('L4 Q2',F('.305')<F('.35'),True),('L4 Q3',F('8.00')==8,True),
        ('L4 Q4',sorted([-3,1,-8,0]),[-8,-3,0,1]),('L4 Q5',2<7,True),
        ('L4 R1',6087>6078,True),('L4 R2',F('.606')<F('.66'),True),
        ('L4 R3',sorted([-1,-5,2]),[-5,-1,2]),
        ('L5 P1',(len(range(6)),5),(6,5)),('L5 P2',sorted([-3,0,2]),[-3,0,2]),
        ('L5 P3',abs(4-(-2)),6),('L5 P4',abs(-5),5),('L5 P5',2+3,5),
        ('L5 P6',3-5,-2),('L5 P7',(3,3*5),(3,15)),('L5 P9',8-0,8),
        ('L5 P10 direct',abs(2-(-1)),3),('L5 P10 detour',1+4,5),
        ('L5 Q1',(len(range(5)),4),(5,4)),('L5 Q2',abs(2-(-3)),5),
        ('L5 Q3',abs(-7),7),('L5 Q4',2*4,8),('L5 Q5',-2+3,1),
        ('L5 R1',(len(range(-2,4)),3-(-2)),(6,5)),('L5 R2',abs(4-(-1)),5),
        ('L5 R3',2*5,10)]:
        check(label,actual,expected)
    # Published addition facts and their independent answer values.
    groups = {
        'L11 examples':[(4,3,7),(8,5,13),(6,0,6),(2,7,9)],
        'L11 guided':[(5,2,7),(9,0,9),(3,4,7),(8,3,11)],
        'L11 practice':[(4,5,9),(7,3,10),(6,4,10),(8,2,10),(0,9,9),(3,8,11)],
        'L11 quiz':[(6,4,10),(7,0,7),(2,9,11),(8,3,11)],
        'L11 reassessment':[(5,4,9),(0,8,8)],
        'L12 examples':[(3,9,12),(0,7,7),(6,6,12),(7,8,15),(9,6,15),(8,5,13),(4,6,10),(5,6,11)],
        'L12 guided':[(4,9,13),(5,6,11),(7,6,13),(8,7,15)],
        'L12 practice':[(9,4,13),(6,6,12),(6,7,13),(8,6,14),(7,5,12),(0,9,9),(5,9,14),(3,9,12),(4,10,14),(8,5,13),(7,8,15)],
        'L12 applied':[(8,7,15),(8,9,17)],
        'L12 quiz':[(9,5,14),(7,7,14),(7,8,15),(8,4,12),(6,7,13)],
        'L12 reassessment':[(9,7,16),(8,8,16),(8,9,17),(7,6,13)],
        'L13 examples':[(27,15,42),(234,152,386),(247,135,382),(586,279,865),(4706,85,4791),(9999,1,10000),(1208,375,1583),(1583,46,1629),(375,46,421)],
        'L13 guided':[(36,48,84),(305,27,332),(698,7,705)],
        'L13 practice':[(213,145,358),(268,157,425),(509,86,595),(786,459,1245),(4008,75,4083),(999,9,1008),(12345,6789,19134),(1007,98,1105)],
        'L13 application':[(499,501,1000),(405,720,1125),(405,72,477),(58,67,125)],
        'L13 quiz':[(324,152,476),(487,268,755),(2009,96,2105),(9999,2,10001)],
        'L13 reassessment':[(356,178,534),(5007,84,5091),(8999,3,9002)]}
    for source,fixtures in groups.items():
        for a,b,answer in fixtures:
            check(f'{source}: {a}+{b}',a+b,answer)
    for label,values,answer in [
        ('L11 E5',[2,3,4],9),('L11 P7',[1,4,5],10),
        ('L11 P9 distinct',[3,1,2],6),('L12 A1',[9,6,4],19),
        ('L13 E6',[468,257,389],1114),('L13 P7',[587,246,398],1231),
        ('L13 P9',[1475,286,39],1800),('L13 A1',[198,203,97],498),
        ('L13 R4',[279,386,458],1123)]:
        check(label,sum(values),answer)
    # Parse all ten Lesson 13 independent problems against their published keys.
    # This catches edits to either a numeric prompt or its first answer numeral.
    import re
    lesson=(ROOT/'curriculum/mathematics/arithmetic/lesson_13_multi_digit_addition.md').read_text()
    prompts=lesson.split('## Independent problem set and explanatory key')[1].split('Solutions:')[0]
    answers=lesson.split('Solutions:')[1].split('## Applied reasoning')[0]
    for n in range(1,11):
        question=re.search(rf'^P{n}\. (.+)$',prompts,re.M).group(1)
        expected=int(re.search(rf'^P{n}\. (?:Correct )?([\d,]+)',answers,re.M).group(1).replace(',',''))
        if n==9:
            numbers=[1475,286,39]
        elif n==10:
            numbers=[1007,98]
        else:
            numbers=[int(x.replace(',','')) for x in re.findall(r'\d[\d,]*',question)]
        check(f'Parsed Lesson 13 P{n} key',sum(numbers),expected)
    def column_add(values):
        # Independent implementation of the taught digit/carry specification.
        digits=[list(reversed(str(v))) for v in values]
        result=[];carry=0
        for position in range(max(map(len,digits))):
            total=carry+sum(int(d[position]) if position<len(d) else 0 for d in digits)
            carry,remainder=divmod(total,10);result.append(str(remainder))
        while carry:
            carry,remainder=divmod(carry,10);result.append(str(remainder))
        return int(''.join(reversed(result)))
    for a in range(100):
        for b in range(100):
            assert column_add([a,b])==a+b
    for a,b,c in [(468,257,389),(587,246,398),(279,386,458),(999,999,999),(0,0,0)]:
        check(f'Column algorithm {a}+{b}+{c}',column_add([a,b,c]),a+b+c)
    check('Fact table all 100 entries',all(a+b==b+a for a in range(10) for b in range(10)),True)
    report={'fixture_checks_passed':len(CHECKS),'fixture_locations':CHECKS,
        'exhaustive_rounding_cases':10001,'exhaustive_two_addend_cases':10000,'fact_table_pairs':100,
        'limits':'Fixtures checked against authored text by source review. This script does not parse or prove every prose claim or establish independent academic validation.'}
    (ROOT/'curriculum/mathematics/arithmetic/VALIDATION_REPORT.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report))

if __name__=='__main__': main()
