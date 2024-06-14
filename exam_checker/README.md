# Exam Checker

## Overview

The Exam Checker project is a simple Python tool designed to automate the process of grading exams. It reads answers from a filled exam file, compares them with a predefined answer key, identifies any mistakes, and calculates the final score. This can be particularly useful for educators who want to quickly and efficiently grade multiple-choice exams.

## Features

- **Read Exam File:** Simulates reading a .doc file containing student answers.
- **Check Mistakes:** Compares student answers with the correct answers to identify mistakes.
- **Calculate Score:** Computes the total score based on the number of correct answers.
- **Test Suite:** Includes unit tests to verify the correctness of the utility functions.


## Setup

### Prerequisites

Ensure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/).

### Installation

1. **Clone the Repository:**

    ```sh
    git clone https://github.com/yourusername/exam_checker.git
    cd exam_checker
    ```

2. **Install Dependencies:**

    The project may use the `python-docx` library for reading `.doc` files. Install it using pip:

    ```sh
    pip install python-docx
    ```

## Usage

1. **Prepare the Filled Exam File:**

    Place your filled exam file (e.g., `filled_exam.doc`) in the project directory. This file should contain the student's answers.

2. **Update the Answer Key:**

    Open `main.py` and update the `answers_key` dictionary with the correct answers for the exam. For example:

    ```python
    answers_key = {
        "Q1": "A",
        "Q2": "B",
        "Q3": "C",
        "Q4": "D",
        "Q5": "A",
    }
    ```

3. **Run the Main Script:**

    Execute the main script to check the exam and calculate the score:

    ```sh
    python main.py
    ```

4. **View Results:**

    The script will output the mistakes and the final score to the console.

## Running Tests

The project includes unit tests to verify the functionality of the utility functions. To run the tests, execute the following command:

```sh
python -m unittest discover tests


