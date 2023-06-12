import sqlite3

# Establish a connection to the database
conn = sqlite3.connect('library_management.db')

details = conn.execute("pragma table_info('users')")
print(details)
for i in details:
    print(i)

details = conn.execute("pragma table_info('books')")
print(details)
for i in details:
    print(i)

details = conn.execute("pragma table_info('records')")
print(details)
for i in details:
    print(i)
