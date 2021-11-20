import unittest
from entities.paddle import Paddle

class EntitiesTest(unittest.TestCase):
    def setUp(self):
        width = 800
        height = 600
        paddle_height = 20
        paddle_width = 100
        self.paddle_speed = 10
        self.x_init = width/2-paddle_width/2
        self.y_init = height - paddle_height
        self.width = width
        self.paddle = Paddle(self.paddle_speed, paddle_width, paddle_height,
                        self.x_init, self.y_init, self.width)

    def test_paddle_moves_left(self):
        self.paddle.move_left()
        self.assertEqual(self.paddle.rect.x, self.x_init-self.paddle_speed)

    def test_paddle_dont_move_through_left_wall(self):
        for i in range(40):
            self.paddle.move_left()
        self.assertEqual(self.paddle.rect.left, 0)

    def test_paddle_moves_right(self):
        self.paddle.move_right()
        self.assertEqual(self.paddle.rect.x, self.x_init+self.paddle_speed)

    def test_paddle_dont_move_through_right_wall(self):
        for i in range(40):
            self.paddle.move_right()
        self.assertEqual(self.paddle.rect.right, self.width)
        
