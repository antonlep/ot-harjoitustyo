import pygame

class Renderer:
    def __init__(self, display):
        self.display = display
        self.font = pygame.font.Font('freesansbold.ttf', 18)

    def render(self, game_level, lives, points, level):
        self.display.fill((0, 0, 0))
        self.display_lives(lives)
        self.display_points(points)
        self.display_level(level)
        self.display_instructions()
        for entity in game_level.all_entities:
            self.display.blit(entity.surf, entity.rect)
        pygame.display.flip()

    def game_over_screen(self, points, level):
        self.display.fill((0, 0, 0))
        self.display_lives(0)
        self.display_instructions()
        self.display_points(points)
        self.display_level(level)
        font = pygame.font.Font('freesansbold.ttf', 40)
        self.print_text("Game Over", (400, 200), font)
        pygame.display.flip()

    def display_lives(self, lives):
        text = "Lives " + str(lives)
        position = (50,20)
        self.print_text(text, position)

    def display_points(self, points):
        text = "Points " + str(points)
        position = (200, 20)
        self.print_text(text, position)

    def display_level(self, level):
        text = "Level " + str(level)
        position = (120, 20)
        self.print_text(text, position)

    def display_instructions(self):
        text = "N to start a new game, Space to launch a ball"
        position = (500, 20)
        self.print_text(text, position)

    def print_text(self, text, position, init_font=None):
        if not init_font:
            font = self.font
        else:
            font = init_font
        text = font.render(text, True, (255,255,255))
        text_rect = text.get_rect()
        text_rect.center = (position[0], position[1])
        self.display.blit(text, text_rect)
