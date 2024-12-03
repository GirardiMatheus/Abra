class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        self.favorite = False

class ContactList:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact {contact.name} added successfully!")

    def list_contacts(self):
        if not self.contacts:
            print("No contacts registered.")
            return
        
        for i, contact in enumerate(self.contacts, 1):
            status = "(Favorite)" if contact.favorite else ""
            print(f"{i}. {contact.name} - {contact.phone} {status}")

    def edit_contact(self, index):
        if 0 < index <= len(self.contacts):
            contact = self.contacts[index - 1]
            print(f"Editing contact: {contact.name}")
            
            new_name = input("New name (Press Enter to keep current): ") or contact.name
            new_phone = input("New phone (Press Enter to keep current): ") or contact.phone
            new_email = input("New email (Press Enter to keep current): ") or contact.email

            contact.name = new_name
            contact.phone = new_phone
            contact.email = new_email
            
            print("Contact updated successfully!")
        else:
            print("Contact not found.")

    def toggle_favorite(self, index):
        if 0 < index <= len(self.contacts):
            contact = self.contacts[index - 1]
            contact.favorite = not contact.favorite
            status = "marked as favorite" if contact.favorite else "removed from favorites"
            print(f"Contact {contact.name} {status}!")
        else:
            print("Contact not found.")

    def list_favorites(self):
        favorites = [c for c in self.contacts if c.favorite]
        if not favorites:
            print("No favorite contacts.")
            return
        
        for i, contact in enumerate(favorites, 1):
            print(f"{i}. {contact.name} - {contact.phone}")

    def delete_contact(self, index):
        if 0 < index <= len(self.contacts):
            removed_contact = self.contacts.pop(index - 1)
            print(f"Contact {removed_contact.name} removed successfully!")
        else:
            print("Contact not found.")

def main():
    contact_list = ContactList()

    while True:
        print("\n--- Abra: A Simple Contact List with Python ---")
        print("1. Add Contact")
        print("2. List Contacts")
        print("3. Edit Contact")
        print("4. Mark/Unmark Favorite")
        print("5. List Favorites")
        print("6. Delete Contact")
        print("7. Exit")

        option = input("Choose an option: ")

        if option == '1':
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            contact = Contact(name, phone, email)
            contact_list.add_contact(contact)

        elif option == '2':
            contact_list.list_contacts()

        elif option == '3':
            contact_list.list_contacts()
            index = int(input("Enter the contact number to edit: "))
            contact_list.edit_contact(index)

        elif option == '4':
            contact_list.list_contacts()
            index = int(input("Enter the contact number to mark/unmark as favorite: "))
            contact_list.toggle_favorite(index)

        elif option == '5':
            contact_list.list_favorites()

        elif option == '6':
            contact_list.list_contacts()
            index = int(input("Enter the contact number to delete: "))
            contact_list.delete_contact(index)

        elif option == '7':
            print("Exiting the application...")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
