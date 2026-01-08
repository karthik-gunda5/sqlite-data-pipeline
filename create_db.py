import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    name TEXT,
    email TEXT
)
""")

conn.commit()
conn.close()

print("Users database and table created successfully")
