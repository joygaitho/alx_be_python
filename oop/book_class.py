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
book = Book('1984', 'George Orwell', 1949)
print(str(book)) # uses __str__
print(repr(book)) # uses __repr__