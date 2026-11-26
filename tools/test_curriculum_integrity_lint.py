"""Regression cases for the two observed false positives; retain real warnings."""
import unittest
from curriculum_integrity_lint import find_issues

class IntegrityTests(unittest.TestCase):
    def test_poincare_resolved_adjacent_open_problem(self):
        self.assertNotIn('resolved_poincare_marked_open', find_issues(
            'The Poincaré conjecture is resolved through Perelman. The Hodge conjecture remains open.', 'geometry.md'))

    def test_open_heading_does_not_reclassify_next_sentence(self):
        self.assertNotIn('resolved_poincare_marked_open', find_issues(
            'Open questions concern Hodge. The Poincaré conjecture is resolved.', 'geometry.md'))

    def test_poincare_still_open_warns(self):
        for text in ['The Poincaré conjecture remains open.',
                     'The Poincare conjecture still remains an open problem.',
                     'Open questions include the Poincaré conjecture (resolved by Perelman).']:
            with self.subTest(text=text):
                self.assertIn('resolved_poincare_marked_open', find_issues(text, 'geometry.md'))

    def test_rans_closure_limitation(self):
        text = ('The Reynolds-Averaged Navier-Stokes (RANS) equations are employed for turbulent flow modeling, '
                'and are commonly used for aerodynamic performance prediction. Their failure mode is often '
                'associated with turbulence modeling and near-wall treatment.')
        self.assertNotIn('navier_stokes_turbulence_breakdown', find_issues(text, 'aerospace_engineering.md'))
        # A valid RANS passage must not suppress a separate invalid statement.
        self.assertIn('navier_stokes_turbulence_breakdown', find_issues(
            text+' Navier-Stokes equations have a breakdown whenever turbulence occurs.', 'aerospace_engineering.md'))

    def test_direct_breakdown_warns(self):
        self.assertIn('navier_stokes_turbulence_breakdown', find_issues(
            'Navier-Stokes equations have a failure mode in turbulent flow.', 'fluid_mechanics.md'))

    def test_foundational_scope(self):
        self.assertIn('frontier_problem_misclassified_in_foundational_course', find_issues(
            'Open questions in arithmetic include the Riemann hypothesis.', 'arithmetic.md'))
        self.assertNotIn('frontier_problem_misclassified_in_foundational_course', find_issues(
            'Downstream analytic number theory investigates the Riemann hypothesis.', 'arithmetic.md'))

    def test_other_rules_retained(self):
        self.assertIn('resolved_geometrization_marked_open', find_issues(
            'The geometrization conjecture remains open.', 'topology.md'))
        self.assertIn('resolved_erdos_discrepancy_marked_open', find_issues(
            'Open questions include the Erdős discrepancy problem.', 'number_theory.md'))

if __name__ == '__main__':
    unittest.main()
