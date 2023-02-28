import mysql.connector
from mysql.connector import Error
from config import db_config

def create_connection():
    """Creates a connection to the MySQL database."""
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            print('Connected to MySQL database')
            return connection
    except Error as e:
        print(f'Error connecting to MySQL database: {e}')
        return None

def close_connection(connection):
    """Closes the connection to the MySQL database."""
    if connection.is_connected():
        connection.close()
        print('Connection to MySQL database closed')

def execute_query(connection, query, values=None):
    """Executes a SQL query on the MySQL database."""
    cursor = connection.cursor()
    try:
        cursor.execute(query, values)
        connection.commit()
        print(f'{cursor.rowcount} rows affected')
    except Error as e:
        print(f'Error executing query: {e}')
    finally:
        cursor.close()

def add_book():
    """Adds a book to the library."""
    print('Enter book details:')
    title = input('Title: ')
    author = input('Author: ')
    published_year = input('Published year: ')
    connection = create_connection()
    if connection is not None:
        query = 'INSERT INTO books (title, author, published_year) VALUES (%s, %s, %s)'
        values = (title, author, published_year)
        execute_query(connection, query, values)
        close_connection(connection)

def search_books():
    """Searches for books in the library."""
    print('Enter search criteria:')
    keyword = input('Keyword: ')
    connection = create_connection()
    if connection is not None:
        query = 'SELECT * FROM books WHERE title LIKE %s OR author LIKE %s'
        values = (f'%{keyword}%', f'%{keyword}%')
        cursor = connection.cursor()
        try:
            cursor.execute(query, values)
            books = cursor.fetchall()
            if len(books) == 0:
                print('No books found')
            else:
                for book in books:
                    print(f'{book[0]} - {book[1]} by {book[2]} ({book[3]})')
        except Error as e:
            print(f'Error executing query: {e}')
        finally:
            cursor.close()
            close_connection(connection)

def get_all_books():
    """Gets all books in the library."""
    print('List of all books:')
    # keyword = input('Keyword: ')
    connection = create_connection()
    if connection is not None:
        query = 'SELECT * FROM books '
        values = ()
        cursor = connection.cursor()
        try:
            cursor.execute(query, values)
            books = cursor.fetchall()
            if len(books) == 0:
                print('No books found')
            else:
                for book in books:
                    print(f'{book[0]} - {book[1]} by {book[2]} ({book[3]})')
        except Error as e:
            print(f'Error executing query: {e}')
        finally:
            cursor.close()
            close_connection(connection)            

def delete_book():
    """Deletes a book from the library."""
    book_id = input('Enter book ID: ')
    connection = create_connection()
    if connection is not None:
        query = 'DELETE FROM books WHERE id = %s'
        values = (book_id,)
        execute_query(connection, query, values)
        close_connection(connection)

def main():
    

    """Main function that runs the program."""
    while True:
        print('Library')
        print('1. Add book')
        print('2. Search books')
        print('3. Delete book')
        print('4. List all books')
        print('5. Exit')
        choice = input('Enter choice: ')
        if choice == '1':
            add_book()
        elif choice == '2':
            search_books()
        elif choice == '3':
            delete_book()
        elif choice == '4':
            get_all_books()    
        elif choice == '5':
            break
        else:
            print('Invalid choice')

if __name__ == '__main__':
    main()
