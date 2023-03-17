def hello():
    print("Hi! This is notes!")
    print("Type 'help' for tips!")
    print()


def goodbye():
    print()
    print("Thanks for working, bye!")


def show_help():
    print()
    print("This is help!")
    print("Type 'help' to find out commands")
    print("Type 'show_all' to show all notes")
    print("Type 'show_date' to show notes created on certain date")
    print("Type 'create' to create a note")
    print("Type 'delete' to delete a note")
    print("Type 'edit' to edit a note")
    print("Type 'exit' to exit a program")
    print()


def input_command():
    command = input("Write a command: ").lower()
    while command not in ["help", "show_all", "show_date",
                          "show_id", "create", "delete", "edit", "exit"]:
        print("Bad command")
        print()
        command = input("Write a command: ")
    return command
