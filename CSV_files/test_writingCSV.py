import pandas as pd
from writing_csv_file import process_data

def test_process_data():
    # Test input data
    test_data = {
                "Name": ["Name1", "Name2", "Name3"],
                "Age": [33, 34, 40]
                 }

    # Expected output
    expected_output = pd.DataFrame(test_data)

    # Call the function to process the data
    result = process_data(test_data)

    # Check if the processed data matches the expected output
    assert result.equals(expected_output)

# You can add more test cases as needed
