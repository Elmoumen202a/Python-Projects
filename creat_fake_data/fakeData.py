from faker import Faker
import pandas as pd

def g_fake_data(num_records):
    """
    Generates fake data using Faker library and creates a pandas DataFrame.
    Parameters: num_records (int), number of records to generate.
    Returns: pd.DataFrame , dataFrame containing fake data.
    """
    fake = Faker()
    data = [fake.profile() for _ in range(num_records)]
    fake_data_df = pd.DataFrame(data)
    return fake_data_df

def main():
    # Explanation: Generating fake data with 100 records
    fake_data = g_fake_data(100)
    # Explanation: Printing the first few rows of the DataFrame
    print(fake_data.head())

if __name__ == "__main__":
    main()
