import sqlite3

# Connect to database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Fetch all users
cursor.execute("SELECT name, email FROM users")
rows = cursor.fetchall()

print("Users stored in database:\n")

for row in rows:
    print("Name:", row[0])
    print("Email:", row[1])
    print("-" * 30)

conn.close()
