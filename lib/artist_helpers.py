# lib/helpers.py
from models.artist import Artist
import colorama

def initialize_artist_data():
    Artist.create_table()
    Artist.get_all()


def interact_with_artist_data():
    print(colorama.Fore.LIGHTGREEN_EX + "You are interacting with the artist data.")
    while True:
        artist_menu()
        user_input = input("Select and option: ")
        if(user_input == 'a'):
             search_artist()
             break
        elif (user_input == 'c'):
             create_new_artist()
             break
        elif (user_input == 'u'):
             update_artist()
             break
        elif (user_input == 'al'):
             get_artist_album()
             break
        elif (user_input == 'd'):
             delete_artist()
             break
        else:
             print(colorama.Fore.RED + 'Invalid input, please try again.')
             print(colorama.Fore.RESET)
            


def artist_menu():
        print("\nPress A to search artists")
        print("Press C to create artist")
        print("Press U to update artist")
        print("Press AL to get artist album's")
        print("Press D to delete artist\n")

        
def search_artist():
     artist_search_options()
     user_input = input("Select option: ")
     while True:
        if(user_input == 'a'):
            for artist in Artist.all:
                print(artist)
            user_input = input("\n Press 'return' to continue.")
            break
        elif(user_input == 'i'):
            while True:
                try:
                    user_input = input("\nEnter the id number for the artist: ")
                    user_input = int(user_input)
                    artist = Artist.find_by_id(user_input)
                    if(artist):
                        print("\nHere is the artist that matched the entered id:")
                        print(Artist.find_by_id(user_input))
                    else:
                            print("\nArtist not found!")
                    user_input = input("\n Press 'return' to continue.")
                    break
                except:
                        print("Invalid input, please try again.")
            break
        elif(user_input == 'n'):
            while True:
                try:
                    print("\nTo search for artist name make sure that every word is Capitalized.")
                    user_input = input("Enter artist's name: ")
                    user_input = str(user_input)
                    artist = Artist.find_by_name(user_input)
                    if(artist):
                         print("\nHere are the artist's that match that name:")
                         print(Artist.find_by_name(user_input))
                    else:
                         print("No artist was found with that name.")
                    user_input = input("\n Press 'return' to continue.")
                    break
                except:
                     print("Invalid input, please try again.")
            break


def artist_search_options():
     print("\nWould you like to see all or search by ID or Name?")
     print("Press A to see all artist's.")
     print("Press I to search by id.")
     print("Press N to search by name.\n")


def create_new_artist():
     user_input = input("Enter new artist name: ")
     new_artist = Artist.create(user_input)
     print("Here is the new artist: ")
     print(new_artist)
     user_input = input("\n Press 'return' to continue.")

def delete_artist():
    user_input = input("Enter artist's id to delete: ")
    user_input = int(user_input)
    artist = Artist.find_by_id(user_input)
    if artist:
        artist.delete()
        print(f"Artist with the id of {user_input} has been deleted.")
    else:
         print(f"Artist with id {user_input} not found")
    user_input = input("\n Press 'return' to continue.")

def update_artist():
    user_input = input("Enter artist's id to update: ")
    user_input = int(user_input)
    artist = Artist.find_by_id(user_input)
    if artist:
        updated_artist_name = input("Enter the updated name for the artist: ")
        artist.name = updated_artist_name
        artist.update()
        print(f"Artist name has been changed to {artist}")
    else:
         raise Exception("Could not update artist.")
    user_input = input("\n Press 'return' to continue.")

def get_artist_album():
     while True:
            try:
                user_input = input("Enter artist's ID to retrieve album: ")
                user_input = int(user_input)
                artist = Artist.find_by_id(user_input)
                if(artist):
                        print(f"Here is Artist #{artist.id}'s albums:")
                        print(artist.albums())
                else:
                     print("\nAlbum was not found.")
                user_input = input("\n Press 'return' to continue.")
                break
            except:
                 print("Please enter correct input.")
                    

          
            

          
     