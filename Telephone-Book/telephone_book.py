class TelephoneBook:
    
    def __init__(self):
       # Initialize an empty telephone book.
        self.entries = {}

    def add_entry(self, name, number):
        """
        Add an entry to the telephone book.
            name (str): The name associated with the phone number.
            number (str): The phone number to add.
        """
        self.entries[name] = number

    def lookup_number(self, name):
        """
        Look up a phone number by name.
            name (str): The name to look up.
            str: The corresponding phone number, or "Number not found" if the name is not found.
        """
        return self.entries.get(name, "Number not found")

    def lookup_name(self, number):
        """
        Look up a name by phone number.
            number (str): The phone number to look up.
            str: The corresponding name, or "Name not found" if the number is not found.
        """
        for name, num in self.entries.items():
            if num == number:
                return name
        return "Name not found"

# Example usage
if __name__ == "__main__":
    # Create a telephone book object
    phone_book = TelephoneBook()

    # Add entries to the telephone book
    phone_book.add_entry("John", "1234567890")
    phone_book.add_entry("Alice", "9876543210")

    # Look up a phone number by name
    print(phone_book.lookup_number("John"))  # Output: 1234567890

    # Look up a name by phone number
    print(phone_book.lookup_name("9876543210"))  # Output: Alice
