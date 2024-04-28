import unittest
from main import TodoList

class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.todo_list = TodoList()

    def test_add_task(self):
        self.todo_list.add_task("Task 1")
        self.assertEqual(self.todo_list.tasks, ["Task 1"])

    def test_remove_task(self):
        self.todo_list.add_task("Task 1")
        self.todo_list.remove_task("Task 1")
        self.assertEqual(self.todo_list.tasks, [])

    def test_is_empty(self):
        self.assertTrue(self.todo_list.is_empty())
        self.todo_list.add_task("Task 1")
        self.assertFalse(self.todo_list.is_empty())

if __name__ == "__main__":
    unittest.main()
