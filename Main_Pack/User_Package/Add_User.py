import sqlite3
import re
conn = sqlite3.connect('library_management.db')

def Add_Users():
    pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$'

    u_name=input("Enter the Name : ")

    u_email = input("Enter the Email : ")
    while(not re.match(pattern,u_email)):
        u_email=input("Enter Valid Email : ")

    u_phNo=input("Enter the phone Number : ")
    while(not u_phNo.isdigit()):
        u_phNo=input("Enter the valid phone number : ")

    conn.execute('''
    Insert INTO users(username,userEmail,phoneNumber)VALUES(?,?,?)
    ''',(u_name,u_email,u_phNo))
    conn.commit()
    print("Data Entered Successfully")


def display_Users():
    cursor=conn.cursor()
    records=cursor.execute("select * from users")
    records=cursor.fetchall()
    print(records)


def delete_user_record():
    user_id=input("Enter user id to delete record : ")

    while(not user_id.isdigit()):
        user_id=input("Enter valid User Id")

    cursor = conn.cursor()
    cursor.execute('''select * from users where id=?''',(user_id,))
    result = cursor.fetchone()

    if result is None:
        print("No records found")
    else:
        conn.execute('''DELETE FROM users WHERE id=?''', (user_id))
        print("record deleted succuessfully")
        conn.commit()









