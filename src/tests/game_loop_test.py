import unittest
import pygame
from game_loop import GameLoop

class StubRenderer:
    def render(self):
        pass

class StubClock:
    def tick(self):
        pass

class StubEventQueue:
    def __init__(self, events):
        self.events = events

    def get_events(self):
        pass

    def get_pressed_key(self):
        pass

class TestGameLoop(unittest.TestCase):
    pass

