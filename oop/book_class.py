class Book: # class definition
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def __del__(self):
        print(f"Deleting {self.title}")
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}."
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
if __name__ == "__main__":
    book = Book("1984", "George Orwell", 1949)
    print(book)  # Uses __str__
    print("Testing __repr__ method (developer-friendly)")
    print(repr(book))  # Uses __repr__
    print("Both representations side by side")
    print(f"str(): {str(book)}")
    print(f"repr(): {repr(book)}")
    print("Testing that __repr__ can recreate the object")
    # The __repr__ output should be valid Python code
    recreated_book = eval(repr(book))
    print(f"Original: {book}")
    print(f"Recreated: {recreated_book}")
    print("Objects will be deleted when program ends")
    # __del__ will be called automatically