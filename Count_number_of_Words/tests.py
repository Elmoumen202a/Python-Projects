import pandas as pd
from main import load_and_print_data

def test_load_and_print_data():
    
    test_url = "path/to/test.csv"
    load_and_print_data(test_url)
