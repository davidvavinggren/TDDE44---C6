class Contact(object):

    def __init__(self, name):
        self.name = name
        self.phone_num = ""

    def __str__(self):
        return "{}, {}".format(self.name, self.phone_num)

    def print_contact(self):
        contact = "{}, {}"
        print(contact.format(self.name, self.phone_num))

    def append_to_name(self, string_to_append):
        self.name = self.name + (string_to_append)

c1 = Contact("Jonas")
c2 = Contact("David")
c3 = Contact("Kalle")

c1.phone_num = "0701-111111"
c2.phone_num = "0702-222222"
c3.phone_num = "0703-333333"

contact_list = [c1, c2, c3]


for contact in contact_list:
    print(contact)

c1.append_to_name(" Asker Svedberg")
c2.append_to_name(" Vävinggren")
#c1.print_contact()
#c2.print_contact()
