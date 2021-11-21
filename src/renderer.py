import pygame

class Renderer:
    def __init__(self, entities, display):
        self.entities = entities
        self.display = display

    def render(self):
        self.display.fill((0, 0, 0))
        for entity in self.entities.all_entities:
            self.display.blit(entity.surf, entity.rect)
        pygame.display.flip()
