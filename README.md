GROUP MEMBERS

ELSIE CHERUIYOT,

ALEX GITONGA,

INNOCENT,

BONIFACE KULANKO,

JEFFREY GITUKU.


This project is a Library Management System created using Python’s Object-Oriented Programming (OOP) concepts. It allows users to manage a collection of books, add new books, search for books by title or author, and remove books. There’s also functionality to handle different book types like eBooks and audiobooks.
Classes, Attributes, and Methods
Class: Book

Attributes:
title: The title of the book.

author: The author of the book.

Methods:
__init__(self, title, author): Initializes the book with a title and an author.
__str__(self): Returns a string representation of the book.

Class: Library

Attributes:
books: A list to store the books in the library.

Methods:
__init__(self): #Initializes an empty list of books.

add_book(self, book): Adds a book to the library.

remove_book(self, title): Removes a book by its title.

search_by_title(self, title): Searches for a book by its title.

search_by_author(self, author): Searches for books by a specific author.

Class: Type (inherits from Book)

Attributes:
file_format: The format of the book (e.g., PDF, MP3).
book_type: The type of book (eBook, audiobook, etc.).
Methods:
__init__(self, title, author, file_format, book_type): Initializes a book with additional attributes for format and type.
identify_book_type(self): Returns a string indicating the book type (eBook, audiobook, etc.).

OOP Concepts Utilized
Encapsulation: The attributes of each class (like title, author, and books) are managed by their respective classes to ensure proper access and modifications.

Inheritance: The Type class inherits from the Book class, allowing it to reuse the attributes and methods from Book.

Polymorphism: The identify_book_type method in Type is an example where the behavior differs based on the type of book (eBook or audiobook).

MEMBERS ROLES
 ELSIE CHERUIYOT:  Introduction and Sammary at the end.
 
 BONIFACE KULANKO: Inheritance.
 
 INNOCENT ALVIN:   Encapsulation.
 
 JEFF GITUKU:  
 
 ALEX GITONGA: 
 
 

