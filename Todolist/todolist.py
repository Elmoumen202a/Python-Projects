# todolist.py

class ToDoList:
    def __init__(self):
        # Initialize an empty list to store tasks
        self.tasks = []

    def add_task(self, task):
        # Method to add a task to the to-do list
        self.tasks.append(task)
        print(f'Task "{task}" added successfully.')

    def view_tasks(self):
        # Method to view all tasks in the to-do list
        if not self.tasks:
            print('No tasks available.')
        else:
            print('Tasks:')
            for index, task in enumerate(self.tasks, start=1):
                print(f'{index}. {task}')

    def remove_task(self, task_index):
        # Method to remove a task from the to-do list based on index
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(f'Task "{removed_task}" removed successfully.')
        else:
            print('Invalid task index. No task removed.')

# Main function for user interaction
def main():
    todo_list = ToDoList()

    while True:
        print('\n===== To-Do List =====')
        print('1. Add Task')
        print('2. View Tasks')
        print('3. Remove Task')
        print('4. Exit')

        choice = input('Enter your choice (1-4): ')

        if choice == '1':
            task = input('Enter the task: ')
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            task_index = int(input('Enter the task index to remove: '))
            todo_list.remove_task(task_index)
        elif choice == '4':
            print('Exiting...')
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 4.')

if __name__ == '__main__':
    main()