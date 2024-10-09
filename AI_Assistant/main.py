import datetime

# Define a class for the AI Assistant
class AIAssistant:
    def __init__(self):
        # Initialize an empty list to store tasks
        self.tasks = []

    # Method to add a task to the to-do list
    def add_task(self, task):
        # Add the task to the list and return a success message
        self.tasks.append(task)
        return f"Task '{task}' added successfully."

    # Method to show all tasks in the to-do list
    def show_tasks(self):
        # If the task list is empty, return a message indicating no tasks
        if not self.tasks:
            return "No tasks available."
        # Join and return all tasks in the list as a string
        return "\n".join(self.tasks)

    # Method to set a reminder for a specific task at a given time
    def set_reminder(self, task, time):
        try:
            # Try to parse the given time string to a datetime object
            reminder_time = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M')
            # Return a message indicating the reminder is set
            return f"Reminder set for '{task}' at {reminder_time}."
        except ValueError:
            # If the time format is incorrect, return an error message
            return "Invalid time format. Use 'YYYY-MM-DD HH:MM'."

    # Method to answer basic questions with hardcoded responses
    def answer_question(self, question):
        # Define a dictionary of responses for specific questions
        responses = {
            "what is your name?": "I am your AI Assistant.",
            "how can you help me?": "I can help you manage tasks, set reminders, and more."
        }
        # Return the appropriate response if the question is known, otherwise return a default message
        return responses.get(question.lower(), "I don't know the answer to that.")

# Example usage of the AIAssistant class
if __name__ == "__main__":
    # Create an instance of the AI Assistant
    assistant = AIAssistant()

    # Add a task and print the response
    print(assistant.add_task("Finish Python project"))

    # Set a reminder for a task and print the response
    print(assistant.set_reminder("Submit project", "2024-10-10 14:00"))

    # Ask the assistant a question and print the response
    print(assistant.answer_question("What is your name?"))
