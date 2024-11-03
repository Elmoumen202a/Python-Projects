# tests.py

import unittest
from farm import Farm

class TestFarm(unittest.TestCase):
    def setUp(self):
        # Set up a Farm instance for testing
        self.farm = Farm()

    def test_add_animal(self):
        # Test adding animals
        self.farm.add_animal("cow", 5)
        self.assertEqual(self.farm.animals["cow"], 5)
        self.farm.add_animal("cow", 3)
        self.assertEqual(self.farm.animals["cow"], 8)

    def test_add_crop(self):
        # Test adding crops
        self.farm.add_crop("corn", 10.0)
        self.assertEqual(self.farm.crops["corn"], 10.0)

    def test_total_animals(self):
        # Test total animal count
        self.farm.add_animal("cow", 5)
        self.farm.add_animal("chicken", 10)
        self.assertEqual(self.farm.total_animals(), 15)

    def test_total_area(self):
        # Test total crop area
        self.farm.add_crop("wheat", 5.5)
        self.farm.add_crop("corn", 3.0)
        self.assertAlmostEqual(self.farm.total_area(), 8.5)

if __name__ == "__main__":
    unittest.main()
