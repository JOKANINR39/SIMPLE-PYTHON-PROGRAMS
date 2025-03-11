# Function to perform string operations on employee details
def employee_string_operations():
# Take basic employee details as input
employee_name = input("Enter the employee's name: ").strip()
employee_id = input("Enter the employee's ID: ").strip()
department = input("Enter the employee's department: ").strip()
print("\n--- Employee Details ---")
print(f"Employee Name: {employee_name}")
print(f"Employee ID: {employee_id}")
print(f"Department: {department}")
# 1. Count occurrences of a substring in the name (e.g., 'a')
substring = input("Enter a substring to count in the name: ").strip()
count = employee_name.lower().count(substring.lower()) # case insensitive
print(f"The substring '{substring}' appears {count} times in the name.")
# 2. Check if the name is alphanumeric
is_alphanumeric = employee_name.isalnum()
print(f"Is the name alphanumeric? {is_alphanumeric}")
# 3. Convert the name to uppercase
print(f"Name in uppercase: {employee_name.upper()}")
# 4. Convert the name to lowercase
print(f"Name in lowercase: {employee_name.lower()}")
# 5. Replace a part of the name (e.g., 'John' with 'Jon')
old_substring = input("Enter part of the name to replace: ").strip()
new_substring = input("Enter the new name part: ").strip()
modified_name = employee_name.replace(old_substring, new_substring)
print(f"Name after replacement: {modified_name}")
# 6. Find the position of a substring in the name
position = employee_name.lower().find(substring.lower())
if position != -1:
print(f"The substring '{substring}' is found at position {position}.")
else:
print(f"The substring '{substring}' is not found in the name.")
# 7. Trim whitespace from the name
trimmed_name = employee_name.strip()
print(f"Name after trimming whitespace: {trimmed_name}")
# Run the program
if __name__ == "__main__":
employee_string_operations()