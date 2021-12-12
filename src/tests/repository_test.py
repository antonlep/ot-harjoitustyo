import sqlite3
import unittest
from repositories.repository import Repository

class TestRepository(unittest.TestCase):
    def setUp(self):
        self.connection = sqlite3.connect(":memory:")
        self.connection.row_factory = sqlite3.Row
        self.repository = Repository(self.connection)

        self.score1 = ("Name1", 10)
        self.score2 = ("Name2", 20)
        self.score3 = ("Name3", 30)

    def test_get_top10(self):
        self.repository.add(self.score1[0], self.score1[1])
        self.repository.add(self.score2[0], self.score2[1])
        self.repository.add(self.score3[0], self.score3[1])

        scores = self.repository.get_top10()
        self.assertEqual(len(scores), 3)
        self.assertEqual(scores[0]["name"], "Name3")
        self.assertEqual(scores[0]["score"], 30)

    def test_get_top10_over_10scores_in_database(self):
        for _ in range(20):
            self.repository.add(self.score1[0], self.score1[1])

        scores = self.repository.get_top10()
        self.assertEqual(len(scores), 10)

    def test_get_top10_no_scores_in_database(self):

        scores = self.repository.get_top10()
        self.assertEqual(scores, None)

    def test_get_top_score(self):
        self.repository.add(self.score1[0], self.score1[1])
        self.repository.add(self.score2[0], self.score2[1])
        self.repository.add(self.score3[0], self.score3[1])

        score = self.repository.get_top_score()
        self.assertEqual(score, 30)
