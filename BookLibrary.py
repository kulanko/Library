class Book:
    def __init__(self, title, author):  # Correct constructor
        self.__title = title  # Strip any extra whitespace
        self.__author = author  # Strip any extra whitespace

    # Getter for title
    def get_title(self):
        return self.__title

    # Getter for author
    def get_author(self):
        return self.__author

    # String representation of the Book
    def __str__(self):  # Correct method name for string representation
        return f"'{self.get_title()}' by {self.get_author()}"


# Derived class EBook inheriting from Book
class EBook(Book):
    def __init__(self, title, author, file_size):  # Correct constructor
        super().__init__(title, author)  # Inheriting from the Book class
        self.__file_size = file_size  # Additional attribute for EBook

    # Getter for file size
    def get_file_size(self):
        return self.__file_size

    # Overriding the string representation of the Book class
    def __str__(self):  # Correct method name for string representation
        return f"'{self.get_title()}' by {self.get_author()} (File size: {self.__file_size} MB)"


class Library:
    def __init__(self):  # Correct constructor
        self.__books = []  # Private attribute to hold books

    # Method to add a book
    def add_book(self, book):
        if isinstance(book, Book):  # Ensuring only Book instances can be added
            self.__books.append(book)
            print(f"Book '{book.get_title()}' by {book.get_author()} added to the library.")
        else:
            print("Only instances of Book can be added.")

    # Method to remove a book by title
    def remove_book(self, title):
        for book in self.__books:
            if book.get_title().strip().lower() == title.strip().lower():
                self.__books.remove(book)
                print(f"Book '{title}' removed from the library.")
                return
        print(f"Book '{title}' not found in the library.")

    # Method to search for a book by title
    def search_by_title(self, title):
        for book in self.__books:
            if book.get_title().strip().lower() == title.strip().lower():
                print(f"Found: {book}")
                return
        print(f"No book with title '{title}' found.")

    # Method to search for books by author
    def search_by_author(self, author):
        found_books = [book for book in self.__books if book.get_author().strip().lower() == author.strip().lower()]
        if found_books:
            print(f"Books by {author}:")
            for book in found_books:
                print(f"- {book}")
        else:
            print(f"No books by {author} found.")


# Example usage
library = Library()

# Adding books
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
ebook1 = EBook("Digital Fortress", "Dan Brown", 5.0)

library.add_book(book1)
library.add_book(book2)
library.add_book(ebook1)

# Searching for books
library.search_by_title("1984")
library.search_by_author("George Orwell")

# Removing a book
library.remove_book("1984")

# Searching again after removal
library.search_by_title("1984")

# Checking the EBook
library.search_by_title("Digital Fortress")
