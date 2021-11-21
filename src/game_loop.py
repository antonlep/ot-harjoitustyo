class GameLoop:
    def __init__(self, paddle, ball, renderer, event_queue, clock):
        self.paddle = paddle
        self.ball = ball
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
            self.paddle.update(events)
            self.ball.update()
            self.renderer.render()
            self.clock.tick(60)
