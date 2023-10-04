{{BOOK STORE`}} Model and Repository Classes Design Recipe
Copy this recipe template to design and implement Model and Repository classes for a database table.

1. Design and create the Table
If the table is already created in the database, you can skip this step.

Otherwise, follow this recipe to design and create the SQL schema for your table.

In this template, we'll use an example table students

# EXAMPLE

Table: students

Columns:
id | name | cohort_name
2. Create Test SQL seeds
Your tests will depend on data stored in PostgreSQL to run.

If seed data is provided (or you already created it), you can skip this step.

-- EXAMPLE
-- (file: spec/seeds_{table_name}.sql)

-- Write your SQL seed here. 

-- First, you'd need to truncate the table - this is so our table is emptied between each test run,
-- so we can start with a fresh state.
-- (RESTART IDENTITY resets the primary key)

TRUNCATE TABLE students RESTART IDENTITY; -- replace with your own table name.

-- Below this line there should only be `INSERT` statements.
-- Replace these statements with your own seed data.

INSERT INTO students (name, cohort_name) VALUES ('David', 'April 2022');
INSERT INTO students (name, cohort_name) VALUES ('Anna', 'May 2022');
Run this SQL file on the database to truncate (empty) the table, and insert the seed data. Be mindful of the fact any existing records in the table will be deleted.

psql -h 127.0.0.1 your_database_name < seeds_{table_name}.sql
3. Define the class names
Usually, the Model class name will be the capitalised table name (single instead of plural). The same name is then suffixed by Repository for the Repository class name.

# EXAMPLE
# Table name: students

# Model class
# (in lib/book.py)
class Book


# Repository class
# (in lib/book_repository.py)
class BookRepository
4. Implement the Model class
Define the attributes of your Model class. You can usually map the table columns to the attributes of the class, including primary and foreign keys.

# EXAMPLE
# Table name: books

# Model class
# (in lib/book.py)

class Book:
    def __init__(self):
        self.id = id
        self.title = title
        self.author_name = author_name

        # Replace the attributes by your own columns.


# We can set the attributes to default empty values and set them later,
# here's an example:
#
# >>> student = Book()
# >>> student.title = "1984"
# >>> student.author_name = "orwel"
# >>> student.title
# '1984'
# >>> student.author_name
# "orwel"
You may choose to test-drive this class, but unless it contains any more logic than the example above, it is probably not needed.

5. Define the Repository Class interface
Your Repository class will need to implement methods for each "read" or "write" operation you'd like to run against the database.

Using comments, define the method signatures (arguments and return value) and what they do - write up the SQL queries that will be used by each method.

# EXAMPLE
# Table name: books

# Repository class
# (in lib/book_repository.py)

class BookRepository():

    # Selecting all records
    # No arguments
    def all():
        # Executes the SQL query:
        # SELECT id, title, author_name FROM books;

        # Returns an array of Book objects.

        # Gets a single record by its ID
        # One argument: the id (number)
    def find(id):
        # Executes the SQL query:
        # SELECT id, title, author_name FROM books WHERE id = $1;

        # Returns a single Student object.

        # Add more methods below for each operation you'd like to implement.

    # def create(book)
    # 

    # def update(book)
    # 

    # def delete(book)
    # 
6. Write Test Examples
Write Python code that defines the expected behaviour of the Repository class, following your design from the table written in step 5.

These examples will later be encoded as Pytest tests.

# EXAMPLES

# 1
# Get all books

repo = BookRepository()

students = repo.all()

len(students) # =>  2

books[0].id # =>  1
books[0].title # =>  'David'
books[0].author_name # =>  'April 2022'

books[1].id # =>  2
books[1].title # =>  'Anna'
books[1].author_name # =>  'May 2022'

# 2
# Get a single student

repo = StudentRepository()

student = repo.find(1)

book.id # =>  1
book.title # =>  'David'
book.author_name # =>  'April 2022'

# Add more examples for each method
Encode this example as a test.

7. Test-drive and implement the Repository class behaviour