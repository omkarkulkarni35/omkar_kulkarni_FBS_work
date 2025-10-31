class Book:
    def __init__(self, bid, name, price, author):
        self.bid = bid
        self.name = name
        self.price = price
        self.author = author

    def display(self):
        print(f"ID: {self.bid}, Name: {self.name}, Price: ₹{self.price}, Author: {self.author}")

book_dict = {}

def add_book():
    bid = input("Enter Book ID: ")
    if bid in book_dict:
        print("Book ID already exists!")
        return
    name = input("Enter Book Name: ")
    price = float(input("Enter Book Price: "))
    author = input("Enter Author Name: ")
    book_dict[bid] = Book(bid, name, price, author)
    print("Book added successfully!")

def delete_book():
    bid = input("Enter Book ID to delete: ")
    if bid in book_dict:
        del book_dict[bid]
        print("Book deleted successfully!")
    else:
        print("Book ID not found.")

def display_all_books():
    if not book_dict:
        print("No books available.")
    else:
        print("\n--- Book List ---")
        for book in book_dict.values():
            book.display()

def search_book():
    bid = input("Enter Book ID to search: ")
    if bid in book_dict:
        print("Book found:")
        book_dict[bid].display()
    else:
        print("Book not found.")

ch = 0
while(ch != 6):
    print("\n--- Book Menu ---")
    print("1. Add Book")
    print("2. Delete Book by ID")
    print("3. Display All Books")
    print("4. Search Book by ID")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_book()
    elif choice == '2':
        delete_book()
    elif choice == '3':
        display_all_books()
    elif choice == '4':
        search_book()
    elif choice == '5':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")