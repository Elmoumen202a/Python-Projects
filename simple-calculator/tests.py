import unittest
import main

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(main.add(3, 5), 8)
    
    def test_subtract(self):
        self.assertEqual(main.subtract(10, 4), 6)
    
    def test_multiply(self):
        self.assertEqual(main.multiply(2, 3), 6)
    
    def test_divide(self):
        self.assertEqual(main.divide(10, 2), 5)
        with self.assertRaises(ValueError):
            main.divide(10, 0)

if __name__ == '__main__':
    unittest.main()
