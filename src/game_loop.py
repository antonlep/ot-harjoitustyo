import sys


class GameLoop:
    """Class that keeps track of the game status during running.

    Attributes:
        lives: Number of lives left.
        game_level: Level number that is currently in play.
        renderer: Renderer object that handles object display.
        event_queue: EventQueue object that handles user generated events.
        clock: pygame.time.Clock object that monitors time.
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
        while self.running:
            events = self.event_queue.get_events()
            self._check_events(events)
            self._update_game_level(events)
            self._check_level()
            self._check_lives()
            self.renderer.render(self.game_level, self.lives, self.points, self.level)
            self.clock.tick(60)

    def _restart(self):
        self.game_level.reset_all()
        self.game_level.ball.speed = 7
        self.level = 1
        self.lives = 3
        self.points = 0
        self.paused = True

    def _start_game(self):
        self.game_level.start()
        self.paused = False

    def _next_level(self):
        self.game_level.reset_all()
        self.game_level.ball.speed += 2
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


    def _check_events(self, events):
        for event in events:
            if event == "QUIT":
                self.running = False
            if event == "N":
                self._restart()
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

    def _game_over(self):
        while True:
            high_scores = self.repository.get_top10()
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
