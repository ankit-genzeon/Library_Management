import sqlite3

# Establish a connection to the database
conn = sqlite3.connect('library_management.db')
cursor = conn.cursor()

def display_all_books():
    records = cursor.execute("select * from books")
    all_books = cursor.fetchall()

    print("All the books in the library:")
    for book in all_books:
        print("Book ID:", book[0])
        print("Title:", book[1])
        print("Author:", book[2])
        print("Genre:", book[3])
        print("Add Date:", book[4])
        print("----------------------------")