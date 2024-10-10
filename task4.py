import sys
import os

contacts = {}

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Error: Give me name and phone, please."
        except KeyError:
            return "Error: Contact not found."
        except IndexError:
            return "Error: Enter the argument for the command"
        except Exception as e:
            return f"Unexpected error: {e}"

    return inner


def parse_input(user_input):
    parts = user_input.strip().lower().split()
    command = parts[0]
    arguments = parts[1:]
    return command, arguments

@input_error
def add_contact(arguments):
    name, phone = arguments
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(arguments):
    name, phone = arguments

    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        raise KeyError()
    
@input_error
def remove_contact(arguments):
    name = arguments[0]

    if name in contacts:
        del contacts[name]
        return "Contact removed."
    else:
        return KeyError()

@input_error
def show_phone(arguments):
    name = arguments[0]

    if name in contacts:
        return contacts[name]
    else:
        return "Error: Contact not found."

@input_error
def show_all():
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts found."

def main():
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter command: ")
        command, arguments = parse_input(user_input)

        if command == "hello":
            print("How can I help you?")
        
        elif command == "add":
            print(add_contact(arguments))
        
        elif command == "change":
            print(change_contact(arguments))

        elif command == "remove":
            print(remove_contact(arguments))
        
        elif command == "phone":
            print(show_phone(arguments))
        
        elif command == "all":
            print(show_all())
        
        elif command in ["close", "exit"]:
            print("Good bye!")
            break
        
        else:
            print("Invalid command.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('\nBye!')
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)