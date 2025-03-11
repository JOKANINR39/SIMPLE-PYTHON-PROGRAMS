import sqlite3
import pandas as pd
# Connect to SQLite database (Creates if not exists)
conn = sqlite3.connect("students.db")
cursor = conn.cursor()
# Create table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INTEGER NOT NULL
)
''')
conn.commit()
print("Database and table created successfully!")
# Function to insert dynamic data
def insert_student(name, age):
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", (name, age))
conn.commit()
print(f"Student '{name}' added successfully!")
# Insert multiple students dynamically
n = int(input("How many students do you want to add? "))
for _ in range(n):
name = input("Enter student name: ")
age = int(input("Enter student age: "))
insert_student(name, age)
# View all students
df = pd.read_sql("SELECT * FROM students", conn)
print("\nStudent Records:")
print(df)
# Close the database connection
conn.close()
print("Database connection closed.")