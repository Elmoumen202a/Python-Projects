# Contact Deduplication Project

This project is designed to read a CSV file containing contact information, remove any duplicate entries based on the name and contact information, and write the deduplicated contacts back to a CSV file.

## Files

- `main.py`: Contains the main functionality to read, process, and write contacts.
- `test.py`: Contains unit tests for the contact deduplication functions.
- `README.md`: This file. It explains the project structure and usage.

## Usage

1. Ensure you have Python installed.
2. Prepare an input CSV file (`input.csv`) with the following structure:
    ```csv
    name,contact
    John Doe,1234567890
    Jane Smith,0987654321
    John Doe,1234567890
    Alice Brown,1112223333
    ```
3. Run the `main.py` script:
    ```bash
    python main.py
    ```
4. The deduplicated contacts will be written to `output.csv`.

## Testing

To run the tests, execute the following command:
```bash
python -m unittest test.py
