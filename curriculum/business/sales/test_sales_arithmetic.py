# Sales validation: executable arithmetic regression
# Draft quality gate. Uses Python standard library only.
# Run: python3 curriculum/business/sales/test_sales_arithmetic.py
from decimal import Decimal
import unittest

D = Decimal

class SalesArithmetic(unittest.TestCase):
    def assertDecimal(self, actual, expected):
        self.assertEqual(actual, D(expected))

    def test_foundations_nested_cohort(self):
        inquiries, conversations, demos, purchases = map(D, ["240", "72", "24", "6"])
        self.assertDecimal(conversations / inquiries * 100, "30")
        self.assertAlmostEqual(float(demos / conversations * 100), 100 / 3, places=10)
        self.assertDecimal(purchases / demos * 100, "25")
        self.assertDecimal(purchases / inquiries * 100, "2.5")
        self.assertDecimal((conversations/inquiries)*(demos/conversations)*(purchases/demos), ".025")

    def test_prospect_segmentation(self):
        self.assertDecimal(D(320)/D(500)*100, "64")
        self.assertDecimal(D(200)/D(320)*100, "62.5")
        self.assertDecimal(D(120)/D(200)*100, "60")
        self.assertDecimal(D(120)/D(500)*100, "24")

    def test_solution_economics(self):
        self.assertDecimal(D(1800)*3, "5400")
        self.assertDecimal(D(700)*3, "2100")
        self.assertDecimal((D(1800)-D(700))*3-D(900), "2400")
        self.assertDecimal(D(2000)*3-D(1800)*3, "600")

    def test_capstone_margin(self):
        self.assertDecimal(D(2499)-D(950), "1549")
        self.assertDecimal(D(1499)-D(600), "899")
        self.assertDecimal(D(1549)+D(899)-D(1300), "1148")
        self.assertDecimal(D(2499)*D(".85"), "2124.15")
        self.assertDecimal(D("2124.15")-D(950), "1174.15")
        self.assertDecimal((D(2499)-D("2124.15"))*12, "4498.20")

    def test_pipeline(self):
        self.assertDecimal(D(12000)*D(".25")+D(24000)*D(".5")+D(18000)*D(".75"), "28500")
        self.assertDecimal((D(".04")+D(".16")+D(".49")+D(".01"))/4, ".175")

    def test_retention(self):
        start = D(50)*D(400)
        end = start-D(2000)+D(2500)-D(500)
        self.assertDecimal(end/start*100, "100")
        self.assertDecimal(D(45)/D(50)*100, "90")

    def test_practical_capstone(self):
        self.assertDecimal(D(300)*D(".18"), "54")
        self.assertDecimal(D(5)*D(75), "375")
        self.assertDecimal(D(2200)-D(850), "1350")
        self.assertDecimal(D(2200)*D(".9")-D(850), "1130")

if __name__ == "__main__":
    unittest.main()
