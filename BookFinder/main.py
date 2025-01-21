import requests

# Base URL for Open Library API
API_URL = "https://openlibrary.org/search.json"

def find_books_by_title(title):
    """
    Search for books by title using the Open Library API.
    :param title: The title of the book to search for.
    :return: A list of books matching the title.
    """
    response = requests.get(API_URL, params={"title": title})
    if response.status_code == 200:
        data = response.json()
        return data.get("docs", [])[:10]  # Return the top 10 results
    else:
        return []

def display_books(books):
    """
    Display a list of books in a readable format.
    :param books: A list of books to display.
    """
    if not books:
        print("No books found.")
        return

    print("\nBooks Found:")
    for i, book in enumerate(books, start=1):
        title = book.get("title", "Unknown Title")
        author = ", ".join(book.get("author_name", ["Unknown Author"]))
        year = book.get("first_publish_year", "Unknown Year")
        print(f"{i}. {title} by {author} (Published: {year})")

if __name__ == "__main__":
    print("Welcome to Book Finder!")
    search_title = input("Enter the book title to search for: ").strip()
    if search_title:
        books = find_books_by_title(search_title)
        display_books(books)
    else:
        print("Please provide a valid book title.")
