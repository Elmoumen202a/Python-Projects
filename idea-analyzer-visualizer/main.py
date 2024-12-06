import random
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Function to analyze an idea and extract keywords
def analyze_idea(idea):
    """
    Analyze the given idea to extract themes and keywords.

    Parameters:
        idea (str): The idea input by the user.

    Returns:
        dict: A dictionary with the extracted keywords and their frequencies.
    """
    # Split the input string into words and count their occurrences
    words = idea.lower().split()  # Convert to lowercase for uniformity
    keywords = {}
    for word in words:
        # Count each word's occurrence
        keywords[word] = keywords.get(word, 0) + 1
    return keywords

# Function to generate and display a word cloud
def draw_wordcloud(keywords):
    """
    Generate and display a word cloud based on the keywords.

    Parameters:
        keywords (dict): A dictionary of keywords and their frequencies.
    """
    # Create a word cloud using the keywords and their frequencies
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(keywords)
    
    # Display the word cloud using Matplotlib
    plt.figure(figsize=(10, 5))  # Set the figure size
    plt.imshow(wordcloud, interpolation='bilinear')  # Render the word cloud
    plt.axis('off')  # Hide the axes for a cleaner look
    plt.show()  # Display the word cloud

# Main program execution
if __name__ == "__main__":
    print("Welcome to the Idea Analyzer and Visualizer!")
    # Ask the user to input their idea
    idea = input("Enter your idea: ")
    
    # Analyze the idea to extract keywords
    keywords = analyze_idea(idea)
    print("\nKeywords extracted:", keywords)  # Display the extracted keywords
    
    # Generate and display the word cloud
    print("Generating a visual representation...")
    draw_wordcloud(keywords)
