# main.py
import re

def respond_to_user_input(user_input):
    # Define patterns and responses
    patterns_responses = {
        r'(hello|hi|hey)': 'Hello!',
        r'how are you': 'I am doing well, thank you!',
        r'(bye|goodbye)': 'Goodbye! Have a great day!',
        r'\b(?:thanks?|thank you)\b': 'You\'re welcome!',
        r'stop': 'Chat session ended. Goodbye!'
    }

    # Search for patterns in user input and provide a response
    for pattern, response in patterns_responses.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return response

    # If no specific pattern matched, provide a default response
    return "I'm not sure how to respond to that. Can you ask something else?"

def chat_ai(input_function=input):
    print("Chat with the AI (Type 'stop' to end):")
    while True:
        user_input = input_function("You: ")
        if user_input.lower() == 'stop':
            break
        response = respond_to_user_input(user_input)
        print(f"AI: {response}")

if __name__ == "__main__":
    chat_ai()
