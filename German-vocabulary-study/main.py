import random

class GermanVocabularyStudy:
    def __init__(self, vocabulary):
        self.vocabulary = vocabulary
        self.current_index = 0

    def display_word(self):
        german_word = self.vocabulary[self.current_index]['german']
        english_translation = self.vocabulary[self.current_index]['english']
        print(f"German Word: {german_word}\nEnglish Translation: {english_translation}")

    def next_word(self):
        self.current_index = (self.current_index + 1) % len(self.vocabulary)
        self.display_word()

if __name__ == "__main__":
    vocabulary = [
        {'german': 'das Haus', 'english': 'House'},
        {'german': 'das Auto', 'english': 'Car'},
        {'german': ' die Schule', 'english': 'School'},
        # Add more words as needed
    ]

    study_tool = GermanVocabularyStudy(vocabulary)
    study_tool.display_word()
