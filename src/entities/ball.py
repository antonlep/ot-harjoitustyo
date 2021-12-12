import pygame

class Ball(pygame.sprite.Sprite):
    """Class that models the ball geometry and movement.

    Attributes:
        speed: Ball speed.

    Args:
        pygame (Sprite): Class inherits pygame Sprite class for game objects.
    """

    def __init__(self, speed):
        super().__init__()
        self.surf = pygame.Surface((10, 10))
        self.surf.fill((200, 200, 200))
        self.rect = self.surf.get_rect()
        self.speed = speed
        self.right = 0
        self.down = 0

    def reset(self, x, y):
        """Resets ball to the specified position and sets movement to zero.

        Args:
            x: X-position in pixels.
            y: Y-position in pixels.
        """
        self.rect.x = x
        self.rect.y = y
        self.right = 0
        self.down = 0

    def move(self):
        """Moves ball according to internal speed and direction.
        """
        self.rect.move_ip(self.right*self.speed, self.down*self.speed)

    def start(self):
        """Sets direction values to nonzero to start the movement to up and right.
        """
        self.right = 1
        self.down = -1
