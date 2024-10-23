import unittest
from main import check_grammar

class TestGermanGrammarChecker(unittest.TestCase):
    
    def test_capitalization(self):
        # Test case for detecting and correcting capitalization errors
        text = "ich habe ein haus."
        mistakes, fixes = check_grammar(text)
        
        # Assert that the function identifies a capitalization error
        self.assertIn('Capitalization', mistakes)
        # Assert that 'haus' was identified as the incorrect noun
        self.assertEqual(mistakes['Capitalization'], ['haus'])
        # Assert that the suggested correction is 'Haus'
        self.assertEqual(fixes['Capitalization'], ['Haus'])

    def test_verb_conjugation(self):
        # Test case for detecting and correcting verb conjugation errors
        text = "er bin gut."
        mistakes, fixes = check_grammar(text)
        
        # Assert that the function identifies a verb conjugation error
        self.assertIn('Verb Conjugation', mistakes)
        # Assert that 'bin' was identified as incorrect
        self.assertEqual(mistakes['Verb Conjugation'], ['bin'])
        # Assert that the suggested correction is 'ist'
        self.assertEqual(fixes['Verb Conjugation'], ['ist'])

    def test_no_errors(self):
        # Test case to ensure no errors are found in a correct sentence
        text = "Ich habe ein Haus. Er ist gut."
        mistakes, fixes = check_grammar(text)
        
        # Assert that no mistakes were found in the text
        self.assertEqual(mistakes, {})
        self.assertEqual(fixes, {})

# Run the unit tests
if __name__ == '__main__':
    unittest.main()
