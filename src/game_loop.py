import sys
from main_menu import MainMenu


class GameLoop:
    """Class that keeps track of the game state and handles events during running.

    Attributes:
        lives: Number of lives left.
        game_level: Level number that is currently in play.
        renderer: Renderer object that handles object display.
        event_queue: EventQueue object that handles user generated events.
        clock: pygame.time.Clock object that monitors time.
        repository: Repository object where top scores are saved.
    """
    def __init__(self, lives, game_level, renderer, event_queue, clock, repository):
        self.game_level = game_level
        self.renderer = renderer
        self.event_queue = event_queue
        self.clock = clock
        self.repository = repository
        self.lives = lives
        self.points = 0
        self.level = 1
        self.running = True
        self.paused = True

    def start(self):
        """Method that is running continuously during gameplay
        and handles various events that can happen using internal methods.
        Sends current game state to the renderer for display and updates the clock.
        """
        self._main_menu()
        while self.running:
            events = self.event_queue.get_events()
            self._check_events(events)
            self._update_game_level(events)
            self._check_level()
            self._check_lives()
            top_score = self._check_top_score()
            self.renderer.render(self.game_level, self.lives, self.points, self.level, top_score)
            self.clock.tick(60)

    def _restart(self):
        self.game_level.reset_all()
        self.level = 1
        self.lives = 3
        self.points = 0
        self.paused = True

    def _start_game(self):
        self.game_level.start()
        self.paused = False

    def _next_level(self):
        self.game_level.reset_all()
        self.level += 1
        self.paused = True

    def _check_lives(self):
        if self.game_level.ball_out():
            self.lives -= 1
            if self.lives == 0:
                self._game_over()
            else:
                self.game_level.reset()
                self.paused = True

    def _check_level(self):
        if not self.paused:
            if self.game_level.no_tiles():
                self._next_level()
        self.game_level.ball.speed = 3 + self.level*2

    def _check_events(self, events):
        for event in events:
            if event == "QUIT":
                self.running = False
            if event == "N":
                self._restart()
                self._main_menu()
            if event == "SPACE" and self.paused:
                self._start_game()

    def _update_game_level(self, events):
        self.game_level.update(events)
        if self.paused:
            self.game_level.ball_on_paddle()
        else:
            self.game_level.check_paddle_collision()
            if self.game_level.tile_collision():
                self.points += 1

    def _check_top_score(self):
        score = self.repository.get_top_score()
        if score:
            return score
        return 0

    def _insert_score(self):
        self.repository.add("", self.points)

    def _game_over(self):
        high_scores = self._update_high_scores()
        while True:
            self.renderer.game_over_screen(self.lives, self.points, self.level, high_scores)
            events = self.event_queue.get_events()
            for event in events:
                if event == "QUIT":
                    sys.exit()
                if event == "N":
                    self.running = True
                    self.paused = True
                    self._restart()
                    self.start()
                    break

    def _update_high_scores(self):
        high_scores = self.repository.get_top10()
        if not high_scores or len(high_scores) < 10 or self.points > high_scores[-1]["score"]:
            self._insert_score()
        return self.repository.get_top10()

    def _main_menu(self):
        main_menu = MainMenu()
        selected = 0
        sel_color = 1
        option = main_menu.options[selected]
        color = main_menu.colors[sel_color]
        level = self.level
        while True:
            self.renderer.main_menu_screen(
                option, level, color
                )
            events = self.event_queue.get_events()
            selected, level, sel_color, start, color, option = main_menu.check_main_menu_events(
                events, selected, level, sel_color
                )
            if start:
                self.game_level.update_color(color)
                self.level = level
                return
