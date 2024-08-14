import unittest
from speed_typing_test import load_words, speed_typing_test

class TestSpeedTyping(unittest.TestCase):
    
    def test_load_words(self):
        words = load_words()
        self.assertIsInstance(words, list)
        self.assertGreater(len(words), 0)
    
    def test_speed_typing(self):
        words = ['hello', 'world', 'test', 'typing', 'speed']
        speed_typing_test(words)  # Manual testing, observe output
        
if __name__ == '__main__':
    unittest.main()
