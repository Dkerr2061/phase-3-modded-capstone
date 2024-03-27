import sqlite3

CONN = sqlite3.connect('artist_albums.db')
CURSOR = CONN.cursor()
