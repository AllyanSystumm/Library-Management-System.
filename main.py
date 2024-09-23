import datetime

# Class representing a book
class Book:
    def __init__(self, title, author, genre, published_year):
        self.title = title
        self.author = author
        self.genre = genre
        self.published_year = published_year
        self.is_available = True
    
    def __str__(self):
        availability = "Available" if self.is_available else "Borrowed"
        return f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Year: {self.published_year}, Status: {availability}"


# Class representing a member of the library
class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
    
    def borrow_book(self, book):
        if book.is_available:
            self.borrowed_books.append(book)
            book.is_available = False
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"Sorry, '{book.title}' is already borrowed.")
    
    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_available = True
            print(f"{self.name} returned '{book.title}'")
        else:
            print(f"{self.name} does not have '{book.title}'")
    
    def __str__(self):
        borrowed_titles = ', '.join([book.title for book in self.borrowed_books]) if self.borrowed_books else "None"
        return f"Member: {self.name}, ID: {self.member_id}, Borrowed Books: {borrowed_titles}"


# Class representing the library
class Library:
    def __init__(self):
        self.books = []
        self.members = []
    
    # Adding a new book to the library
    def add_book(self, title, author, genre, year):
        book = Book(title, author, genre, year)
        self.books.append(book)
        print(f"Book '{title}' added to the library.")
    
    # Removing a book from the library
    def remove_book(self, title):
        for book in self.books:
            if book.title == title and book.is_available:
                self.books.remove(book)
                print(f"Book '{title}' removed from the library.")
                return
        print(f"Book '{title}' not found or is currently borrowed.")
    
    # Searching for a book
    def search_book(self, title=None, author=None, genre=None):
        results = [book for book in self.books if
                   (title and title.lower() in book.title.lower()) or
                   (author and author.lower() in book.author.lower()) or
                   (genre and genre.lower() in book.genre.lower())]
        if results:
            print("\nSearch Results:")
            for book in results:
                print(book)
        else:
            print("No matching books found.")
    
    # Listing all available books
    def list_books(self):
        print("\nLibrary Books:")
        for book in self.books:
            print(book)
    
    # Adding a member to the library
    def add_member(self, name, member_id):
        member = Member(name, member_id)
        self.members.append(member)
        print(f"Member '{name}' added to the library.")
    
    # Removing a member from the library
    def remove_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                self.members.remove(member)
                print(f"Member '{member.name}' removed from the library.")
                return
        print(f"Member with ID '{member_id}' not found.")
    
    # Borrowing a book
    def borrow_book(self, member_id, title):
        member = self.get_member(member_id)
        book = self.get_book(title)
        if member and book:
            member.borrow_book(book)
    
    # Returning a book
    def return_book(self, member_id, title):
        member = self.get_member(member_id)
        book = self.get_book(title)
        if member and book:
            member.return_book(book)
    
    # Displaying the borrowing history of a member
    def display_member_info(self, member_id):
        member = self.get_member(member_id)
        if member:
            print(member)
        else:
            print(f"No member found with ID '{member_id}'")

    # Helper method to get a book by title
    def get_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        print(f"Book '{title}' not found.")
        return None
    
    # Helper method to get a member by ID
    def get_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        print(f"Member with ID '{member_id}' not found.")
        return None


# Main menu for interacting with the library
def main():
    library = Library()
    
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. List All Books")
        print("5. Add Member")
        print("6. Remove Member")
        print("7. Borrow Book")
        print("8. Return Book")
        print("9. Display Member Info")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            genre = input("Enter book genre: ")
            year = input("Enter book published year: ")
            library.add_book(title, author, genre, year)
        
        elif choice == '2':
            title = input("Enter book title to remove: ")
            library.remove_book(title)
        
        elif choice == '3':
            print("Search by:")
            search_choice = input("1. Title\n2. Author\n3. Genre\nEnter your choice: ")
            if search_choice == '1':
                title = input("Enter book title to search: ")
                library.search_book(title=title)
            elif search_choice == '2':
                author = input("Enter author to search: ")
                library.search_book(author=author)
            elif search_choice == '3':
                genre = input("Enter genre to search: ")
                library.search_book(genre=genre)
        
        elif choice == '4':
            library.list_books()
        
        elif choice == '5':
            name = input("Enter member name: ")
            member_id = input("Enter member ID: ")
            library.add_member(name, member_id)
        
        elif choice == '6':
            member_id = input("Enter member ID to remove: ")
            library.remove_member(member_id)
        
        elif choice == '7':
            member_id = input("Enter member ID: ")
            title = input("Enter book title to borrow: ")
            library.borrow_book(member_id, title)
        
        elif choice == '8':
            member_id = input("Enter member ID: ")
            title = input("Enter book title to return: ")
            library.return_book(member_id, title)
        
        elif choice == '9':
            member_id = input("Enter member ID: ")
            library.display_member_info(member_id)
        
        elif choice == '0':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")


# Running the main function
if __name__ == "__main__":
    main()
