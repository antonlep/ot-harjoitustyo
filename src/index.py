import pygame
from objects.paddle import Paddle

def main():
    height = 600
    width = 800
    paddle_height = 20
    paddle_width = 100
    screen = pygame.display.set_mode([width, height])
    paddle = Paddle(paddle_width, paddle_height,
                    width/2-paddle_width/2, height-paddle_height)
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pressed_keys = pygame.key.get_pressed()
        paddle.update(pressed_keys)
        screen.fill((0, 0, 0))
        screen.blit(paddle.surf, paddle.rect)
        pygame.display.flip()
        clock.tick(60)

if __name__=="__main__":
    main()