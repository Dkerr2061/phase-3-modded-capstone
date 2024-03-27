# lib/helpers.py
from models.artist import Artist
from rich.console import Console
from fetching_code import *
from rich.table import Table
from load_bar import *
import colorama

console = Console()

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
            fetching_animation()
            table = Table(title="All Artists")
            table.add_column("ID", style="cyan")
            table.add_column("Name", style="magenta")
            for artist in Artist.all:
                table.add_row(str(artist.id), artist.name)
            console.print(table)
            user_input = input("\n Press 'return' to continue.")
            break
        elif(user_input == 'i'):
            while True:
                try:
                    user_input = input("\nEnter the id number for the artist: ")
                    user_input = int(user_input)
                    artist = Artist.find_by_id(user_input)
                    if(artist):
                        shorter_fetching_animation()
                        table = Table(title="Artist by ID")
                        table.add_column("ID", style="cyan")
                        table.add_column("Name", style="magenta")
                        table.add_row(str(artist.id), artist.name)
                        console.print(table)
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
                        shorter_fetching_animation()
                        table = Table(title="Artist by ID")
                        table.add_column("ID", style="cyan")
                        table.add_column("Name", style="magenta")
                        table.add_row(str(artist.id), artist.name)
                        console.print(table)
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
     experimental_loadbar()
     table = Table(title="Here is the new artist you created:")
     table.add_column("ID", style="cyan")
     table.add_column("Name", style="magenta")
     table.add_row(str(new_artist.id), new_artist.name)
     console.print(table)
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
        experimental_loadbar()
        table = Table(title="Here is the updated artist:")
        table.add_column("ID", style="cyan")
        table.add_column("Name", style="magenta")
        table.add_row(str(artist.id), artist.name)
        console.print(table)
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
          artist_album = artist.albums()
          if artist_album:
            fetching_animation()
            table = Table(title=f"Albums by Artist #{artist.id}")
            table.add_column("ID", style="cyan")
            table.add_column("Name", style="green")
            table.add_column("Year", style="blue")
            table.add_column("Favorite Song", style="magenta")
            table.add_column("Artist ID",style="white")
            for album in artist_album:
              table.add_row(str(album.id), album.name, str(album.year), album.songs, str(album.artist_id))
            console.print(table)
      else:
            print("\nAlbum was not found.")
      user_input = input("\n Press 'return' to continue.")
      break
    except:
          print("Please enter correct input.")
                    

          
            

          
     