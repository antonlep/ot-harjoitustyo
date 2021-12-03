import unittest
from entities.ball import Ball
from entities.game_area import GameArea

class BallTest(unittest.TestCase):
    def setUp(self):
        self.width = 800
        self.height = 600
        ball_speed = 10
        game_area = GameArea(self.height, self.width)
        self.ball = Ball(ball_speed, game_area)
        self.ball.rect.x = 100
        self.ball.rect.y = 100

    def test_ball_changes_direction_when_hits_paddle(self):
        self.ball.paddle_collide()
        self.assertEqual(self.ball.down, -1)

    def test_ball_dont_go_through_left_wall(self):
        self.ball.rect.x = 0
        self.ball.rect.y = 100
        self.ball.right = -1
        self.ball.down = 1
        self.ball.update()
        self.ball.update()
        self.ball.update()
        self.assertEqual(self.ball.right, 1)
        self.assertEqual(self.ball.down, 1)
        self.assertEqual(self.ball.rect.x, 10)
        self.assertEqual(self.ball.rect.y, 130)

    def test_ball_dont_go_through_right_wall(self):
        self.ball.rect.x = self.width
        self.ball.rect.y = 100
        self.ball.right = 1
        self.ball.down = 1
        self.ball.update()
        self.ball.update()
        self.ball.update()
        self.assertEqual(self.ball.right, -1)
        self.assertEqual(self.ball.down, 1)
        self.assertEqual(self.ball.rect.x, self.width-30)
        self.assertEqual(self.ball.rect.y, 130)

    def test_ball_dont_go_through_roof(self):
        self.ball.rect.x = 200
        self.ball.rect.y = 0
        self.ball.right = 1
        self.ball.down = -1
        self.ball.update()
        self.ball.update()
        self.ball.update()
        self.assertEqual(self.ball.right, 1)
        self.assertEqual(self.ball.down, 1)
        self.assertEqual(self.ball.rect.x, 230)
        self.assertEqual(self.ball.rect.y, 10)

    def test_ball_goes_out_through_floor(self):
        self.ball.rect.x = 200
        self.ball.rect.y = self.height-10
        self.ball.right = 1
        self.ball.down = 1
        self.ball.update()
        self.ball.update()
        self.ball.update()
        self.assertEqual(self.ball.out, True)

    def test_ball_resets_to_correct_position(self):
        self.ball.reset()
        self.assertEqual(self.ball.rect.x, self.width/2)
        self.assertEqual(self.ball.rect.y, 560)
