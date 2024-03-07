from input_error import input_error


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error("Give me please name and phone to add.")
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error("Give me please name and phone to change.")
def change_contact(args, contacts):
    name, phone = args
    if not name in contacts.keys():
        return f"Contact {name} doesn't exist. Please add contact first"
    contacts[name] = phone
    return "Contact is changed."

@input_error()
def phone(args, contacts):
    name = args[0]
    return f"Contact's {name} phone is {contacts[name]}."

def print_contacts(contacts):
    if len(contacts) > 0:
        print(f'|{'Name':^15}|{'Phone':^15}|')
    for name, phone in contacts.items():
        print(f'|{name:^15}|{phone:^15}|')
    else: 
        print("No added contacts yet")