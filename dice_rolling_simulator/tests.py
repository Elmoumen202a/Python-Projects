import unittest
from main import Dice

# Unit test class for the Dice class
class TestDice(unittest.TestCase):
    def test_roll(self):
        # Create a standard 6-sided dice
        dice = Dice()
        # Roll the dice 
        roll_result = dice.roll() 
        # Check if the result is between 1 and 6 
        self.assertIn(roll_result, range(1, 7))  

    def test_custom_sides(self):
        # Custom number of sides
        sides = 10  
        # Create a dice with 10 sides
        dice = Dice(sides)
         # Roll the dice  
        roll_result = dice.roll() 
        # Check if the result is between 1 and 10
        self.assertIn(roll_result, range(1, sides + 1))  

# Entry point of the test script
if __name__ == "__main__":
    unittest.main()
