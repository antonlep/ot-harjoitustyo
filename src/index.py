import pygame
from entities.paddle import Paddle
from entities.ball import Ball
from game_loop import GameLoop
from renderer import Renderer
from event_queue import EventQueue

def main():
    height = 600
    width = 800
    paddle_height = 20
    paddle_width = 100
    paddle_speed = 10
    ball_speed = 5
    ball_size = 10
    display = pygame.display.set_mode([width, height])
    pygame.display.set_caption("Breakout")
    paddle = Paddle(paddle_speed, paddle_width, paddle_height,
                    width/2-paddle_width/2, height-paddle_height, width)
    ball = Ball(ball_speed, ball_size, width/2, height/2, width, height)
    clock = pygame.time.Clock()
    renderer = Renderer(paddle, ball, display)
    event_queue = EventQueue()
    game_loop = GameLoop(paddle, ball, renderer, event_queue, clock)
    pygame.init()
    game_loop.start()

if __name__=="__main__":
    main()
