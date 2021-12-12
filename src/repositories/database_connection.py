import os 
import sqlite3

def get_database_connection(db_file):
    """Sets up sqlite3 database connection.

    Args:
        db_file: Database name as string.

    Returns:
        Sqlite connection object that represents the database.
    """
    connection = sqlite3.connect(db_file)
    connection.row_factory = sqlite3.Row
    return connection