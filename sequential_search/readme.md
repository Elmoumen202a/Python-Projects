# Sequential Search Function

This is a simple Python implementation of the sequential search algorithm.

## Usage

```python
from search import sequential_search

# Example
my_list = [1, 2, 3, 4, 5]
number_to_find = 3
result = sequential_search(my_list, number_to_find)
print(f"Is {number_to_find} in the list? {result}")

```
## Running Tests

```To run tests, use pytest:

pip install -r requirements.txt
pytest tests.py
