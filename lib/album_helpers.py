from models.album import Album
import colorama

def initialize_album_data():
    Album.create_table()
    Album.get_all()

def interact_with_album_data():
    print(colorama.Fore.LIGHTYELLOW_EX + "You are interacting with the album data.")
    while True:
        album_menu()
        user_input = input("Please select one of the following options:")
        if(user_input == 'a'):
            search_for_album()
            break
        elif(user_input == 'c'):
            create_new_album()
            break
        elif(user_input == 'u'):
            update_album()
            break
        elif(user_input == 'ar'):
            list_of_artists()
            break
        elif(user_input == 'd'):
            delete_album()
            break
        else:
            print("Invalid input, please try again.")


def album_menu():
    print("\nEnter A to search for album:")
    print("Enter C to create a new album:")
    print("Enter U to update an existing album:")
    print("Enter AR to get the album's artist information:")
    print("Enter D to delete album\n")

def search_for_album_menu():
    print("\nChoose one of the following options:")
    print("Press A to get all albums:")
    print("Press I to search by id:")
    print("Press Y to search by year:\n")

def search_for_album():
    search_for_album_menu()
    user_input = input("Please choose option:")
    while True:
        if(user_input == 'a'):
            for album in Album.all:
                print(album)
            user_input = input("\n Press 'return' to continue.")
            break
        elif(user_input == 'i'):
            while True:
                try:
                    user_input = input("\nEnter the album's ID: ")
                    user_input = int(user_input)
                    album = Album.find_by_id(user_input)
                    if(album):
                        print("\nHere is the album that matched the entered id:")
                        print(Album.find_by_id(user_input))
                    else:
                            print("\nAlbum not found!")
                    user_input = input("\n Press 'return' to continue.")
                    break
                except:
                    print("\n Invalid input, please try again.")
            break
        elif(user_input == 'y'):
            while True:
                try:
                    user_input = input("\nEnter album's release year: ")
                    user_input = int(user_input)
                    year = Album.find_by_year(user_input)
                    if(year):
                        print("\nHere is the album that matched the entered year:")
                        print(Album.find_by_year(user_input))
                    else:
                        print("\nAlbum not found!")
                    user_input = input("\n Press 'return' to continue.")
                    break
                except:
                    print("\n Invalid input, please try again.")
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
        print(f"Success {new_album} was created")
        user_input = input("\n Press 'return' to continue.")
    except Exception as exc:
        print("Error, new album could not be created.", exc)

def update_album():
    user_input = input("Enter album's ID: ")
    user_input = int(user_input)
    album = Album.find_by_id(user_input)
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
        print(f"Success, {album} was updated.")
        user_input = input("\n Press 'return' to continue.")
    else:
        raise Exception("Album could not be updated.")
    
def delete_album():
    id_ = input("Enter album's ID to delete: ")
    id_ = int(id_)
    album = Album.find_by_id(id_)
    if(album):
        album.delete()
        print(f"Album with the id of {id_} has been deleted.")
    else:
         print(f"Album with id {id_} not found")
    user_input = input("\n Press 'return' to continue.")

def list_of_artists():
    from models.artist import Artist
    artist_id = input("Enter artist's ID: ")
    artist_id = int(artist_id)
    artist = Artist.find_by_id(artist_id)
    if(artist):
        albums = artist.albums()
        for album in albums:
            print(artist)
            print(album)
    else:
        print(f"Artist {artist_id} was not found.")
    user_input = input("\n Press 'return' to continue.")
