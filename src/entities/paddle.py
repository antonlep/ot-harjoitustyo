import pygame

class Paddle(pygame.sprite.Sprite):
    def __init__(self, speed, size, game_area):
        super().__init__()
        self.surf = pygame.Surface((size[1], size[0]))
        self.surf.fill((200, 200, 200))
        self.rect = self.surf.get_rect()
        self.rect.x = game_area.width/2 - size[1]/2
        self.rect.y = game_area.height - size[0]
        self.width = game_area.width
        self.speed = speed
        self.left = False
        self.right = False
        self.game_area = game_area
        self.size = size

    def update(self, events):
        for event in events:
            if event == "LEFT_DOWN":
                self.left = True
            if event == "RIGHT_DOWN":
                self.right = True
            if event == "LEFT_UP":
                self.left = False
            if event == "RIGHT_UP":
                self.right = False
        self.move()

    def move(self):
        if self.left:
            self.move_left()
        if self.right:
            self.move_right()

    def move_left(self):
        if self.rect.left > 0:
            self.rect.move_ip(-self.speed, 0)

    def move_right(self):
        if self.rect.right < self.width:
            self.rect.move_ip(self.speed, 0)

    def reset(self):
        self.rect.x = self.game_area.width/2 - self.size[1]/2
        self.left = False
        self.right = False
