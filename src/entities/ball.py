import pygame

class Ball(pygame.sprite.Sprite):
    """Class that models the ball in the game.

    Attributes:
        speed: Ball speed.
        game_area: GameArea object that defines game area size.

    Args:
        pygame (Sprite): Class inherits pygame Sprite class for game objects.
    """

    def __init__(self, speed, game_area):
        super().__init__()
        self.surf = pygame.Surface((10, 10))
        self.surf.fill((200, 200, 200))
        self.rect = self.surf.get_rect()
        self.game_area_size = (game_area.height, game_area.width)
        self.speed = speed
        self.reset()

    def reset(self):
        """Resets the ball to the default position and sets movement to zero.
        """
        self.rect.x = self.game_area_size[1]/2
        self.rect.y = self.game_area_size[0]-40
        self.right = 0
        self.down = 0
        self.out = False

    def update(self):
        """Checks collisions to walls, and sets the ball direction accordingly.
        Also checks if the ball has gone outside the game area.
        Finally moves the ball according to direction and speed.
        """
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
        """Sets the ball direction when it collides with the paddle.
        """
        self.down = -1

    def start(self):
        """Sets direction values to nonzero to start the movement.
        """
        self.right = 1
        self.down = -1
