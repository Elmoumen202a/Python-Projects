import pandas as pd

def read_csv_file(file_path):
    """
    Read a CSV file and print the head of the data.
    Parameters: file_path (str): The path to the CSV file.
    Returns: pd.DataFrame: The DataFrame containing the read data.
    """
    data = pd.read_csv(file_path)
    print(data.head())
    return data

# Example usage:
# file_path = "age_data.csv"
# read_csv_file(file_path)
