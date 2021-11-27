import pygame

class Renderer:
    def __init__(self, game_level, display):
        self.game_level = game_level
        self.display = display
        self.font = pygame.font.Font('freesansbold.ttf', 20)

    def render(self, lives):
        self.display.fill((0, 0, 0))
        text = self.font.render(f"Lives: {str(lives)}", True, (255,255,255))
        text_rect = text.get_rect()
        text_rect.center = (50,20)
        self.display.blit(text, text_rect)
        for entity in self.game_level.all_entities:
            self.display.blit(entity.surf, entity.rect)
        pygame.display.flip()
