from models.__init__ import CONN, CURSOR
import colorama

class Album:
    
  all = []

  def __init__(self, name, year, songs, artist_id, id=None):
          self.name = name
          self.year = year
          self.songs = songs
          self.artist_id = artist_id
          self.id = id

  @property
  def name(self):
        return self._name
  @name.setter
  def name(self, name_param):
        if(isinstance(name_param, str)):
              self._name = name_param
        else:
              raise Exception('Album name has to be a string and cannot be repeated.')
        
  @property
  def year(self):
        return self._year
  @year.setter
  def year(self, year_param):
        if(isinstance(year_param, int)) and (1900 <= year_param <= 2024):
              self._year = year_param
        else:
              raise Exception('Year must be an integer between the years 1900 and 2024.')
        
  @property
  def songs(self):
        return self._songs
  @songs.setter
  def songs(self, songs_param):
        if(isinstance(songs_param, str)) and ( 1 <= len(songs_param) <= 40):
              self._songs = songs_param
        else:
              raise Exception('Song has to be a string between 1 to 40 characters.')
        
  @property
  def artist_id(self):
        return self._artist_id
  @artist_id.setter
  def artist_id(self, artist_id_param):
        if(isinstance(artist_id_param, int)):
              self._artist_id = artist_id_param
        else:
              raise Exception('Artist ID must be an Integer.')
        
  def __repr__(self):
        return (colorama.Fore.LIGHTGREEN_EX + f"< Album {self.id}: Name = {self.name}, Year = {self.year}, Songs = {self.songs}, Artist ID = {self.artist_id} >")
  
  @classmethod
  def create_table(cls):
        sql = """
          CREATE TABLE IF NOT EXISTS albums(
          id INTEGER PRIMARY KEY,
          name TEXT,
          year INTEGER,
          songs TEXT,
          artist_id INTEGER
          )
        """
        CURSOR.execute(sql)
  
  @classmethod
  def drop_table(cls):
        sql = """
          DROP TABLE IF EXISTS albums;
        """
        CURSOR.execute(sql)
  
  def save(self):
        sql = """
          INSERT INTO albums (
          name,
          year,
          songs,
          artist_id
          ) VALUES (?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.year, self.songs, self.artist_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        Album.all.append(self)

  @classmethod
  def create(cls, name, year, songs, artist_id):
        album = cls(name, year, songs, artist_id)
        album.save()
        return album
  
  @classmethod
  def instance_from_db(cls, row):
        album = cls(row[1], row[2], row[3], row[4])
        album.id = row[0]
        return album
  
  @classmethod
  def get_all(cls):
        sql = """
          SELECT * FROM albums
        """
        rows = CURSOR.execute(sql).fetchall()

        cls.all = [cls.instance_from_db(row) for row in rows]

        return cls.all
  
  @classmethod
  def find_by_id(cls, id):
        sql = """
          SELECT * FROM albums
          WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()

        if row:
              return cls.instance_from_db(row)
        else:
              return None
  
  @classmethod
  def find_by_name(cls, name):
        sql = """
          SELECT * FROM albums
          WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()

        if row:
              return cls.instance_from_db(row)
        else:
              return None
  
  @classmethod
  def find_by_year(cls, year):
        sql = """
          SELECT * FROM albums
          WHERE year = ?
        """
        rows = CURSOR.execute(sql, (year,)).fetchall()

        albums_found = [album for album in cls.all if album.year == year]
        return albums_found if albums_found else None
  
  def update(self):
        sql = """
          UPDATE albums
          SET name = ?, year = ?, songs = ?, artist_id = ?
          WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.year, self.songs, self.artist_id, self.id))
        CONN.commit()

  def delete(self):
        sql = """
          DELETE FROM albums
          WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        Album.all = [album for album in Album.all if album.id != self.id]
  
  def artists(self):
        from models.artist import Artist

        sql = """
          SELECT artists.id, artists.name
          FROM artists
          INNER JOIN albums
          ON artists.id = artist_id
          WHERE artist_id = ?
        """
        row = CURSOR.execute(sql, (self.artist_id,)).fetchone()

        if row:
              return Artist.instance_from_db(row)
        else:
              return None