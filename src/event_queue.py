import pygame

class EventQueue:
    """Class that handles user generated events.
    """
    def get_events(self):
        """Gets keypress events from the queue with pygame method.

        Returns:
            A list that contains events in string format.
        """
        events = pygame.event.get()
        result = []
        for event in events:
            if event.type == pygame.QUIT:
                result.append("QUIT")
            if event.type == pygame.KEYDOWN:
                result = self._add_keydown_event(event, result)
            if event.type == pygame.KEYUP:
                result = self._add_keyup_event(event, result)
        return result

    def _add_keydown_event(self, event, result):
        if event.key == pygame.K_LEFT:
            result.append("LEFT_DOWN")
        if event.key == pygame.K_RIGHT:
            result.append("RIGHT_DOWN")
        if event.key == pygame.K_UP:
            result.append("UP_DOWN")
        if event.key == pygame.K_DOWN:
            result.append("DOWN_DOWN")
        if event.key == pygame.K_RETURN:
            result.append("RETURN_DOWN")
        if event.key == pygame.K_SPACE:
            result.append("SPACE_DOWN")
        if event.key == pygame.K_n:
            result.append("N")
        if event.key == pygame.K_SPACE:
            result.append("SPACE")
        return result

    def _add_keyup_event(self, event, result):
        if event.key == pygame.K_LEFT:
            result.append("LEFT_UP")
        if event.key == pygame.K_RIGHT:
            result.append("RIGHT_UP")
        return result
