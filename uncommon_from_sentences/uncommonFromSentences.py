# Function to find uncommon words between two sentences
def uncommonFromSentences(s1, s2):
    # Split the input sentences into lists of words
    words1 = s1.split()
    words2 = s2.split()

    # Create a dictionary to store the count of each word
    counts = {}
    
    # Iterate through the words in both sentences
    for word in words1 + words2:
        # Update the count of the word in the dictionary
        counts[word] = counts.get(word, 0) + 1

    # Create a list of words that appear only once in the sentences
    uncommon = [word for word in counts if counts[word] == 1]
    
    # Return the list of uncommon words
    return uncommon

# Main function to demonstrate the usage of uncommonFromSentences
def main():
    # Example sentences
    x1 = "this code is cool"
    x2 = "this code is Python"
    
    # Call the uncommonFromSentences function with the example sentences
    result = uncommonFromSentences(x1, x2)
    
    # Print the result
    print(result)

# Check if the script is run as the main program
if __name__ == "__main__":
    # Call the main function when the script is executed
    main()
