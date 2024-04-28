class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
        else:
            print("Task not found in the list.")

    def is_empty(self):
        return len(self.tasks) == 0

def main():
    todo_list = TodoList()

    print("Welcome to the To-Do List Manager!")
    while True:
        print("\n1. Add Task\n2. Remove Task\n3. View Tasks\n4. Check if list is empty\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
            print("Task added successfully.")

        elif choice == '2':
            task = input("Enter the task to remove: ")
            todo_list.remove_task(task)

        elif choice == '3':
            print("Tasks:")
            for index, task in enumerate(todo_list.tasks, start=1):
                print(f"{index}. {task}")

        elif choice == '4':
            if todo_list.is_empty():
                print("Your to-do list is empty.")
            else:
                print("You still have tasks to do.")

        elif choice == '5':
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")

    if todo_list.is_empty():
        print("Congratulations! You have completed all tasks in your to-do list.")

if __name__ == "__main__":
    main()
