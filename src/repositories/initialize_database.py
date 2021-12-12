from database_connection import get_database_connection
from config import DATABASE

def drop_tables(connection):
    cursor = connection.cursor()
    cursor.execute("""
        DROP TABLE IF EXISTS Scores""")
    connection.commit()

def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE Scores (
            id INTEGER PRIMARY KEY,
            name TEXT,
            score INTEGER
        );
    """)
    connection.commit()

def initialize_database():
    connection = get_database_connection(DATABASE)
    drop_tables(connection)
    create_tables(connection)

if __name__ == "__main__":
    initialize_database()
