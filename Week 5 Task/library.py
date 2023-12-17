# Create Book Class
class Book:
    def __int__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __init__(self):
        self.availability_status = True

    def display_books_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")

    def borrow_book(self):
        if self.availability_status:
            self.availability_status = False
            print(f"{self.title} has been borrowed.")
        else:
            print(f"{self.title} is currently borrowed ")

    def return_book(self):
        if not self.availability_status:
            print(f"Thank you for returning {self.title}.")
        else:
            print(f"{self.title} is already available in the library.")


# Create User Class
class User:
    def __int__(self, user_id, name, books_borrowed, returning_books):
        self.user_id = user_id
        self.name = name
        self.books_borrowed = []

    def display_user_detail(self):
        print(f"User name: {self.name}")
        print(f"User id: {self.user_id}")

    def borrow_book(self, book):
        if book.availability_status:
            book.availability_status = False
            self.books_borrowed.append(book.title)
            print(f"{self.name} has borrowed {book.title}")
        else:
            print(f"{self.name} are not borrowed books from Library")


# Create Library Class
class Library:
    def __int__(self):
        self.books = []
        self.user_info = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book {book.title} has been added to Library!")

    def new_user(self, user):
        self.user_info.append(user)
        print(f"{user.name} has been registered and his ID is {user.user_id}")

    def book_transaction(self, user, book_title, action):
        book = next((bo for bo in self.books if bo.title == book_title), None)

        if book is not None:
            if action == "borrow":
                user.borrow_book(book)
            elif action == "return":
                user.return_book(book)
            else:
                print("Invalid action. You can only 'borrow' or 'return' book.")
        else:
            print(f"Book '{book_title}' is not exist in the library.")


# Create Transaction Class
class Transaction:
    def __int__(self, user_name, user_id, book, action):
        self.user_name = user_name
        self.user_id = user_id
        self.book = book
        self.action = action

    def transaction_info(self):
        print(f"Transaction: {id(self)}")
        print(f"User name: {self.user_name}")
        print(f"User ID no: {self.user_id}")
        print(f"Books: {self.book}")
        print(f"Action: {self.action}")
