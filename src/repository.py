import sqlite3
from config import DATABASE
from sqlite3.dbapi2 import DatabaseError
from database_connection import get_database_connection

class Repository:
    def __init__(self, connection=get_database_connection(DATABASE)):
        self._connection = connection
        cursor = self._connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Scores (
                id INTEGER PRIMARY KEY,
                name TEXT,
                score INTEGER
                );
            """)
        self._connection.commit()

    def get_top_score(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM Scores ORDER BY score DESC LIMIT 1")
        row = cursor.fetchone()
        if row:
            return row["score"]
        else:
            return None

    def get_top10(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM Scores ORDER BY score DESC LIMIT 10")
        rows = cursor.fetchall()
        if rows:
            return rows
        else:
            return None

    def add(self, name, score):
        cursor = self._connection.cursor()
        try:
            cursor.execute("INSERT INTO Scores (name, score) VALUES (?, ?)",
                (name, score))
            self._connection.commit()
            return True
        except sqlite3.Error as err:
            raise DatabaseError(err)
