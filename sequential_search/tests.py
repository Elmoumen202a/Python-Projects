from search import sequential_search

def test_sequential_search():
    # Test case 1
    assert sequential_search([1, 2, 3, 4, 5], 3) == True

    # Test case 2
    assert sequential_search(['apple', 'banana', 'orange', 'grape'], 'orange') == True

    # Test case 3
    assert sequential_search([1, 2, 3, 4, 5], 6) == False

    # Test case 4
    assert sequential_search(['apple', 'banana', 'orange', 'grape'], 'kiwi') == False
