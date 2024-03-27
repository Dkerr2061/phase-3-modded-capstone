from models.artist import Artist
from models.album import Album

from models.__init__ import CURSOR, CONN

Artist.create_table()
Album.create_table()

CURSOR.execute("DELETE FROM artists")
CURSOR.execute("DELETE FROM albums")
CONN.commit()


Artist.create("Tool")
Artist.create("Pink Floyd")
Artist.create("Flume")
Artist.create("Soda Stero")
Artist.create("Halsey")
Artist.create("The Pillows")
Artist.create("Yoko Kanno")
Artist.create("Ice Cube")
Artist.create("Dr. Dre")
Artist.create("Primus")
Artist.create("Residente")
Artist.create("Rage Against The Machine")

Album.create("Lateralus", 2001, "Schism", 1)
Album.create("Dark Side of the Moon", 1973, "Time", 2)
Album.create("Skin", 2016, "Say it", 3)
Album.create("Obras Cumbres", 2001, "De musica ligera", 4)
Album.create("Badlands", 2015, "Gasoline", 5)
Album.create("FLCL", 2003, "Hybrid Rainbow", 6)
Album.create("Stand Alone Complex", 2011, "Inner Universe", 7)
Album.create("The Predator", 1992, 'It was a good day', 8)
Album.create("2001", 1999, "Still Dre", 9)
Album.create("They can't all be Zingers", 2006, "Blue collar tweekers", 10)
Album.create("Bajo y Bateria", 2023, "Bajo y Bateria", 11)
Album.create("Battle of Los Angeles", 1999, "Guerrilla Radio", 12)
