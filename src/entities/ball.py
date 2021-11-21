import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self, speed, size, x_init, y_init, display_width, display_height):
        super().__init__()
        self.surf = pygame.Surface((size, size))
        self.surf.fill((200, 200, 200))
        # pygame.draw.circle(self.surf, (200, 200, 200), (size, size), size)
        # self.rect = self.surf.get_rect(center = (x_init, y_init))
        self.rect = self.surf.get_rect()
        self.rect.x = x_init
        self.rect.y = y_init
        self.speed = speed
        self.right = 1
        self.down = 1
        self.display_height = display_height
        self.display_width = display_width

    def update(self):
        if self.rect.left < 0:
            self.right = 1
        if self.rect.right > self.display_width:
            self.right = -1
        if self.rect.top < 0:
            self.down = 1
        if self.rect.bottom > self.display_height:
            self.down = -1
        self.rect.move_ip(self.right*self.speed, self.down*self.speed)
