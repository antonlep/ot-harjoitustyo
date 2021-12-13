import sqlite3
from sqlite3.dbapi2 import DatabaseError

class Repository:
    """Class that handles data storage using sqlite database.

    Attributes:
        connection: Sqlite connection object that represents the database.
    """
    def __init__(self, connection):
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
        """Gets top score from database.

        Returns:
            Top score as integer. If no records exists, returns None.
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM Scores ORDER BY score DESC LIMIT 1")
        row = cursor.fetchone()
        if row:
            return row["score"]
        return None

    def get_top10(self):
        """Gets top 10 scores from database.

        Returns:
            List of name-score pairs in descending order. If no records exists, returns None.
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM Scores ORDER BY score DESC LIMIT 10")
        rows = cursor.fetchall()
        if rows:
            return rows
        return None

    def add(self, name, score):
        """Stores name and score to database.

        Args:
            name: Player name.
            score: Number of points.

        Raises:
            DatabaseError: Data saving didn't succeed.

        Returns:
            True if operation was succesful.
        """
        cursor = self._connection.cursor()
        try:
            cursor.execute("INSERT INTO Scores (name, score) VALUES (?, ?)",
                (name, score))
            self._connection.commit()
            return True
        except sqlite3.Error as err:
            raise DatabaseError(err)
