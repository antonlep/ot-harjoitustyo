import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, x_init, y_init):
        super().__init__()
        self.surf = pygame.Surface((95,15))
        self.surf.fill((200, 200, 200))
        self.rect = self.surf.get_rect(center=(x_init, y_init))
