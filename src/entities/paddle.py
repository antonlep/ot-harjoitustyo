import pygame

class Paddle(pygame.sprite.Sprite):
    def __init__(self, speed, width, height, x_init, y_init, display_width):
        super().__init__()
        self.surf = pygame.Surface((width, height))
        self.surf.fill((200, 200, 200))
        self.rect = self.surf.get_rect()
        self.rect.x = x_init
        self.rect.y = y_init
        self.display_width = display_width
        self.speed = speed
        self.left = False
        self.right = False

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
        if self.left:
            self.move_left()        
        if self.right:
            self.move_right()

    def move_left(self):
        if self.rect.left > 0:
            self.rect.move_ip(-self.speed, 0)

    def move_right(self):
        if self.rect.right < self.display_width:
            self.rect.move_ip(self.speed, 0)

    
