import ui
import csv
from Note import *


def show_all():
    return


def show_date():
    return


def show_id():
    return


def create():
    note = Note()
    note.set_id()
    note.set_date()
    note.set_title(input("Title: "))
    note.set_body(input("Body: "))
    with open("notes.csv", mode='a', newline="", encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([note.to_string()])


def delete():
    return


def edit():
    return


def exit():
    ui.goodbye()
    quit()


def choice(command: str):
    if command == "show_all":
        show_all()
    elif command == "show_date":
        show_date()
    elif command == "show_id":
        show_id()
    elif command == "create":
        create()
    elif command == "delete":
        delete()
    elif command == "edit":
        edit()
    elif command == "exit":
        exit()
    elif command == "help":
        ui.show_help()
