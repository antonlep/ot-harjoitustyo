import sys


class GameLoop:
    def __init__(self, lives, game_level, renderer, event_queue, clock):
        self.game_level = game_level
        self.renderer = renderer
        self.event_queue = event_queue
        self.clock = clock
        self.lives = lives
        self.points = 0
        self.running = True

    def start(self):
        while self.running:
            events = self.event_queue.get_events()
            self.check_lives()
            self.check_events(events)
            self.update_game_level(events)
            self.renderer.render(self.game_level, self.lives, self.points)
            self.clock.tick(60)

    def restart(self):
        self.game_level.reset()
        self.lives = 3
        self.points = 0

    def check_lives(self):
        if self.game_level.ball_out():
            self.lives -= 1
            self.game_level.reset()
        if self.lives == 0:
            self.game_over()

    def check_events(self, events):
        for event in events:
            if event == "QUIT":
                self.running = False
            if event == "N":
                self.restart()

    def update_game_level(self, events):
        self.game_level.update(events)
        self.game_level.check_paddle_collision()
        if self.game_level.tile_collision():
            self.points += 1

    def game_over(self):
        while True:
            self.renderer.game_over_screen()
            events = self.event_queue.get_events()
            for event in events:
                if event == "QUIT":
                    sys.exit()
