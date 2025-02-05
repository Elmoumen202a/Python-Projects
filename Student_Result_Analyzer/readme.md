# Student Result Analyzer

A Python application to analyze student exam results and generate reports.

## Features
- Load student data from CSV files
- Determine pass/fail status based on:
  - Minimum 40 marks in all subjects
  - Overall average of at least 50%
- Generate class statistics:
  - Total number of students
  - Pass/fail counts
  - Class average
  - Highest average
- Output results to console or CSV

## Requirements
- Python 3.x
- pytest (for running tests)

## Usage
1. Prepare your data in CSV format (see sample below)
2. Run the program:
   ```bash
   python main.py --data data.csv --output console