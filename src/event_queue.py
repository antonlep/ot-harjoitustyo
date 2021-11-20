import pygame

class EventQueue:
    def get_events(self):
        events = pygame.event.get()
        result = []
        for event in events:
            if event.type == pygame.QUIT:
                result.append("QUIT")
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    result.append("LEFT_DOWN")
                if event.key == pygame.K_RIGHT:
                    result.append("RIGHT_DOWN")
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    result.append("LEFT_UP")
                if event.key == pygame.K_RIGHT:
                    result.append("RIGHT_UP")
        return result
