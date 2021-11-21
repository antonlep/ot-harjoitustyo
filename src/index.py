import pygame
from entities.paddle import Paddle
from game_loop import GameLoop
from renderer import Renderer
from event_queue import EventQueue

def main():
    height = 600
    width = 800
    paddle_height = 20
    paddle_width = 100
    paddle_speed = 10
    display = pygame.display.set_mode([width, height])
    pygame.display.set_caption("Breakout")
    paddle = Paddle(paddle_speed, paddle_width, paddle_height,
                    width/2-paddle_width/2, height-paddle_height, width)
    clock = pygame.time.Clock()
    renderer = Renderer(paddle, display)
    event_queue = EventQueue()
    game_loop = GameLoop(paddle, renderer, event_queue, clock)
    pygame.init()
    game_loop.start()

if __name__=="__main__":
    main()
