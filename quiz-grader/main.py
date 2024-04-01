def grade_quiz(answers, key):
    """
    Grade a quiz by comparing student answers to the answer key.

    Args:
    - answers (list): A list containing student answers.
    - key (list): A list containing correct answers.

    Returns:
    - int: The total points earned by the student.
    """
    points = 0
    for i in range(len(answers)):
        if answers[i] == key[i]:
            points += 1
    return points

def main():
    # Example quiz answers and answer key
    answers = ['A', 'B', 'C', 'D', 'A']
    answer_key = ['A', 'B', 'C', 'D', 'A']

    total_points = grade_quiz(answers, answer_key)
    print("Total points earned:", total_points)

if __name__ == "__main__":
    main()
