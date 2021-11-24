import pygame

class Renderer:
    def __init__(self, game_level, display):
        self.game_level = game_level
        self.display = display

    def render(self):
        self.display.fill((0, 0, 0))
        for entity in self.game_level.all_entities:
            self.display.blit(entity.surf, entity.rect)
        pygame.display.flip()
