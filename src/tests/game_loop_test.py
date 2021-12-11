import unittest
from unittest.mock import Mock
import pygame
from entities.paddle import Paddle
from entities.ball import Ball
from entities.game_area import GameArea
from game_level import GameLevel
from game_loop import GameLoop

class StubRepository:
    def get_top10(self):
        pass

class StubRenderer:
    def render(self, game_level, lives, points, level):
        pass

    def game_over_screen(self):
        pass

class StubClock:
    def tick(self, framerate):
        pass

class StubEventQueue:
    def __init__(self, events):
        self.events = events

    def get_events(self):
        return self.events

class TestGameLoop(unittest.TestCase):
    def setUp(self):
        paddle_size = (20, 100)
        self.speed = 10
        game_area = GameArea(600, 800)
        self.paddle = Paddle(self.speed, paddle_size)
        self.ball = Ball(self.speed)
        self.game_level = GameLevel(game_area, self.paddle, self.ball)
        self.lives = 2

    def test_game_is_in_correct_state_in_the_beginning(self):
        events = ["QUIT"]
        game_loop = GameLoop(self.lives,
                            self.game_level,
                            StubRenderer(),
                            StubEventQueue(events),
                            StubClock(),
                            StubRepository)
        game_loop.start()
        self.assertEqual(self.game_level.ball.right, 0)
        self.assertEqual(self.game_level.ball.down, 0)
        self.assertEqual(self.game_level.ball.rect.x, 400)
        self.assertEqual(self.game_level.ball.rect.y, 560)
        self.assertEqual(self.game_level.paddle.rect.x, 350)
        self.assertEqual(game_loop.lives, 2)
        self.assertEqual(game_loop.points, 0)
        self.assertEqual(game_loop.paused, True)

    def test_paddle_moves_left(self):
        events = ["LEFT_DOWN", "QUIT"]
        game_loop = GameLoop(self.lives,
                            self.game_level,
                            StubRenderer(),
                            StubEventQueue(events),
                            StubClock(),
                            StubRepository())
        game_loop.start()
        self.assertEqual(self.paddle.rect.x, 340)

    def test_new_game_resets_the_game(self):
        self.lives = 1
        self.points = 10
        self.ball.right = 1
        self.ball.down = -1
        self.ball.rectx = 100
        self.ball.recty = 100
        self.paddle.rectx = 10
        events = ["LEFT", "LEFT", "SPACE", "N", "QUIT"]
        game_loop = GameLoop(self.lives,
                            self.game_level,
                            StubRenderer(),
                            StubEventQueue(events),
                            StubClock(),
                            StubRepository())
        game_loop.paused = False
        game_loop.start()
        self.assertEqual(self.ball.right, 0)
        self.assertEqual(self.ball.down, 0)
        self.assertEqual(self.ball.rect.x, 400)
        self.assertEqual(self.ball.rect.y, 560)
        self.assertEqual(self.paddle.rect.x, 350)
        self.assertEqual(game_loop.lives, 3)
        self.assertEqual(game_loop.points, 0)
        self.assertEqual(game_loop.paused, True)

    def test_ball_starts_to_move_at_the_beginning_when_pressed_space(self):
        events = ["SPACE", "QUIT"]
        game_loop = GameLoop(self.lives,
                            self.game_level,
                            StubRenderer(),
                            StubEventQueue(events),
                            StubClock(),
                            StubRepository())
        game_loop.start()
        self.assertEqual(self.ball.right, 1)
        self.assertEqual(self.ball.down, -1)

    def test_game_over_called_when_ball_is_out_and_zero_lives(self):
        renderer_mock = Mock()
        self.lives = 1
        self.points = 10
        events = ["LEFT", "LEFT","QUIT"]
        game_loop = GameLoop(self.lives,
                            self.game_level,
                            renderer_mock,
                            StubEventQueue(events),
                            StubClock(),
                            StubRepository())
        self.ball.rect.y = 1000
        game_loop.paused = False
        with self.assertRaises(SystemExit):
            game_loop.start()
        self.assertEqual(game_loop.lives, 0)
        renderer_mock.game_over_screen.assert_called()
