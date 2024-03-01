from emoji_converter import EmojiConverter

# Initialize the EmojiConverter with a custom sentiment mapping
sentiment_mapping = {
    "😊": "Happy",
    "😢": "Sad",
    "😡": "Angry",
    "😍": "Love",
    "😂": "Laugh",
    # Add more emojis and sentiments as needed
}
converter = EmojiConverter(sentiment_mapping)

# Example usage
text_with_emojis = "I'm feeling 😊 today! This news makes me 😡 and 😢 at the same time. 😍"
sentiments = converter.convert(text_with_emojis)

# Print the results
print("Sentiments in the text:")
for sentiment, count in sentiments.items():
    print(f"{sentiment}: {count} occurrences")
