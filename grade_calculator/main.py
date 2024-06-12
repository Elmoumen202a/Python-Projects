class GradeCalculator:
    def __init__(self):
        # Initialize an empty list to store scores
        self.scores = []

    def add_score(self, score):
        # Validate the score to be within the range of 0 to 100
        if 0 <= score <= 100:
            self.scores.append(score)
        else:
            raise ValueError("Score must be between 0 and 100")

    def calculate_average(self):
        # Check if there are scores to calculate the average
        if not self.scores:
            raise ValueError("No scores to calculate average")
        # Calculate and return the average score
        return sum(self.scores) / len(self.scores)

    def determine_grade(self):
        # Determine the grade based on the average score
        average = self.calculate_average()
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'

if __name__ == "__main__":
    calc = GradeCalculator()
    while True:
        try:
            # Prompt user to enter a score or 'done' to finish
            score = input("Enter a score (or 'done' to finish): ")
            if score.lower() == 'done':
                break
            # Add the score to the calculator
            calc.add_score(float(score))
        except ValueError as e:
            # Handle invalid score input
            print(e)

    try:
        # Output the average score and final grade
        print(f"Average Score: {calc.calculate_average()}")
        print(f"Final Grade: {calc.determine_grade()}")
    except ValueError as e:
        # Handle the case where no scores were entered
        print(e)
