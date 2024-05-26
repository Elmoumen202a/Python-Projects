import unittest
from main import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_initial_location(self):
        self.assertEqual(self.game.current_location, "forest")

    def test_move(self):
        self.game.move_to("castle")
        self.assertEqual(self.game.current_location, "castle")

    def test_explore(self):
        self.game.explore()
        self.assertIn("a mystical leaf", self.game.inventory)

    def test_invalid_move(self):
        current_location = self.game.current_location
        self.game.move_to("ocean")
        self.assertEqual(self.game.current_location, current_location)

if __name__ == "__main__":
    unittest.main()
