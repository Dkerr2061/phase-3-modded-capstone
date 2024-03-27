from models.__init__ import CONN, CURSOR


class Artist:
    
    all = []
    
    def __init__(self, name, id=None):
        self.name = name
        self.id = id

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name_param):
        if(isinstance(name_param, str)):
            self._name = name_param
        else:
            raise Exception('Artist name has to be a string.')

    @classmethod
    def create_table(cls):
        sql = """
          CREATE TABLE IF NOT EXISTS artists (
          id INTEGER PRIMARY KEY,
          name TEXT
          )
        """
        CURSOR.execute(sql)
    
    @classmethod
    def drop_table(cls):
        sql = """
          DROP TABLE IF EXISTS artists;
        """
        CURSOR.execute(sql)
    
    def save(self):
        sql = """
          INSERT INTO artists (name) 
          VALUES (?)
        """
        CURSOR.execute(sql, (self.name,))
        CONN.commit()

        self.id = CURSOR.lastrowid

        Artist.all.append(self)
    
    @classmethod
    def create(cls, name):
        artist = cls(name)
        artist.save()
        return artist
    
    @classmethod
    def instance_from_db(cls, row):
        artist = cls(row[1])
        artist.id = row[0]
        return artist
    
    @classmethod
    def get_all(cls):
        sql = """
          SELECT * FROM artists
        """
        rows = CURSOR.execute(sql).fetchall()
        cls.all = [cls.instance_from_db(row) for row in rows]
        return cls.all
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
          SELECT * FROM artists
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
          SELECT * FROM artists
          WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()

        if row:
            return cls.instance_from_db(row)
        else:
            None
    
    def update(self):
        sql = """
          UPDATE artists
          SET name = ?
          WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()
    
    def delete(self):
        sql = """
          DELETE FROM artists
          WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        Artist.all = [artist for artist in Artist.all if artist.id != self.id]
    
    def albums(self):
        from models.album import Album

        sql = """
          SELECT * FROM albums
          WHERE albums.artist_id = ?
        """
        rows = CURSOR.execute(sql, (self.id,)).fetchall()
        return [Album.instance_from_db(row) for row in rows]