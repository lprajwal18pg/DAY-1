class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"{self.title} by {self.author}"


def sort_books(books, key):
    """Sorts a list of books based on the provided key."""
    return sorted(books, key=lambda book: getattr(book, key))


def get_book_details():
    """book details from the user."""
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    return Book(title, author)


def main():
    books = []

    while True:
        print("\nOptions:")
        print("Add a book")
        print("Sort books")
        print("View books")
        print("Quit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            book = get_book_details()
            books.append(book)
            print(f"Added book: {book}")
        elif choice == "2":
            if not books:
                print("No books to sort. Please add some books first.")
                continue

            print("\nSorting Options:")
            print("1. Sort by Title")
            print("2. Sort by Author")

            sort_choice = input("Enter your choice (1/2): ")

            if sort_choice == "1":
                sorted_books = sort_books(books, "title")
                print("\nSorted Books by Title:")
                for book in sorted_books:
                    print(book)
            elif sort_choice == "2":
                sorted_books = sort_books(books, "author")
                print("\nSorted Books by Author:")
                for book in sorted_books:
                    print(book)
            else:
                print("Invalid choice. Please try again.")
        elif choice == "3":
            if not books:
                print("No books to view. Please add some books first.")
                continue

            print("\nAvailable Books:")
            for book in books:
                print(book)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()