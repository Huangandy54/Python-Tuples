# Task 1: Library System Enhancement Sharpen your skills in managing and modifying data within tuples and lists.

# Problem Statement: You are maintaining a library system where each book is stored as a tuple within a list. Your task is to update this system by adding new books and ensuring no duplicates.

# Existing Library Data:

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
# - Add functionality to insert new books into `library`. Ensure that adding a duplicate book is handled appropriately.

def add_book(new_book):
    if new_book in library:
        print("This book already exists in the library.")
    else:
        library.append(new_book)

add_book(("1984","George Orwell"))
add_book(("123","1234"))
print(library)