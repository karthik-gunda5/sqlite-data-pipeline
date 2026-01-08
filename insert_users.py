import csv
import sqlite3

# Connect to database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Read CSV and insert data
with open("users.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (row["name"], row["email"])
        )

conn.commit()
conn.close()

print("CSV data inserted into database successfully")
