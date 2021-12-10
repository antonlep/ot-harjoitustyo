import pygame
from entities.tile import Tile

class GameLevel:
    """Class that models game objects inside the game area.

    Attributes:
        game_area: GameArea object that defines game area size.
        paddle: Paddle object.
        ball: Ball object.
    """
    def __init__(self, game_area, paddle, ball):
        self.game_area = game_area
        self.paddle = paddle
        self.ball = ball
        self.reset_all()

    def update(self, events):
        """Updates ball and paddle positions.

        Args:
            events: List of keypress events.
        """
        self.ball.update()
        self.paddle.update(events)

    def check_paddle_collision(self):
        """Checks collisions between the ball and the paddle.
        """
        if pygame.sprite.spritecollideany(self.paddle, self.ball_group):
            self.ball.paddle_collide()

    def tile_collision(self):
        """Checks collisions between the ball and tiles.

        Returns:
            True if tile has been hit, False otherwise.
        """
        hitted_tile =  pygame.sprite.spritecollideany(self.ball, self.tiles_group)
        if hitted_tile:
            hitted_tile.kill()
            self.ball.down = -self.ball.down
            return True
        return False

    def ball_out(self):
        """Checks if ball has gone outside the game area.

        Returns:
            True if ball is out, False otherwise.
        """
        if self.ball.out:
            return True
        return False

    def reset(self):
        """Sets ball to the default position.
        """
        self.ball.reset()

    def reset_all(self):
        """Sets ball and paddle to the default position.
        Creates new tiles and new sprite Group objects.
        """
        self.ball.reset()
        self.paddle.reset()
        self.create_tiles()
        self.paddle_group = pygame.sprite.Group(self.paddle)
        self.ball_group = pygame.sprite.Group(self.ball)
        self.all_entities = pygame.sprite.Group(
            self.ball_group,
            self.paddle_group,
            self.tiles_group)

    def create_tiles(self):
        """Removes old tiles and creates new ones that are put inside sprite Group object.
        """
        self.tiles_group = pygame.sprite.Group()
        for i in range(105, self.game_area.width, 100):
        # for i in range(505, self.game_area.width, 100):
            for j in range(40, 80, 20):
            # for j in range(40, 60, 20):
                tile = Tile(i, j)
                self.tiles_group.add(tile)

    def ball_on_paddle(self):
        """Puts the ball on the top of the paddle.
        """
        self.ball.rect.x = self.paddle.rect.x + self.paddle.size[1]/2

    def start(self):
        """Starts the ball movement.
        """
        self.ball.start()

    def no_tiles(self):
        """Checks if there are any tiles inside game area.

        Returns:
            True if no tiles left, False otherwise.
        """
        return not self.tiles_group
