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
        """Checks user generated events and sets movement direction accordingly.
        Calls _move() method to move the paddle.

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
        self._move()

    def _move(self):
        if self.left:
            self._move_left()
        if self.right:
            self._move_right()

    def _move_left(self):
        if self.rect.left > 0:
            self.rect.move_ip(-self.speed, 0)

    def _move_right(self):
        if self.rect.right < self.width:
            self.rect.move_ip(self.speed, 0)

    def reset(self):
        """Resets the paddle to the default position and sets movement to zero.
        """
        self.rect.x = self.game_area.width/2 - self.size[1]/2
        self.left = False
        self.right = False
