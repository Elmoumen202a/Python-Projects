import unittest
from main import add_note, view_notes

class TestNoteTakingApp(unittest.TestCase):

    def test_add_note(self):
        add_note()
        with open("notes.txt", "r") as file:
            notes = file.read()
            self.assertIn("Test Note", notes)

    def test_view_notes(self):
        view_notes()  # Just testing if the function runs without errors

if __name__ == "__main__":
    unittest.main()
