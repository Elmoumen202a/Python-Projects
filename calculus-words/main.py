def count_words(text):
    """
    Count the number of words in the given text.
    """
    words = text.split()
    return len(words)

def estimate_pages(word_count, words_per_page=250):
    """
    Estimate the number of pages based on word count and a standard word per page ratio.
    """
    pages = word_count / words_per_page
    return pages

if __name__ == "__main__":
    text = input("Enter your text: ")
    word_count = count_words(text)
    print("Total words:", word_count)
    pages = estimate_pages(word_count)
    print("Estimated pages:", round(pages, 2))
