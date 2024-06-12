import unittest
from main import GradeCalculator

class TestGradeCalculator(unittest.TestCase):
    def test_add_score(self):
        calc = GradeCalculator()
        # Test adding a valid score
        calc.add_score(85)
        self.assertEqual(calc.scores, [85])
        # Test adding an invalid score
        with self.assertRaises(ValueError):
            calc.add_score(105)

    def test_calculate_average(self):
        calc = GradeCalculator()
        # Add scores and test average calculation
        calc.add_score(85)
        calc.add_score(95)
        self.assertAlmostEqual(calc.calculate_average(), 90)
        # Test calculating average with no scores
        with self.assertRaises(ValueError):
            GradeCalculator().calculate_average()

    def test_determine_grade(self):
        calc = GradeCalculator()
        # Test grade determination for various averages
        calc.add_score(85)
        calc.add_score(95)
        self.assertEqual(calc.determine_grade(), 'A')
        calc = GradeCalculator()
        calc.add_score(75)
        calc.add_score(70)
        self.assertEqual(calc.determine_grade(), 'C')
        calc = GradeCalculator()
        calc.add_score(55)
        self.assertEqual(calc.determine_grade(), 'F')

if __name__ == "__main__":
    unittest.main()
