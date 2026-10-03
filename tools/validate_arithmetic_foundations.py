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
    report={'fixture_checks_passed':len(CHECKS),'fixture_locations':CHECKS,
        'exhaustive_rounding_cases':10001,
        'limits':'Fixtures checked against authored text by source review. This script does not parse or prove every prose claim or establish independent academic validation.'}
    (ROOT/'curriculum/mathematics/arithmetic/VALIDATION_REPORT.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report))

if __name__=='__main__': main()
