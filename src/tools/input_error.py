def input_error(message = ''):
    def wrapper(func):
        def inner(*args, **kwargs):
            contact = args[0]
            try:
                return func(*args, **kwargs)
            except ValueError:
                return message
            except KeyError:
                name = contact[0]
                return f"Contact {name} doesn't exist. Please add contact first"
            except IndexError:
                return "Enter user name"
        return inner
    return wrapper