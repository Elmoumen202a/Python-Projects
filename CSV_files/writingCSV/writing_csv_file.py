import csv
import pandas as pd

def process_data(data):
    """
    Process the input data and create a new DataFrame.
    Args: data (dict): Input data dictionary with "Name" and "Age" keys.
    Returns:  pd.DataFrame: Processed data in a DataFrame.
    """
    # Creating a DataFrame from the input data
    processed_data = pd.DataFrame(data)
    # Additional processing or transformations can be added here if needed
    return processed_data

# Initial data
initial_data = {
                "Name": ["Name1", "Name2", "Name3", "Name4", "Name5"],
                "Age": [33, 34, 40, 23, 10]
                }

# Process the data
processed_data = process_data(initial_data)

# Save the processed data to a CSV file
processed_data.to_csv("processed_data.csv", index=False)
print(processed_data.head())
