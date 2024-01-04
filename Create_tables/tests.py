from createTables import print_table
import pytest
from io import StringIO
import sys

# Define a test function for print_population_table
def test_print_population_table(capsys):
    # Call the function to print the population table
    print_table()
    # Capture the printed output
    captured = capsys.readouterr()
    # Split the output into lines for easier comparison
    output_lines = captured.out.strip().split('\n')

    # Check headers
    assert "City" in output_lines[0]
    assert "Population (millions)" in output_lines[0]
    assert "Country" in output_lines[0]

    # Check data
    assert "Tokyo" in output_lines[2]
    assert "37.8" in output_lines[2]
    assert "Japan" in output_lines[2]

    assert "Delhi" in output_lines[4]
    assert "31.4" in output_lines[4]
    assert "India" in output_lines[4]

    assert "Shanghai" in output_lines[6]
    assert "27.6" in output_lines[6]
    assert "China" in output_lines[6]

    assert "Sao Paulo" in output_lines[8]
    assert "21.7" in output_lines[8]
    assert "Brazil" in output_lines[8]

if __name__ == "__main__":
    pytest.main()
