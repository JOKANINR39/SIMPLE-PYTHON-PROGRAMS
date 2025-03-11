7. Implementing a Simple Contact Book by using Modules
import os
import sys
CONTACTS_FILE = "contacts.txt" # File to store contacts
# Load contacts from file
def load_contacts():
if os.path.exists(CONTACTS_FILE):
with open(CONTACTS_FILE, "r") as file:
return [line.strip() for line in file.readlines()]
return []
# Save contacts to file
def save_contacts(contacts):
with open(CONTACTS_FILE, "w") as file:
file.writelines("\n".join(contacts))
# Add a new contact
def add_contact():
name = input("Enter contact name: ")
phone = input("Enter contact number: ")
contact = f"{name}: {phone}"
contacts = load_contacts()
contacts.append(contact)
save_contacts(contacts)
print(f"Contact '{name}' added successfully!")
# View all contacts
def view_contacts():
contacts = load_contacts()
if not contacts:
print("No contacts available.")
else:
print("\nContact List:")
for idx, contact in enumerate(contacts, start=1):
print(f"{idx}. {contact}")
# Delete a contact
def delete_contact():
view_contacts()
contacts = load_contacts()
if not contacts:
return
try:
contact_number = int(input("Enter contact number to delete: ")) - 1
if 0 <= contact_number < len(contacts):
removed_contact = contacts.pop(contact_number)
save_contacts(contacts)
print(f"Deleted contact: {removed_contact}")
else:
print("Invalid contact number.")
except ValueError:
print("Please enter a valid number.")
# Display menu
def display_menu():
print("\nContact Book")
print("1. Add Contact")
print("2. View Contacts")
print("3. Delete Contact")
print("4. Exit")
# Main program loop
while True:
display_menu()
choice = input("\nEnter your choice (1-4): ")
if choice == "1":
add_contact()
elif choice == "2":
view_contacts()
elif choice == "3":
delete_contact()
elif choice == "4":
print("Exiting Contact Book. Goodbye!")
sys.exit()
else:
print("Invalid choice. Please try again.")