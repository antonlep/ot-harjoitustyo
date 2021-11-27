import unittest
import pygame
from event_queue import EventQueue

class TestEventQueue(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.event_queue = EventQueue()

    def test_quit_event_works(self):
        event = pygame.event.Event(pygame.QUIT)
        pygame.event.post(event)
        result = self.event_queue.get_events()
        self.assertEqual(result[0], "QUIT")

    def test_left_key_press_works(self):
        event = pygame.event.Event(pygame.KEYDOWN)
        event.key = pygame.K_LEFT
        pygame.event.post(event)
        result = self.event_queue.get_events()
        self.assertEqual(result[0], "LEFT_DOWN")

    def test_right_key_press_works(self):
        event = pygame.event.Event(pygame.KEYDOWN)
        event.key = pygame.K_RIGHT
        pygame.event.post(event)
        result = self.event_queue.get_events()
        self.assertEqual(result[0], "RIGHT_DOWN")

    def test_left_key_up_works(self):
        event = pygame.event.Event(pygame.KEYUP)
        event.key = pygame.K_LEFT
        pygame.event.post(event)
        result = self.event_queue.get_events()
        self.assertEqual(result[0], "LEFT_UP")

    def test_right_key_up_works(self):
        event = pygame.event.Event(pygame.KEYUP)
        event.key = pygame.K_RIGHT
        pygame.event.post(event)
        result = self.event_queue.get_events()
        self.assertEqual(result[0], "RIGHT_UP")
