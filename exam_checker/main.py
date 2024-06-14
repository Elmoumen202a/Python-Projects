from exam_utils import read_exam_file, check_mistakes, calculate_score

def main():
    # Path to the filled exam file
    exam_file = "filled_exam.doc"  # The file to be processed
    
    # Answer key dictionary: Replace with actual correct answers
    answers_key = {
        "Q1": "A",
        "Q2": "B",
        "Q3": "C",
        "Q4": "D",
        "Q5": "A",
    }  # This is a mock example of answer key

    # Read the answers from the filled exam file
    answers = read_exam_file(exam_file)
    
    # Check for mistakes by comparing answers with the answer key
    mistakes = check_mistakes(answers, answers_key)
    
    # Calculate the score based on correct answers
    score = calculate_score(answers, answers_key)

    # Print the results
    print("Mistakes:", mistakes)
    print("Score:", score)

if __name__ == "__main__":
    main()
