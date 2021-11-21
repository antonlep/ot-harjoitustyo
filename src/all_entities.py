import pygame

class AllEntities:
    def __init__(self, paddle, ball):
        self.ball = pygame.sprite.Group(ball)
        self.paddle = pygame.sprite.Group(paddle)
        self.all_entities = pygame.sprite.Group(ball, paddle)
