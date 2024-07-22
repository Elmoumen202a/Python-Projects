import random

class GermanGrammarGame:
    def __init__(self):
        # Initialize the game with a list of questions and a starting score of 0
        self.questions = [
            {
                "question": "What is the correct form of the article in '___ Hund ist groß.'?",
                "options": ["Der", "Die", "Das"],
                "answer": "Der"
            },
            {
                "question": "What is the correct form of the verb in 'Ich ___ Fußball.'?",
                "options": ["spiele", "spielst", "spielt"],
                "answer": "spiele"
            },
            {
                "question": "Choose the correct preposition: 'Ich gehe ___ Schule.'",
                "options": ["zu", "in", "nach"],
                "answer": "in"
            }
        ]
        self.score = 0

    def start_game(self):
        # Start the game and iterate through each question
        print("Welcome to the German Grammar Checker Game!")
        for question in self.questions:
            self.ask_question(question)
        # Print the final score after all questions have been asked
        print(f"Your final score is {self.score}/{len(self.questions)}.")

    def ask_question(self, question):
        # Display the question and the multiple choice options
        print(question["question"])
        for i, option in enumerate(question["options"], 1):
            print(f"{i}. {option}")
        # Get the user's answer
        answer = input("Your answer (number): ")
        # Check if the user's answer is correct and update the score accordingly
        if question["options"][int(answer) - 1] == question["answer"]:
            print("Correct!")
            self.score += 1
        else:
            print(f"Incorrect! The correct answer is {question['answer']}.")

if __name__ == "__main__":
    # Create an instance of the game and start it
    game = GermanGrammarGame()
    game.start_game()
