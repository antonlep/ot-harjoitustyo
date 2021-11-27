import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self, speed, game_area):
        super().__init__()
        self.surf = pygame.Surface((10, 10))
        self.surf.fill((200, 200, 200))
        self.rect = self.surf.get_rect()
        self.game_area_size = (game_area.height, game_area.width)
        self.rect.x = self.game_area_size[1]/2
        self.rect.y = self.game_area_size[0]/2
        self.speed = speed
        self.right = 1
        self.down = 1
        self.out = False

    def update(self):
        if self.rect.left < 0:
            self.right = 1
        if self.rect.right > self.game_area_size[1]:
            self.right = -1
        if self.rect.top < 0:
            self.down = 1
        if self.rect.bottom > self.game_area_size[0]:
            self.out = True
        self.rect.move_ip(self.right*self.speed, self.down*self.speed)

    def paddle_collide(self):
        self.down = -1

    def reset(self):
        self.rect.x = self.game_area_size[1]/2
        self.rect.y = self.game_area_size[0]/2
        self.right = 1
        self.down = 1
        self.out = False
