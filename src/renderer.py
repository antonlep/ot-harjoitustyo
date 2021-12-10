import pygame

class Renderer:
    """Class that renders game objects to the screen.

    Attributes:
        display: Pygame display object with display width and height.
    """
    def __init__(self, display):
        self.display = display
        self.font = pygame.font.Font('freesansbold.ttf', 18)

    def render(self, game_level, lives, points, level):
        """Renders all game level objects to the screen.
        Also displays current game state information and displays instructions."

        Args:
            game_level: GameLevel object that includes all game objects.
            lives: Number of lives.
            points: Number of points.
            level: Current level number.
        """
        self.display.fill((0, 0, 0))
        self._display_lives(lives)
        self._display_points(points)
        self._display_level(level)
        self._display_instructions()
        for entity in game_level.all_entities:
            self.display.blit(entity.surf, entity.rect)
        pygame.display.flip()

    def game_over_screen(self, lives, points, level):
        """Shows game over screen.

        Args:
            points: Number of points.
            level: Current level number.
        """
        self.display.fill((0, 0, 0))
        self._display_lives(lives)
        self._display_points(points)
        self._display_level(level)
        self._display_instructions()
        font = pygame.font.Font('freesansbold.ttf', 40)
        self._print_text("Game Over", (400, 200), font)
        pygame.display.flip()

    def _display_lives(self, lives):
        text = "Lives " + str(lives)
        position = (50,20)
        self._print_text(text, position)

    def _display_points(self, points):
        text = "Points " + str(points)
        position = (200, 20)
        self._print_text(text, position)

    def _display_level(self, level):
        text = "Level " + str(level)
        position = (120, 20)
        self._print_text(text, position)

    def _display_instructions(self):
        text = "N to start a new game, Space to launch a ball"
        position = (500, 20)
        self._print_text(text, position)

    def _print_text(self, text, position, init_font=None):
        if not init_font:
            font = self.font
        else:
            font = init_font
        text = font.render(text, True, (255,255,255))
        text_rect = text.get_rect()
        text_rect.center = (position[0], position[1])
        self.display.blit(text, text_rect)
