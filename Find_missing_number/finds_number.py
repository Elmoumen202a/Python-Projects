def findMissingNumbers(n):
    # Convert the list of numbers to a set for faster membership checks
    numbers = set(n)
      
    # Initialize an empty list to store missing numbers
    output = []
    
    # Iterate through the range of numbers from 1 to the last element in the input list
    for i in range(1, n[-1]):
        # Check if the current number is not in the set of input numbers
        if i not in numbers:
            # If not, add it to the list of missing numbers
            output.append(i)
    
    # Return the list of missing numbers
    return output
    
if __name__ == "__main__":
    # Example usage with a list of numbers
    listOfNumbers = [1, 2, 3, 5, 7, 8, 9, 10]
    
    # Call the findMissingNumbers function with the example list
    result = findMissingNumbers(listOfNumbers)
    
    # Print the result
    print("Missing numbers:", result)
