import re

def check_grammar(text):
    """
    Check common grammatical mistakes in German text and provide corrections.
    
    Parameters:
    text (str): The text to check.
    
    Returns:
    dict: A dictionary of errors found and their corrections.
    """
    # Initialize dictionaries to store errors and corrections
    errors = {}
    corrections = {}

    # Split the input text into individual words for easier analysis
    words = text.split()
    
    # --- Capitalization Check for Nouns ---
    # Articles in German (these are typically followed by nouns)
    articles = ['der', 'die', 'das', 'ein', 'eine']
    
    # Lists to store errors and their corrections
    noun_errors = []
    corrected_nouns = []
    
    # Iterate through words to detect nouns that should be capitalized
    for i in range(len(words) - 1):
        # If the previous word is an article and the next word isn't capitalized, it's likely a noun
        if words[i].lower() in articles and words[i + 1][0].islower():
            noun_errors.append(words[i + 1])  # Add the noun to errors list
            corrected_nouns.append(words[i + 1].capitalize())  # Capitalize the noun for correction

    # If any capitalization mistakes were found, add them to the errors dictionary
    if noun_errors:
        errors['Capitalization'] = noun_errors
        corrections['Capitalization'] = corrected_nouns
    
    # --- Verb Conjugation Check ---
    # Dictionary of common conjugation errors (simplified for "er", "sie", "es" subjects)
    conjugation_errors = {
        "bin": "ist",   # 'er bin' -> 'er ist'
        "habe": "hat",  # 'er habe' -> 'er hat'
    }
    
    # Lists to store verb conjugation errors and their corrections
    verb_errors = []
    verb_corrections = []
    
    # Check if a verb conjugation error occurs after 'er', 'sie', or 'es'
    for i in range(len(words) - 1):
        # If the word is 'er', 'sie', or 'es' and the following verb is wrong, it's an error
        if words[i].lower() in ['er', 'sie', 'es'] and words[i + 1] in conjugation_errors:
            verb_errors.append(words[i + 1])  # Add the incorrect verb to the error list
            verb_corrections.append(conjugation_errors[words[i + 1]])  # Suggest the correct conjugation

    # If any verb conjugation mistakes were found, add them to the errors dictionary
    if verb_errors:
        errors['Verb Conjugation'] = verb_errors
        corrections['Verb Conjugation'] = verb_corrections

    return errors, corrections

# Main block to test the function with an example text
if __name__ == "__main__":
    sample_text = "ich habe ein haus. er bin gut."
    print("Checking text:", sample_text)
    mistakes, fixes = check_grammar(sample_text)

    # Print mistakes and suggested corrections
    if mistakes:
        print("Mistakes found:")
        for category, words in mistakes.items():
            print(f"{category}: {', '.join(words)}")
        
        print("\nSuggested corrections:")
        for category, words in fixes.items():
            print(f"{category}: {', '.join(words)}")
    else:
        print("No mistakes found.")
