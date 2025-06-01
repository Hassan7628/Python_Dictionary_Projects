from ContactBook import ContactBook
from time import sleep

book = ContactBook()


def menu():

    while True:
        sleep(1)

        print("\nWelcome to Contact Manager\n")

        print(
            """
            1.Add a contact
            2.Update a contact
            3.Delete a contact
            4.Search a contact
            5.Display the contact list
            6.Quit the program\n
            """
        )

        try:
            choice = int(input("Enter your choice: "))

        except ValueError:
            print("\nEnter a numeric value!")
            continue

        if choice == 1:
            name = input("\nEnter a name: ")
            contact = int(input("\nEnter his/her contact: "))

            book.add_contact(name, contact)

        elif choice == 2:
            upd_name = input("\nEnter the contact name: ")
            book.update_contact(upd_name)

        elif choice == 3:
            del_name = input("\nEnter the contact name you want to delete: ")
            book.delete_contact(del_name)

        elif choice == 4:
            srch_name = input("\nEnter the contact name you want to search: ")
            print(book.search_contact(srch_name))

        elif choice == 5:
            print(book.display_contacts())

        elif choice == 6:
            print("\nExiting the program!\n")
            break

        else:
            print("\nInvalid Choice! Choose from the given options.")