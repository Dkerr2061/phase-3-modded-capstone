from models.album import Album
from rich.console import Console
from fetching_code import *
from rich.table import Table
from load_bar import *


console = Console()

def initialize_album_data():
    Album.create_table()
    Album.get_all()

def interact_with_album_data():
    console.print("You are interacting with the album data.", style="bright_cyan")
    while True:
        album_menu()
        user_input = input("Please select one of the following options:")
        if(user_input == '1'):
            search_for_album()
            break
        elif(user_input == '2'):
            create_new_album()
            break
        elif(user_input == '3'):
            update_album()
            break
        elif(user_input == '4'):
            list_of_artists()
            break
        elif(user_input == '5'):
            delete_album()
            break
        else:
            console.print("Invalid input, please try again.", style="orange_red1")


def album_menu():
    console.print("\n1. To search for album:", style="bright_magenta")
    console.print("2. To create a new album:", style="bright_magenta")
    console.print("3. To update an existing album:", style="bright_magenta")
    console.print("4. To get the album's artist information:", style="bright_magenta")
    console.print("5. To delete album\n", style="bright_magenta")

def search_for_album_menu():
    console.print("\nChoose one of the following options:", style="bright_cyan")
    console.print("1. To get all albums:", style="bright_magenta")
    console.print("2. To search by id:", style="bright_magenta")
    console.print("3. To search by year:\n", style="bright_magenta")

def search_for_album():
    search_for_album_menu()
    user_input = input("Please choose option:")
    while True:
        if(user_input == '1'):
            fetching_animation()
            table = Table(title="All albums")
            table.add_column("ID", style="cyan")
            table.add_column("Name", style="green")
            table.add_column("Year", style="blue")
            table.add_column("Favorite Song", style="magenta")
            table.add_column("Artist ID", style="white")
            for album in Album.all:
                table.add_row(str(album.id), album.name, str(album.year), album.songs, str(album.artist_id))
            console.print(table)
            user_input = input("\n Press 'return' to continue.")
            break
        elif(user_input == '2'):
            while True:
                try:
                    user_input = input("\nEnter the album's ID: ")
                    user_input = int(user_input)
                    album = Album.find_by_id(user_input)
                    if(album):
                        shorter_fetching_animation()
                        table = Table(title="Album by ID")
                        table.add_column("ID", style="cyan")
                        table.add_column("Name", style="magenta")
                        table.add_column("Year", style="blue")
                        table.add_column("Favorite Song", style="magenta")
                        table.add_column("Artist ID", style="white")
                        table.add_row(str(album.id), album.name, str(album.year), album.songs, str(album.artist_id))
                        console.print(table)
                    else:
                            console.print("\nAlbum not found!", style="orange_red1")
                    user_input = input("\n Press 'return' to continue.")
                    break
                except:
                    console.print("\n Invalid input, please try again.", style="orange_red1")
            break
        elif(user_input == '3'):
            while True:
                try:
                    user_input = input("\nEnter album's release year: ")
                    user_input = int(user_input)
                    albums = Album.find_by_year(user_input)
                    if(albums):
                        shorter_fetching_animation()
                        table = Table(title="Album by year")
                        table.add_column("ID", style="cyan")
                        table.add_column("Name", style="magenta")
                        table.add_column("Year", style="blue")
                        table.add_column("Favorite Song", style="magenta")
                        table.add_column("Artist ID", style="white")
                        for album in albums:
                          table.add_row(str(album.id), album.name, str(album.year), album.songs, str(album.artist_id))
                        console.print(table)                        
                    else:
                        console.print("\nAlbum not found!", style="orange_red1")
                    user_input = input("\n Press 'return' to continue.")
                    break
                except:
                    console.print("\n Invalid input, please try again.", style="orange_red1")
            break


def create_new_album():
    name = input("Enter new album's name: ")
    year = input("Enter new album's release year: ")
    year = int(year)
    songs = input("Enter your favorite song from album: ")
    artist_id = input("Enter the ID of the album's artist: ")
    artist_id = int(artist_id)
    try:
        new_album = Album.create(name, year, songs, artist_id)
        experimental_loadbar()
        table = Table(title="Here is the new album you created:")
        table.add_column("ID", style="cyan")
        table.add_column("Name", style="magenta")
        table.add_column("Year", style="blue")
        table.add_column("Favorite Song", style="magenta")
        table.add_column("Artist ID", style="white")
        table.add_row(str(new_album.id), new_album.name, str(new_album.year), new_album.songs, str(new_album.artist_id))
        console.print(table)
        user_input = input("\n Press 'return' to continue.")
    except Exception:
        console.print("Error, new album could not be created.", style="orange_red1")

def update_album():
    user_input = input("Enter album's ID: ")
    user_input = int(user_input)
    album = Album.find_by_id(user_input)
    shorter_fetching_animation()
    if(album):
        updated_album_name = input("Enter updated album name: ")
        album.name = updated_album_name
        updated_album_year = input("Enter updated album year: ")
        album.year = int(updated_album_year)
        updated_album_song = input("Enter updated favorite song: ")
        album.songs = updated_album_song
        updated_album_artist_id = input("Enter updated album artist's ID: ")
        album.artist_id = int(updated_album_artist_id)
        album.update()
        experimental_loadbar()
        table = Table(title="Here is the new album you created:")
        table.add_column("ID", style="cyan")
        table.add_column("Name", style="magenta")
        table.add_column("Year", style="blue")
        table.add_column("Favorite Song", style="magenta")
        table.add_column("Artist ID", style="white")
        table.add_row(str(album.id), album.name, str(album.year), album.songs, str(album.artist_id))
        console.print(table)
        user_input = input("\n Press 'return' to continue.")
    else:
        raise Exception("Album could not be updated.")
    
def delete_album():
    id_ = input("Enter album's ID to delete: ")
    id_ = int(id_)
    album = Album.find_by_id(id_)
    if(album):
        album.delete()
        console.print(f"Album with the id of {id_} has been deleted.", style="orange_red1")
    else:
         console.print(f"Album with id {id_} not found", style="orange_red1")
    user_input = input("\n Press 'return' to continue.")

def list_of_artists():
    from models.artist import Artist
    artist_id = input("Enter artist's ID: ")
    artist_id = int(artist_id)
    artist = Artist.find_by_id(artist_id)
    fetching_animation()
    if(artist):
        albums = artist.albums()
            
        table = Table(title="Here's a list of the Artists and their albums:")
        table.add_column("Artist Name", style="slate_blue3")
        table.add_column("ID", style="cyan")
        table.add_column("Name", style="magenta")
        table.add_column("Year", style="blue")
        table.add_column("Favorite Song", style="magenta")
        table.add_column("Artist ID", style="white")
        for album in albums:
            table.add_row(artist.name, str(album.id), album.name, str(album.year), album.songs, str(album.artist_id))
        console.print(table)

    else:
        console.print(f"Artist {artist_id} was not found.", style="orange_red1")
    user_input = input("\n Press 'return' to continue.")
