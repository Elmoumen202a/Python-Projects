from search import sequential_search

# Example 1
list1 = [1, 2, 3, 4, 5]
number_to_find1 = 3
result1 = sequential_search(list1, number_to_find1)
print(f"Is {number_to_find1} in the list? {result1}")

# Example 2
list2 = ['apple', 'banana', 'orange', 'grape']
item_to_find2 = 'orange'
result2 = sequential_search(list2, item_to_find2)
print(f"Is {item_to_find2} in the list? {result2}")
