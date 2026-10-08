def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name."
    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    return "Contact not found."

@input_error
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    return "Contact not found."


@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts."
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        cmd, *args = parse_input(user_input)

        if cmd in ["close", "exit"]:
            print("Good bye!")
            break
        elif cmd == "hello":
            print("How can I help you?")
        elif cmd == "add":
            print(add_contact(args, contacts))
        elif cmd == "change":
            print(change_contact(args, contacts))
        elif cmd == "phone":
            print(show_phone(args, contacts))
        elif cmd == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()