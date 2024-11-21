import random

# Define sample questions for TELC B1 practice. Each question is a tuple containing
# the question text and the correct answer.
GRAMMAR_QUESTIONS = [
    ("Correct the sentence: 'She go to the market yesterday.'", "She went to the market yesterday."),
    ("Fill in the blank: 'I ___ at home yesterday.' (to be)", "was"),
    ("Choose the correct form: 'He ___ football every weekend.' (play/plays)", "plays")
]

VOCABULARY_QUESTIONS = [
    ("Translate to German: 'House'", "Haus"),
    ("Translate to English: 'Buch'", "Book"),
    ("What is the plural of 'Child'?", "Children")
]

SENTENCE_CONSTRUCTION = [
    ("Construct a sentence using 'because':", "Your sentence must include 'because'."),
    ("Construct a sentence using 'although':", "Your sentence must include 'although'.")
]

def ask_question(question, correct_answer=None):
    """
    Displays a question to the user. If a correct_answer is provided,
    it checks the user's answer and gives feedback; otherwise, it prompts the user to write an answer.

    Parameters:
        question (str): The question to display.
        correct_answer (str, optional): The correct answer to validate against.
    """
    print(question)
    if correct_answer:
        # Ask the user for their answer and compare it to the correct answer.
        user_answer = input("Your answer: ")
        if user_answer.strip().lower() == correct_answer.strip().lower():
            print("Correct!")  # If the answer matches, show a success message.
        else:
            print(f"Incorrect. The correct answer is: {correct_answer}")  # Show the correct answer.
    else:
        # For open-ended questions, just ask for input without validating.
        input("Write your answer and press Enter. No validation for this question.")

def start_practice():
    """
    The main function to start the TELC B1 practice session. 
    It asks the user to choose a category and then displays a question from that category.
    """
    print("Welcome to TELC B1 Practice!")  # Welcome message for the user.
    print("Choose a category:\n1. Grammar\n2. Vocabulary\n3. Sentence Construction")
    choice = input("Enter the number of your choice: ").strip()
    
    # Show a random question based on the user's choice.
    if choice == "1":
        question = random.choice(GRAMMAR_QUESTIONS)
        ask_question(*question)
    elif choice == "2":
        question = random.choice(VOCABULARY_QUESTIONS)
        ask_question(*question)
    elif choice == "3":
        question = random.choice(SENTENCE_CONSTRUCTION)
        ask_question(*question)
    else:
        print("Invalid choice. Please select 1, 2, or 3.")  # Handle invalid input.
    
    print("\nPractice complete. Good luck with your TELC exam!")  # Closing message.

# Check if the script is being run directly (not imported) and start the practice session.
if __name__ == "__main__":
    start_practice()
