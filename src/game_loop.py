import pygame

class GameLoop:
    def __init__(self, paddle, renderer, event_queue, clock):
        self.paddle = paddle
        self.renderer = renderer
        self.event_queue = event_queue
        self.clock = clock

    def start(self):
        running = True
        while running:
            for event in self.event_queue.get_events():
                if event.type == pygame.QUIT:
                    running = False
            pressed_keys = self.event_queue.get_pressed_key()
            self.paddle.update(pressed_keys)
            self.renderer.render()
            self.clock.tick(60)