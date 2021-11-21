import pygame

class Renderer:
    def __init__(self, paddle, ball, display):
        self.paddle = paddle
        self.ball = ball
        self.display = display

    def render(self):
        self.display.fill((0, 0, 0))
        self.display.blit(self.paddle.surf, self.paddle.rect)
        self.display.blit(self.ball.surf, self.ball.rect)
        pygame.display.flip()
