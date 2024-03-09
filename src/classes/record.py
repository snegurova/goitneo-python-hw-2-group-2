from name import Name
from phone import Phone


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        phone_field = Phone(phone)
        self.phones.append(phone_field)

    def remove_phone(self, phone_to_delete):
        for phone in self.phones:
            if phone.value == phone_to_delete:
                self.phones.remove(phone)

    def edit_phone(self, phone_to_change, new_phone):
        for phone in self.phones:
            if phone.value == phone_to_change:
                phone.value = new_phone

    def find_phone(self, phone_to_find):
        for phone in self.phones:
            if phone.value == phone_to_find:
                return f"{phone_to_find} exists"
        return f"{phone_to_find} have not been added yet"

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    
    def __repr__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
