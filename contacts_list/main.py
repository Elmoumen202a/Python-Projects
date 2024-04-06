# Define a class to manage contacts
class ContactsList:
    def __init__(self):
        # Initialize an empty dictionary to store contacts
        self.contacts = {}

    # Method to add a contact
    def add_contact(self, name, number):
        self.contacts[name] = number

    # Method to delete a contact
    def delete_contact(self, name):
        # Check if the contact exists in the dictionary
        if name in self.contacts:
            # Delete the contact if it exists
            del self.contacts[name]
        else:
            print("Contact not found.")

    # Method to search for a contact
    def search_contact(self, name):
        # Check if the contact exists in the dictionary
        if name in self.contacts:
            # Return the contact details
            return f"Name: {name}, Number: {self.contacts[name]}"
        else:
            return "Contact not found."

    # Method to display all contacts
    def display_all_contacts(self):
        # Check if there are any contacts in the dictionary
        if self.contacts:
            # Iterate through the contacts and display them
            for name, number in self.contacts.items():
                print(f"Name: {name}, Number: {number}")
        else:
            print("Contacts list is empty.")
