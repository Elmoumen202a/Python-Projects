import re

class ChatAI:
    def __init__(self):
        # Define patterns and responses in the constructor
        self.patterns_responses = {
            r'hello|hi|hey': 'Hello there!',
            r'how are you': 'I am doing well, thank you!',
            r'bye|goodbye': 'Goodbye! Have a great day!',
            r'\b(?:thanks?|thank you)\b': 'You\'re welcome!',
            r'stop': 'Chat session ended. Goodbye!'
        }

    def respond_to_user_input(self, user_input):
        # Iterate over patterns and responses to find a match
        for pattern, response in self.patterns_responses.items():
            if re.search(pattern, user_input, re.IGNORECASE):
                return response
        # If no specific pattern matched, provide a default response
        return "I'm not sure how to respond to that. Can you ask something else?"

    def chat_loop(self):
        print("Chat with the AI (Type 'stop' to end):")
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'stop':
                break
            # Get AI's response based on user input
            response = self.respond_to_user_input(user_input)
            print(f"AI: {response}")

# Main execution part
if __name__ == "__main__":
    # Create an instance of the ChatAI class
    chat_ai = ChatAI()
    # Start the chat loop
    chat_ai.chat_loop()
