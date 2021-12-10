import pygame

class EventQueue:
    """Class that handles user generated events.
    """
    def get_events(self):
        """Gets keypress events from the queue with pygame method.
        Stores events to the list.

        Returns:
            A list that contains various events in string format.
        """
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
                if event.key == pygame.K_n:
                    result.append("N")
                if event.key == pygame.K_SPACE:
                    result.append("SPACE")
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    result.append("LEFT_UP")
                if event.key == pygame.K_RIGHT:
                    result.append("RIGHT_UP")
        return result
