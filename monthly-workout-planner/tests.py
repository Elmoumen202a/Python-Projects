import unittest
from main import WorkoutPlanner

class TestWorkoutPlanner(unittest.TestCase):
    def setUp(self):
        self.planner = WorkoutPlanner()

    def test_january_workout(self):
        self.assertEqual(self.planner.suggest_workout(1), "For January, you can train: Legs, Cardio")

    def test_february_workout(self):
        self.assertEqual(self.planner.suggest_workout(2), "For February, you can train: Arms, Core")


if __name__ == "__main__":
    unittest.main()
