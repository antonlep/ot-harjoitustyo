import sys


class GameLoop:
    def __init__(self, lives, renderer, event_queue, clock):
        self.renderer = renderer
        self.event_queue = event_queue
        self.clock = clock
        self.lives = lives
        self.points = 0
        self.running = True

    def start(self, game_level):
        while self.running:
            events = self.event_queue.get_events()
            self.check_lives(game_level)
            self.check_events(events)
            self.update_game_level(game_level, events)
            self.renderer.render(game_level, self.lives, self.points)
            self.clock.tick(60)

    def check_lives(self, game_level):
        if game_level.ball_out():
            self.lives -= 1
            game_level.reset()
        if self.lives == 0:
            self.game_over()

    def check_events(self, events):
        for event in events:
            if event == "QUIT":
                self.running = False

    def update_game_level(self, game_level, events):
        game_level.update(events)
        game_level.check_paddle_collision()
        if game_level.tile_collision():
            self.points += 1

    def game_over(self):
        while True:
            self.renderer.game_over_screen()
            events = self.event_queue.get_events()
            for event in events:
                if event == "QUIT":
                    sys.exit()
