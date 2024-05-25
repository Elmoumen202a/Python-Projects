# Financial Data Analysis and Visualization

This project reads financial transaction data from a CSV file, performs analysis, and generates visualizations to help users understand their financial status.

## Features

- **Read and preprocess data:** Load data from a CSV file and prepare it for analysis.
- **Calculate summary statistics:** Compute total income, total expenses, and average monthly expenses.
- **Categorize expenses:** Group expenses by category and calculate totals.
- **Generate visualizations:** Create pie charts for expense distribution and line charts for expense trends over time.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Elmoumen202a/Python-Projects.git

    ```
2. Navigate to the project directory:
    ```sh
    cd financial_analysis
    ```
3. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
4. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Place your transaction data in the `data/transactions.csv` file.
2. Run the main script:
    ```sh
    python main.py
    ```

## Testing
    ```sh
    tests.py

    ```

### Additional Notes

1. **requirements.txt**:
    ```txt
    pandas
    matplotlib
    seaborn
    ```

2. **transactions.csv**:
    - Create a sample `transactions.csv` file with appropriate columns to test the functionality.

This project provides a comprehensive practice for working with data, performing analysis, and generating visualizations in Python. It includes reading and preprocessing data, calculating summary statistics, categorizing expenses, and generating visualizations, all while ensuring code quality through testing.
