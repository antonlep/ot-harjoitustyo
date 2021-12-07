import pygame
from entities.tile import Tile

class GameLevel:
    def __init__(self, game_area, paddle, ball):
        self.game_area = game_area
        self.paddle = paddle
        self.ball = ball
        self.reset_all()

    def update(self, events):
        self.ball.update()
        self.paddle.update(events)

    def check_paddle_collision(self):
        if pygame.sprite.spritecollideany(self.paddle, self.ball_group):
            self.ball.paddle_collide()

    def tile_collision(self):
        hitted_tile =  pygame.sprite.spritecollideany(self.ball, self.tiles_group)
        if hitted_tile:
            hitted_tile.kill()
            self.ball.down = -self.ball.down
            return True
        return False

    def ball_out(self):
        if self.ball.out:
            return True
        return False

    def reset(self):
        self.ball.reset()

    def reset_all(self):
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
        self.tiles_group = pygame.sprite.Group()
        for i in range(105, self.game_area.width, 100):
            for j in range(40, 100, 20):
                tile = Tile(i, j)
                self.tiles_group.add(tile)

    def ball_on_paddle(self):
        self.ball.rect.x = self.paddle.rect.x + self.paddle.size[1]/2

    def start(self):
        self.ball.start()
