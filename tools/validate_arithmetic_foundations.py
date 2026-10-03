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
    report={'fixture_checks_passed':len(CHECKS),'fixture_locations':CHECKS,
        'exhaustive_rounding_cases':10001,
        'limits':'Fixtures checked against authored text by source review. This script does not parse or prove every prose claim or establish independent academic validation.'}
    (ROOT/'curriculum/mathematics/arithmetic/VALIDATION_REPORT.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report))

if __name__=='__main__': main()
