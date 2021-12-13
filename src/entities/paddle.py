import pygame

class Paddle(pygame.sprite.Sprite):
    """Class that models the paddle geometry and movement.

    Attributes:
        speed: Paddle speed.
        size: Tuple that defines paddle height and width in pixels.

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
            events: List of strings of various events that the user can make.
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
        """Moves paddle to the right according to internal speed.
        """
        self.rect.move_ip(self.speed, 0)

    def move_left(self):
        """Moves paddle to the left according to internal speed.
        """
        self.rect.move_ip(-self.speed, 0)

    def reset(self, x_coord, y_coord):
        """Resets the paddle to the given position and sets movement to zero.

        Args:
            x_coord: X-position in pixels.
            y_coord: Y-position in pixels.
        """
        self.rect.x = x_coord
        self.rect.y = y_coord
        self.left = False
        self.right = False
