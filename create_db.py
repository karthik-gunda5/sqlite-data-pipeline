import sqlite3

# Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect("books.db")

cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    title TEXT,
    author TEXT,
    published_year TEXT
)
""")

conn.commit()
conn.close()

print("Database and table created successfully")
