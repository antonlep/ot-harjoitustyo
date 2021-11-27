import unittest
import pygame
from entities.paddle import Paddle
from entities.game_area import GameArea
from game_level import GameLevel
from game_loop import GameLoop

class StubRenderer:
    def render(self, lives):
        pass

class StubBall(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((0,0))
        self.rect = self.surf.get_rect()
        self.game_area_size = (0,0)
        self.out = False

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
        paddle_size = (20, 100)
        self.speed = 10
        game_area = GameArea(600, 800)
        self.paddle = Paddle(self.speed, paddle_size, game_area)
        self.game_level = GameLevel(game_area, self.paddle, StubBall())

    def test_paddle_moves_left(self):
        lives = 2
        events = ["LEFT_DOWN", "QUIT"]
        game_loop = GameLoop(self.game_level, lives, StubRenderer(), StubEventQueue(events), StubClock())
        game_loop.start()
        self.assertEqual(self.paddle.rect.x, 340)
