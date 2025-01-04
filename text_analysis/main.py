import re
from collections import Counter

def analyze_text(text):
    """
    Analyzes the provided German text and returns statistics.

    Args:
        text (str): The input German text.

    Returns:
        dict: A dictionary containing word count, sentence count,
              and the most common words.
    """
    # Count sentences using regex
    sentences = re.split(r'[.!?]', text)
    sentence_count = len([s for s in sentences if s.strip()])

    # Count words
    words = re.findall(r'\w+', text.lower())
    word_count = len(words)

    # Find common words
    word_frequency = Counter(words)
    common_words = word_frequency.most_common(5)

    return {
        "sentence_count": sentence_count,
        "word_count": word_count,
        "common_words": common_words,
    }

if __name__ == "__main__":
    sample_text = input("Enter a German text: ")
    result = analyze_text(sample_text)
    print("\nText Analysis Results:")
    print(f"Number of sentences: {result['sentence_count']}")
    print(f"Number of words: {result['word_count']}")
    print("Most common words:")
    for word, count in result['common_words']:
        print(f"  {word}: {count}")
