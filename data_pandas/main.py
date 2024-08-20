import pandas as pd

def load_data(file_path):
    """Loads data from a CSV file and returns a DataFrame."""
    try:
        df = pd.read_csv(file_path)  # change this file_path to path of the CSV file
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def calculate_statistics(df):
    """Calculates basic statistics (mean, median, etc.) for numeric columns in the DataFrame."""
    return df.describe()

def filter_data(df, column_name, threshold):
    """Filters the DataFrame where the column value is above the threshold."""
    return df[df[column_name] > threshold]

if __name__ == "__main__":
    data = load_data('data.csv')
    if data is not None:
        print(calculate_statistics(data))
        filtered_data = filter_data(data, 'column_name', 50)
        print(filtered_data)
