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
    def _init_(self):

        self.library_data = {}

    def add_author(self, author):
        if author not in self.library_data:
            self.library_data[author] = []
            print(f"Author '{author}' added.")
        else:
            print(f"Author '{author}' already exists.")

    # Method to add a book to an existing author
    def add_book(self, author, book):
        if author in self.library_data:
            self.library_data[author].append(book)
            print(f"Added '{book}' by {author}.")
        else:
            print(f"Author '{author}' does not exist. Please add the author first.")

    # Method to remove a book from the library
    def remove_book(self, author, book):
        if author in self.library_data and book in self.library_data[author]:
            self.library_data[author].remove(book)
            print(f"Removed '{book}' by {author}.")

        elif book not in self.library_data[author]:
            print(f"Could not find '{book}' by {author} to remove.")

    def search_by_title(self, book):
        found = False
        for author, books in self.library_data.items():
            if book in books:
                print(f"Book found: '{book}' by {author}")
                found = True
                break
        if not found:
            print(f"Book titled '{book}' not found.")

    # Method to search for a book by author
    def search_by_author(self, author):
        if author in self.library_data:
            books = self.library_data[author]
            print(f"Books by {author}: ", books)
        else:
            print(f"Author '{author}' does not exist. Please add the author first.")


def display_menu():
    print("\nWelcome to the Library!!!")
    print("1. Search by book title")
    print("2. Search by author")
    print("3. Add an author")
    print("4. Add a book to an author")
    print("5. Remove a book")
    print("6. Quit")


def run_library_menu():
    library = Library()  # Create an instance of the Library class
    menu_options = ('1', '2', '3', '4', '5', '6')

    while True:
        display_menu()
        option = input("Enter option: ")
        if option in menu_options:
            if option == '1':
                title = input("Enter the book title to search: ")
                library.search_by_title(title)
            elif option == '2':
                author = input("Enter the author's name to search: ")
                library.search_by_author(author)
            elif option == '3':
                author = input("Enter the author's name to add: ")
                library.add_author(author)
            elif option == '4':
                author = input("Enter the author's name: ")
                book = input("Enter the book title: ")
                library.add_book(author, book)
            elif option == '5':
                author = input("Enter the author's name: ")
                book = input("Enter the book title to remove: ")
                library.remove_book(author, book)
            elif option == '6':
                print("Exiting the library system.")
                break  # Exit the menu loop
            else:
                print("Invalid input. Please try again.")


run_library_menu()
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

