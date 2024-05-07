# Hello Project

## Overview
This is a simple Python project that checks if it's being run from its own folder. If it is, it prints "Hello!". Otherwise, it prints "This is not your folder."

## Files
- `main.py`: This is the main Python script of the project. It contains the code to check if the script is being run from its own folder and prints "Hello!" or "This is not your folder." accordingly.
- `tests.py`: This file can be used to write tests for the code in `main.py`. At the moment, it's empty since there are no tests provided.
    This tests.py file contains two test cases:
        `test_say_hello_from_main_folder`: This test sets the current directory to the main folder of the project and verifies that the say_hello function prints "Hello!" when called.
        `test_say_hello_from_different_folde`r: This test sets the current directory to a different folder and verifies that the say_hello function prints "This is not your folder." when called.
- `README.md`: This file provides an overview of the project, explains its purpose, and describes the files in the project.

## How to Run
1. Make sure you have Python installed on your system.
2. Clone or download this repository to your local machine.
3. Navigate to the `hello` folder in your terminal.
4. Run the following command:
This will execute the `main.py` script. If it's being run from its own folder, it will print "Hello!". Otherwise, it will print "This is not your folder."

## Future Improvements
- Add more functionality to the project, such as accepting user input or performing additional actions.
- Expand the testing suite to cover more edge cases and ensure the reliability of the code.
- Create a more detailed documentation explaining the usage of the project and its functionalities.

Feel free to contribute to this project by submitting pull requests or opening issues for any bugs or suggestions!
