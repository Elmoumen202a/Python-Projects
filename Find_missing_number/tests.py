from finds_number import findMissingNumbers

def test_findMissingNumbers():
    assert findMissingNumbers([1, 2, 3, 5, 6, 7, 8, 9]) == [4]
    assert findMissingNumbers([1, 3, 4, 6]) == [2, 5]
    assert findMissingNumbers([1, 2, 3, 4]) == []
    # Add more test cases as needed
