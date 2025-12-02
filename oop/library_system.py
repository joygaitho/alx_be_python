class Book:
    """
    Base Class: Represents a generic book.
    """
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """
    Derived Class: Represents an electronic book.
    Inherits from Book.
    """
    def __init__(self, title, author, file_size):
        # Call the constructor of the base class (Book)
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """
    Derived Class: Represents a physical printed book.
    Inherits from Book.
    """
    def __init__(self, title, author, page_count):
        # Call the constructor of the base class (Book)
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """
    Composition Class: Manages a collection of books.
    """
    def __init__(self):
        # Composition: The library 'has a' list of books
        self.books = []

    def add_book(self, book):
        """
        Adds a Book, EBook, or PrintBook instance to the library.
        """
        if isinstance(book, Book):
            self.books.append(book)
            print(f"Added: {book.title}")
        else:
            print("Error: Only instances of Book (or subclasses) can be added.")

    def list_books(self):
        """
        Prints details of each book in the library.
        """
        if not self.books:
            print("The library is empty.")
        else:
            for book in self.books:
                # Polymorphism: This calls the specific __str__ method 
                # for whatever type of book (EBook or PrintBook) is in the list.
                print(book)


# --- Example Usage ---
if __name__ == "__main__":
    # Create the Library instance
    my_library = Library()

    # Create instances of different book types
    generic_book = Book("The Great Gatsby", "F. Scott Fitzgerald")
    ebook = EBook("Python 101", "Mike Driscoll", 5) 
    print_book = PrintBook("Clean Code", "Robert C. Martin", 464)

    # Add books to the library
    my_library.add_book(generic_book)
    my_library.add_book(ebook)
    my_library.add_book(print_book)

    # List all books
    my_library.list_books()