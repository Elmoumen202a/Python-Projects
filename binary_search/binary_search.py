def binary_search(arr, target):
    """
    Parameters:
    arr (list): A sorted list of elements.
    target:     The element to search for in the list.

    Returns:
    int: The index of the target element if found, otherwise -1.
    """
    # Initialize the left and right pointers
    left, right = 0, len(arr) - 1  
    # Continue until the pointers cross
    while left <= right:  
         # Find the middle index
        mid = (left + right) // 2 
        # If the middle element is the target, return its index
        if arr[mid] == target:  
            return mid
        # If the target is greater, ignore the left half
        elif arr[mid] < target: 
            left = mid + 1
        # If the target is smaller, ignore the right half
        else: 
            right = mid - 1
    # If the target is not found, return -1
    return -1 

if __name__ == "__main__":
    # Example usage :
    # A sorted list of numbers
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
    # The element to search for 
    target = 5 
    # Perform binary search
    result = binary_search(arr, target)  
    # Output the result
    print(f"Element {target} is at index: {result}")  
