# Telephone Book

This Python project implements a simple telephone book that allows you to look up phone numbers by name and vice versa.

## Features
- Add entries to the telephone book with names and numbers.
- Look up a phone number by name.
- Look up a name by phone number.

## Usage
1. Clone the repository.
2. Run `python test.py` to execute the test cases and ensure the functionality.
3. Integrate `telephone_book.py` into your own project by importing the `TelephoneBook` class and utilizing its methods.

## Example
```python
phone_book = TelephoneBook()
phone_book.add_entry("John", "1234567890")
phone_book.add_entry("Alice", "9876543210")

print(phone_book.lookup_number("John"))  # Output: 1234567890
print(phone_book.lookup_name("9876543210"))  # Output: Alice
