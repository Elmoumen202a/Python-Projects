import datetime
import json

class DailyPlannerAIChat:
    def __init__(self):
        self.tasks = []
        self.daily_plan = []

    def add_task(self, task_name, priority, duration):
        """
        Adds a task to the planner.
        Args:
            task_name (str): The name of the task.
            priority (str): The task's priority (high, medium, low).
            duration (int): The task's duration in minutes.
        """
        task = {
            "task_name": task_name,
            "priority": priority,
            "duration": duration,
            "added_time": datetime.datetime.now()
        }
        self.tasks.append(task)

    def get_daily_plan(self, available_time):
        """
        Generates a daily plan based on available time.
        Args:
            available_time (int): The time available for planning (in minutes).
        Returns:
            list: A list of tasks for the day.
        """
        priority_order = {"high": 1, "medium": 2, "low": 3}
        sorted_tasks = sorted(self.tasks, key=lambda x: (priority_order[x['priority']], x['duration']))

        self.daily_plan = []
        time_remaining = available_time

        for task in sorted_tasks:
            if task['duration'] <= time_remaining:
                self.daily_plan.append(task)
                time_remaining -= task['duration']

        return self.daily_plan

    def save_plan_to_file(self, filename="daily_plan.json"):
        """
        Saves the daily plan to a JSON file.
        Args:
            filename (str): The file name to save the plan.
        """
        with open(filename, 'w') as f:
            json.dump(self.daily_plan, f, indent=4)
        print(f"✅ Daily plan saved to {filename}")

    def check_progress(self):
        """
        Checks the progress of the tasks by asking the user.
        """
        completed_tasks = 0
        print("🔍 Checking task progress...")
        for task in self.daily_plan:
            status = input(f"Did you complete '{task['task_name']}'? (yes/no): ")
            if status.lower() == 'yes':
                completed_tasks += 1
        print(f"🎉 You completed {completed_tasks}/{len(self.daily_plan)} tasks today!")

def display_menu():
    """
    Displays a simple menu with options for the user.
    """
    print("\n🧠 Welcome to Daily Planner AI!")
    print("1️⃣ Add a Task")
    print("2️⃣ Generate Daily Plan")
    print("3️⃣ Check Task Progress")
    print("4️⃣ Exit")
    choice = input("Please choose an option (1-4): ")
    return choice

def chat_with_ai():
    """
    The main function to interact with the AI via a simple numbered menu.
    """
    planner = DailyPlannerAIChat()
    
    while True:
        user_choice = display_menu()
        
        if user_choice == "1":
            task_name = input("📌 What's the task name? ")
            priority = input("🔥 Priority (high, medium, low)? ")
            duration = int(input("⏳ How many minutes will it take? "))
            planner.add_task(task_name, priority, duration)
            print(f"✅ Task '{task_name}' added!")

        elif user_choice == "2":
            available_time = int(input("⏱️ How many minutes do you have for the day? "))
            plan = planner.get_daily_plan(available_time)
            if plan:
                print("📅 Here’s your daily plan:")
                for task in plan:
                    print(f"- {task['task_name']} ({task['duration']} minutes)")
                save = input("💾 Would you like to save the plan to a file? (yes/no) ").strip().lower()
                if save == 'yes':
                    planner.save_plan_to_file()
            else:
                print("🚫 Not enough tasks to fit the available time.")

        elif user_choice == "3":
            planner.check_progress()

        elif user_choice == "4":
            print("👋 Goodbye! Have a productive day!")
            break

        else:
            print("🤔 Invalid choice. Please select a number between 1 and 4.")

if __name__ == "__main__":
    chat_with_ai()
