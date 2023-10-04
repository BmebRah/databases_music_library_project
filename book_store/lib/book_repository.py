from lib.book import *

class BookRepository:
    def __init__(self, connection):
        self._connection = connection
    def get_all(self):
        books = []
        rows = self._connection.execute("SELECT * FROM books")
        for row in rows:
            item = row["id"], row["title"], row["author_name"] 
            books.append(item)
        return books
        
    
