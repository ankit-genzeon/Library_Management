# Connect with database "library_management.db" and use table "books"
import sqlite3
import re
from datetime import date

# Establish a connection to the database
conn = sqlite3.connect('../../library_management.db')

#function to add a book
def add_book():
    # title - string , trim, not empty,
    # title -string ,trim, not empty
    # genre - string "Fiction" or "Non-Fiction"
    # add_date- date as YYYY-MM-DD
    title=input("Enter Book title:-")
    while len(title.strip()) == 0:
        title=input("ERROR(Please Enter Non-Empty title):-").strip()

    author = input("Enter Book Author Name:-")
    while len(author.strip()) == 0:
        author = input("ERROR(Please Enter Non-Empty Author name):-").strip()

    genre = input("Enter Book Genre(Fiction/Non-Fiction):-")
    # pattern to match Genre
    pattern = r"\bFiction\b|\bNon-Fiction\b"
    while len(genre.strip()) == 0 or not bool(re.match(pattern, genre)):
        genre = input("ERROR(Please Enter Either 'Fiction' or 'Non-Fiction'):-").strip()

    today_date = date.today()
    add_date = today_date.strftime("%Y-%m-%d")

    query = '''INSERT INTO books(title, author, genre, add_date) VALUES(?,?,?,?)'''

    conn.execute(query, (title, author, genre, add_date))
    conn.commit()

# add_book()

# function to delete a book using bookID
def delete_book():
    book_id = input("Enter Book ID:-")

    while not book_id.isnumeric():
        book_id = input("ERROR(Enter valid Book ID):-")

    query = '''
    DELETE FROM books WHERE id = ?
    '''
    conn.execute(query, book_id)
    conn.commit()

# delete_book()