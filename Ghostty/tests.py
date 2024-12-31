import unittest
from main import choose_room, choose_ability

class TestGhosttyGame(unittest.TestCase):
    """Test the functionality of the Ghostty game"""

    # Test if the chosen room is one of the valid rooms
    def test_choose_room(self):
        room = choose_room()
        self.assertIn(room, ["Living Room", "Kitchen", "Attic", "Basement", "Library"])

    # Test if the chosen ability is one of the valid abilities
    def test_choose_ability(self):
        ability = choose_ability()
        self.assertIn(ability, ["Telekinesis", "Scaring people", "Invisibility", "Shape-shifting"])

if __name__ == "__main__":
    unittest.main()
