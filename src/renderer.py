import pygame

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
        self._display_info(lives, points, level)
        self._display_top_score(top_score)
        self._display_instructions()
        for entity in game_level.all_entities:
            self.display.blit(entity.surf, entity.rect)
        pygame.display.flip()

    def main_menu_screen(self, option, level, color):
        self.display.fill((0, 0, 0))
        if option == "start":
            self._display_menu_options(True, False, False, False, level, color)
        elif option == "change_level":
            self._display_menu_options(False, True, False, False, level, color)
        elif option == "change_color":
            self._display_menu_options(False, False, True, False, level, color)
        elif option == "quit":
            self._display_menu_options(False, False, False, True, level, color)
        pygame.display.flip()

    def game_over_screen(self, lives, points, level, high_scores):
        """Shows game over screen.

        Args:
            points: Number of points.
            level: Current level number.
        """
        self.display.fill((0, 0, 0))
        self._display_info(lives, points, level)
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

    def _display_info(self, lives, points, level):
        info = [("Lives " + str(lives), (50, 20)),
                ("Points " + str(points), (200, 20)),
                ("Level " + str(level), (120, 20))]
        for text in info:
            self._print_text(text[0], text[1])

    def _display_top_score(self, score):
        text = "Top score " + str(score)
        position = (305,20)
        self._print_text(text, position)

    def _display_instructions(self):
        text = "N to start a new game, Space to launch a ball"
        position = (600, 20)
        self._print_text(text, position)

    def _display_menu_options(self, start, level, color, quit, level_number, color_number):
        self._display_option(start, "START", 200)
        self._display_option(level, "LEVEL " + str(level_number), 250)
        self._display_option(color, "COLOR " + str(color_number), 300)
        self._display_option(quit, "QUIT", 350)

    def _display_option(self, active, text, y_position):
        if active:
            color = (255,255,255)
        else:
            color = (100, 100, 100)
        self._print_text(text, (self.width/2, y_position), self.font_large, color)

    def _print_text(self, text, position, init_font=None, color=(255,255,255)):
        if not init_font:
            font = self.font
        else:
            font = init_font
        text = font.render(text, True, color)
        text_rect = text.get_rect()
        text_rect.center = (position[0], position[1])
        self.display.blit(text, text_rect)
