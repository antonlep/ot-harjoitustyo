import pygame
from game_level import GameLevel
from entities.paddle import Paddle
from entities.ball import Ball
from entities.game_area import GameArea
from game_loop import GameLoop
from renderer import Renderer
from event_queue import EventQueue

HEIGHT = 600
WIDTH = 800
PADDLE_SIZE = (20, 100)
PADDLE_SPEED = 10
BALL_SPEED = 5
LIVES = 3

def main():
    display = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption("Breakout")
    game_area = GameArea(HEIGHT, WIDTH)
    paddle = Paddle(PADDLE_SPEED, PADDLE_SIZE, game_area)
    ball = Ball(BALL_SPEED, game_area)
    game_level = GameLevel(game_area, paddle, ball)
    clock = pygame.time.Clock()
    pygame.init()
    renderer = Renderer(game_level, display)
    event_queue = EventQueue()
    game_loop = GameLoop(game_level, LIVES, renderer, event_queue, clock)
    game_loop.start()

if __name__=="__main__":
    main()
