import re

def identify_errors(text):
    """
    Identifies common German language errors in the given text.
    - param text: A string in German.
    - return: A list of detected errors.
    """
    errors = []
    
    # Example 1: Check for common capitalization errors.
    if not text[0].isupper():
        errors.append("Sentences should start with a capital letter.")
    
    # Example 2: Check for incorrect verb conjugation (simple rule example).
    if "gegangen habe" in text:
        errors.append("Incorrect verb placement. Use 'bin gegangen' instead.")
    
    return errors

def correct_text(text):
    """
    Suggests corrections for common German errors.
    - param text: A string in German.
    - return: The corrected text.
    """
    corrections = text
    # Simple corrections examples
    corrections = re.sub(r'\bgegangen habe\b', 'bin gegangen', corrections)
    return corrections

def main():
    print("Willkommen beim Fehler-Korrektur-Chat!")
    user_input = input("Bitte geben Sie einen deutschen Satz ein: ")
    errors = identify_errors(user_input)
    if errors:
        print("\nGefundene Fehler:")
        for error in errors:
            print(f"- {error}")
        corrected_text = correct_text(user_input)
        print("\nVorgeschlagene Korrektur:")
        print(corrected_text)
    else:
        print("Kein Fehler gefunden!")

if __name__ == "__main__":
    main()
