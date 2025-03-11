# Initialize an empty dictionary to store student details
students = {}
# Menu for student management
def display_menu():
print("\nStudent Management System")
print("1. Add Student")
print("2. View All Students")
print("3. Search Student by Roll Number")
print("4. Delete Student by Roll Number")
print("5. Exit")
while True:
display_menu()
choice = input("\nEnter your choice (1-5): ")
if choice == "1":
# Add a student
roll_no = input("Enter Roll Number: ")
if roll_no in students:
print("Roll Number already exists. Please try again.")
else:
name = input("Enter Student Name: ")
marks = float(input("Enter Marks: "))
students[roll_no] = {"name": name, "marks": marks}
print(f"Student {name} added successfully!")
elif choice == "2":
# View all students
if students:
print("\nAll Students:")
print("-" * 30)
for roll_no, details in students.items():
print(f"Roll No: {roll_no}, Name: {details['name']}, Marks: {details['marks']}")
else:
print("No students found.")
elif choice == "3":
# Search for a student
roll_no = input("Enter Roll Number to search: ")
if roll_no in students:
details = students[roll_no]
print(f"Roll No: {roll_no}, Name: {details['name']}, Marks: {details['marks']}")
else:
print("Student not found.")
elif choice == "4":
# Delete a student
roll_no = input("Enter Roll Number to delete: ")
if roll_no in students:
del students[roll_no]
print("Student deleted successfully.")
else:
print("Student not found.")
elif choice == "5":
# Exit the program
print("Exiting the Student Management System. Goodbye!")
break
else:
print("Invalid choice. Please try again.")