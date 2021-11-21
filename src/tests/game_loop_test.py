import unittest
import pygame
from entities.paddle import Paddle
from game_loop import GameLoop

class StubRenderer:
    def render(self):
        pass

class StubBall:
    def update(self):
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
        self.width = 800
        height = 600
        paddle_height = 20
        paddle_width = 100
        self.x_init = self.width/2-paddle_width/2
        self.speed = 10
        self.paddle = Paddle(self.speed, paddle_width, paddle_height,
                        self.x_init, height-paddle_height, self.width)

    def test_paddle_moves_left(self):
        events = ["LEFT_DOWN", "QUIT"]
        print(self.paddle.rect.x)
        game_loop = GameLoop(self.paddle, StubBall(), StubRenderer(), StubEventQueue(events), StubClock())
        game_loop.start()
        self.assertEqual(self.paddle.rect.x, self.x_init - self.speed)
        print(self.paddle.rect.x)



