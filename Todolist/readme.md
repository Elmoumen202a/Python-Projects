# To-Do List Application

## Description

A simple console-based to-do list application written in Python. Users can add, view, and remove tasks from their to-do list.

## Usage

1. Run the `todolist.py` file.
2. Follow the on-screen menu to interact with the to-do list.

## Methods

### `ToDoList` Class

- `__init__(self)`: Initializes an empty to-do list.
- `add_task(self, task)`: Adds a task to the to-do list.
- `view_tasks(self)`: Displays all tasks in the to-do list.
- `remove_task(self, task_index)`: Removes a task from the to-do list based on the index.

## Example

```python
from todolist import ToDoList

todo_list = ToDoList()

todo_list.add_task("Buy groceries")
todo_list.view_tasks()
todo_list.remove_task(1)
