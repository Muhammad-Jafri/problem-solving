import uuid


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            return True

        return False

    def return_book(self):
        self.available = True

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {'Available' if self.available else 'Borrowed'}"


class User:
    def __init__(self, name, max_books=3):  # Added max_books with a default value
        self.name = name
        self.borrowed_books = []
        self.id = str(uuid.uuid4())
        self.max_books = max_books  # Max books a user can borrow

    def borrow_book(self, book) -> str:
        if len(self.borrowed_books) >= self.max_books:  # Check limit first
            return f"You can't borrow more than {self.max_books} books."

        if not book.borrow():  # Check if book is available
            return f"Sorry, {book.title} is not available."

        self.borrowed_books.append(book)  # Add book to borrowed list
        return f"{self.name} successfully borrowed '{book.title}'."

    def return_book(self, book):
        for borrowed in self.borrowed_books:
            if borrowed.isbn == book.isbn:  # Compare by ISBN
                borrowed.return_book()  # Mark the book as available
                self.borrowed_books.remove(borrowed)  # Remove from list
                return f"{self.name} returned '{book.title}'."

        return f"{self.name} doesn't have '{book.title}'."

    def get_borrowed_books(self):
        return self.borrowed_books

    def __str__(self):
        return f"{self.name} with {self.id} has the followed books -> {self.borrowed_books}"


class PremiumUser(User):
    def __init__(self, name, max_books=10):  # Higher default limit
        super().__init__(name, max_books)

    def force_borrow(self, book):
        """Allows premium users to borrow even if the book is unavailable."""
        if len(self.borrowed_books) >= self.max_books:
            return f"You can't borrow more than {self.max_books} books."

        if book.borrow():
            self.borrow_book(book)
            book.b
            return f"book borrowed gracefully"

        book.available = False  # Force borrow by overriding availability
        self.borrowed_books.append(book)
        return f"{self.name} force borrowed '{book.title}', even though it was unavailable."


if __name__ == "__main__":
    # Create a book
    book1 = Book("The Alchemist", "Paulo Coelho", "978-0061122415")

    # Create a regular user
    user1 = User("John Doe")

    # John borrows the book
    print(
        user1.borrow_book(book1)
    )  # ✅ "John Doe successfully borrowed 'The Alchemist'."

    # Trying to borrow the same book again (should fail)
    print(user1.borrow_book(book1))  # ❌ "Sorry, The Alchemist is not available."

    # Returning the book
    print(user1.return_book(book1))  # ✅ "John Doe returned 'The Alchemist'."

    # Borrowing again after returning
    print(
        user1.borrow_book(book1)
    )  # ✅ "John Doe successfully borrowed 'The Alchemist'."

    # Create multiple books
    book2 = Book("1984", "George Orwell", "978-0451524935")
    book3 = Book("To Kill a Mockingbird", "Harper Lee", "978-0060935467")

    # John has a borrowing limit of 3 (default)
    print(user1.borrow_book(book2))  # ✅ "John Doe successfully borrowed '1984'."
    print(
        user1.borrow_book(book3)
    )  # ✅ "John Doe successfully borrowed 'To Kill a Mockingbird'."

    # Borrowing a fourth book (should fail)
    book4 = Book("Brave New World", "Aldous Huxley", "978-0060850524")
    print(user1.borrow_book(book4))  # ❌ "You can't borrow more than 3 books."

    # Create a premium user (higher borrowing limit)
    premium_user = PremiumUser("Alice", max_books=5)

    # Alice borrows multiple books
    print(
        premium_user.force_borrow(book1)
    )  # ✅ "Alice successfully borrowed 'The Alchemist'."
    print(premium_user.force_borrow(book2))  # ✅ "Alice successfully borrowed '1984'."
    print(
        premium_user.force_borrow(book3)
    )  # ✅ "Alice successfully borrowed 'To Kill a Mockingbird'."
    print(
        premium_user.force_borrow(book4)
    )  # ✅ "Alice successfully borrowed 'Brave New World'."

    # Borrowing a 5th book (should still work for PremiumUser)
    book5 = Book("Moby-Dick", "Herman Melville", "978-1503280786")
    print(
        premium_user.force_borrow(book5)
    )  # ✅ "Alice successfully borrowed 'Moby-Dick'."

    # Borrowing a 6th book (should fail)
    book6 = Book("Pride and Prejudice", "Jane Austen", "978-1503290563")
    print(premium_user.force_borrow(book6))  # ❌ "You can't borrow more than 5 books."
