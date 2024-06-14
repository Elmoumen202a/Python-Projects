def read_exam_file(file_path):
    """
    Mock function to simulate reading a .doc file and extracting answers.
    In reality, you would use libraries like python-docx to read .doc/.docx files.
    
    :param file_path: Path to the filled exam file
    :return: Dictionary with question IDs as keys and selected answers as values
    """
    return {
        "Q1": "A",
        "Q2": "C",
        "Q3": "C",
        "Q4": "D",
        "Q5": "B",
    }

def check_mistakes(answers, answers_key):
    """
    Compare the provided answers with the answer key to find mistakes.
    
    :param answers: Dictionary of answers provided by the student
    :param answers_key: Dictionary of correct answers
    :return: Dictionary with questions and the provided incorrect answers
    """
    mistakes = {}
    for question, correct_answer in answers_key.items():
        if answers.get(question) != correct_answer:
            mistakes[question] = answers.get(question)
    return mistakes

def calculate_score(answers, answers_key):
    """
    Calculate the score based on the number of correct answers.
    
    :param answers: Dictionary of answers provided by the student
    :param answers_key: Dictionary of correct answers
    :return: Integer score representing the number of correct answers
    """
    score = 0
    for question, correct_answer in answers_key.items():
        if answers.get(question) == correct_answer:
            score += 1
    return score
