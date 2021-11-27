import pygame

class Renderer:
    def __init__(self, game_level, display):
        self.game_level = game_level
        self.display = display
        self.font = pygame.font.Font('freesansbold.ttf', 20)

    def render(self, lives):
        self.display.fill((0, 0, 0))
        if lives == 0:
            self.show_game_over_screen()
        text = self.font.render("Lives " + str(lives), True, (255,255,255))
        text_rect = text.get_rect()
        text_rect.center = (50,20)
        self.display.blit(text, text_rect)
        for entity in self.game_level.all_entities:
            self.display.blit(entity.surf, entity.rect)
        pygame.display.flip()

    def show_game_over_screen(self):
        font = pygame.font.Font('freesansbold.ttf', 40)
        text = font.render("Game Over", True, (255,255,255))
        text_rect = text.get_rect()
        text_rect.center = (400,200)
        self.display.blit(text, text_rect)
