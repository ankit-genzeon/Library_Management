import sqlite3

# Establish a connection to the database
conn = sqlite3.connect('library_management.db')


# Function to display all issued books
def display_issued_books():
    query = '''
    SELECT books.title, users.username, records.issueDate
    FROM books
    JOIN records ON books.id = records.bookID
    JOIN users ON users.id = records.userID
    '''
    result = conn.execute(query).fetchall()

    if len(result) == 0:
        print("No issued books found.")
    else:
        print("Issued Books:")
        for book in result:
            print(f"Book Title: {book[0]}")
            print(f"User Name: {book[1]}")
            print(f"Issue Date: {book[2]}")
            print()
