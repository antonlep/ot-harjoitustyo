import unittest
from entities.paddle import Paddle
from entities.game_area import GameArea

class PaddleTest(unittest.TestCase):
    def setUp(self):
        width = 800
        height = 600
        paddle_size = (20, 100)
        self.paddle_speed = 10
        game_area = GameArea(height, width)
        self.paddle = Paddle(self.paddle_speed, paddle_size, game_area)

    def test_paddle_moves_left(self):
        self.paddle.move_left()
        self.assertEqual(self.paddle.rect.x, 340)

    def test_paddle_dont_move_through_left_wall(self):
        for _ in range(40):
            self.paddle.move_left()
        self.assertEqual(self.paddle.rect.left, 0)

    def test_paddle_moves_right(self):
        self.paddle.move_right()
        self.assertEqual(self.paddle.rect.x, 360)

    def test_paddle_dont_move_through_right_wall(self):
        for _ in range(40):
            self.paddle.move_right()
        self.assertEqual(self.paddle.rect.right, 800)
