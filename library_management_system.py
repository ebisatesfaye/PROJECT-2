class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.checked_out = False

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            print(f"Book '{self.title}' checked out.")
        else:
            print(f"Book '{self.title}' is already checked out.")

    def check_in(self):
        if self.checked_out:
            self.checked_out = False
            print(f"Book '{self.title}' checked in.")
        else:
            print(f"Book '{self.title}' was not checked out.")

    def __str__(self):
        status = "Checked Out" if self.checked_out else "Available"
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        for book in self.books:
            print(book)


# Example usage
book1 = Book("1984", "George Orwell", "1234567890")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "0987654321")

library = Library()
library.add_book(book1)
library.add_book(book2)

library.show_books()

book1.check_out()
book2.check_in()

library.show_books()
