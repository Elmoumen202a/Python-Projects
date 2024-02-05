import pandas as pd
import pytest
from main_code import plot_machine_learning_trends

# Define a simple test case
def test_plot_machine_learning_trends():
    # Create a sample DataFrame for testing
    test_data = pd.DataFrame({
        'geoName': ['Location1', 'Location2', 'Location3'],
        'Machine Learning': [10, 20, 30]
    })

    # Use pytest's 'capfd' fixture to capture stdout
    with pytest.raises(SystemExit):
        # Call the function with the sample data
        plot_machine_learning_trends(test_data)

if __name__ == "__main__":
    pass
