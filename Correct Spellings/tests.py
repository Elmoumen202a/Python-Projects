from CorrectSpellings import checker
from spellchecker import SpellChecker

def test_checker():
    spell_checker = SpellChecker()
    result = checker(spell_checker, "word")

    # Check if the word is correct
    if result == "It is correct":
        assert result == "It is correct"
    else:
        # If the word is incorrect, check if the corrected spelling is returned
        assert result.startswith("Correct Spelling of the word is:")


