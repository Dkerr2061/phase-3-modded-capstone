# lib/cli.py

from rich.console import Console
from load_bar import *
from artist_helpers import *
from album_helpers import *

console = Console()


def exit_program():
    console.print("Goodbye!\n")
    exit()


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            interact_with_artist_data()
        elif choice == "2":
            interact_with_album_data()
        else:
            console.print("Invalid choice, please try again!\n", style="bright_red")


def menu():
    console.print("Welcome!", style="blink")
    console.print("\nPlease select an option:", style="underline")
    console.print("1. Access Artist Data", style="bright_yellow")
    console.print("2. Access Album Data", style="bright_yellow")
    console.print("0. Exit the program", style="bright_yellow")


if __name__ == "__main__":
    initialize_artist_data()
    initialize_album_data()
    main()
