import unittest
from entities.paddle import Paddle
from entities.game_area import GameArea

class PaddleTest(unittest.TestCase):
    def setUp(self):
        width = 800
        height = 600
        paddle_size = (20, 100)
        self.paddle_speed = 10
        self.paddle = Paddle(self.paddle_speed, paddle_size)
        self.paddle.reset(width/2-paddle_size[1]/2, height-paddle_size[0])

    def test_paddle_moves_left(self):
        self.paddle.move_left()
        self.assertEqual(self.paddle.rect.x, 340)

    def test_paddle_moves_right(self):
        self.paddle.move_right()
        self.assertEqual(self.paddle.rect.x, 360)

