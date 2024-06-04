import sqlite3
import hashlib

# Create a SQLite database or connect to an existing one
conn = sqlite3.connect('user_database.db')
cursor = conn.cursor()

# Create a table to store user information
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')
conn.commit()

# Function to register a new user
def register_user(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
    conn.commit()
    print("Registration successful!")

# Function to check if a user exists and the provided password is correct
def login_user(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, hashed_password))
    user = cursor.fetchone()
    if user:
        print("Login successful!")
    else:
        print("Login failed. Please check your credentials.")

# Main program loop
while True:
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Select an option: ")

    if choice == '1':
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        register_user(username, password)
    elif choice == '2':
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        login_user(username, password)
    elif choice == '3':
        break

# Close the database connection
conn.close()