# Define a class for Lessons
class Lesson:
    def __init__(self, title, content):
     
        #param title, the title of the lesson.
        #param content ,the content of the lesson.
        self.title = title
        self.content = content

    def display(self):
        # Display the lesson title and content.
        print(f"\nLesson: {self.title}\n{self.content}\n")


# Define a class for Quizzes
class Quiz:
    def __init__(self, question, answer):
        
        #param question, the quiz question.
        #param answer,the correct answer to the quiz question.    
        self.question = question
        self.answer = answer

    def take_quiz(self):
     
        
        #return: True if the answer is correct, False otherwise.
        user_answer = input(f"Question: {self.question}\nYour answer: ")
        return user_answer.strip().lower() == self.answer.strip().lower()


# Define the main E-Learning Platform class
class ELearningPlatform:
    def __init__(self):
        
        #Initialize the platform with empty lists for lessons and quizzes.
        self.lessons = []
        self.quizzes = []

    def add_lesson(self, lesson):
        
        #param lesson: A Lesson object to be added.
        self.lessons.append(lesson)

    def add_quiz(self, quiz):
        
        # A Quiz object to be added.
        self.quizzes.append(quiz)

    def start(self):
 
        # Display all lessons
        for lesson in self.lessons:
            lesson.display()

        # Run all quizzes and calculate the score
        score = 0
        for quiz in self.quizzes:
            if quiz.take_quiz():
                score += 1
        
        # Display the final score
        print(f"\nYour score: {score}/{len(self.quizzes)}")



if __name__ == "__main__":
    # Create an instance of the platform
    platform = ELearningPlatform()

    # Adding lessons to the platform
    platform.add_lesson(Lesson("Introduction to German", "Welcome to German learning!"))
    platform.add_lesson(Lesson("Basic Greetings", "Hallo, Guten Tag, Wie geht's?"))

    # Adding quizzes to the platform
    platform.add_quiz(Quiz("What is 'Hello' in German?", "Hallo"))

    # Start the platform
    platform.start()
