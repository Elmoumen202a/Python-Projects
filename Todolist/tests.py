from todolist import ToDoList

def test_add_task():
    # Test case for the add_task method
    todo_list = ToDoList()
    
    # Add a task to the to-do list
    todo_list.add_task("Test Task")
    
    # Check if the task is added successfully
    assert todo_list.tasks == ["Test Task"]

def test_remove_task():
    # Test case for the remove_task method
    todo_list = ToDoList()
    
    # Add tasks to the to-do list
    todo_list.add_task("Task 1")
    todo_list.add_task("Task 2")
    
    # Remove a task from the to-do list
    todo_list.remove_task(1)
    
    # Check if the specified task is removed successfully
    assert todo_list.tasks == ["Task 2"]

def test_view_tasks(capfd):
    # Test case for the view_tasks method
    todo_list = ToDoList()
    
    # View tasks when no tasks are present
    todo_list.view_tasks()
    
    # Capture the output to check if the correct message is displayed
    captured = capfd.readouterr()
    assert "No tasks available." in captured.out
