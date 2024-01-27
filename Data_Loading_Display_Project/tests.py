from my_main import load_and_display_data
import pandas as pd
import pytest

@pytest.fixture
def sample_data():
    # Sample data for testing
    data = pd.DataFrame({'Column1': [1, 2, 3], 'Column2': ['A', 'B', 'C']})
    return data

def test_load_and_display_data(sample_data, capsys):
    # Test the function with a sample DataFrame
    url = "https://example.com/sample.csv"
    loaded_data = load_and_display_data(url)

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the function returns the correct DataFrame
    assert loaded_data.equals(sample_data)

    # Check if the function prints the first 5 rows
    assert "Column1 Column2\n0       1       A\n1       2       B\n2       3       C" in captured.out
