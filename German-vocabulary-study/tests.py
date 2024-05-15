import unittest
from main import GermanVocabularyStudy

class TestGermanVocabularyStudy(unittest.TestCase):
    def setUp(self):
        self.vocabulary = [
            {'german': 'Haus', 'english': 'House'},
            {'german': 'Auto', 'english': 'Car'},
            {'german': 'Schule', 'english': 'School'},
        ]
        self.study_tool = GermanVocabularyStudy(self.vocabulary)

    def test_display_word(self):
        # Just checking if there are no exceptions raised
        self.study_tool.display_word()

    def test_next_word(self):
        initial_index = self.study_tool.current_index
        self.study_tool.next_word()
        new_index = self.study_tool.current_index
        self.assertNotEqual(initial_index, new_index)

if __name__ == '__main__':
    unittest.main()
