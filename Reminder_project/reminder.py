from datetime import datetime

def create_reminder(task, due_date):
    reminder = f"Task: {task}\nDue Date: {due_date}\nStatus: Pending"
    
    with open("reminder.md", "a") as file:
        file.write(reminder + "\n\n")

if __name__ == "__main__":
    task = input("Enter the task: ")
    due_date_str = input("Enter the due date (YYYY-MM-DD): ")

    try:
        due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
        create_reminder(task, due_date.strftime("%Y-%m-%d %H:%M:%S"))
        print("Reminder added successfully.")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
