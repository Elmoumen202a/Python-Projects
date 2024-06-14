import unittest
from exam_utils import read_exam_file, check_mistakes, calculate_score

class TestExamUtils(unittest.TestCase):

    def setUp(self):
        """
        Set up the necessary variables for the tests.
        This method is called before each test.
        """
        self.answers_key = {
            "Q1": "A",
            "Q2": "B",
            "Q3": "C",
            "Q4": "D",
            "Q5": "A",
        }
        self.answers = read_exam_file("filled_exam.doc")

    def test_read_exam_file(self):
        """
        Test the read_exam_file function to ensure it returns the correct answers.
        """
        self.assertEqual(self.answers, {
            "Q1": "A",
            "Q2": "C",
            "Q3": "C",
            "Q4": "D",
            "Q5": "B",
        })

    def test_check_mistakes(self):
        """
        Test the check_mistakes function to ensure it identifies mistakes correctly.
        """
        mistakes = check_mistakes(self.answers, self.answers_key)
        self.assertEqual(mistakes, {
            "Q2": "C",
            "Q5": "B",
        })

    def test_calculate_score(self):
        """
        Test the calculate_score function to ensure it calculates the score correctly.
        """
        score = calculate_score(self.answers, self.answers_key)
        self.assertEqual(score, 3)

if __name__ == "__main__":
    unittest.main()
