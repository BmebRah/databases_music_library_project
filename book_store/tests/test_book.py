from lib.book import *

def test_it_constructs_with_the_correct_attributes():
    book = Book(1, "1984", "George Orwel")
    assert book.id == 1
    assert book.title =="1984"
    assert book.author_name == "George Orwel"
def test_formats_correctly():
    book = Book(1, "1984", "George Orwel")
    assert str(book) == f"Book(1, 1984, George Orwel)"

def test_two_instances_are_equal():
    assert Book(1, "1984", "George Orwel") == Book(1, "1984", "George Orwel")