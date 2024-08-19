import unittest
from main import Lesson, Quiz, ELearningPlatform

class TestELearningPlatform(unittest.TestCase):
    
    def test_lesson_display(self):
        # Test if the lesson object is initialized correctly
        lesson = Lesson("Test Lesson", "This is a test.")
        self.assertEqual(lesson.title, "Test Lesson")
        self.assertEqual(lesson.content, "This is a test.")
    
    def test_quiz_correct(self):
        # Test if the quiz returns True for a correct answer
        quiz = Quiz("What is 1 + 1?", "2")
        # Simulate correct answer
        with unittest.mock.patch('builtins.input', return_value='2'):
            self.assertTrue(quiz.take_quiz())
    
    def test_quiz_incorrect(self):
        # Test if the quiz returns False for an incorrect answer
        quiz = Quiz("What is 1 + 1?", "2")
        # Simulate incorrect answer
        with unittest.mock.patch('builtins.input', return_value='3'):
            self.assertFalse(quiz.take_quiz())

    def test_adding_lesson_to_platform(self):
        # Test if a lesson can be added to the platform
        platform = ELearningPlatform()
        lesson = Lesson("Test Lesson", "This is a test.")
        platform.add_lesson(lesson)
        self.assertIn(lesson, platform.lessons)

    def test_adding_quiz_to_platform(self):
        # Test if a quiz can be added to the platform
        platform = ELearningPlatform()
        quiz = Quiz("Test Question", "Test Answer")
        platform.add_quiz(quiz)
        self.assertIn(quiz, platform.quizzes)

    def test_platform_start(self):
        # Test the full platform flow with lessons and quizzes
        platform = ELearningPlatform()
        lesson = Lesson("Test Lesson", "This is a test lesson.")
        quiz = Quiz("What is 1 + 1?", "2")

        platform.add_lesson(lesson)
        platform.add_quiz(quiz)
        
        with unittest.mock.patch('builtins.input', return_value='2'):
            # Capture the printed output using unittest's patch on 'print'
            with unittest.mock.patch('builtins.print') as mocked_print:
                platform.start()
                # Verify if the platform's start method outputs the correct lesson and quiz results
                mocked_print.assert_any_call("\nLesson: Test Lesson\nThis is a test lesson.\n")
                mocked_print.assert_any_call("\nYour score: 1/1")

if __name__ == '__main__':
    unittest.main()
