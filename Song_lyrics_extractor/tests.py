import unittest
from unittest.mock import patch
from lyrics_extractor import extract_lyrics

class TestLyricsExtractor(unittest.TestCase):

    @patch('lyrics_extractor.requests.get')
    def test_extract_lyrics_success(self, mock_get):
        # Mocking the API response with lyrics
        mock_get.return_value.json.return_value = {"lyrics": "Sample lyrics"}

        # Redirecting stdout to capture printed output
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            extract_lyrics()

        # Asserting that the printed message matches the expected output
        self.assertEqual(mock_stdout.getvalue().strip(), "Sample lyrics")
        
        # Asserting that the message box is shown
        mb.showinfo.assert_called_with('Lyrics printed', 'The lyrics to the song have been extracted and printed on your command terminal.')

    @patch('lyrics_extractor.requests.get')
    def test_extract_lyrics_failure(self, mock_get):
        # Mocking the API response with an error
        mock_get.return_value.json.return_value = {"error": "Song not found"}

        # Redirecting stdout to capture printed output
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            extract_lyrics()

        # Asserting that the printed error message matches the expected output
        self.assertEqual(mock_stdout.getvalue().strip(), "Song not found")
        
        # Asserting that the error message box is shown
        mb.showerror.assert_called_with('Error', 'Song not found')

if __name__ == '__main__':
    unittest.main()
