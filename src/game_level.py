import pygame

class GameLevel:
    def __init__(self, game_area, paddle, ball):
        self.game_area = game_area
        self.paddle = paddle
        self.ball = ball
        self.paddle_sprite = pygame.sprite.Group(self.paddle)
        self.ball_sprite = pygame.sprite.Group(self.ball)
        self.all_entities = pygame.sprite.Group(self.ball_sprite, self.paddle_sprite)
