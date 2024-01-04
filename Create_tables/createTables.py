# Import the 'tabulate' function from the 'tabulate' module
from tabulate import tabulate

# Define a function named 'print_table'
def print_table():
    # Create a list named 'data' containing lists representing rows of a table
    data = [
        ["City", "Population (millions)", "Country"],
        ["Tokyo", 37.8, "Japan"],
        ["Delhi", 31.4, "India"],
        ["Shanghai", 27.6, "China"],
        ["Sao Paulo", 21.7, "Brazil"]
    ]
    # Use the 'tabulate' function to format and print the table
    # 'headers="firstrow"' specifies that the first row of 'data' should be treated as headers
    # 'tablefmt="fancy_grid"' specifies the table format as 'fancy_grid'
    print(tabulate(data, headers="firstrow", tablefmt="fancy_grid"))

# If the script is executed directly (not imported as a module)
if __name__ == "__main__":
    # Call the 'print_table' function to print the population table
    print_table()
