import unittest
from main import diagnose

class TestMedicalTool(unittest.TestCase):
    def test_known_symptoms(self):
        self.assertEqual(diagnose(["fever"]), ["You might have an infection. Stay hydrated and monitor your temperature."])
        self.assertEqual(diagnose(["cough"]), ["It could be a cold or allergy. If persistent, consider seeing a doctor."])

    def test_unknown_symptoms(self):
        self.assertEqual(diagnose(["dizziness"]), ["No specific advice for dizziness. Please consult a doctor."])

    def test_multiple_symptoms(self):
        symptoms = ["fever", "headache", "unknown"]
        expected = [
            "You might have an infection. Stay hydrated and monitor your temperature.",
            "This may be due to stress or dehydration. Rest and drink water.",
            "No specific advice for unknown. Please consult a doctor."
        ]
        self.assertEqual(diagnose(symptoms), expected)

if __name__ == "__main__":
    unittest.main()
