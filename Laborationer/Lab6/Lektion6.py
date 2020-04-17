class Contact(object):

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        string = "{}, {}"
        return string.format(self.last_name, self.first_name)

class ContactList(object):

    def __init__(self):
        self.contacts = []

    def create_and_add_contact(self, first_name, last_name):
        self.contacts.append(Contact(first_name, last_name))

    def __str__(self):
        str = ""
        for contact in self.contacts:
            str += contact.__str__() + "\n"
        return str[:-1]

contactlist = ContactList()
contactlist.create_and_add_contact("Ada", "Lovelace")
contactlist.create_and_add_contact("Alan", "Turing")
contactlist.create_and_add_contact("Grace", "Hopper")
print(contactlist)
