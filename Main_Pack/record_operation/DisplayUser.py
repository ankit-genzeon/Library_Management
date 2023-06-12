import sqlite3
from datetime import date

# Establish a connection to the database
conn = sqlite3.connect('../../library_management.db')
cursor = conn.cursor()

def display_users():

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    if len(users) == 0:
        print("No users found in the database.")
    else:
        for user in users:
            print(user)

display_users()