import ui


def show_all():
    return


def show_date():
    return


def show_id():
    return


def create():
    return


def delete():
    return


def edit():
    return


def exit():
    ui.goodbye()
    quit()


def choice(command: str):
    if command.lower() == "show_all":
        show_all()
    elif command.lower() == "show_date":
        show_date()
    elif command.lower() == "show_id":
        show_id()
    elif command.lower() == "create":
        create()
    elif command.lower() == "delete":
        delete()
    elif command.lower() == "edit":
        edit()
    elif command.lower() == "exit":
        exit()
    elif command.lower() == "help":
        ui.show_help()
