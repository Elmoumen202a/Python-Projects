import pandas as pd

def load_and_display_data(csv_url):
    """
    Load data from a CSV file and display the first 5 rows.

    Parameters:
    - csv_url (str): URL of the CSV file.

    Returns:
    - pd.DataFrame: Loaded DataFrame.
    """
    # Load data
    data = pd.read_csv(csv_url, encoding='latin1')

    # Display the first 5 rows
    print(data.head())

    return data
