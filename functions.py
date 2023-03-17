import os
import time

import ui
import csv
from Note import *


def show_all():
    try:
        with open("data/notes.csv", mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                print("id: " + row[0])
                print("Date: " + row[1])
                print("Title: " + row[2][0:12])
                print("Body: " + row[3][0:12])
                print()
    except IOError:
        print("IOError")


def show_date():
    date = input("Input date dd.mm.yyyy: ")
    status = False
    try:
        with open("data/notes.csv", mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                if row[1][0:10] == date:
                    status = True
                    print("id: " + row[0])
                    print("Date: " + row[1])
                    print("Title: " + row[2][0:12])
                    print("Body: " + row[3][0:12])
                    print()
            if not status:
                print("None was found")
                print()
    except IOError:
        print("IOError")


def show_id():
    id = input("Input id(4 chars): ")
    status = False
    try:
        with open("data/notes.csv", mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                if row[0] == id:
                    status = True
                    print("id: " + row[0])
                    print("Date: " + row[1])
                    print("Title: " + row[2][0:12])
                    print("Body: " + row[3][0:12])
                    print()
            if not status:
                print("None was found")
                print()
    except IOError:
        print("IOError")


def create():
    note = Note()
    note.set_id()
    note.set_date()
    note.set_title(input("Title: "))
    note.set_body(input("Body: "))
    with open("data/notes.csv", mode='a', newline="", encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([note.to_string()])


def delete():
    id = input("Input id(4 chars) to delete: ")
    status = False
    try:
        with open("data/notes.csv", mode='r', encoding='utf-8') as file1:
            reader = csv.reader(file1, delimiter=';')
            with open("data/notes_deleted.csv", mode='w', newline="", encoding='utf-8') as file2:
                writer = csv.writer(file2)
                for row in reader:
                    note = Note()
                    note.set_id()
                    note.set_date()
                    note.set_title(row[2])
                    note.set_body(row[3])
                    if row[0] != id:
                        writer.writerow([note.to_string()])
                    elif row[0] == id:
                        status = True
                    del note
                    time.sleep(0.005)
        os.remove("data/notes.csv")
        os.rename("data/notes_deleted.csv", "data/notes.csv")
        if not status:
            print("None was found")
            print()
    except IOError as e:
        print("Cannot open file. Try to create a note")


def edit():
    id = input("Input id(4 chars) to edit: ")
    status = False
    try:
        with open("data/notes.csv", mode='r+', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                if row[0] == id:
                    print("Title: " + row[2])
                    print("Body: " + row[3])
                    note = Note()
                    note.set_id()
                    note.set_date()
                    note.set_title(input("Edit title: "))
                    note.set_body(input("Edit body: "))
                    csv.writer(file).writerow([note.to_string()])
                    del note
                    time.sleep(0.005)
    except IOError as e:
        print("Cannot open file. Try to create a note")


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
