class GameLoop:
    def __init__(self, game_level, lives, renderer, event_queue, clock):
        self.game_level = game_level
        self.renderer = renderer
        self.event_queue = event_queue
        self.clock = clock
        self.lives = lives

    def start(self):
        while True:
            events = self.event_queue.get_events()
            self.check_lives()
            self.check_events(events)
            self.update_game_level(events)
            self.renderer.render()
            self.clock.tick(60)

    def check_lives(self):
        if self.game_level.ball_out():
            self.lives -= 1
            self.game_level.reset()
        if self.lives == 0:
            self.game_over()

    def check_events(self, events):
        for event in events:
            if event == "QUIT":
                exit()

    def update_game_level(self, events):
        self.game_level.update(events)
        self.game_level.check_collisions()

    def game_over(self):
        while True:
            events = self.event_queue.get_events()
            self.check_events(events)
