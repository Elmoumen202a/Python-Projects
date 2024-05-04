def count_words(text):
    # Convert text to lowercase and split into words
    words = text.lower().split()
    
    word_count = {}
    
    # Count the frequency of each word
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    return word_count

def common_words(text, n=10):
    word_count = count_words(text)
    
    # Sort words by frequency in descending order
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    
    # Return the top n common words
    return sorted_words[:n]

if __name__ == "__main__":
    text = input("Enter text: ")
    common = common_words(text)
    print("Top 10 common words:")
    for word, count in common:
        print(f"{word}: {count}")
