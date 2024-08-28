import unittest

class TestWordCount(unittest.TestCase):
    def test_word_count(self):
        corrected_text = """
        Liebe Nadja,

        wie geht es dir? Mir geht es gut. Ich freue mich sehr über deinen Brief. Außerdem liebe ich deinen Vorschlag. Wenn ich Lust habe, tue ich das gerne.

        Gärtnern macht mir Spaß, und wir könnten uns mal treffen. Also, du weißt, dass ich den Garten mag. Könntest du mir bitte sagen, ob der Garten in der Nähe ist? Ich habe mich gefragt, ob es möglich ist, Blumen und Gemüse im Garten zu haben.

        Diese Tage habe ich eine neue Nachricht: Ich bereite mich auf die Deutschprüfung (Zertifikat B1) vor, die am Montag um 08:00 Uhr stattfindet. Danach plane ich, eine Ausbildung zur Informatikerin in Deutschland zu machen. Ich werde mich sehr freuen, wenn wir uns bald treffen und ich deinen schönen Garten sehe.

        Bis bald!

        Liebe Grüße
        Youssef
        """
        expected_count = 175  # Adjust the expected count as necessary
        self.assertEqual(len(corrected_text.split()), expected_count)

if __name__ == '__main__':
    unittest.main()
