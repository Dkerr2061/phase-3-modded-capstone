# lib/helpers.py
from models.artist import Artist
from rich.console import Console
from fetching_code import *
from rich.table import Table
from load_bar import *


console = Console()

def initialize_artist_data():
    Artist.create_table()
    Artist.get_all()


def interact_with_artist_data():
    console.log("You are interacting with the artist data.", style="bright_green")
    while True:
        artist_menu()
        user_input = input("Select option: ")
        if(user_input == '1'):
             search_artist()
             break
        elif (user_input == '2'):
             create_new_artist()
             break
        elif (user_input == '3'):
             update_artist()
             break
        elif (user_input == '4'):
             get_artist_album()
             break
        elif (user_input == '5'):
             delete_artist()
             break
        else:
             console.print('Invalid input, please try again.', style="orange_red1")
             
            


def artist_menu():
        console.print("\n1. To search artists", style="royal_blue1")
        console.print("2. To create artist", style="royal_blue1")
        console.print("3. To update artist", style="royal_blue1")
        console.print("4. To get artist album's", style="royal_blue1")
        console.print("5. To delete artist\n", style="royal_blue1")

        
def search_artist():
     artist_search_options()
     user_input = input("Select option: ")
     while True:
        if(user_input == '1'):
            fetching_animation()
            table = Table(title="All Artists")
            table.add_column("ID", style="cyan")
            table.add_column("Name", style="magenta")
            for artist in Artist.all:
                table.add_row(str(artist.id), artist.name)
            console.print(table)
            user_input = input("\n Press 'return' to continue.")
            break
        elif(user_input == '2'):
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
                            console.print("\nArtist not found!", style="orange_red1")
                    user_input = input("\n Press 'return' to continue.")
                    break
                except:
                        console.print("Invalid input, please try again.", style="orange_red1")
            break
        elif(user_input == '3'):
            while True:
                try:
                    console.print("\nTo search for artist name make sure that every word is Capitalized.", style="green")
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
     console.print("\nWould you like to see all or search by ID or Name?", style="bright_green")
     console.print("1. To see all artist's.", style="royal_blue1")
     console.print("2. To search by id.", style="royal_blue1")
     console.print("3. To search by name.\n", style="royal_blue1")


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
        console.print(f"Artist with the id of {user_input} has been deleted.", style="orange_red1")
    else:
         console.print(f"Artist with id {user_input} not found", style="red1")
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
            console.print("\nAlbum was not found.", style="red1")
      user_input = input("\n Press 'return' to continue.")
      break
    except:
          console.print("Please enter correct input.", style="red1")
                    

          
            

          
     