import sqlite3
from Main_Pack.display_records import display_books as db
from Main_Pack.display_records import display_av_books as dab
# Establish a connection to the database
conn = sqlite3.connect('library_management.db')

# Menu-driven program
while True:
    print("\n==== Library Management System ====")
    print("1. Display all books in the library")
    print("2. Display available books for issuing")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        db.display_all_books()
    elif choice == "2":
        dab.display_av_books()
    elif choice == "0":
        break
    else:
        print("Invalid choice. Please try again.")
