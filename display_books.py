import sqlite3

# Connect to database
conn = sqlite3.connect("books.db")
cursor = conn.cursor()

# Fetch all records
cursor.execute("SELECT title, author, published_year FROM books")
rows = cursor.fetchall()

print("Books stored in database:\n")

for row in rows:
    print("Title:", row[0])
    print("Author:", row[1])
    print("Published:", row[2])
    print("-" * 30)

conn.close()
