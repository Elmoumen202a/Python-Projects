import emoji

class EmojiConverter:
    def __init__(self, sentiment_mapping=None):
        """
        Initializes the EmojiConverter.

        Args:
            sentiment_mapping (dict): A mapping of emoji codes to their corresponding sentiment.
                If not provided, a default mapping is used.
        """
        self.sentiment_mapping = sentiment_mapping or {
            "😊": "Happy",
            "😢": "Sad",
            "😡": "Angry",
            "😍": "Love",
            "😂": "Laugh",
            # Add more emojis and sentiments as needed
        }

    def convert(self, text):
        """
        Converts emojis in the given text into their corresponding sentiment.

        Args:
            text (str): The input text containing emojis.

        Returns:
            dict: A dictionary mapping sentiments to their occurrences in the input text.
        """
        # Use emoji module to handle different representations of emojis
        text_with_unicode_emojis = emoji.demojize(text)
        
        sentiments = {}
        for emoji_code, sentiment in self.sentiment_mapping.items():
            count = text_with_unicode_emojis.count(emoji_code)
            if count > 0:
                sentiments[sentiment] = count

        return sentiments
