import pygame

class Paddle(pygame.sprite.Sprite):
    """Class that models the paddle in the game.

    Attributes:
        speed: Paddle speed.
        size: Tuple that defines paddle height and width in pixels.
        game_area: GameArea object that defines game area size.

    Args:
        pygame (Sprite): Class inherits pygame Sprite class for game objects.
    """
    def __init__(self, speed, size):
        super().__init__()
        self.surf = pygame.Surface((size[1], size[0]))
        self.surf.fill((200, 200, 200))
        self.rect = self.surf.get_rect()
        self.speed = speed
        self.left = False
        self.right = False
        self.size = size

    def update(self, events):
        """Checks user generated events and sets movement direction accordingly.

        Args:
            events: List of various events that the user can make.
        """
        for event in events:
            if event == "LEFT_DOWN":
                self.left = True
            if event == "RIGHT_DOWN":
                self.right = True
            if event == "LEFT_UP":
                self.left = False
            if event == "RIGHT_UP":
                self.right = False

    def move_right(self):
        self.rect.move_ip(self.speed, 0)

    def move_left(self):
        self.rect.move_ip(-self.speed, 0)

    def reset(self, x, y):
        """Resets the paddle to the given position and sets movement to zero.
        """
        self.rect.x = x
        self.rect.y = y
        self.left = False
        self.right = False
