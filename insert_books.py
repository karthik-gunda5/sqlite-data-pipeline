import requests
import sqlite3

# Fetch data from API
url = "https://fakerapi.it/api/v1/books?_quantity=5"
response = requests.get(url)
books = response.json()["data"]

# Connect to database
conn = sqlite3.connect("books.db")
cursor = conn.cursor()

# Insert data
for book in books:
    cursor.execute(
        "INSERT INTO books (title, author, published_year) VALUES (?, ?, ?)",
        (book["title"], book["author"], book["published"])
    )

conn.commit()
conn.close()

print("Book data inserted successfully")
