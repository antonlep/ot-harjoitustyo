import pygame
from entities.paddle import Paddle
from entities.ball import Ball
from all_entities import AllEntities
from game_loop import GameLoop
from renderer import Renderer
from event_queue import EventQueue

HEIGHT = 600
WIDTH = 800
PADDLE_HEIGHT = 20
PADDLE_WIDTH = 100
PADDLE_SPEED = 10
BALL_SPEED = 5
BALL_SIZE = 10

def main():
    display = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption("Breakout")
    paddle = Paddle(PADDLE_SPEED,  PADDLE_WIDTH, PADDLE_HEIGHT,
                    WIDTH/2-PADDLE_WIDTH/2, HEIGHT-PADDLE_HEIGHT, WIDTH)
    ball = Ball(BALL_SPEED, BALL_SIZE, WIDTH/2, HEIGHT/2, WIDTH, HEIGHT)
    entities = AllEntities(paddle, ball)
    clock = pygame.time.Clock()
    renderer = Renderer(entities, display)
    event_queue = EventQueue()
    game_loop = GameLoop(entities, renderer, event_queue, clock)
    pygame.init()
    game_loop.start()

if __name__=="__main__":
    main()
