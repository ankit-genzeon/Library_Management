import sqlite3

# Establish a connection to the database
conn = sqlite3.connect('library_management.db')


def display_all_books():
    records = conn.execute("select * from books")
    for i in records:
        print(i)