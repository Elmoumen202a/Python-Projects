import unittest
from main import grade_quiz

class TestQuizGrader(unittest.TestCase):
    def test_grade_quiz(self):
        answers = ['A', 'B', 'C', 'D', 'A']
        answer_key = ['A', 'B', 'C', 'D', 'A']
        self.assertEqual(grade_quiz(answers, answer_key), 5)

if __name__ == '__main__':
    unittest.main()
