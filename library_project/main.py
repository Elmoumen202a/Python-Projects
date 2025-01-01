class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        # Adds a book to the library
        self.books.append({"title": title, "author": author})
        print(f"'{title}' by {author} has been added to the library.")

    def remove_book(self, title):
        # Removes a book from the library by its title
        for book in self.books:
            if book["title"].lower() == title.lower():
                self.books.remove(book)
                print(f"'{title}' has been removed from the library.")
                return
        print(f"Book titled '{title}' not found.")

    def search_book(self, title):
        # Searches for a book by its title
        for book in self.books:
            if book["title"].lower() == title.lower():
                print(f"Found: '{book['title']}' by {book['author']}")
                return
        print(f"No book titled '{title}' found.")

# usage
if __name__ == "__main__":
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter the book title: ")
            author = input("Enter the book author: ")
            library.add_book(title, author)
        elif choice == "2":
            title = input("Enter the book title to remove: ")
            library.remove_book(title)
        elif choice == "3":
            title = input("Enter the book title to search for: ")
            library.search_book(title)
        elif choice == "4":
            print("Exiting the Library Management System. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
