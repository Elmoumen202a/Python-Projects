# Binary Search Project

This project contains a simple implementation of the binary search algorithm in Python, along with a set of unit tests.

## Files

- `binary_search.py`: Contains the implementation of the binary search algorithm.
- `test_binary_search.py`: Contains unit tests for the binary search algorithm.

## Binary Search Algorithm

Binary search is a fast search algorithm with a run-time complexity of O(log n). This search algorithm works on the principle of divide and conquer. For binary search to work, the list should be sorted.

### How It Works

1. Find the middle element of the array.
2. If the middle element is the target element, return its index.
3. If the target element is smaller than the middle element, repeat the search on the left half of the array.
4. If the target element is larger than the middle element, repeat the search on the right half of the array.
5. If the search interval is empty, the target is not in the array.

## Usage

You can run the binary search algorithm by executing `binary_search.py`:

```sh
python binary_search.py
```

## Testing

```sh
python -m unittest test_binary_search.py

```
# License

This setup provides a clear structure for the binary search project, including an implementation of the algorithm, unit tests, and documentation on how to use and test the code.
