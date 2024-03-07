def input_error(message = ''):
    def wrapper(func):
        def inner(*args, **kwargs):
            contact = args[0]
            if len(contact) == 0:
                return "Enter user name"
            try:
                return func(*args, **kwargs)
            except ValueError:
                return message
            except KeyError:
                name = contact[0]
                return f"Contact {name} doesn't exist. Please add contact first"
        return inner
    return wrapper