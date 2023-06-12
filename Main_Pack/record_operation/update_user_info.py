import sqlite3
from datetime import date

# Establish a connection to the database
conn = sqlite3.connect('../../library_management.db')
cursor = conn.cursor()


import re

def update_user_info():
    # Prompt the user for input

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    for user in users:
        print(user)
    while True:
        user_id = input("Enter the User ID: ")
        if not user_id.isdigit():
            print("Invalid input! Please enter a valid User ID.")
            continue
        user_id = int(user_id)
        cursor.execute("SELECT COUNT(*) FROM users WHERE id = ?", (user_id,))
        if cursor.fetchone()[0] == 0:
            print("User ID not found in the database. Please enter a valid User ID.")
            continue
        break

    while True:
        new_name = input("Enter the new name: ")
        if not new_name:
            print("Name cannot be empty. Please enter a valid name.")
            continue
        elif len(new_name) > 100:
            print("Name is too long. Please enter a name with maximum 100 characters.")
            continue
        break

    while True:
        new_email = input("Enter the new email: ")
        if not new_email:
            print("Email cannot be empty. Please enter a valid email.")
            continue
        elif len(new_email) > 100:
            print("Email is too long. Please enter an email with maximum 100 characters.")
            continue
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", new_email):
            print("Invalid email format. Please enter a valid email.")
            continue
        break

    while True:
        new_phone = input("Enter the new phone number: ")
        if not new_phone:
            print("Phone number cannot be empty. Please enter a valid phone number.")
            continue
        elif len(new_phone) > 20:
            print("Phone number is too long. Please enter a phone number with maximum 20 characters.")
            continue
        elif not re.match(r"^[0-9-]+$", new_phone):
            print("Invalid phone number format. Please enter a valid phone number.")
            continue
        break

    # Update the user's name, email, and phone number
    cursor.execute("UPDATE users SET username = ?, userEmail = ?, phoneNumber = ? WHERE id = ?", (new_name, new_email, new_phone, user_id))
    conn.commit()

    print("User information updated successfully!")

    # Close the connection
    conn.close()

# Usage example
#update_user_info()
