import unittest
from main import translate_body_part, show_medication, medication_reminder
from io import StringIO
import sys

class TestMainFunctions(unittest.TestCase):

    def test_translate_body_part(self):
        # Test if known body part translates correctly
        self.assertEqual(translate_body_part("Heart"), "Heart in German is Herz")
        # Test if unknown body part returns the correct message
        self.assertEqual(translate_body_part("Unknown"), "Body part not found.")

    def test_show_medication(self):
        # Capture printed output
        output = StringIO(); sys.stdout = output
        # Test medication for a valid time (Morning)
        show_medication("Morning")
        # Check if "Aspirin" is in the output
        self.assertIn("Aspirin", output.getvalue())
        # Test medication for an invalid time (Night)
        show_medication("Night")
        # Check if the no medications message is displayed
        self.assertIn("No medications", output.getvalue())

    def test_medication_reminder(self):
        # Capture printed output
        output = StringIO(); sys.stdout = output
        # Test the reminder function for all times of the day
        medication_reminder()
        # Check if reminder for "Morning" is in the output
        self.assertIn("Reminder for Morning", output.getvalue())

if __name__ == "__main__":
    unittest.main()
