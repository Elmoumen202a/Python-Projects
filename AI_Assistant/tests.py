import unittest
from main import AIAssistant

class TestAIAssistant(unittest.TestCase):
    def setUp(self):
        self.assistant = AIAssistant()

    def test_add_task(self):
        response = self.assistant.add_task("Test task")
        self.assertEqual(response, "Task 'Test task' added successfully.")

    def test_show_tasks(self):
        self.assistant.add_task("Test task")
        tasks = self.assistant.show_tasks()
        self.assertEqual(tasks, "Test task")

    def test_set_reminder_valid(self):
        response = self.assistant.set_reminder("Test task", "2024-10-10 14:00")
        self.assertIn("Reminder set for 'Test task'", response)

    def test_set_reminder_invalid(self):
        response = self.assistant.set_reminder("Test task", "invalid date")
        self.assertEqual(response, "Invalid time format. Use 'YYYY-MM-DD HH:MM'.")

    def test_answer_question(self):
        response = self.assistant.answer_question("What is your name?")
        self.assertEqual(response, "I am your AI Assistant.")

if __name__ == "__main__":
    unittest.main()
