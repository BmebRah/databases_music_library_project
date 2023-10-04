from lib.book import *
from lib.book_repository import *
from lib.database_connection import DatabaseConnection

connection = DatabaseConnection()
connection.connect()

connection.seed("/Users/bereket/database_model_and_repository/seeds/book_store.sql")
repository = BookRepository(connection)

books = repository.get_all()

for book in books:
    print(book)