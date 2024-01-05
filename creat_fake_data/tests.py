# test_main.py
from fakeData import g_fake_data
import pandas as pd

def test_g_fake_data():
    # Explanation: Testing if the function returns a DataFrame
    fake_data = g_fake_data(10)
    assert isinstance(fake_data, pd.DataFrame)

    # Explanation: Testing if the number of generated records matches the input
    assert len(fake_data) == 10

