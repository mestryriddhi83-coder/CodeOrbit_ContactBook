import json
import os

FILE_NAME = "contacts.json"


def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {}


def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    contacts[name] = {
        "phone": phone,
        "email": email
    }

    save_contacts(contacts)
    print("Contact added successfully!")


def search_contact(contacts):
    name = input("Enter name to search: ").strip()

    if name in contacts:
        print("\nContact Found!")
        print("Name:", name)
        print("Phone:", contacts[name]["phone"])
        print("Email:", contacts[name]["email"])
    else:
        print("Contact not found.")


def update_contact(contacts):
    name = input("Enter name to update: ").strip()

    if name in contacts:
        phone = input("Enter new phone number: ").strip()
        email = input("Enter new email: ").strip()

        contacts[name]["phone"] = phone
        contacts[name]["email"] = email

        save_contacts(contacts)
        print("Contact updated successfully!")
    else:
        print("Contact not found.")


def delete_contact(contacts):
    name = input("Enter name to delete: ").strip()

    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")


def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return

    print("\n===== CONTACT LIST =====")

    for name, details in contacts.items():
        print(f"\nName: {name}")
        print(f"Phone: {details['phone']}")
        print(f"Email: {details['email']}")


def main():
    contacts = load_contacts()

    while True:
        print("\n===== CONTACT BOOK =====")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. View All Contacts")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)

        elif choice == "2":
            search_contact(contacts)

        elif choice == "3":
            update_contact(contacts)

        elif choice == "4":
            delete_contact(contacts)

        elif choice == "5":
            view_contacts(contacts)

        elif choice == "6":
            print("Thank you for using Contact Book!")
            break

        else:
            print("Invalid choice. Please try again.")


main()