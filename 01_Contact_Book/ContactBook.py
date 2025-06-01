class ContactBook:
    def __init__(self):
        self.contacts = {}

    def __repr__(self):
        return f"ContactBook({self.contacts})"

    def add_contact(self, name: str, contact: int):
        str_contact = str(contact)
        assert (
            str_contact.isdigit() and len(str_contact) == 11
        ), "Contact should be 11 digits!"

        self.contacts[name] = contact
        print(f"\n{name} added successfully!")

    def update_contact(self, name):
        if name in self.contacts:
            ctc = input("\nEnter the updated number: ")

            if ctc.isdigit() and len(ctc) == 11:
                self.contacts[name] = ctc

                print(f"\n{name} updated successfully!")

            else:
                print("\nContact should be 11 digits!")

        else:
            print("\nName not found!")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]

            print(f"\n{name} successfully removed!")

        else:
            print("\nName not found!")

    def search_contact(self, name):
        if name in self.contacts:
            return f"\n{name} : {self.contacts [name]}"

        else:
            return f"\n{name} does not exists!"

    def display_contacts(self):
        if not self.contacts:
            return "\nNo Contacts found!"

        result = "\nContacts:\n"
        for k, v in self.contacts.items():
            result += f"{k} : {v}\n"

        return result