class Contact:
    phone_directory = []

    def __init__(self, name, phone_number):
        self.name = name
        self.phone = phone_number
        Contact.phone_directory.append(self)

    def show_contact(self):
        return f"Name: {self.name}, Contact number: {self.phone}"

    @classmethod
    def show_all_contacts(cls):
        if len(cls.phone_directory) == 0:
            print("No contacts found in the directory!")
        else:
            for contact in cls.phone_directory:
                print(contact.show_contact())

    @classmethod
    def search_contact(cls, search_name):
        for Contact in cls.phone_directory:
            if Contact.name.lower() == search_name.lower():
                return Contact.phone

        return f"No contact found for {search_name}."

    @staticmethod
    def validate_phone_number(number):
        if len(number) >= 8 and number.isdigit():
            return True
        else:
            return False

n_contacts = int(input("How many contacts do you want to add? :  "))

for _ in range(n_contacts):
    name = input("Enter the Name of the contact: ")
    phone_number = input("Enter the Contact Number: ")
    if Contact.validate_phone_number(phone_number):
        Contact(name, phone_number)
    else:
        print(f"Invalid Contact Number for {name}, phone number should be 8 digits and should only contain numbers 0-9.")

# c1 = Contact("Medhavi", "0123345673")
# c2 = Contact("Rajshree", "9876543219")
# c3 = Contact("Bandu", "1236789045")
# print(Contact.phone_directory)

# print(c1.show_contact())
# print(c2.show_contact())
Contact.show_all_contacts()

# print(Contact.search_contact("rajshree"))
# print(Contact.search_contact("Siddhant"))
# print(Contact.search_contact("bandu"))
# print(Contact.search_contact("Medhavi"))
