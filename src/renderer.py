import pygame
import pygame_menu

class Renderer:
    """Class that renders game objects to the screen.

    Attributes:
        display: Pygame display object with display width and height.
    """
    def __init__(self, display):
        self.display = display
        self.font = pygame.font.Font('freesansbold.ttf', 16)
        self.font_large = pygame.font.Font('freesansbold.ttf', 32)
        self.width = self.display.get_size()[0]
        self.height = self.display.get_size()[1]

    def render(self, game_level, lives, points, level, top_score):
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
        self._display_top_score(top_score)
        self._display_instructions()
        for entity in game_level.all_entities:
            self.display.blit(entity.surf, entity.rect)
        pygame.display.flip()

    def main_menu_screen(self, selected):
        self.display.fill((0, 0, 0))
        if selected == 0:
            text_start = self.font_large.render("START", self.font_large, (255, 255, 255))
        else:
            text_start = self.font_large.render("START", self.font_large, (200, 200, 200))
        if selected == 1:
            text_quit = self.font_large.render("QUIT", self.font_large, (255, 255, 255))
        else:
            text_quit = self.font_large.render("QUIT", self.font_large, (200, 200, 200))
        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()
        self.display.blit(text_start, (self.width/2 - (start_rect[2]/2), 200))
        self.display.blit(text_quit, (self.width/2 - (quit_rect[2]/2), 250))
        pygame.display.flip()

    def game_over_screen(self, lives, points, level, high_scores):
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
        self._print_text("Game Over", (400, 150), font)
        self._display_high_scores(high_scores)
        pygame.display.flip()

    def _display_high_scores(self, high_scores):
        title_font = pygame.font.Font('freesansbold.ttf', 30)
        self._print_text("High scores", (400, 250), title_font)
        y_pos = 300
        if high_scores:
            for row in high_scores:
                self._print_text(row["name"] + " " + str(row["score"]), (400, y_pos))
                y_pos += 20

    def _display_lives(self, lives):
        text = "Lives " + str(lives)
        position = (50,20)
        self._print_text(text, position)

    def _display_top_score(self, score):
        text = "Top score " + str(score)
        position = (305,20)
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
        position = (600, 20)
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
