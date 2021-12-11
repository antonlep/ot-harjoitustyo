import os 
import sqlite3

def get_database_connection(db_file):
    connection = sqlite3.connect(db_file)
    connection.row_factory = sqlite3.Row
    return connection