import sqlite3
from datetime import date

# Establish a connection to the database
conn = sqlite3.connect('../../library_management.db')
cursor = conn.cursor()

import sqlite3

def update_book_title_author():
  # Prompt the user for input
        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        for book in books:
            print(book)
        while True:
            book_id = input("Enter the Book ID: ")
            if not book_id.isdigit():
                print("Invalid input! Please enter a valid Book ID.")
                continue
            book_id = int(book_id)
            cursor.execute("SELECT COUNT(*) FROM books WHERE id = ?", (book_id,))
            if cursor.fetchone()[0] == 0:
                print("Book ID not found in the database. Please enter a valid Book ID.")
                continue
            break

        while True:
            new_title = input("Enter the new title: ")
            if not new_title:
                print("Title cannot be empty. Please enter a valid title.")
                continue
            elif len(new_title) < 1:
                print("Title is too short. Please enter a title with maximum 10 characters.")
                continue
            break

        while True:
            new_author = input("Enter the new author: ")
            if not new_author:
                print("Author cannot be empty. Please enter a valid author.")
                continue
            elif len(new_author) < 1:
                print("Author name is too short. Please enter an author name with maximum 10 characters.")
                continue
            break

        # Update the book's title and author
        cursor.execute("UPDATE books SET title = ?, author = ? WHERE id = ?", (new_title, new_author, book_id))
        conn.commit()

        print("Book information updated successfully!")


        cursor.execute("SELECT * FROM books")
        books = cursor.fetchall()
        for bi in books:
            print(bi)
        # Close the connection
        conn.close()


update_book_title_author()