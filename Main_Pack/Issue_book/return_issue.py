import sqlite3
from datetime import date

# Establish a connection to the database
conn = sqlite3.connect('library_management.db')


# Function to return a book
def return_book():
    book_id = input("Enter Book ID: ")
    user_id = input("Enter User ID: ")

    # Check if the book exists
    book_query = "SELECT * FROM books WHERE id = ?"
    book_result = conn.execute(book_query, (book_id,)).fetchone()
    if not book_result:
        print("Book not found.")
        return

    # Check if the user exists
    user_query = "SELECT * FROM users WHERE id = ?"
    user_result = conn.execute(user_query, (user_id,)).fetchone()
    if not user_result:
        print("User not found.")
        return

    # Check if the book is issued to the user
    issued_query = "SELECT * FROM records WHERE userID = ? AND bookID = ?"
    issued_result = conn.execute(issued_query, (user_id, book_id)).fetchone()
    if not issued_result:
        print("Book is not issued to the user.")
        return

    today_date = date.today()
    return_date = today_date.strftime("%Y-%m-%d")

    # Update the book's availability
    update_query = "UPDATE books SET available = 1 WHERE id = ?"
    conn.execute(update_query, (book_id,))

    # Update the return date in the records table
    return_query = "UPDATE records SET returnDate = ? WHERE userID = ? AND bookID = ?"
    conn.execute(return_query, (return_date, user_id, book_id))

    conn.commit()
    print("Book returned successfully.")
