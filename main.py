from address_book import AddressBook
from fields import Name, Phone, Birthday
from record import Record
from functools import wraps

File_name ="Contact.bin"

def parse_input(command_line: str) -> tuple[str, list]:
    for command in COMMANDS:
        if command_line.lower().startswith(command):
            args = command_line.lstrip(command).strip().split(" ")
            args = (s.strip() for s in args)
            return command, args
    return command_line.lower(),()


def input_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError):
            return "Sorry, there are not enough parameters or their value may be incorrect. "\
                   "Please use the help for more information."
        # except Exception as e:
        #     return "**** Exception other" + e
    return wrapper  
  
def output_operation_describe(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if type(result) == str:
                return result
            else:
                return "Successfully" if result else "The operation was not successful"
            
    return wrapper

@input_error
def command_add(*args) -> str:
    name = Name(args[0])
    phone = Phone(args[1])
    rec = a_book.get(str(name))
    if rec:
        return rec.add_phone(phone)
    rec = Record(name, phone)
    return a_book.add_record(rec)


@output_operation_describe
@input_error
def command_add_birthday(*args) -> str:
    user = Name(args[0])
    birthday = Birthday(args[1])
    rec = a_book.get(str(user))
    if rec:
        return rec.add_birthday(birthday)
    else:
        rec = Record(user)
        rec.add_birthday(birthday)
        return a_book.add_record(rec)

@input_error
def command_change_phone(*args) -> str:
    user = Name(args[0])
    old_phone = Phone(args[1])
    new_phone = Phone(args[2])
    rec = a_book[str(user)]
    return rec.change_phone(old_phone, new_phone)

@input_error
def command_show_phone(*args) -> str:
     user = Name(args[0])
     return a_book[str(user)].phones 

def command_show_all(*args) -> str:
    if any(a_book.keys()):
        return a_book
    else:
        return "No users found, you must first add name and phone"


def greetings(*args) -> str:
    return "Hello! How can I help you?"

@output_operation_describe
@input_error
def command_delete_birthday(*args) -> str:
    user = Name(args[0])
    rec = a_book.get(str(user))
    if rec and rec.birthday:
        return rec.delete_birthday()
    else:
        return "No birthday found for the user"

@input_error
def command_delete_record(*args) -> str:
    user = Name(args[0])
    a_book.remove_phone(user)
    return "Successfully"

@input_error
def command_delete_phone(*args) -> str:
    user = Name(args[0])
    phone = Phone(args[1])
    a_book.remove_phone(user, Phone(phone))
    return "Successfully" 

def command_help(*args) -> str:
    command = " ".join(args)
    if not command:
        commands = list(COMMANDS.keys())
        commands.extend(COMMAND_EXIT)
        return "List of commands: " + ", ".join(commands)
    else:
        return COMMANDS_HELP.get(command,  f"Help for this command '{command}' is not yet available")


COMMAND_EXIT=("good bye", "close", "exit", "q")

COMMANDS = {
    "hello": greetings,
    "add": command_add,
    "change": command_change_phone,
    "phone": command_show_phone ,
    "show all": command_show_all,
    "help": command_help,
    "delet record": command_delete_record,
    "delet phone": command_delete_phone,
    "add birthday": command_add_birthday,
    "delete birthday": command_delete_birthday 
}

COMMANDS_HELP = {
    "hello": "Say hello",
    "add": "Add user and phone. Required username and phone.",
    "change": "Change user's phone. Required username and phone.",
    "phone": "Show user's phone. Required username." ,
    "delet record": "Delet record of user ",
    "delet phone": "Delet phone record of user",
    "show all": "Show all user phone numbers.",
    "help": "List of commands  and their description.",
    "exit": "Exit of bot.",
    "close": "Exit of bot." ,
    "good bye": "Exit of bot."
}

a_book = AddressBook()
#.load(File_name)

def main():
    print("Welcome to the Address Book CLI")
    while True:
        try:
            user_input = input("Enter your command:")
        except KeyboardInterrupt:
            print("\r")
            break
        if user_input.lower() in COMMAND_EXIT:
            # a_book.save(File_name)
            break

        else:
            command, args = parse_input(user_input)
            try:
                result=COMMANDS[command](*args)
            except KeyError:
                 print("Your command is not recognized, try to enter other command. "
                       "To get a list of all commands, you can use the 'help' command")
            else:
                if result:
                    print(result)
    print("Good bye")

if __name__ == "__main__":
    main()