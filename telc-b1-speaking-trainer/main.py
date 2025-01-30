import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_question(topic: str) -> str:
    """
    Generates a German speaking test question using OpenAI API
    Args:
        topic: The topic for the question (e.g., 'travel', 'shopping')
    Returns:
        Generated question in German
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "system",
            "content": f"Generate a German speaking question for TELC B1 level about {topic}. "
                       "The question should require a 2-3 sentence response."
        }]
    )
    return response.choices[0].message['content'].strip()

def evaluate_answer(question: str, answer: str) -> dict:
    """
    Evaluates user's German answer using OpenAI API
    Args:
        question: The original question
        answer: User's response in German
    Returns:
        Dictionary with score and feedback
    """
    prompt = f"""Evaluate this German B1 speaking test answer:
    Question: {question}
    Answer: {answer}
    
    Provide feedback focusing on:
    - Grammar correctness
    - Vocabulary appropriateness
    - Relevance to question
    - Overall B1 level adequacy
    Give a score between 1-10 and specific feedback in English."""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": prompt}]
    )
    
    feedback_text = response.choices[0].message['content'].strip()
    score = int(feedback_text.split("Score: ")[1].split("/")[0])
    feedback = feedback_text.split("Feedback: ")[1] if "Feedback: " in feedback_text else feedback_text
    
    return {"score": score, "feedback": feedback}

def main():
   # Main interaction loop
    topics = ['travel', 'shopping', 'health', 'work', 'hobbies', 'environment']
    
    print("Welcome to German Speaking Test Trainer!")
    print("Available topics:", ", ".join(topics))
    
    while True:
        topic = input("\nChoose a topic or 'q' to quit: ").lower()
        if topic == 'q':
            break
            
        if topic not in topics:
            print("Invalid topic, please choose from the list")
            continue
            
        question = generate_question(topic)
        print(f"\nQuestion: {question}")
        answer = input("Your answer (in German): ")
        
        evaluation = evaluate_answer(question, answer)
        print(f"\nScore: {evaluation['score']}/10")
        print(f"Feedback: {evaluation['feedback']}\n")

if __name__ == "__main__":
    main()