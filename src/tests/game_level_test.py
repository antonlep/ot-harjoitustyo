import unittest
import pygame
from game_level import GameLevel
from entities.ball import Ball
from entities.paddle import Paddle
from entities.game_area import GameArea

class TestGameLevel(unittest.TestCase):
    def setUp(self):
        HEIGHT = 600
        WIDTH = 800
        PADDLE_SIZE = (20, 100)
        PADDLE_SPEED = 10
        BALL_SPEED = 5
        self.game_area = GameArea(HEIGHT, WIDTH)
        self.paddle = Paddle(PADDLE_SPEED, PADDLE_SIZE)
        self.ball = Ball(BALL_SPEED)
        self.width = WIDTH
        self.height = HEIGHT


    def test_ball_changes_direction_when_hits_paddle(self):
        game_level = GameLevel(self.game_area, self.paddle, self.ball)
        game_level.ball.down = 1
        game_level.ball.rect.y = self.game_area.height - 5
        game_level.check_paddle_collision()
        self.assertEqual(game_level.ball.down, -1)

    def test_ball_resets_to_correct_position(self):
        game_level = GameLevel(self.game_area, self.paddle, self.ball)
        game_level.ball.rect.x = 0
        game_level.ball.rect.y = 100
        game_level.reset()
        self.assertEqual(game_level.ball.rect.x, self.width/2)
        self.assertEqual(game_level.ball.rect.y, 560)

    def test_ball_dont_go_through_left_wall(self):
        game_level = GameLevel(self.game_area, self.paddle, self.ball)
        game_level.ball.rect.x = 0
        game_level.ball.rect.y = 100
        game_level.ball.right = -1
        game_level.ball.down = 1
        game_level._ball_update()
        game_level._ball_update()
        game_level._ball_update()
        self.assertEqual(game_level.ball.right, 1)
        self.assertEqual(game_level.ball.down, 1)
        self.assertEqual(game_level.ball.rect.x, 5)
        self.assertEqual(game_level.ball.rect.y, 115)

    def test_ball_dont_go_through_right_wall(self):
        game_level = GameLevel(self.game_area, self.paddle, self.ball)
        game_level.ball.rect.x = self.width
        game_level.ball.rect.y = 100
        game_level.ball.right = 1
        game_level.ball.down = 1
        game_level._ball_update()
        game_level._ball_update()
        game_level._ball_update()
        self.assertEqual(game_level.ball.right, -1)
        self.assertEqual(game_level.ball.down, 1)
        self.assertEqual(game_level.ball.rect.x, self.width-15)
        self.assertEqual(game_level.ball.rect.y, 115)

    def test_ball_dont_go_through_roof(self):
        game_level = GameLevel(self.game_area, self.paddle, self.ball)
        game_level.ball.rect.x = 200
        game_level.ball.rect.y = 0
        game_level.ball.right = 1
        game_level.ball.down = -1
        game_level._ball_update()
        game_level._ball_update()
        game_level._ball_update()
        self.assertEqual(game_level.ball.right, 1)
        self.assertEqual(game_level.ball.down, 1)
        self.assertEqual(game_level.ball.rect.x, 215)
        self.assertEqual(game_level.ball.rect.y, 5)

    def test_ball_goes_out_through_floor(self):
        game_level = GameLevel(self.game_area, self.paddle, self.ball)
        game_level.ball.rect.x = 200
        game_level.ball.rect.y = self.height-10
        game_level.ball.right = 1
        game_level.ball.down = 1
        print(game_level.ball.rect.bottom, game_level.game_area_size[1])
        game_level._ball_update()
        print(game_level.ball.rect.bottom, game_level.game_area_size[1])
        game_level._ball_update()
        print(game_level.ball.rect.bottom, game_level.game_area_size[1])
        game_level._ball_update()
        print(game_level.ball.rect.bottom, game_level.game_area_size[1])
        ball_out = game_level.ball_out()
        self.assertEqual(ball_out, True)

    def test_paddle_dont_move_through_right_wall(self):
        game_level = GameLevel(self.game_area, self.paddle, self.ball)
        for _ in range(40):
            game_level._paddle_update(["RIGHT_DOWN"])
        self.assertEqual(game_level.paddle.rect.right, 800)

    def test_paddle_dont_move_through_left_wall(self):
        game_level = GameLevel(self.game_area, self.paddle, self.ball)
        for _ in range(40):
            game_level._paddle_update(["LEFT_DOWN"])
        self.assertEqual(game_level.paddle.rect.left, 0)