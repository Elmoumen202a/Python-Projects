import random

class QuestionGenerator:
    # Initialize the QuestionGenerator with a list of predefined questions
    def __init__(self):
        self.questions = [
            "What is the capital of France?",
            "Who wrote 'Hamlet'?",
            "What is the chemical symbol for water?",
            "What is the square root of 64?",
            "Who painted the Mona Lisa?"
        ]
        
    # Function to randomly select and return a question from the list
    def generate_question(self):
        return random.choice(self.questions)
    
# If this script is run directly, generate and print a random question
if __name__ == "__main__":
    generator = QuestionGenerator()
    print(generator.generate_question())
