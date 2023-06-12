import sqlite3

def display_issued_books():
    conn = sqlite3.connect('library_management.db')  # Replace 'your_database.db' with your actual database file
    cursor = conn.cursor()

    # Execute a query to retrieve the issued books
    query = "SELECT * FROM books WHERE available = 0"
    cursor.execute(query)

    # Fetch and display the results
    books = cursor.fetchall()
    for book in books:
        print(book)  # Modify this line to display the specific information you want from the book

    # Close the cursor and connection
    cursor.close()
    conn.close()


