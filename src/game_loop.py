import sys


class GameLoop:
    def __init__(self, lives, game_level, renderer, event_queue, clock):
        self.game_level = game_level
        self.renderer = renderer
        self.event_queue = event_queue
        self.clock = clock
        self.lives = lives
        self.points = 0
        self.level = 1
        self.running = True
        self.paused = True

    def start(self):
        while self.running:
            events = self.event_queue.get_events()
            self.check_events(events)
            self.update_game_level(events)
            self.check_level()
            self.check_lives()
            self.renderer.render(self.game_level, self.lives, self.points, self.level)
            self.clock.tick(60)

    def restart(self):
        self.game_level.reset_all()
        self.game_level.ball.speed = 7
        self.level = 1
        self.lives = 3
        self.points = 0
        self.paused = True

    def start_game(self):
        self.game_level.start()
        self.paused = False

    def next_level(self):
        self.game_level.reset_all()
        self.game_level.ball.speed += 2
        self.level += 1
        self.paused = True

    def check_lives(self):
        if self.game_level.ball_out():
            self.lives -= 1
            if self.lives == 0:
                self.game_over()
            else:
                self.game_level.reset()
                self.paused = True

    def check_level(self):
        if not self.paused:
            if self.game_level.no_tiles():
                self.next_level()


    def check_events(self, events):
        for event in events:
            if event == "QUIT":
                self.running = False
            if event == "N":
                self.restart()
            if event == "SPACE" and self.paused:
                self.start_game()

    def update_game_level(self, events):
        self.game_level.update(events)
        if self.paused:
            self.game_level.ball_on_paddle()
        else:
            self.game_level.check_paddle_collision()
            if self.game_level.tile_collision():
                self.points += 1

    def game_over(self):
        while True:
            self.renderer.game_over_screen(self.points, self.level)
            events = self.event_queue.get_events()
            for event in events:
                if event == "QUIT":
                    sys.exit()
                if event == "N":
                    self.running = True
                    self.paused = True
                    self.restart()
                    self.start()
                    break
