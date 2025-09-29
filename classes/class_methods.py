class book:
    total_books = 0 # total number of books created

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        book.total_books += 1

    
    # I want to create a method which will work with total_books
    #class method
    @classmethod
    def reset_total_books(cls):
        """Reset the total book count to zero"""
        cls.total_books = 0

    @classmethod
    def from_dict(cls, data: dict):
        return cls(data["title"], data["author"], data["year"])
    
book1 = book("Python 101", "J.Doe", 2023)
data = {"title": "Learning Python", "author": "John smith", "year": 2020}
book2 = book.from_dict(data)

print (book1)
print (book2)