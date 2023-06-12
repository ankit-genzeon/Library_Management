import sqlite3
from Main_Pack.display_records import display_books as db
from Main_Pack.display_records import display_av_books as dab
from Main_Pack.book_table_crud_ops import book_operations as bo
from Main_Pack.record_operation import DisplayUser as du, update_user_info as uui, update_bookTitle_author as ubt
from Main_Pack.User_package import Add_User as au
from Main_Pack.Issue_book import Issue_book as Ib, Display_issue_books as dib

# Establish a connection to the database
conn = sqlite3.connect('library_management.db')

# Menu-driven program
while True:

    print("\n==== Library Management System ====")
    print("1. Add new books to library")
    print("2. Display all books in the library")
    print("3. Display available books for issuing")
    print("4. Delete a book")
    print("5. Add new user")
    print("6. Update User's Details")
    print("7. Delete user")
    print("8. Display all user")
    print("9. Issue a Book")
    print("10. Display all Issued Books")
    print("11. Update Book's Details")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        bo.add_book()
    elif choice == "2":
        db.display_all_books()
    elif choice == "3":
        dab.display_av_books()
    elif choice == "4":
        bo.delete_book()
    elif choice == "5":
        au.Add_Users()
    elif choice == "6":
        uui.update_user_info()
    elif choice == "7":
        au.delete_user_record()
    elif choice == "8":
        du.display_users()
    elif choice == "9":
        Ib.issue_book_to_user()
    elif choice == "10":
        dib.display_issued_books()
    elif choice == "11":
        ubt.update_book_title_author()
    elif choice == "0":
        break
    else:
        print("Invalid choice. Please try again.")
