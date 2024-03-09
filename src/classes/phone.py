from field import Field


class Phone(Field):
    def __init__(self, phone):
        if len(phone) == 10:
            super().__init__(phone)
        else:
            print("Error. Phone number should contain 10 numbers. Please enter correct number")