import sqlite3
from datetime import date

# Establish a connection to the database
conn = sqlite3.connect('library_management.db')

# Function to issue a book to a user
def issue_book_to_user():
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

    # Check if the book is available
    if book_result[4] == 0:
        print("Book is not available.")
        return

    # Check if the book is already issued to the user
    issued_query = "SELECT * FROM records WHERE userID = ? AND bookID = ?"
    issued_result = conn.execute(issued_query, (user_id, book_id)).fetchone()
    if issued_result:
        print("Book is already issued to the user.")
        return

    today_date = date.today()
    issue_date = today_date.strftime("%Y-%m-%d")

    # Update the book's availability and create a new record
    update_query = "UPDATE books SET available = 0 WHERE id = ?"
    conn.execute(update_query, (book_id,))

    insert_query = "INSERT INTO records(userID, bookID, issueDate) VALUES (?, ?, ?)"
    conn.execute(insert_query, (user_id, book_id, issue_date))

    conn.commit()
    print("Book issued to user successfully.")
