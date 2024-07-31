# Pandas Data Analysis Project

## Overview

This project demonstrates basic data analysis using Python and pandas. The main script reads data from a CSV file, performs basic analysis, and saves the results to another CSV file. Tests are included to ensure the functionality of the main script.

## Files

- `main.py`: The main script for data analysis.
- `tests.py`: Unit tests for the main script.
- `data.csv`: Sample data file.
- `README.md`: Project overview and instructions.

## Requirements

- Python 3.12.4
- pandas 2.2.2
- unittest

## Usage

1. Install the required packages:
    ```sh
    pip install pandas
    ```

2. Run the main script:
    ```sh
    python main.py
    ```

3. Run the tests:
    ```sh
    python tests.py
    ```

## Description

- `main.py`: Contains functions to load data from a CSV file, perform basic data analysis, and save the results to another CSV file.
  - `load_data(file_path)`: Loads data from a CSV file.
  - `analyze_data(df)`: Performs basic data analysis and returns a summary DataFrame.
  - `save_data(df, file_path)`: Saves a DataFrame to a CSV file.
  - `main()`: Main function to orchestrate the data analysis workflow.

- `tests.py`: Contains unit tests for the functions in `main.py`.
  - `TestMain`: A test case class that tests the functions in `main.py`.
  - `setUp()`: Prepares a sample DataFrame for testing.
  - `test_load_data()`: Tests the `load_data` function.
  - `test_analyze_data()`: Tests the `analyze_data` function.
  - `test_save_data()`: Tests the `save_data` function.

- `data.csv`: Sample data file used for testing and demonstration purposes.

## License

This project is licensed under the MIT License.
