import csv

def read_contacts(file_path):
    """
    Reads contacts from a CSV file.
    
    Args:
    file_path (str): The path to the CSV file.
    
    Returns:
    list of dict: A list of contacts where each contact is represented as a dictionary.
    """
    contacts = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            contacts.append(row)
    return contacts

def remove_duplicates(contacts):
    """
    Removes duplicate contacts based on name and contact information.
    
    Args:
    contacts (list of dict): The list of contacts.
    
    Returns:
    list of dict: A list of contacts with duplicates removed.
    """
    seen = set()
    unique_contacts = []
    for contact in contacts:
        identifier = (contact['name'], contact['contact'])
        if identifier not in seen:
            seen.add(identifier)
            unique_contacts.append(contact)
    return unique_contacts

def write_contacts(file_path, contacts):
    """
    Writes contacts to a CSV file.
    
    Args:
    file_path (str): The path to the CSV file.
    contacts (list of dict): The list of contacts to write.
    """
    with open(file_path, mode='w', newline='') as file:
        fieldnames = contacts[0].keys()
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()
        csv_writer.writerows(contacts)

def main(input_file, output_file):
    """
    Main function to read, remove duplicates, and write contacts.
    
    Args:
    input_file (str): The path to the input CSV file.
    output_file (str): The path to the output CSV file.
    """
    contacts = read_contacts(input_file)
    unique_contacts = remove_duplicates(contacts)
    write_contacts(output_file, unique_contacts)

if __name__ == "__main__":
    # Example usage: Replace 'input.csv' and 'output.csv' with actual file paths
    main('input.csv', 'output.csv')
