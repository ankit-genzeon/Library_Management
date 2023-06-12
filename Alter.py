import sqlite3

# Establish a connection to the database
conn = sqlite3.connect('library_management.db')

alter_books_table_query = '''
ALTER TABLE books
ADD COLUMN available BOOLEAN DEFAULT 1;
'''

conn.execute(alter_books_table_query)
