import sys

class MainMenu:
    def __init__(self, event_queue, renderer, game_level):
        self.event_queue = event_queue
        self.renderer = renderer
        self.game_level = game_level
        self.options = {0: "start", 1: "change_level", 2: "change_color",  3: "quit"}
        self.colors = {1: "white", 2: "red", 3: "green", 4: "blue", 5: "yellow", 6: "cyan"}
        self.actions = {"DOWN_DOWN": self._menu_move_down,
                   "UP_DOWN": self._menu_move_up,
                   "RETURN_DOWN": self._menu_select,
                   "LEFT_DOWN": self._menu_move_left,
                   "RIGHT_DOWN": self._menu_move_right}

    def check_main_menu_events(self, events, selected, level, selected_color):
        start = False
        option = self.options[selected]

        for event in events:
            if event == "QUIT":
                sys.exit()
            if event in self.actions:
                selected, level, selected_color, start = self.actions[event](
                    selected, level, selected_color, option
                    )
                if start:
                    break
        option = self.options[selected]
        color = self.colors[selected_color]
        return selected, level, selected_color, start, color, option

    def _menu_move_down(self, selected, level, selected_color, option):
        return min(3, selected + 1), level, selected_color, False

    def _menu_move_up(self, selected, level, selected_color, option):
        return max(0, selected - 1), level, selected_color, False

    def _menu_move_left(self, selected, level, selected_color, option):
        if option == "change_level":
            level = max(1, level - 1)
        if option == "change_color":
            selected_color = max(1, selected_color - 1)
        return selected, level, selected_color, False

    def _menu_move_right(self, selected, level, selected_color, option):
        if option == "change_level":
            level = min(10, level + 1)
        if option == "change_color":
            selected_color = min(6, selected_color + 1)
        return selected, level, selected_color, False

    def _menu_select(self, selected, level, selected_color, option):
        chosen = False
        if option == "start":
            chosen = True
        elif option == "quit":
            sys.exit()
        return selected, level, selected_color, chosen
