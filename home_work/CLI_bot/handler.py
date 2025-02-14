def command_parser(command):

    cmd, *args = command.split(' ')
    cmd = cmd.strip().lower()

    return cmd, args


def add_contact(args: list, contacts: dict):

    if len(args) != 2:
        print('For add contact, please, enter <add name phone>')

    else:
        name, phone = args

        if name in contacts.keys():
            print("This name is busy. Please, try enother one")

        else:
            contacts[name] = phone

        return contacts


def change_contact(args: list, contacts: dict):

    if len(args) != 2:
        print('For change contact, please, enter <change name new_phone>')
    else:

        name, phone = args

        if name in contacts.keys():

            contacts[name] = phone
        else:
            print(f'This name: {name.title()} is absent')

    return contacts


def show_phone(args: list, contacts: dict):

    if len(args) != 1:
        print('For change contact, please, enter <change name new_phone>')
    else:
        name = args[0]

        if name in contacts.keys():
            return contacts[name]

        else:
            print('No contact with this name.')


def show_all(contacts: dict):

    for name in contacts:
        print(f"{name.title()}.....{contacts[name]}")
