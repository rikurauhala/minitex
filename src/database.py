import os
import sqlite3

from config import DATABASE_FILE_PATH, DATA_FOLDER_PATH


def get_database_connection():
    """Gets the database connection.

    Returns:
        connection (Connection): Database connection object.
    """
    check_if_path_exists()
    connection = sqlite3.connect(
        DATABASE_FILE_PATH,
        detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES
    )
    connection.row_factory = sqlite3.Row
    check_if_table_exists(connection)
    return connection


def drop_tables(connection):
    """Clears all data from the database.

    Args:
        connection (Connection): Database connection object.
    """
    cursor = connection.cursor()
    cursor.execute("""
        DROP TABLE IF EXISTS bookreferences;
    """)
    connection.commit()


def create_tables(connection):
    """Creates database tables.

    Args:
        connection (Connection): Database connection object.
    """
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE bookreferences (
            id INTEGER PRIMARY KEY,
            author TEXT,
            title TEXT,
            year INTEGER,
            publisher TEXT
        )"""
    )
    connection.commit()

def check_if_path_exists():
    if not os.path.isdir(DATA_FOLDER_PATH):
        current_directory = os.path.dirname(__file__)
        os.makedirs(os.path.join(current_directory, "..", "data"), exist_ok=True)

def check_if_table_exists(connection):
    cursor = connection.cursor()
    tables = cursor.execute("""
        SELECT name FROM sqlite_master WHERE type='table' AND name='bookreferences'
        """
    )
    if len(tables.fetchall()) == 0:
        create_tables(connection)


def initialize_database():
    """Initializes the database."""
    current_directory = os.path.dirname(__file__)
    os.makedirs(os.path.join(current_directory, "..", "data"), exist_ok=True)
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)
    print("Database initialized!")
