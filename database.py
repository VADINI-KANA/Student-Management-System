import sqlite3
DATABASE_NAME="students.db"

def connect_database():
    connection= sqlite3.connect(DATABASE_NAME)
    return connection

def create_table():
    connection=connect_database()
    cursor= connection.cursor()
    cursor.execute (""" CREATE TABLE IF NOT EXISTS students(
        id  INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        age INTEGER,
        course TEXT,
        email TEXT UNIQUE NOT NULL
    )""")
    connection.commit()
    connection.close()

