import sqlite3

# Establish a connection to the database
conn = sqlite3.connect('library_management.db')


<<<<<<< Updated upstream
def display_all_available_books():
    records = conn.execute("select * from books")
    for i in records:
        print(i)
=======
def display_av_books():
    # Query to retrieve available books from the "books" table
    select_available_books_query = '''
    SELECT * FROM books
    WHERE available = 1;
    '''
    cursor.execute(select_available_books_query)
    available_books = cursor.fetchall()

    # Display the available books
    print("Available books in the library:")
    for book in available_books:
        print("Book ID:", book[0])
        print("Title:", book[1])
        print("Author:", book[2])
        print("Genre:", book[3])
        print("Add Date:", book[4])
        print("----------------------------")

>>>>>>> Stashed changes
