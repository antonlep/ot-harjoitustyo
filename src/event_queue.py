import pygame

class EventQueue:
    def get_events(self):
        return pygame.event.get()

    def get_pressed_key(self):
        return pygame.key.get_pressed()
