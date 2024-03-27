# lib/cli.py
import colorama

from load_bar import *
from artist_helpers import *
from album_helpers import *
    

def exit_program():
    print(colorama.Fore.LIGHTYELLOW_EX + "Goodbye!\n")
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
            print("Invalid choice, please try again!\n")


def menu():
    print(colorama.Fore.LIGHTMAGENTA_EX + "\nWelcome!")
    print(colorama.Back.RESET)
    print(colorama.Fore.LIGHTRED_EX + "Please select an option:")
    print(colorama.Fore.RESET)
    print(colorama.Fore.LIGHTCYAN_EX + "1. Access Artist Data")
    print(colorama.Fore.LIGHTCYAN_EX + "2. Access Album Data")
    print(colorama.Fore.LIGHTCYAN_EX + "0. Exit the program")
    print(colorama.Fore.RESET)
    



if __name__ == "__main__":
    initialize_artist_data()
    initialize_album_data()
    main()
