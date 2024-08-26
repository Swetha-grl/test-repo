def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Search Contact")
        print("4. Display Contacts")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            contact = Contact(name, phone, email)
            contact_book.add_contact(contact)

        elif choice == "2":
            name = input("Enter the name of the contact to remove: ")
            contact_book.remove_contact(name)

        elif choice == "3":
            name = input("Enter the name of the contact to search: ")
            contact = contact_book.search_contact(name)
            if contact:
                print(contact)
            else:
                print("Contact not found.")

        elif choice == "4":
            contact_book.display_contacts()

        elif choice == "5":
            print("Exiting the contact book. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()