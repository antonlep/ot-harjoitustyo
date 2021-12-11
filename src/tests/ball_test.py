import unittest
from entities.ball import Ball
from entities.game_area import GameArea

class BallTest(unittest.TestCase):
    def setUp(self):
        self.width = 800
        self.height = 600
        ball_speed = 10
        self.ball = Ball(ball_speed)
        self.ball.rect.x = 100
        self.ball.rect.y = 100


