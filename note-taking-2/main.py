import os

def display_menu():
    print("Note-Taking App")
    print("1. View Notes")
    print("2. Add Note")
    print("3. Exit")

def view_notes():
    try:
        with open("notes.txt", "r") as file:
            notes = file.read()
            if notes:
                print("Your Notes:")
                print(notes)
            else:
                print("No notes found.")
    except FileNotFoundError:
        print("No notes found.")

def add_note():
    note = input("Enter your note: ")
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("Note added successfully.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            view_notes()
        elif choice == "2":
            add_note()
        elif choice == "3":
            print("Exiting Note-Taking App.")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
