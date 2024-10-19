class Book:
    def __init__(self, title, author):  # Constructor to initialize book attributes
        self.__title = title
        self.__author = author

    # Getter for title
    def get_title(self):
        return self.__title

    # Getter for author
    def get_author(self):
        return self.__author

    # String representation of the Book (implicitly called when the object is printed)
    def __str__(self):
        return f"'{self.get_title()}' by {self.get_author()}"


# Derived class EBook inheriting from Book
class EBook(Book):
    def __init__(self, title, author, file_size):  # Constructor for EBook
        super().__init__(title, author)  # Inheriting attributes from Book
        self.__file_size = file_size  # Additional attribute for EBook

    # Getter for file size
    def get_file_size(self):
        return self.__file_size

    # Overriding the string representation of the Book class (for EBook)
    def __str__(self):  # Custom string representation for EBook
        return f"'{self.get_title()}' by {self.get_author()} (File size: {self.__file_size} pages)"


# Library class to manage books
class Library:
    def __init__(self):  # Constructor to initialize the library's book list
        self.__books = []  # Private attribute to hold books

    # Method to add a book to the library
    def add_book(self, book):
        if isinstance(book, Book):  # Ensuring only Book instances are added
            self.__books.append(book)
            # Implicitly calling the __str__ method of book here using print()
            print(f"Book added to the library: {book}")  # Implicit __str__()
        else:
            print("Only instances of Book or EBook can be added.")

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
                # Implicitly calling the __str__ method when printing
                print(f"Found: {book}")  # Implicit __str__()
                return
        print(f"No book with title '{title}' found.")

    # Method to search for books by author
    def search_by_author(self, author):
        found_books = [book for book in self.__books if book.get_author().strip().lower() == author.strip().lower()]
        if found_books:
            print(f"Books by {author}:")
            for book in found_books:
                # Implicitly calling the __str__ method when printing each book
                print(f"- {book}")  # Implicit __str__()
        else:
            print(f"No books by {author} found.")


# Example usage of the classes
library = Library()

# Creating instances of Book and EBook
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
ebook1 = EBook("Digital Fortress", "Dan Brown", 500)

# Adding books to the library (implicitly calling __str__ method)
library.add_book(book1)
library.add_book(book2)
library.add_book(ebook1)

# Searching for books (implicitly calling __str__ method)
library.search_by_title("1984")
library.search_by_author("George Orwell")

# Explicitly calling the __str__ method for each book
print("...................................................................................................")
print("\nNow we can explicitly call the __str__ method used to print the books:\n")
print(book1.__str__())  # Explicit __str__ call for book1
print(book2.__str__())
print(ebook1.__str__())  #Explicit __str__ call for ebook1

# Removing a book
library.remove_book("1984")

# Searching again after removal
library.search_by_title("1984")

# Checking the EBook
library.search_by_title("Digital Fortress")

