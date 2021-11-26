import pygame

class GameLevel:
    def __init__(self, game_area, paddle, ball):
        self.game_area = game_area
        self.paddle = paddle
        self.ball = ball
        self.paddle_group = pygame.sprite.Group(self.paddle)
        self.ball_group = pygame.sprite.Group(self.ball)
        self.all_entities = pygame.sprite.Group(self.ball, self.paddle)

    def update(self, events):
        self.ball.update()
        self.paddle.update(events)

    def check_collisions(self):
        if pygame.sprite.spritecollideany(self.paddle, self.ball_group):
            self.ball.paddle_collide()

    def ball_out(self):
        if self.ball.out:
            return True
        else:
            return False

    def reset(self):
        self.ball.reset()
        self.paddle.reset()

