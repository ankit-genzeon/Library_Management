import sqlite3

# Establish a connection to the database
conn = sqlite3.connect('library_management.db')

# Create the "users" table
create_user_table = '''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    userEmail TEXT NOT NULL,
    phoneNumber TEXT NOT NULL
);
'''
conn.execute(create_user_table)

# create the "books" table
create_book_table = '''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    genre TEXT NOT NULL COLLATE NOCASE CHECK (genre IN ('fiction', 'non-fiction')),
    add_date DATE NOT NULL
);
'''
conn.execute(create_book_table)

# Create the "records" table
create_record_table = '''
CREATE TABLE IF NOT EXISTS records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    userID INTEGER NOT NULL,
    bookID INTEGER NOT NULL,
    issueDate DATE NOT NULL,
    returnDate DATE,
    FOREIGN KEY (userID) REFERENCES users(id),
    FOREIGN KEY (bookID) REFERENCES books(id)
);
'''
conn.execute(create_record_table)

# Close the connection
conn.close()
