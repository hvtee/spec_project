from ui import *
from functions import *


def main_loop():
    hello()
    while True:
        command = input_command()
        choice(command)
