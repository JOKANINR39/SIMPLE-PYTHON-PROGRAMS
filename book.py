def display_books(books):
    if books:
        print("\nList of Books:")
        for book in books:
            print(book)
    else:
        print("No books available in the list.")

def add_book(books):
    book_name = input("Enter the name of the book to add: ")
    books.append(book_name)
    print(f"Book '{book_name}' added to the list.")


def remove_book(books):
    book_name = input("Enter the name of the book to remove: ")
    if book_name in books:
        books.remove(book_name)
        print(f"Book '{book_name}' removed from the list.")
    else:
        print(f"Book '{book_name}' not found in the list.")


def sort_books(books):
    books.sort()
    print("\nBooks sorted alphabetically.")


def reverse_books(books):
    books.reverse()
    print("\nBooks list has been reversed.")


def get_total_books(books):
    return len(books)


def book_management_system():
    books = []  
    while True:
        print("\n--- Book Management System ---")
        print("1. Display List of Books")
        print("2. Add a Book")
        print("3. Remove a Book")
        print("4. Sort Books Alphabetically")
        print("5. Reverse the List of Books")
        print("6. Show Total Number of Books")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            display_books(books)
        elif choice == '2':
            add_book(books)
        elif choice == '3':
            remove_book(books)
        elif choice == '4':
            sort_books(books)
            display_books(books)
        elif choice == '5':
            reverse_books(books)
            display_books(books)
        elif choice == '6':
            print(f"Total number of books: {get_total_books(books)}")
        elif choice == '7':
            print("Exiting the Book Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")


book_management_system()

output

--- Book Management System ---
1. Display List of Books
2. Add a Book
3. Remove a Book
4. Sort Books Alphabetically
5. Reverse the List of Books
6. Show Total Number of Books
7. Exit
Enter your choice (1-7): 1
No books available in the list.

--- Book Management System ---
1. Display List of Books
2. Add a Book
3. Remove a Book
4. Sort Books Alphabetically
5. Reverse the List of Books
6. Show Total Number of Books
7. Exit
Enter your choice (1-7): 2
Enter the name of the book to add: alchemist
Book 'alchemist' added to the list.

--- Book Management System ---
1. Display List of Books
2. Add a Book
3. Remove a Book
4. Sort Books Alphabetically
5. Reverse the List of Books
6. Show Total Number of Books
7. Exit
Enter your choice (1-7): 3
Enter the name of the book to remove: alchemist
Book 'alchemist' removed from the list.

--- Book Management System ---
1. Display List of Books
2. Add a Book
3. Remove a Book
4. Sort Books Alphabetically
5. Reverse the List of Books
6. Show Total Number of Books
7. Exit
Enter your choice (1-7): 4

Books sorted alphabetically.
No books available in the list.

--- Book Management System ---
1. Display List of Books
2. Add a Book
3. Remove a Book
4. Sort Books Alphabetically
5. Reverse the List of Books
6. Show Total Number of Books
7. Exit
Enter your choice (1-7): 5

Books list has been reversed.
No books available in the list.

--- Book Management System ---
1. Display List of Books
2. Add a Book
3. Remove a Book
4. Sort Books Alphabetically
5. Reverse the List of Books
6. Show Total Number of Books
7. Exit
Enter your choice (1-7): 6
Total number of books: 0

--- Book Management System ---
1. Display List of Books
2. Add a Book
3. Remove a Book
4. Sort Books Alphabetically
5. Reverse the List of Books
6. Show Total Number of Books
7. Exit
Enter your choice (1-7): 
​