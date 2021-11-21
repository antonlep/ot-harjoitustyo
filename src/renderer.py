import pygame

class Renderer:
    def __init__(self, paddle, display):
        self.paddle = paddle
        self.display = display

    def render(self):
        self.display.fill((0, 0, 0))
        self.display.blit(self.paddle.surf, self.paddle.rect)
        pygame.display.flip()
