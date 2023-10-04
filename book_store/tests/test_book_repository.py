from lib.book_repository import *
from lib.book import *
from lib.database_connection import DatabaseConnection

def test_it_gets_all_book_instances(db_connection):

    db_connection.seed("/Users/bereket/database_model_and_repository/seeds/book_store.sql")
    repositorry = BookRepository(db_connection)

    books = repositorry.get_all()
    assert books == [
        (1, 'Nineteen Eighty-Four', 'George Orwell'),
        (2, 'Mrs Dalloway', 'Virginia Woolf'),
        (3, 'Emma', 'Jane Austen'),
        (4, 'Dracula', 'Bram Stoker'),
        (5, 'The Age of Innocence', 'Edith Wharton')

        ]
