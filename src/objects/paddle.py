import pygame

class Paddle(pygame.sprite.Sprite):
    def __init__(self, width, height, x_init, y_init):
        super().__init__()
        self.surf = pygame.Surface((width, height))
        self.surf.fill((200, 200, 200))
        self.rect = self.surf.get_rect()
        self.rect.x = x_init
        self.rect.y = y_init

    def update(self, pressed_keys):
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-10, 0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(10, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800