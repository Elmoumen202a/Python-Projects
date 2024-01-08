import pandas as pd
from reading_csv_file import read_csv_file  

@pytest.fixture
def sample_csv(tmp_path):
    # Create a sample CSV file for testing
    data = {'Name': ['John', 'Alice', 'Bob'],
            'Age': [25, 30, 22]}
    df = pd.DataFrame(data)
    file_path = tmp_path / 'test_age_data.csv'
    df.to_csv(file_path, index=False)
    return file_path

def test_read_csv_file(sample_csv, capsys):
    # Test the read_csv_file function
    read_csv_file(sample_csv)
    captured = capsys.readouterr()
    assert "Name  Age" in captured.out
    assert "John  25" in captured.out
    assert "Alice  30" in captured.out
    assert "Bob  22" in captured.out