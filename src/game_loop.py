class GameLoop:
    def __init__(self, game_level, renderer, event_queue, clock):
        self.game_level = game_level
        self.renderer = renderer
        self.event_queue = event_queue
        self.clock = clock

    def start(self):
        running = True
        while running:
            events = self.event_queue.get_events()
            for event in events:
                if event == "QUIT":
                    running = False
            self.game_level.update(events)
            self.renderer.render()
            self.clock.tick(60)
