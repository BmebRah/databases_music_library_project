from lib.album import Album

class AlbumRepository:

    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM albums")
        albums = []
        for row in rows:
            item = Album(row["id"], row["title"], row["release_year"],row["artist_id"])
            albums.append(item)
        return albums
    def find(self, artist_id):
        rows = self._connection.execute('SELECT title FROM albums WHERE id= %s', [artist_id])
        row = rows[0]
        return Album(row["id"],row["title"], row["release_year"])
    def create(self, artist):
        self._connection.execute('INSERT INTO artist (name, title) VALUES (%s, %s)', [artist.name, artist.title])
        return None
    def delete(self, artist_id):
        self._connection.execute(
            'DELETE FROM albums WHERE id = %s', [artist_id]
        )
        return None

