import pygame
from entities.tile import Tile

class GameLevel:
    """Class that models game objects and their interactions inside the game area.

    Attributes:
        game_area: GameArea object that defines game area size.
        paddle: Paddle object.
        ball: Ball object.
    """
    def __init__(self, game_area, paddle, ball):
        self.game_area = game_area
        self.paddle = paddle
        self.ball = ball
        self.game_area_size = (game_area.height, game_area.width)
        self.color = "white"
        self.reset_all()

    def _ball_update(self):
        if self.ball.rect.left < 0:
            self.ball.right = 1
        if self.ball.rect.right > self.game_area_size[1]:
            self.ball.right = -1
        if self.ball.rect.top < 0:
            self.ball.down = 1
        self.ball.move()

    def _paddle_update(self, events):
        self.paddle.update(events)
        if self.paddle.right and self.paddle.rect.right < self.game_area_size[1]:
            self.paddle.move_right()
        if self.paddle.left and self.paddle.rect.left > 0:
            self.paddle.move_left()

    def update(self, events):
        """Updates ball and paddle positions.

        Args:
            events: List of strings of keypress events.
        """
        self._ball_update()
        self._paddle_update(events)

    def check_paddle_collision(self):
        """Checks collisions between the ball and the paddle.
        """
        if pygame.sprite.spritecollideany(self.paddle, self.ball_group):
            self.ball.down = -1

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
        if self.ball.rect.bottom > self.game_area_size[0]:
            return True
        return False

    def reset(self):
        """Resets ball to the default position.
        """
        self.ball.reset(self.game_area_size[1]/2, self.game_area_size[0]-40)

    def reset_all(self):
        """Sets ball and paddle to the default position.
        Removes old tles and creates new ones.
        """
        self.reset()
        self.paddle.reset(self.game_area_size[1]/2-self.paddle.size[1]/2,
                            self.game_area_size[0]-self.paddle.size[0])
        self._create_tiles()
        self.paddle_group = pygame.sprite.Group(self.paddle)
        self.ball_group = pygame.sprite.Group(self.ball)
        self.all_entities = pygame.sprite.Group(
            self.ball_group,
            self.paddle_group,
            self.tiles_group)

    def _create_tiles(self):
        self.tiles_group = pygame.sprite.Group()
        for i in range(105, self.game_area.width, 100):
            for j in range(40, 80, 20):
                tile = Tile(i, j)
                tile.surf.fill(self.color)
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

    def update_color(self, color):
        self.color = color
        colors = {"white": (255, 255, 255),
                "red": (255, 0, 0),
                "green": (0, 255, 0),
                "blue": (0, 0, 255),
                "yellow": (255, 255, 0),
                "cyan": (0, 255, 255)}
        for entity in self.all_entities:
            entity.surf.fill(colors[self.color])
