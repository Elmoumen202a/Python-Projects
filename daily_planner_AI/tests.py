import unittest
from main import DailyPlannerAI

class TestDailyPlannerAI(unittest.TestCase):
    def setUp(self):
        """Set up a test planner instance before each test"""
        self.planner = DailyPlannerAI()
        self.planner.add_task("Write report", "high", 120)
        self.planner.add_task("Check emails", "medium", 30)
        self.planner.add_task("Team meeting", "high", 60)
        self.planner.add_task("Exercise", "low", 45)

    def test_add_task(self):
        """Test if a task is added correctly"""
        self.planner.add_task("Test task", "low", 15)
        self.assertEqual(len(self.planner.tasks), 5)
        self.assertEqual(self.planner.tasks[-1]['task_name'], "Test task")

    def test_daily_plan(self):
        """Test if the daily plan is generated correctly"""
        daily_plan = self.planner.get_daily_plan(180)
        self.assertEqual(len(daily_plan), 3)  # Should return 3 tasks that fit within 180 minutes
        self.assertEqual(daily_plan[0]['task_name'], "Team meeting")  # High priority, short duration first

    def test_not_enough_time(self):
        """Test if the planner skips tasks that do not fit in available time"""
        daily_plan = self.planner.get_daily_plan(60)
        self.assertEqual(len(daily_plan), 1)  # Only one task fits in 60 minutes
        self.assertEqual(daily_plan[0]['task_name'], "Team meeting")

if __name__ == "__main__":
    unittest.main()
