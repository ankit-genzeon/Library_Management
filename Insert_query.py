import sqlite3
from datetime import date

# Establish a connection to the database
conn = sqlite3.connect('library_management.db')
cursor = conn.cursor()

# Insert sample data into the "users" table
insert_users_table = '''
INSERT INTO users(username, userEmail, phoneNumber)
VALUES
    ('Ankit Singh', 'ankit@gmail.com', '1234567890'),
    ('Swanand Kale', 'kale@gmail.com', '9876543210')
'''
cursor.execute(insert_users_table)

# Insert sample data into the "books" table
insert_books_query = '''
INSERT INTO books(title, author, genre, add_date)
VALUES
    ('Java- The Unresolved Mystery', 'Arjun', 'Fiction', ?),
    ('Siva- The Tygun Guy', 'Sudhanshu', 'Non-Fiction', ?)
'''
current_date = date.today().isoformat()
cursor.execute(insert_books_query, (current_date, current_date))

# Get the last inserted book ID
book_id = cursor.lastrowid

# Insert sample data into the "records" table
insert_records_query = '''
INSERT INTO records(userID, bookID, issueDate, returnDate)
VALUES
    (1, ?, ?, NULL),
    (2, ?, ?, NULL)
'''
cursor.execute(insert_records_query, (book_id, current_date, book_id, current_date))

# Commit the changes and close the connection
conn.commit()
conn.close()
