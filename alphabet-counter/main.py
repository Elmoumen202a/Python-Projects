def count_alphabets(text):
    """
    Count the occurrences of each alphabet in the given text.
    
    Args:
        text (str): The input text.
    
    Returns:
        dict: A dictionary containing the count of each alphabet.
    """
    # Initialize a dictionary to store the count of each alphabet
    alphabet_count = {}
    
    # Iterate through each character in the text
    for char in text:
        # Check if the character is an alphabet
        if char.isalpha():
            # Convert the character to lowercase to avoid case sensitivity
            char = char.lower()
            # Increment the count of the alphabet in the dictionary
            alphabet_count[char] = alphabet_count.get(char, 0) + 1
    
    return alphabet_count

def main():
    text = input("Enter a word or sentence: ")
    result = count_alphabets(text)
    print("Alphabet counts:")
    for alphabet, count in result.items():
        print(f"{alphabet}: {count}")

if __name__ == "__main__":
    main()
