import re

def detect_language(code):
    # Define simple heuristics for identifying the programming language
    patterns = {
        'python': [r'\bdef\b', r'\bimport\b', r'\bprint\b'],
        'java': [r'\bclass\b', r'\bpublic\b', r'\bSystem\.out\.print'],
        'c': [r'#include\s*<stdio.h>', r'\bprintf\b', r'\bscanf\b'],
        'cpp': [r'#include\s*<iostream>', r'\bstd::cout\b', r'\bstd::cin\b'],
    }

    # Initialize a dictionary to keep score for each language
    scores = {language: 0 for language in patterns.keys()}

    # Check the code against each pattern for each language
    for language, regex_patterns in patterns.items():
        for pattern in regex_patterns:
            if re.search(pattern, code):
                scores[language] += 1

    # Determine the language with the highest score
    detected_language = max(scores, key=scores.get)
    
    # Return the detected language, or 'unknown' if no patterns were matched
    return detected_language if scores[detected_language] > 0 else 'unknown'

if __name__ == "__main__":
    # Sample code snippet for testing
    sample_code = """
    #include <iostream>
    int main() {
        std::cout << "Hello, World!" << std::endl;
        return 0;
    }
    """
    # Detect the language of the sample code
    language = detect_language(sample_code)
    print(f"The detected programming language is: {language}")
